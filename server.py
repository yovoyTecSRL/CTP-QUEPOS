#!/usr/bin/env python3
"""
Servidor web simple para desarrollo local
Sirve archivos HTML, CSS y JS desde el directorio actual
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from datetime import datetime

# Configuración del servidor
PORT = 8080
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler personalizado con logging mejorado"""
    
    def log_message(self, format, *args):
        """Log personalizado con timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {format % args}")
    
    def end_headers(self):
        """Agregar headers CORS para desarrollo"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    """Inicia el servidor web"""
    try:
        # Cambiar al directorio del script
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Crear el servidor
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print("=" * 60)
            print("🚀 SERVIDOR WEB INICIADO EXITOSAMENTE")
            print("=" * 60)
            print(f"📡 Servidor corriendo en: http://{HOST}:{PORT}")
            print(f"📁 Directorio base: {os.getcwd()}")
            print(f"🌐 Páginas disponibles:")
            print(f"   • http://{HOST}:{PORT}/index.html (Inicio)")
            print(f"   • http://{HOST}:{PORT}/servicios.html")
            print(f"   • http://{HOST}:{PORT}/portafolio.html")
            print(f"   • http://{HOST}:{PORT}/contacto.html")
            print("=" * 60)
            print("💡 Para detener el servidor presiona Ctrl+C")
            print("🔄 El servidor se recarga automáticamente")
            print("=" * 60)
            
            # Abrir automáticamente en el navegador
            webbrowser.open(f'http://{HOST}:{PORT}')
            
            # Servir indefinidamente
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Error: El puerto {PORT} ya está en uso")
            print(f"💡 Intenta usar otro puerto o cierra el proceso que usa el puerto {PORT}")
            print(f"🔍 Para matar el proceso: netstat -ano | findstr {PORT}")
        else:
            print(f"❌ Error al iniciar servidor: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()
