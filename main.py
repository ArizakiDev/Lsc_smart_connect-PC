import tkinter as tk
from tkinter import messagebox, ttk
from tuya_iot import TuyaOpenAPI, TUYA_LOGGER
from PIL import Image, ImageTk

# Configuration des identifiants API Tuya
ACCESS_ID = "ton_access_id"  # Remplace avec ton ACCESS_ID Tuya
ACCESS_KEY = "ton_access_key"  # Remplace avec ton ACCESS_KEY Tuya
API_REGION = "eu"  # ou "us", "cn", selon ta région
USERNAME = "ton_email"  # Ton email utilisé pour LSC Smart Connect
PASSWORD = "ton_mot_de_passe"  # Mot de passe de ton compte

# Classe principale de l'application
class TuyaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lsc Smart Connect - by Arizaki")
        self.geometry("500x400")

        self.label_info = tk.Label(self, text="Connexion à l'API Tuya...")
        self.label_info.pack(pady=10)

        self.device_listbox = tk.Listbox(self)
        self.device_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.button_show_info = tk.Button(self, text="Afficher infos appareil", command=self.show_device_info)
        self.button_show_info.pack(pady=5)

        self.api = TuyaOpenAPI(f"https://openapi.{API_REGION}.tuyaus.com", ACCESS_ID, ACCESS_KEY)
        self.connect_to_api()

    def connect_to_api(self):
        try:
            self.api.connect(USERNAME, PASSWORD)
            messagebox.showinfo("Succès", "Connexion réussie à l'API Tuya !")
            self.load_devices()
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de se connecter : {str(e)}")

    def load_devices(self):
        try:
            devices = self.api.get("/v1.0/users/{}/devices".format(self.api.token_info.uid))
            self.devices = devices['result']
            self.display_device_list()
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger les appareils : {str(e)}")

    def display_device_list(self):
        self.device_listbox.delete(0, tk.END)
        for device in self.devices:
            self.device_listbox.insert(tk.END, f"{device['name']} - {device['id']}")

    def show_device_info(self):
        selected_index = self.device_listbox.curselection()
        if selected_index:
            device = self.devices[selected_index[0]]
            device_name = device['name']
            device_id = device['id']
            device_category = device['category']
            device_status = device.get('status', 'N/A')

            messagebox.showinfo("Info Appareil",
                                f"Nom: {device_name}\nID: {device_id}\nCatégorie: {device_category}\nStatut: {device_status}")
        else:
            messagebox.showwarning("Attention", "Aucun appareil sélectionné !")
            
if __name__ == "__main__":
    app = TuyaApp()
    app.mainloop()
