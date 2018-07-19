#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon
from os import abort
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def navegador(proxy=None, port=None, out_dir='/tmp'):
    """
        Configura el perfil del browser a invocar
    """
    profile = webdriver.FirefoxProfile()

    if proxy:
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", proxy)
        profile.set_preference("network.proxy.socks_port", int(port))
        profile.set_preference("network.proxy.socks_version", 5)
    
    profile.set_preference("browser.download.panel.shown", False)
    profile.set_preference("browser.helperApps.neverAsk.openFile","application/pdf")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", out_dir)
    profile.set_preference("browser.safebrowsing.downloads.enabled", False)
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
          "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream")
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.manager.focusWhenStarting", False)
    profile.set_preference("browser.download.useDownloadDir", True)
    profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference("browser.download.manager.closeWhenDone", True)
    profile.set_preference("browser.download.manager.showAlertOnComplete", False)
    profile.set_preference("browser.download.manager.useWindow", False)
    profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
    profile.set_preference("pdfjs.disabled", True)
    
    profile.update_preferences()
    try:
        driver = webdriver.Firefox(firefox_profile=profile)
        return driver
    except:     
        print "ERROR; No se pudo generar una instancia de Firefox, revise que el webdriver gecko este en el PATH"
        abort()
         

