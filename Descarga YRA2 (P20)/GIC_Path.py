#SEGUNDO EN CORRER DE LOS ARCHIVOS GIC

import tkinter as tk
import pickle
import GIC_Mover


class Archivo_GIC:
    def __init__(self, master):
        
        self.master = master

        master.title('Confirmar la Descarga del Archivo GIC') #Titulo en el Pop up de ingresar Usuario y contraeña

        # Load saved Path if they exist
        try:
            with open('Path_GIC.bin', 'rb') as f:
                self.Path_GIC = pickle.load(f)
        except:
            self.Path_GIC = {'Path': '', 'Nombre_GIC': ''}

        # Create labels and input fields
        self.Path_label = tk.Label(master, text='SEGUIR LAS SIGUIENTES INDICACIONES (Si Edge te solicita conservar o eliminar el archivo GIC):')
        self.Path_label.grid(row=0, column=0, padx=30, pady=10)

        self.Path_label = tk.Label(master, text='1. Abrir la Ventana de Edge de "DataQ Production" que se acaba de ejecutar')
        self.Path_label.grid(row=2, column=0, padx=30, pady=10)

        self.Path_label = tk.Label(master, text='2. Click a "Conservar" en la ventana de descarga de Edge, si no esta abierta, abrirla y clickear "Conservar el archivo"')
        self.Path_label.grid(row=3, column=0, padx=30, pady=10)

        self.Path_label = tk.Label(master, text='3. Una vez "Conservado el archivo" darle click a SUBMIT para continuar el proceso')
        self.Path_label.grid(row=4, column=0, padx=30, pady=10)

        self.Path_label = tk.Label(master, text='NOTA. Si no hay Ventana de Edge de "DataQ Production" abierta, entonces clickear SUBMIT')
        self.Path_label.grid(row=6, column=0, padx=30, pady=10)


        # Create submit button
        self.submit_button = tk.Button(master, text='Submit', command=self.submit)
        self.submit_button.grid(row=7, column=0, padx=5, pady=5)

        # Lift the window to the front
        self.master.attributes('-topmost', True)

    def submit(self):
       
        #   Close the window and end the program pero si quieren seguir las varialbles se debe pner return al final del todo
        self.master.destroy()


        #   SE EJECUTA MOVER EL GIC
        GIC_Mover.Mover_GIC()
       
        with open('Path_GIC.bin', 'wb') as f:
            pickle.dump(self.Path_GIC, f)

        #   Esto permte que se cierre la ventana emergente con self.master.destroy() pero que las variables no se borren

        return

#       """""""""En dado caso que quiera ejecutarlo aca en el archivo:""""""""""
#if __name__ == '__main__':
#    root = tk.Tk()
#    root.iconbitmap(r"C:\Users\migumart\OneDrive - Nokia\Archivos personales\Automatizacion Python\Descarga YRA2 (P20)\nokia.ico")
#    # el "r" es para que el path de la imagen no tome como caracteres especiales los slash "\" sino como texto
#    input_form = Archivo_GIC(root)
#    root.mainloop()

