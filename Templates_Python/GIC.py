#PRIMERO EN CORRER DE LOS ARCHIVOS GIC

from selenium import webdriver
from selenium.webdriver.common.by import By
#import shutil
#import os
import time
from GIC_Path import Archivo_GIC
import tkinter as tk
import pywinauto

def Descargar_GIC():   

    print("========================================================================================================================")
    print("====INICIALIZACION DE LA DESCARGA DEL ARCHIVO GIC")
    print("========================================================================================================================\n")

    # ----Inicializa el navegador Edge con las opciones configuradas (Genera error -Abre sin el usuario-)
    #edge_driver_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"
    #driver = webdriver.Edge(executable_path=edge_driver_path)

    # ----Inicia el navegador Edge (-Abre sin el usuario-) Alternatuiva 2 (Se ejecuta en Edge como Codigo de prueba ?)
    driver = webdriver.Edge()

    print("========================================================================")
    print("----Inicio del Navegador Edge")
    print("========================================================================\n")

    # ----Minimizar la ventana de Edge (Solo funciona para el inicio)
    driver.minimize_window()

    # Direccionamiento a la Pagina de GIC y descarga el archivo de GIC
    driver.get('http://dataq-prod.int.net.nokia.com:7780/')
    driver.set_window_size(1500, 700)
    driver.switch_to.frame(0)
    driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) tr:nth-child(3) span").click()
    driver.find_element(By.LINK_TEXT, "Export Excel").click()

    print("========================================================================")
    print("----Descargando Archivo GIC")
    print("========================================================================\n")
    
    # wait for the download
    time.sleep(15)

    #   En teoria deberia permitir la descarga del archivo "corrupto"
    # time.sleep(20)
    # alert = driver.switch_to.alert
    # alert.accept()
    # time.sleep(5)

    #   Ejecutar buscar el Path del Archivo del GIC (Class) es decir Ejecuta el archivo py. GIC_Path
    root = tk.Tk()
    root.iconbitmap(r"C:\Users\migumart\OneDrive - Nokia\Archivos personales\Automatizacion Python\Descarga YRA2 (P20)\nokia.ico")
    input_form = Archivo_GIC(root)
    root.mainloop()

    # close the browser
    driver.quit()

    print("========================================================================================================================")
    print("====FINALIZACION DE LA DESCARGA DEL ARCHIVO GIC")
    print("========================================================================================================================\n")


#  Ejecutar Descarga_GIC junto a Buscar Archivo del GIC
if __name__ == '__main__':
    Descargar_GIC()
    
