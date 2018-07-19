#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
"""
    Cargador de configuracion 
"""
import ConfigParser
import os

def load_config(file_name = 'default.conf', section = "default"):
    """ 
        Carga la configuracion del archivo especificado y lo regresa en dict
    """
    currentwd = os.getcwd()
    config = ConfigParser.ConfigParser()
    try:
        if not os.path.isfile(os.path.join(currentwd, file_name)):
            raise ValueError('No se pudo leer el contenido del archivo de configuracion ' + file_name)
        config.read(os.path.join(currentwd, file_name))
        if not config.has_section(section):
            raise ValueError('No se encontro la seccion [' + section + '] en el archivo de configuracion')
        configuracion = dict(config.items(section))
        if len(configuracion) == 0: 
            raise ValueError('No existen atributos en la seccion [' + section + '] del archivo de configuracion')
        return configuracion
    except ValueError as val:
        print(val)
        os.abort()
