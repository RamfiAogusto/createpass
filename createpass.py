import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import webbrowser
import json
import os

class GeneradorContraseñasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Estilo
        self.root.configure(bg='#f0f0f0')
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TLabel', background='#f0f0f0')
        
        # Frame principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill='both', expand=True)
        
        # Frame para opciones de generación
        opciones_frame = ttk.LabelFrame(main_frame, text="Opciones", padding="10")
        opciones_frame.pack(fill='x', pady=5)
        
        # Longitud de la contraseña
        ttk.Label(opciones_frame, text="Longitud:").pack(side='left', padx=5)
        self.longitud_var = tk.StringVar(value="12")
        self.longitud_entry = ttk.Entry(opciones_frame, textvariable=self.longitud_var, width=5)
        self.longitud_entry.pack(side='left', padx=5)
        
        # Frame para checkboxes
        checks_frame = ttk.Frame(main_frame)
        checks_frame.pack(fill='x', pady=5)
        
        # Opciones en dos columnas
        left_frame = ttk.Frame(checks_frame)
        left_frame.pack(side='left', padx=20)
        right_frame = ttk.Frame(checks_frame)
        right_frame.pack(side='left', padx=20)
        
        self.usar_mayusculas = tk.BooleanVar(value=True)
        ttk.Checkbutton(left_frame, text="Mayúsculas", 
                       variable=self.usar_mayusculas).pack(anchor='w')
        
        self.usar_minusculas = tk.BooleanVar(value=True)
        ttk.Checkbutton(left_frame, text="Minúsculas", 
                       variable=self.usar_minusculas).pack(anchor='w')
        
        self.usar_numeros = tk.BooleanVar(value=True)
        ttk.Checkbutton(right_frame, text="Números", 
                       variable=self.usar_numeros).pack(anchor='w')
        
        self.usar_simbolos = tk.BooleanVar(value=True)
        ttk.Checkbutton(right_frame, text="Símbolos", 
                       variable=self.usar_simbolos).pack(anchor='w')
        
        # Frame para texto específico
        texto_frame = ttk.LabelFrame(main_frame, text="Texto específico", padding="10")
        texto_frame.pack(fill='x', pady=5)
        
        self.texto_especifico_var = tk.StringVar()
        ttk.Entry(texto_frame, textvariable=self.texto_especifico_var, 
                 width=30).pack(side='left', padx=5)
        
        # Posición del texto específico
        self.posicion_texto = tk.StringVar(value="aleatorio")
        ttk.Radiobutton(texto_frame, text="Inicio", 
                       variable=self.posicion_texto, 
                       value="inicio").pack(side='left', padx=5)
        ttk.Radiobutton(texto_frame, text="Final", 
                       variable=self.posicion_texto, 
                       value="final").pack(side='left', padx=5)
        ttk.Radiobutton(texto_frame, text="Aleatorio", 
                       variable=self.posicion_texto, 
                       value="aleatorio").pack(side='left', padx=5)
        
        # Frame para la contraseña generada
        contraseña_frame = ttk.LabelFrame(main_frame, text="Contraseña generada", padding="10")
        contraseña_frame.pack(fill='x', pady=5)
        
        self.contraseña_var = tk.StringVar()
        self.contraseña_entry = ttk.Entry(contraseña_frame, 
                                        textvariable=self.contraseña_var,
                                        width=40)
        self.contraseña_entry.pack(pady=5)
        
        # Botón generar
        tk.Button(contraseña_frame, 
                 text="Generar Contraseña",
                 command=self.generar_y_mostrar,
                 bg='#e1e1e1',
                 width=15).pack(pady=5)
        
        # Frame para botones principales
        botones_frame = ttk.Frame(main_frame)
        botones_frame.pack(fill='x', pady=10)
        
        # Primera fila de botones
        botones_fila1 = ttk.Frame(botones_frame)
        botones_fila1.pack(fill='x', pady=5)
        
        tk.Button(botones_fila1, text="Copiar", 
                 command=self.copiar_contraseña,
                 bg='#e1e1e1', width=15).pack(side='left', padx=5)
        
        tk.Button(botones_fila1, text="Verificar Fortaleza", 
                 command=self.verificar_fortaleza,
                 bg='#e1e1e1', width=15).pack(side='right', padx=5)
        
        # Segunda fila de botones
        botones_fila2 = ttk.Frame(botones_frame)
        botones_fila2.pack(fill='x', pady=5)
        
        tk.Button(botones_fila2, text="Guardar", 
                 command=self.mostrar_dialogo_guardar,
                 bg='#e1e1e1', width=15).pack(side='left', padx=5)
        
        tk.Button(botones_fila2, text="Ver Guardadas", 
                 command=self.ver_contraseñas,
                 bg='#e1e1e1', width=15).pack(side='right', padx=5)
        
        # Etiqueta de estado
        self.estado_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.estado_var).pack(pady=5)

    def generar_contraseña(self, longitud=12):
        caracteres = ""
        caracteres_obligatorios = []
        
        # Añadir caracteres según las opciones seleccionadas
        if self.usar_mayusculas.get():
            caracteres += string.ascii_uppercase
            caracteres_obligatorios.append(random.choice(string.ascii_uppercase))
            
        if self.usar_minusculas.get():
            caracteres += string.ascii_lowercase
            caracteres_obligatorios.append(random.choice(string.ascii_lowercase))
            
        if self.usar_numeros.get():
            caracteres += string.digits
            caracteres_obligatorios.append(random.choice(string.digits))
            
        if self.usar_simbolos.get():
            caracteres += string.punctuation
            caracteres_obligatorios.append(random.choice(string.punctuation))
        
        if not caracteres:
            return "Seleccione al menos un tipo de caracteres"
        
        # Obtener el texto específico
        texto_especifico = self.texto_especifico_var.get()
        
        # Calcular cuántos caracteres aleatorios necesitamos
        caracteres_restantes = longitud - len(texto_especifico) - len(caracteres_obligatorios)
        
        if caracteres_restantes < 0:
            return "La longitud es muy corta para incluir todos los requisitos"
        
        # Generar el resto de la contraseña
        contraseña = caracteres_obligatorios + [random.choice(caracteres) for _ in range(caracteres_restantes)]
        random.shuffle(contraseña)
        contraseña = ''.join(contraseña)
        
        # Añadir el texto específico según la posición seleccionada
        if texto_especifico:
            posicion = self.posicion_texto.get()
            if posicion == "inicio":
                contraseña = texto_especifico + contraseña
            elif posicion == "final":
                contraseña = contraseña + texto_especifico
            else:  # aleatorio
                punto_insercion = random.randint(0, len(contraseña))
                contraseña = contraseña[:punto_insercion] + texto_especifico + contraseña[punto_insercion:]
        
        return contraseña

    def generar_y_mostrar(self):
        try:
            longitud = int(self.longitud_var.get())
            if longitud < 4:
                self.estado_var.set("La longitud mínima es 4 caracteres")
                return
                
            contraseña = self.generar_contraseña(longitud)
            self.contraseña_var.set(contraseña)
            
            if isinstance(contraseña, str) and len(contraseña) == longitud:
                self.estado_var.set("Contraseña generada exitosamente")
            else:
                self.estado_var.set(contraseña)  # Mostrar mensaje de error
                
        except ValueError:
            self.estado_var.set("Por favor, ingrese un número válido")

    def copiar_contraseña(self):
        contraseña = self.contraseña_var.get()
        if contraseña:
            try:
                pyperclip.copy(contraseña)
                self.estado_var.set("Contraseña copiada al portapapeles")
            except Exception as e:
                self.estado_var.set("Error al copiar: Asegúrate de tener pyperclip instalado")
        else:
            self.estado_var.set("Genere una contraseña primero")

    def verificar_fortaleza(self):
        """Abre el navegador con la contraseña actual para verificar su fortaleza"""
        contraseña = self.contraseña_var.get()
        if contraseña:
            # Copiamos automáticamente la contraseña al portapapeles
            pyperclip.copy(contraseña)
            
            # Usamos el verificador de security.org
            url = "https://www.security.org/how-secure-is-my-password/"
            
            webbrowser.open(url)
            self.estado_var.set("Página de verificación abierta en el navegador.\nLa contraseña se ha copiado al portapapeles.\nPégala en el sitio web para verificar su fortaleza.")
        else:
            self.estado_var.set("Genera una contraseña primero")

    def mostrar_dialogo_guardar(self):
        """Muestra una ventana de diálogo para guardar la contraseña"""
        contraseña = self.contraseña_var.get()
        if not contraseña:
            self.estado_var.set("Genere una contraseña primero")
            return
            
        # Crear ventana de diálogo
        dialogo = tk.Toplevel(self.root)
        dialogo.title("Guardar Contraseña")
        dialogo.geometry("300x150")
        dialogo.resizable(False, False)
        
        # Centrar la ventana
        dialogo.transient(self.root)
        dialogo.grab_set()
        
        # Frame principal
        frame = ttk.Frame(dialogo, padding="20")
        frame.pack(fill='both', expand=True)
        
        # Campo para el nombre
        ttk.Label(frame, text="Nombre para la contraseña:").pack(pady=5)
        nombre_var = tk.StringVar()
        nombre_entry = ttk.Entry(frame, textvariable=nombre_var, width=30)
        nombre_entry.pack(pady=5)
        nombre_entry.focus()
        
        def guardar():
            nombre = nombre_var.get().strip()
            if nombre:
                self.guardar_contraseña(nombre, contraseña)
                dialogo.destroy()
            else:
                messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre")
        
        # Botón guardar
        ttk.Button(frame, text="Guardar", command=guardar).pack(pady=10)

    def guardar_contraseña(self, nombre, contraseña):
        """Guarda la contraseña con el nombre proporcionado"""
        contraseñas = {}
        if os.path.exists('contraseñas.json'):
            try:
                with open('contraseñas.json', 'r', encoding='utf-8') as f:
                    contraseñas = json.load(f)
            except json.JSONDecodeError:
                pass
        
        if nombre in contraseñas:
            if not messagebox.askyesno("Confirmar", 
                                     "Ya existe una contraseña con ese nombre. ¿Desea sobrescribirla?"):
                return
        
        contraseñas[nombre] = contraseña
        
        try:
            with open('contraseñas.json', 'w', encoding='utf-8') as f:
                json.dump(contraseñas, f, indent=4, ensure_ascii=False)
            self.estado_var.set("Contraseña guardada exitosamente")
        except Exception as e:
            self.estado_var.set(f"Error al guardar la contraseña: {str(e)}")

    def ver_contraseñas(self):
        """Muestra una ventana con las contraseñas guardadas"""
        if not os.path.exists('contraseñas.json'):
            messagebox.showinfo("Info", "No hay contraseñas guardadas")
            return
            
        try:
            with open('contraseñas.json', 'r', encoding='utf-8') as f:
                contraseñas = json.load(f)
            
            if not contraseñas:
                messagebox.showinfo("Info", "No hay contraseñas guardadas")
                return
            
            # Crear ventana para mostrar contraseñas
            ventana = tk.Toplevel(self.root)
            ventana.title("Contraseñas Guardadas")
            ventana.geometry("500x400")  # Ventana más grande
            
            # Crear frame con scroll
            frame = ttk.Frame(ventana)
            frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Crear canvas y scrollbar
            canvas = tk.Canvas(frame)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            def eliminar_contraseña(nombre):
                if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la contraseña '{nombre}'?"):
                    contraseñas.pop(nombre)
                    with open('contraseñas.json', 'w', encoding='utf-8') as f:
                        json.dump(contraseñas, f, indent=4, ensure_ascii=False)
                    ventana.destroy()
                    self.ver_contraseñas()  # Recargar la ventana
            
            # Encabezados
            header_frame = ttk.Frame(scrollable_frame)
            header_frame.pack(fill='x', pady=(0, 10))
            ttk.Label(header_frame, text="Nombre", width=20).pack(side='left', padx=5)
            ttk.Label(header_frame, text="Contraseña", width=30).pack(side='left', padx=5)
            ttk.Label(header_frame, text="Acciones", width=20).pack(side='left', padx=5)
            
            ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=5)
            
            # Mostrar contraseñas
            for nombre, contraseña in contraseñas.items():
                frame_contraseña = ttk.Frame(scrollable_frame)
                frame_contraseña.pack(fill='x', pady=5)
                
                # Nombre
                ttk.Label(frame_contraseña, text=nombre, width=20).pack(side='left', padx=5)
                
                # Campo de contraseña
                entry_contraseña = ttk.Entry(frame_contraseña, show="*", width=30)
                entry_contraseña.insert(0, contraseña)
                entry_contraseña.configure(state='readonly')
                entry_contraseña.pack(side='left', padx=5)
                
                # Frame para botones
                botones_frame = ttk.Frame(frame_contraseña)
                botones_frame.pack(side='left', padx=5)
                
                def mostrar_contraseña(entry=entry_contraseña, c=contraseña):
                    if entry['show'] == '*':
                        entry.configure(show='')
                    else:
                        entry.configure(show='*')
                
                def copiar_contraseña(c=contraseña):
                    pyperclip.copy(c)
                    messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")
                
                ttk.Button(botones_frame, 
                          text="👁️",
                          width=3,
                          command=lambda e=entry_contraseña, c=contraseña: mostrar_contraseña(e, c)).pack(side='left', padx=2)
                
                ttk.Button(botones_frame, 
                          text="📋",
                          width=3,
                          command=lambda c=contraseña: copiar_contraseña(c)).pack(side='left', padx=2)
                
                ttk.Button(botones_frame, 
                          text="🗑️",
                          width=3,
                          command=lambda n=nombre: eliminar_contraseña(n)).pack(side='left', padx=2)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar las contraseñas: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorContraseñasGUI(root)
    root.mainloop()
