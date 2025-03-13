from fastapi import APIRouter
import logging
import importlib
from config.settings import AVAILABLE_CLIENTS

logger = logging.getLogger(__name__)

# Crear el router principal
api_router = APIRouter()

# Cargar dinámicamente los routers de los clientes disponibles
for client in AVAILABLE_CLIENTS:
    try:
        # Importar dinámicamente el módulo del cliente
        module_path = f"backend.api.endpoints.{client}"
        module = importlib.import_module(module_path)
        
        # Verificar si el módulo tiene un router definido
        if hasattr(module, "router"):
            # Incluir el router del cliente
            api_router.include_router(
                module.router,
                prefix=f"/{client}",
                tags=[client],
                responses={404: {"description": "Not found"}},
            )
            logger.info(f"Router para cliente '{client}' cargado correctamente")
        else:
            logger.warning(f"No se encontró router en el módulo {module_path}")
    except ImportError as e:
        # No interrumpir si un módulo no existe
        logger.warning(f"No se pudo cargar el módulo para el cliente '{client}': {str(e)}")
        continue
    except Exception as e:
        # Registrar cualquier otro error pero continuar
        logger.error(f"Error al cargar el router para el cliente '{client}': {str(e)}")
        continue

# Endpoint de prueba para el router principal
@api_router.get("/status")
def get_api_status():
    """Retorna el estado de la API"""
    return {"status": "operational", "clients_loaded": AVAILABLE_CLIENTS}
