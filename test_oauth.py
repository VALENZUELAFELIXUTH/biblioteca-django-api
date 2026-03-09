import requests

# === CONFIGURACIÓN ===
# IMPORTANTE: Asegúrate de que estas URLs coincidan con tus urls.py
TOKEN_URL = 'http://127.0.0.1:8000/auth/jwt/login/'  # Endpoint de SimpleJWT
API_URL = 'http://127.0.0.1:8000/api/libros/'   # Tu API protegida

# Credenciales de un usuario existente en tu base de datos (puedes usar el admin)
USERNAME = 'admin'
PASSWORD = '123'

def run_test():
    print("=== 1. Obteniendo Token JWT desde Django ===")
    
    # En SimpleJWT enviamos un JSON con username y password
    credentials = {
        'username': USERNAME,
        'password': PASSWORD
    }
    
    try:
        # Petición para obtener el token
        response = requests.post(TOKEN_URL, json=credentials, timeout=10)
        
        if response.status_code == 200:
            token_data = response.json()
            # JWT devuelve 'access', no 'access_token'
            access_token = token_data.get('access')
            
            print(f"✅ Login exitoso.")
            print(f"🔑 Token JWT (primeros 50 caracteres): {access_token[:50]}...")
            print("-" * 40)
            
            print("=== 2. Accediendo a la API de Libros ===")
            
            # El header DEBE llevar la palabra 'Bearer' seguida del token
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            api_response = requests.get(API_URL, headers=headers, timeout=10)
            
            print(f"Status Code: {api_response.status_code}")
            
            if api_response.status_code == 200:
                print("📚 DATOS RECIBIDOS EXITOSAMENTE:")
                print(api_response.json())
            else:
                print("❌ Error de Autorización en la API:")
                print(api_response.json())
                
        else:
            print(f"❌ Error al obtener el token (Status {response.status_code}):")
            print(response.json())

    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar con el servidor. ¿Olvidaste hacer 'python manage.py runserver'?")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    run_test()