# Generador de Contraseñas Seguras

## Descripción
Esta aplicación de escritorio permite generar contraseñas seguras con diferentes opciones de personalización, guardarlas y administrarlas de manera eficiente.

## Características Principales
- Generación de contraseñas personalizables
- Interfaz gráfica intuitiva
- Almacenamiento seguro de contraseñas
- Verificación de fortaleza de contraseñas
- Sistema de gestión de contraseñas guardadas

## Requisitos del Sistema
- Python 3.x
- Bibliotecas requeridas:
  ```bash
  pip install tkinter
  pip install pyperclip
  ```

## Instalación
1. Clone o descargue este repositorio
2. Instale las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecute el archivo principal:
   ```bash
   python createpass.py
   ```

## Uso

### Generación de Contraseñas
1. **Opciones de Generación:**
   - Longitud: Define el número de caracteres
   - Mayúsculas: Incluye letras mayúsculas (A-Z)
   - Minúsculas: Incluye letras minúsculas (a-z)
   - Números: Incluye dígitos (0-9)
   - Símbolos: Incluye caracteres especiales

2. **Texto Específico:**
   - Permite incluir texto personalizado
   - Opciones de posición: inicio, final o aleatorio

3. **Controles Principales:**
   - Generar: Crea una nueva contraseña
   - Copiar: Copia la contraseña al portapapeles
   - Verificar Fortaleza: Abre una herramienta web para verificar la seguridad
   - Guardar: Almacena la contraseña con un nombre personalizado

### Gestión de Contraseñas Guardadas
- **Ver Contraseñas:**
  - Lista todas las contraseñas almacenadas
  - Muestra nombre y contraseña (oculta por defecto)
  
- **Acciones Disponibles:**
  - 👁️ Mostrar/Ocultar contraseña
  - 📋 Copiar al portapapeles
  - 🗑️ Eliminar contraseña

## Seguridad
- Las contraseñas se almacenan localmente en formato JSON
- El archivo de contraseñas se guarda con codificación UTF-8
- Se implementan verificaciones de seguridad básicas

## Funcionalidades Detalladas

### Generador de Contraseñas
- Asegura la inclusión de al menos un carácter de cada tipo seleccionado
- Permite personalizar la longitud mínima (4 caracteres)
- Distribución aleatoria de caracteres

### Almacenamiento
- Guarda las contraseñas en 'contraseñas.json'
- Permite sobrescribir contraseñas existentes
- Confirmación antes de eliminar

### Interfaz de Usuario
- Diseño moderno y limpio
- Feedback visual de acciones
- Mensajes de estado claros
- Ventanas modales para acciones importantes

## Solución de Problemas
1. **Error de Codificación:**
   - Asegúrese de que los archivos estén guardados en UTF-8
   - Verifique la compatibilidad de caracteres especiales

2. **Problemas de Permisos:**
   - Verifique los permisos de escritura en el directorio
   - Asegúrese de tener acceso al archivo de contraseñas

3. **Errores de Dependencias:**
   - Reinstale las dependencias requeridas
   - Verifique la versión de Python

## Contribuciones
Las contribuciones son bienvenidas. Por favor, siga estos pasos:
1. Fork del repositorio
2. Cree una rama para su función
3. Realice sus cambios
4. Envíe un pull request

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## Contacto
Para reportar problemas o sugerir mejoras, por favor abra un issue en el repositorio.
