#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
from selenium import webdriver
from os.path import join
import logging
import os
import threading

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tqdm import tqdm

from aps_report import config
from aps_report import calcdates
from aps_report import browser
from aps_report import login
from aps_report import loadgroups
from aps_report import descargapdf
from aps_report import gendocx
from aps_report import cmdparser

def main():
    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    arglines = cmdparser.loadargs()
    if arglines.debug:
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    logging.debug("Cargando configuracion")
    args = vars(arglines) 
    logging.info("Cargando configuracion desde %s", args["config_file"])
    configuracion = config.load_config(args["config_file"], "APS")
    # args.copy() 
    for key in args.copy().iterkeys():
        if args[key] is None:
            args.pop(key)
    args.pop("config_file")
    configuracion.update(args)
    
    logging.debug(configuracion)
    fechas = calcdates.start(configuracion) 
    #fechas = calcdates.start(configuracion['cortemat'], 
    #                         configuracion['cortemd'], 
    #                         configuracion['cortevsp'])
    logging.debug(fechas)
    logging.info("Hoy es %s", fechas['ahora'])
    #Se planchan las fechas de linea de comando si es que fueron introducidas
    fechas.update(args)
    logging.info("El reporte será del %s de %s de %s a las %s%s hasta %s de %s de %s a las %s%s",
                 fechas['dia_ini'], 
                 calcdates.mestotext(str(int(fechas['mes_ini']))), 
                 fechas['year_ini'],
                 fechas['hora_ini'], 
                 fechas['start_meridian'], 
                 fechas['dia_fin'], 
                 calcdates.mestotext(fechas['mes_fin']), 
                 fechas['year_fin'],
                 fechas['hora_fin'], 
                 fechas['end_meridian']) 
    
    #print configuracion.get('proxy') 
    logging.debug("configurando Firefox...")
    if configuracion.get('proxy'):
        logging.info("Configuracion: proxy %s, puerto %s, directorio: %s", 
                      configuracion['proxy'], 
                      configuracion['proxyport'], configuracion['output_dir'])
    
    #Abrir el listado de grupos para agarrar las URL de los grupos configurados (se buscan por nombre)
    driver = browser.navegador(configuracion.get('proxy'),      
                               configuracion.get('proxyport'), 
                               configuracion['output_dir'] )    
     
    #Abriendo la sesion principal
    logging.info("Abriendo navegador en https://%s/", configuracion['endpoint'])
    driver.get("https://" + configuracion['endpoint'] + "/")
    logging.debug("Haciendo login en https://%s/", configuracion['endpoint'])
    login.login(driver, configuracion['user'], configuracion['password'])
   
    logging.debug("Abriendo listado de grupos")
    driver.get("https://" + configuracion['endpoint'] + "/groups/list/")
    conf_groups = loadgroups.loadnames(configuracion['listado'])
    view_groups = []
    for p_group in driver.find_elements_by_xpath('//a[contains(@href, \
                                                 "/groups/view/?id=")]'):
        if p_group.get_attribute("innerHTML") in conf_groups:
            logging.info("Se generara reporte para: %s", 
                         p_group.get_attribute("innerHTML"))
            view_groups.append([
                                p_group.get_attribute("innerHTML"), 
                                p_group.get_attribute("href")
                               ])
    #driver.close() 
    
    #Arrancando el loop para lanzar los threads
    #threads = []
    logging.info("Limpiando directorio de salida")
    try:
        os.remove(join(configuracion['output_dir'], 'Arbor_Networks_APS-View_Protection_Group.pdf'))
    except:
        pass
    for gp_url in tqdm(view_groups, desc="Descargando PDFs", unit="pdf"):
        #Crea el directorio de slaida si no existe"
        #setoutput.checkmkdir('output/' + gp_url[0])
        hilo = descargapdf.descargapdf(driver, 
                                       gp_url,
                                       fechas,
                                       configuracion) 
#                                       fechas['mes_ini'], 
#                                       fechas['mes_fin'], 
#                                       fechas['dia_ini'], 
#                                       fechas['dia_fin'], 
#                                       fechas['hora_ini'],
#                                       fechas['hora_fin'], 
#                                       fechas['start_meridian'], 
#                                       fechas['end_meridian'], 
#                                       configuracion['endpoint'], 
#                                       configuracion['output_dir'], 
#                                       configuracion['pdf_timeout'])
        hilo.start()
        hilo.join()
        #threads.append(hilo)

    #Esprando que los hilos terminen
    #for t in threads:
        #t.join()
    driver.close()
    #Genera el archivo .docx
    logging.info("Generando reporte final...")
    anio = str(fechas['current_year'])
    reporte = 'Reporte_Pravail_APS_' + str(fechas['marcial_fin']) + '_Horas_' + configuracion['hostname'] + '_' + str(fechas['dia_fin']) + str(fechas['mes_fin']) + str(fechas['year_fin']) + '.docx'
    gendocx.generadoc(configuracion, 
            reporte,
            #configuracion['output_dir'],
            #configuracion['hostname'],
            view_groups,
            fechas
            #str(fechas['dia_ini']) + '/' + str(fechas['mes_ini']) + '/' + anio + '  ' + str(fechas['marcial_ini']) + ':00 HORAS',
            #str(fechas['dia_fin']) + '/' + str(fechas['mes_fin']) + '/' + anio + '  ' + str(fechas['marcial_fin']) + ':00 HORAS',
            #configuracion['guardapdf']
            )
    logging.info("Se completo la generacion del reporte %s", reporte)

if __name__ == "__main__":
    main()
