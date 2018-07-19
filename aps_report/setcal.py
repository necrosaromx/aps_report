#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
import logging
import calcdates

#funcion que manipula los calendarios para poner fecha inicio y fin
def set_year(driver, year_to_set):
    """
        Recibe un año e intenta hacer click hasta llegar a el
    """
    logging.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>INTENTANDO COLOCAR EL AÑO %s", year_to_set)
    title = driver.find_element_by_xpath("//div[@id='caltitle']").get_attribute("innerHTML")
    selected_year = title.split()[1]
    if int(selected_year) > int(year_to_set):
        while int(selected_year) != int(year_to_set): 
            logging.debug("While IZQ: Click hacia la izquierda")
            driver.find_element_by_id("calprev").click()
            selected_year = driver.find_element_by_xpath("//div[@id='caltitle']").get_attribute("innerHTML").split()[1]
            logging.debug("WHILE IZQ: Año confugurado despues de click %s", int(selected_year))
    elif int(selected_year) < int(year_to_set):
        while int(selected_year) != int(year_to_set): 
            logging.debug("While DER: Click hacia la Derecha")
            driver.find_element_by_id("calnext").click()
            selected_year = driver.find_element_by_xpath("//div[@id='caltitle']").get_attribute("innerHTML").split()[1]
            logging.debug("WHILE DER: Año confugurado despues de click %s", int(selected_year))

def set_month(driver, mes_to_set):
    """
        Recibe un mes e intenta hacer click hasta llegar a el
    """
    logging.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>INTENTANDO COLOCAR EL MES %s", mes_to_set)
    title = driver.find_element_by_xpath("//div[@id='caltitle']").get_attribute("innerHTML")
    selected_month = title.split()[0]
    if int(calcdates.mestotext(selected_month)) > int(mes_to_set):
        logging.debug("Mes seleccionado %s", selected_month)
        selected_month_int = calcdates.mestotext(selected_month)
        logging.debug("valor numerico del mes seleccionado: %s", selected_month_int)
        while selected_month_int != int(mes_to_set):
            logging.debug("While IZQ: Click hacia la izquierda")
            driver.find_element_by_id("calprev").click()
            selected_month = driver.find_element_by_xpath("//div[@id='caltitle']").get_attribute("innerHTML").split()[0]
            logging.debug("WHILE IZQ: Mes confugurado despues de click %s", selected_month)
            selected_month_int = int(calcdates.mestotext(selected_month))
            logging.debug("valor numerico del mes seleccionado: %s", selected_month_int)
    elif calcdates.mestotext(selected_month) < int(mes_to_set):
        logging.debug("ELIF: mes seleccionado %s", selected_month)
        while selected_month_int != int(mes_to_set):
            logging.debug("WHILE DER:Click hacia la derecha")
            driver.find_element_by_id("calnext").click()
            selected_month = driver.find_element_by_xpath("//div[@id='caltitle']").get_attribute("innerHTML").split()[0]
            logging.debug("WHILE DER:Mes confugurado despues de click %s", selected_month)
            selected_month_int = int(calcdates.mestotext(selected_month))
            logging.debug("valor numerico del mes seleccionado: %s", selected_month_int)

def set_day(driver, dia):
    """
        Recibe un dia y hace click directamente en el que esta habilitado en el calendario
    """
    logging.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>INTENTANDO COLOCAR EL DIA %s", dia)
    #El problema es distinguir el dia que esta resaltado, el sombreado es el primero que encuentra  
    logging.debug("Seleccionando el dia %s" , dia)
    #Iteramos los tags hasta encontrae el que NO esta deshabilitado
    for tag in driver.find_elements_by_xpath('//a[@href="#' + str(int(dia)) +'"]'):
        #Si encuentra que no tiene el caloff, regresa numero negavito (buscamos que NO tenga caloff)
        if  tag.get_attribute("outerHTML").find("caloff") < 0:
            dia = tag
    dia.click()

    
def set_hour(driver, hora, minuto, meridiano):
    """
        Recibe un hora, minutos y meridiano y los coloca
    """
    logging.debug("Configurando hora inicio %s", hora)
    driver.find_element_by_xpath("//select[@name='hour']/option[@value='" + str(hora) + "']").click()
    logging.debug("intentando seleccionar minuto")
    driver.find_element_by_xpath("//select[@name='minute']/option[@value='" + str(minuto) + "']").click()
    logging.debug("intentando seleccionar meridiano")
    driver.find_element_by_xpath("//select[@name='meridian']/option[@value='" + meridiano + "']").click()

def set_cal(driver, fechas):
    """
        Cambia los calendarios a las fechas indicadas
    """
    #Se inicializaron las variables por flojera, ya estaban antes por argumentos y ahora se pasa toda el dict "fechas"
    mes_ini = fechas['mes_ini']
    mes_fin = fechas['mes_fin']
    dia_ini = fechas['dia_ini']
    dia_fin = fechas['dia_fin']
    hora_ini = fechas['hora_ini']
    hora_fin = fechas['hora_fin']
    minuto_ini = '00'
    minuto_fin = '00'
    year_ini = fechas.get('year_ini')
    year_fin = fechas.get('year_fin')
    start_meridian = fechas['start_meridian']
    end_meridian = fechas['end_meridian']

    logging.debug("Haciendo click en From, esto hará visibles los input de fechas from y to")
    driver.find_element_by_xpath("//*[contains(text(), 'From')]").click()

    logging.debug("Configurando calendario From, esto debe abrir el calendario from")
    driver.find_element_by_xpath("//input[@name='time_start']").click()

    set_year(driver, year_ini)
    set_month(driver, mes_ini)
    set_day(driver, dia_ini)
    set_hour(driver, hora_ini, minuto_ini, start_meridian)
 

    logging.debug("intentado abrir calendario TO")
    driver.find_element_by_xpath("//input[@name='time_end']").click()

    set_year(driver, year_fin)
    set_month(driver, mes_fin)
    set_day(driver, dia_fin)
    set_hour(driver, hora_fin, minuto_fin, end_meridian)

