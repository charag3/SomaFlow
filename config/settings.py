import os
from typing import Dict, Any
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env si existe
load_dotenv()

# Entorno de ejecución
ENV = os.getenv("ENV", "development")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Configuración de la aplicación
APP_NAME = "SomaFlow"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "Sistema de automatización para optimizar la gestión interna de negocios"

# Configuración de API
API_PREFIX = "/api"
API_VERSION = "v1"

# Configuración de base de datos (si se usa)
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Configuraciones de clientes
AVAILABLE_CLIENTS = ["xamanic", "lasdelbarrio", "revolver"]

# Función para obtener configuración específica por entorno
def get_env_config() -> Dict[str, Any]:
    """
    Retorna configuraciones específicas según el entorno de ejecución.
    """
    if ENV == "production":
        return {
            "cors_origins": os.getenv("CORS_ORIGINS", "").split(","),
            "reload": False,
            "workers": int(os.getenv("WORKERS", 1)),
        }
    else:  # development o testing
        return {
            "cors_origins": ["*"],
            "reload": True,
            "workers": 1,
        }

# Configuración específica del entorno actual
env_config = get_env_config()
