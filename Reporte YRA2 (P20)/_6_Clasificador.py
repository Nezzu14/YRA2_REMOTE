import pandas as pd
import os
from datetime import datetime


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

    # ----Define first DataFrame
    excel_YRA2 = pd.read_excel(YRA2_file_path)

    # ----Define second DataFrame
    excel_GIC = pd.read_excel(GIC_file_path)

    excel_YRA2.columns = excel_YRA2.columns.str.strip()
    excel_YRA2 = excel_YRA2.dropna(how='all')
    excel_YRA2 = excel_YRA2.dropna(axis=1, how='all')

    excel_GIC.columns = excel_GIC.columns.str.strip()
    excel_GIC = excel_GIC.dropna(how='all')
    excel_GIC = excel_GIC.dropna(axis=1, how='all')    

    excel_YRA2['GIC']=excel_YRA2['GIC'].astype(str)
    excel_GIC[['GIC', 'PC Business Group']]=excel_GIC[['GIC', 'PC Business Group']].astype(str)

    vlookup_df = pd.merge(excel_YRA2,
                         excel_GIC[['GIC', 'PC Business Group']],
                         on ='GIC',
                         how ='left')

    # ----View df1
    print(vlookup_df)

    # ----Save vlookup_df to Excel file
    vlookup_df.to_excel(doc_final_REPORTE_path, index=False)

    print("========================================================================")
    print("----Fin del vlookup entre reporte YRA2 y archivo GIC")
    print("========================================================================\n")

    print("==============================================================================================================")
    print("====FINALIZACION DE -VLOOKUP-")
    print("==============================================================================================================\n")



#       """""""""En dado caso que quiera ejecutarlo aca en el archivo:""""""""""
#vlookup()
