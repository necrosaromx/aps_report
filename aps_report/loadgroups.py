#!/usr/bin/python
 # -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
#SCITUM 2018
import os
""" Lectura de archivo port lineas

"""

def loadnames(file_name):
    """
        Lee las lineas de (file_name) y regresa en una lista
    """
    names = []
    try:
        with open(file_name) as f:
            names = list(str.rstrip(i) for i in f)
        return names
    except:
        print 'No se pudo leer el archivo: ' + file_name
        os.abort() 
