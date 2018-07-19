#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
import selenium.webdriver.support.ui as ui
import logging
import threading
import login
import browser
import setcal
import os
from os.path import isfile, join
"""
    Clase para threads
"""
class descargapdf(threading.Thread):
    def __init__(self, driver, gp_url, fechas, configuracion):
        threading.Thread.__init__(self)
        self.driver = driver
        self.gp_url = gp_url
        self.fechas = fechas
        self.configuracion = configuracion
        self.output_dir = configuracion['output_dir']
        self.mes_ini = fechas['mes_ini']
        self.mes_fin = fechas['mes_fin']
        self.dia_ini = fechas['dia_ini']
        self.dia_fin = fechas['dia_fin']
        self.hora_ini = fechas['hora_ini']
        self.hora_fin = fechas['hora_fin']
        self.start_meridian = fechas['start_meridian']
        self.end_meridian = fechas['end_meridian']
        self.endpoint = configuracion['endpoint']
        self.pdf_timeout = configuracion['pdf_timeout']
    def run(self):
        logging.debug("%s> ", self.gp_url[0])
        
        logging.debug("%s> Abriendo detalle de grupo %s", self.gp_url[0], self.gp_url[0])
        self.driver.get(self.gp_url[1])
        
        #Cambiamos los calendarios:
        setcal.set_cal(self.driver, self.fechas)
    
        logging.debug("%s> Actualizando graficas", self.gp_url[0])
    
        wait_pdf = ui.WebDriverWait(self.driver, int(self.pdf_timeout))
        self.driver.find_element_by_xpath("//*[contains(text(), 'Update')]").click()
        wait_pdf.until(lambda driver: self.driver.find_element_by_xpath("//div[@style='display: none;']"))
        self.driver.find_element_by_xpath("//*[contains(text(), 'Update')]").click()
        wait_pdf.until(lambda driver: self.driver.find_element_by_xpath("//div[@style='display: none;']"))
        
        #Descarga de PDF 
        logging.debug("%s> Solicitando generacion de PDF", self.gp_url[0])
        self.driver.find_element_by_id("nav-id-pdf").click()
        logging.debug("%s> Esperando descarga de PDF %s segundos", self.gp_url[0], self.pdf_timeout)
        pdffile = join(self.output_dir, 'Arbor_Networks_APS-View_Protection_Group.pdf')
        try:
            wait_pdf.until(lambda driver: self.driver.find_element_by_name("nonexistantname"))
        except: 
            pass
        while not (isfile(pdffile) and os.stat(pdffile).st_size != 0):
            logging.debug("%s> Esperando descarga de PDF %s segundos", self.gp_url[0], self.pdf_timeout)
            try:
                wait_pdf.until(lambda driver: self.driver.find_element_by_name("nonexistantname"))
            except: 
                pass
        logging.debug("%s> Descarga de PDF terminada.", self.gp_url[0])

        os.rename(pdffile, join(self.output_dir, self.gp_url[0] + '.pdf'))
        logging.debug("%s> Finaliza hilo.", self.gp_url[0])

