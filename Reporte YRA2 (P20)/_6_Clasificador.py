import pandas as pd
import os
from datetime import datetime
import shutil
import openpyxl


def vlookup():

   print("==============================================================================================================")
   print("====INICIALIZACION DE -VLOOKUP-")
   print("==============================================================================================================\n")

   # ----Toma la fecha actual de hoy
   fecha= "{:%Y_%m_%d}".format(datetime.now())
   
   # ----Se definen los paths de los archivos, el archivo .xlsx y el archivo .csv
   YRA2_file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'YRA2') + "\\YRA2_TMOBILE_" + fecha + ".xlsx"
   GIC_file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'YRA2') + "\\F&C GIC - SIG PC List - " + fecha + ".xlsx"
   
   # ----Se define el nombre y path del documento final
   doc_final_REPORTE_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'YRA2','Reporte final') + "\\ Reporte_YRA2_TMOBILE_" + fecha + ".xlsx"
   filename_doc_final_REPORTE_path = "Reporte_YRA2_TMOBILE_" + fecha + ".xlsx"

   # ----Check if file already exists
   directorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','YRA2','Reporte final')
   try:
      os.stat(directorio)
   except:
      os.mkdir(directorio)
   
   print("========================================================================")
   print("Archivo xlsx = " + YRA2_file_path)
   print("Archivo csv = " + GIC_file_path)
   print("Archivo final = " + doc_final_REPORTE_path)
   print("========================================================================\n")

   print("========================================================================")
   print("----Inicio del vlookup entre reporte YRA2 y archivo GIC")
   print("========================================================================\n")
   
   # ----Define first DataFrame, especificando que el encabezado empieza en le fila 2 ya que en el codigo de columna la fila 1 es 0 entonces la 2 es 1
   excel_YRA2 = pd.read_excel(YRA2_file_path, header=1)
   # ----Define second DataFrame
   excel_GIC = pd.read_excel(GIC_file_path)

   # ----Se renombra el encabezado de la columna AK1=GIC code a AK1=GIC
   excel_YRA2 = excel_YRA2.rename(columns={'GIC code': 'GIC'})

   # ----No toma las columnas que estan en blanco
   #excel_YRA2.columns = excel_YRA2.columns.str.strip()
   #excel_YRA2 = excel_YRA2.dropna(how='all')
   #excel_YRA2 = excel_YRA2.dropna(axis=1, how='all')

   # ----No toma las columnas que estan en blanco
   excel_GIC.columns = excel_GIC.columns.str.strip()
   excel_GIC = excel_GIC.dropna(how='all')
   excel_GIC = excel_GIC.dropna(axis=1, how='all')    
   
   print(excel_YRA2.columns)

   # ----Esto convierte los datos de las columnas [['...']] en object
   excel_YRA2['GIC']=excel_YRA2['GIC'].astype(str)
   excel_GIC[['GIC', 'PC Business Group']]=excel_GIC[['GIC', 'PC Business Group']].astype(str)

   print(excel_YRA2['GIC'])
   print(excel_GIC[['GIC', 'PC Business Group']])
   
   vlookup_df = pd.merge(excel_YRA2,  
                         excel_GIC[['GIC', 'PC Business Group']], 
                         on ='GIC', 
                         how ='left')
   
   # ----View df1
   print(vlookup_df)
   
   # ----Check if file already exists
   if os.path.isdir(doc_final_REPORTE_path):
       print("========================================================================")
       print('----'+filename_doc_final_REPORTE_path, '____ Exists in the destination path!')
       print("========================================================================\n")
       shutil.rmtree(doc_final_REPORTE_path)
   
   elif os.path.isfile(doc_final_REPORTE_path):
       os.remove(doc_final_REPORTE_path)
       print("========================================================================")
       print('----'+filename_doc_final_REPORTE_path, '____ Deleted in', 'YRA2', 'becuase is duplicate')
       print("========================================================================\n")

   print("========================================================================")
   print("----Fin del vlookup entre reporte YRA2 y archivo GIC")
   print("========================================================================\n")

   print("========================================================================")
   print("----Inicio de guardado del DataFrame en archivo .XLSX")
   print("----Archivo xlsx final =" + doc_final_REPORTE_path)
   print("========================================================================\n")

   # ----Save vlookup_df to Excel file
   vlookup_df.to_excel(doc_final_REPORTE_path, index=False)

   print("========================================================================")
   print("----Fin de guardado del DataFrame en archivo .XLSX")
   print("----Archivo xlsx final = " + doc_final_REPORTE_path)
   print("========================================================================\n")

   print("==============================================================================================================")
   print("====FINALIZACION DE -VLOOKUP-")
   print("==============================================================================================================\n")



#       """""""""En dado caso que quiera ejecutarlo aca en el archivo:""""""""""
#vlookup()