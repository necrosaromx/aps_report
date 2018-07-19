#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
from datetime import  datetime
from datetime import  date
from datetime import  timedelta
from datetime import  time

def _calculayer():
    """
        Brinca los fines de semana hacia atras
    """
    if date.today().weekday() is 0:
        ayer = date.today() - timedelta(3)
    else:
        ayer = date.today() - timedelta(1)
    return ayer

def start(configuracion):
    """
        Regresa en diccionario la fecha de inicio de los reportes
    """
    
    cortes = [configuracion['cortemat'], configuracion['cortemd'], configuracion['cortevsp']]
    hoy = datetime.now()
    pasadas = []
    if hoy.hour < int(min(cortes)):
        hora_ini = configuracion['cortemd']
        hora_fin = configuracion['cortevsp']
        dia_fin = _calculayer()
        dia_ini = dia_fin
    else: 
        dia_fin = date.today()
        for hora in cortes:
            if hoy.hour >= int(hora):
                pasadas.append(hora)
        hora_fin = max(pasadas)

    # Esto es para calcular si ayerr cayo en domingo, de ser asi, se recorre al viernes
        if int(hora_fin) == int(configuracion['cortemat']):
            hora_ini = configuracion['cortevsp']
            dia_ini = _calculayer()
        else:
            pasadas.remove(hora_fin)
            hora_ini = max(pasadas)
            dia_ini = date.today()
    marcial_ini = hora_ini
    marcial_fin = hora_fin
    if int(hora_ini) > 12:
        start_meridian = 'PM'
        hora_ini = int(hora_ini) - 12
    else:
        start_meridian = 'AM'
        hora_ini = int(hora_ini)    
    if int(hora_fin) > 12:
        end_meridian = 'PM' 
        hora_fin = int(hora_fin) - 12
    else:
        end_meridian = 'AM'
        hora_fin = int(hora_fin)
    this_year =  date.today().strftime('%Y')
    if configuracion.get('year_ini') is None:
        year_ini = this_year
    else:
        year_ini = configuracion.get('year_ini')
    if configuracion.get('year_fin') is None:
        year_fin = this_year
    else:
        year_fin = configuracion.get('year_fin')
    return {
              'marcial_ini': marcial_ini,
              'marcial_fin': marcial_fin,
              'hora_ini': hora_ini, 
              'hora_fin': hora_fin, 
              'start_meridian': start_meridian, 
              'end_meridian': end_meridian,
              'dia_ini': dia_ini.strftime('%d'), 
              'dia_fin': dia_fin.strftime('%d'), 
              'mes_ini': dia_ini.strftime('%m'), 
              'mes_fin': dia_fin.strftime('%m'), 
              'year_ini': year_ini,
              'year_fin': year_fin,
              'hoy': date.today().strftime('%d%m%Y'), 
              'ahora': datetime.now(),
              'current_year': hoy.year,
             }

def mestotext(mes):
    """
        Regresa texto si se le envia numero de mes y viceversa
    """
    meses = {
            'January': '1', 'February': '2', 'March': '3', 'April': '4', 
            'May': '5', 'June': '6', 'July': '7', 'August': '8', 
            'September': '9', 'October': '10', 'November': '11', 
            'December': '12'
            }
    meses_inv = {
            '1': 'January', '2': 'February','3': 'March','4': 'April',
            '5': 'May','6': 'June','7': 'July','8': 'August',
            '9': 'September','10': 'October','11': 'November',
            '12': 'December'
            }
    if meses.get(str(mes)) != None:
        return meses[str(mes)]
    elif meses_inv.get(str(int(mes))) != None:
        return meses_inv[str(int(mes))]

def to_martial(hora, meridian):
    """
        Regresa la hora en formato militar
    """
    if meridian == 'PM':
        if int(hora) < 12:
            return hora + 12
        else:
            return hora
    else:
        return hora
