import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytubefix import YouTube
import subprocess

# Programa hecho en Tkinter, llamado "Geogaddi" que busca poder descargar vídeos y audio de YouTube, álbumes de Bandcamp, y música de Soundcloud.
# Autor: mentalapraxia
# Fecha: 28-12-2024 

# Crear los widgets solo para la pestaña de YouTube
def youtube_tab_content(parent):
    label = ttk.Label(parent, text="Descargar videos de YouTube", font=("Arial", 16))
    label.pack(pady=20)

    url_label = ttk.Label(parent, text="Enlace del video de YouTube:")
    url_label.pack(pady=10)

    url_entry = ttk.Entry(parent, width=60)
    url_entry.pack(pady=5)

    download_button = ttk.Button(parent, text="Descargar", command=lambda: download_video(url_entry))
    download_button.pack(pady=20)

    return url_entry

# Crear los widgets solo para la pestaña de Bandcamp
def bandcamp_tab_content(parent):
    label = ttk.Label(parent, text="Descargar música de Bandcamp", font=("Arial", 16))
    label.pack(pady=20)

    url_label = ttk.Label(parent, text="Enlace del álbum de Bandcamp:")
    url_label.pack(pady=10)

    url_entry = ttk.Entry(parent, width=60)
    url_entry.pack(pady=5)

    download_button = ttk.Button(parent, text="Descargar", command=lambda: download_bandcamp_album(url_entry))
    download_button.pack(pady=20)

    return url_entry  

# Lógica para descargar vídeos de YouTube con pytubefix
def download_video(url_entry):
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "Por favor, introduce un enlace de YouTube.")
        return

    save_path = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    if not save_path:
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_title = yt.title
        stream.download(output_path=save_path)
        messagebox.showinfo("Completado", f"El video '{video_title}' ha sido descargado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al descargar el video: {e}")

# Lógica para descargar música de Bandcamp con bandcamp-dl
def download_bandcamp_album(url_entry):
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "Por favor, introduce un enlace de Bandcamp.")
        return
    
    save_path = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    if not save_path:
        return
    
    try:
        subprocess.run(["bandcamp-dl", "-d", save_path, url], check=True)
        messagebox.showinfo("Completado", "El álbum de Bandcamp ha sido descargado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al descargar el álbum de Bandcamp: {e}")

# Propiedades de la ventana
ventana = tk.Tk()
ventana.title("Geogaddi")
ventana.geometry("500x300")
ventana.resizable(False, False)
ventana.iconphoto(True, tk.PhotoImage(file="Projects/Tkinter/Geogaddi Code/geogaddi2.png"))

# Crear notebook
notebook = ttk.Notebook(ventana)

# Crear Frames para cada pestaña
youtube_tab = ttk.Frame(notebook)
bandcamp_tab = ttk.Frame(notebook)

# Añadir pestañas al Notebook
notebook.add(youtube_tab, text="YouTube")
notebook.add(bandcamp_tab, text="Bandcamp")

# Empaquetar el Notebook
notebook.pack(expand=True, fill="both")

# Añadir contenido a cada pestaña
youtube_url_entry = youtube_tab_content(youtube_tab)  
bandcamp_url_entry = bandcamp_tab_content(bandcamp_tab)

# Modo oscuro
def enable_dark_mode():
    style = ttk.Style()
    style.theme_use("clam")
    
    # Fondo y texto de la ventana
    style.configure("TFrame", background="#2B2B2B")
    style.configure("TLabel", background="#2B2B2B", foreground="#E0E0E0", font=("Arial", 12))
    style.configure("TButton", background="#444444", foreground="#FFFFFF", font=("Arial", 11, "bold"))
    style.map("TButton", 
              background=[("active", "#555555")],
              foreground=[("active", "#FFFFFF")])
    style.configure("TEntry", fieldbackground="#3E3E3E", foreground="#FFFFFF", insertcolor="#FFFFFF", font=("Arial", 11))

    style.configure("TNotebook", background="#2B2B2B", tabmargins=[5, 5, 5, 0])
    style.configure("TNotebook.Tab", background="#3B3B3B", foreground="#FFFFFF", font=("Arial", 10, "bold"))
    style.map("TNotebook.Tab", 
              background=[("selected", "#444444")],
              foreground=[("selected", "#FFFFFF")])

# Comentar si se quiere el modo claro normal
enable_dark_mode()


# Loop principal
ventana.mainloop()
