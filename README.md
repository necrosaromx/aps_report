# aps_report
Herramienta para descarga de reportes (pdf) automatizada de Grupos de proteccion en Arbor Pravail APS 

Esta herramienta se encarga de descargar archivos PDF de grupos de protección de un equpo ARBOR Pravail APS de manera automatizada
Haace uso de Selenium Webdriver sobre Firefox, los reportes se pueden conservar en PDF o auotmáticamente se agregan como imágenes a un archivo Word formato docx

Requisitos:
- Gecko WebDriver
- Firefox

Es necesario crear un directorio conf con al menos los siguientes archivos:

default.conf
listado-grupos.txt
plantilla.docx

default.conf:

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

