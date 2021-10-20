import psutil
from tkinter import messagebox

bateria = psutil.sensors_battery()
percent = str(bateria.percent)

messagebox.showinfo(title="Bateria",
                    message=f"Bateria em {percent}%")

if bateria.percent < 25:
    messagebox.showwarning(title="Bateria Baixa",
                           message=f"Bateria em {percent}%")
