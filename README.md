# aps_report
## Herramienta para descarga de reportes (pdf) automatizada de Grupos de proteccion en Arbor Pravail APS 

Esta herramienta se encarga de descargar archivos PDF de grupos de protección de un equpo ARBOR Pravail APS de manera automatizada
Haace uso de Selenium Webdriver sobre Firefox, los reportes se pueden conservar en PDF o auotmáticamente se agregan como imágenes a un archivo Word formato docx

## Requisitos:
* [Selenium](https://selenium-python.readthedocs.io/) - El binding de Selenium para python
* [Gecko WebDriver](https://github.com/mozilla/geckodriver/releases) - El webdriver para selenium con Firefox
* [Firefox](https://www.mozilla.org/es-ES/firefox/) - ¿Hay otro?

Es necesario crear un directorio conf con al menos los siguientes archivos:
```
default.conf
listado-grupos.txt
plantilla.docx
```

## default.conf:
```
[APS]
hostname = APS
endpoint = 192.168.1.1
user = admin
password = arbor
#Esta es la hora de corte matutino
cortemat = 10
#Esta es la hora de corte medio dia
cortemd = 14
#Esta es la hora de corte fin dia
cortevsp = 19
#Tiempo de espear para descarga de PDF (ciclada)
pdf_timeout = 5
#Directorio de salida
output_dir = output
#Archivo con el listado de los grupos de proteccion tal como aparcen en el APS, uno por linea 
listado = conf/gruposproteccion.txt
#Platinlla de word para reporte
plantilla = conf/templete.docx
#Bandera para mantener los PDF descargados
guardapdf = False
```
## Uso:
```
python aps_report.py --help
usage: aps_report.py [-h] [--config CONFIG_FILE]
                     [--horaini {1,2,3,4,5,6,7,8,9,10,11,12}]
                     [--horafin {1,2,3,4,5,6,7,8,9,10,11,12}]
                     [--merini {AM,PM}] [--merfin {AM,PM}]
                     [--diaini {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}]
                     [--diafin {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}]
                     [--mesini {1,2,3,4,5,6,7,8,9,10,11,12}]
                     [--mesfin {1,2,3,4,5,6,7,8,9,10,11,12}]
                     [--yearini {2013,2014,2015,2016,2017,2018}]
                     [--yearfin {2013,2014,2015,2016,2017,2018}]
                     [--keep GUARDAPDF] [--grupos LISTADO] [--debug]
Herramienta para obtener reportes de Grupos de proteccion desde Arbor APS
optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG_FILE  Archivo de configuracion a cargar
  --horaini {1,2,3,4,5,6,7,8,9,10,11,12}
                        Hora inicial de reporte
  --horafin {1,2,3,4,5,6,7,8,9,10,11,12}
                        Hora inicial de reporte
  --merini {AM,PM}      AM/PM de hora inicial
  --merfin {AM,PM}      AM/PM de hora final
  --diaini {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
                        Dia inicial de reporte
  --diafin {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
                        Dia final de reporte
  --mesini {1,2,3,4,5,6,7,8,9,10,11,12}
                        Mes inicial de reporte
  --mesfin {1,2,3,4,5,6,7,8,9,10,11,12}
                        Mes final de reporte
  --yearini {2013,2014,2015,2016,2017,2018}
                        Año inicial de reporte
  --yearfin {2013,2014,2015,2016,2017,2018}
                        Año final de reporte
  --keep GUARDAPDF      Bandera para conservar archivos PDF
  --grupos LISTADO      Archivo con listado de grupos
  --debug               Despliega debug

Las opciones establecidas por linea de comando tienen prioridad sobre las del archivo de configuracion. Saul Vargas @ SCITUM 2018
``` 
