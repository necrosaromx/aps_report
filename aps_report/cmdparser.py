#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
from datetime import datetime 
from os.path import join
import argparse

def loadargs():
    year = datetime.now().year
    parser = argparse.ArgumentParser(description='Herramienta para obtener report'\
                                     'es de Grupos de proteccion desde Arbor APS', 
                                     epilog='Las opciones establecidas por linea de'\
                                     ' comando tienen prioridad sobre las del arc'\
                                     'hivo de configuracion. Saul Vargas @ SCITUM 2018')
    parser.add_argument('--config', action='store', 
                        help='Archivo de configuracion a cargar', 
                        dest='config_file', default=join('conf', 'default.conf'))
    parser.add_argument('--horaini', action='store', 
                        type=int,
                        choices=range(1, 13),
                        help='Hora inicial de reporte', 
                        dest='hora_ini', default=None)
    parser.add_argument('--horafin', action='store', 
                        type=int,
                        choices=range(1, 13),
                        help='Hora inicial de reporte', 
                        dest='hora_fin', default=None)
    parser.add_argument('--merini', action='store', 
                        choices=['AM', 'PM'],
                        help='AM/PM de hora inicial', 
                        dest='start_meridian', default=None)
    parser.add_argument('--merfin', action='store', 
                        choices=['AM', 'PM'],
                        help='AM/PM de hora final', 
                        dest='end_meridian', default=None)
    parser.add_argument('--diaini', action='store', 
                        type=int,
                        choices=range(1, 32),
                        help='Dia inicial de reporte', 
                        dest='dia_ini', default=None)
    parser.add_argument('--diafin', action='store', 
                        type=int,
                        choices=range(1, 32),
                        help='Dia final de reporte', 
                        dest='dia_fin', default=None)
    parser.add_argument('--mesini', action='store', 
                        type=int,
                        choices=range(1, 13),
                        help='Mes inicial de reporte', 
                        dest='mes_ini', default=None)
    parser.add_argument('--mesfin', action='store', 
                        type=int,
                        choices=range(1, 13),
                        help='Mes final de reporte', 
                        dest='mes_fin', default=None)
    parser.add_argument('--yearini', action='store', 
                        type=int,
                        choices=range(year - 5, year + 1),
                        help='Año inicial de reporte', 
                        dest='year_ini', default=None)
    parser.add_argument('--yearfin', action='store', 
                        type=int,
                        choices=range(year - 5, year + 1),
                        help='Año final de reporte', 
                        dest='year_fin', default=None)
    parser.add_argument('--keep', action='store', 
                        help='Bandera para conservar archivos PDF', 
                        dest='guardapdf', default=False)
    parser.add_argument('--grupos', action='store', 
                        help='Archivo con listado de grupos', 
                        dest='listado', default=None)
    parser.add_argument('--debug', action='store_true', 
                        help='Despliega debug', 
                        )
    line_args = parser.parse_args()
    return line_args

