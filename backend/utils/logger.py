import logging
import os
import sys
from typing import Optional

def setup_logger(level: Optional[str] = None):
    """
    Configura el logger global para la aplicación.
    
    Args:
        level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Obtener nivel de logging desde variables de entorno o parámetro
    log_level = level or os.environ.get("LOG_LEVEL", "INFO").upper()
    
    # Mapear string a constante de logging
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    
    # Configurar formato de logging
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        format=log_format,
        level=level_map.get(log_level, logging.INFO),
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Configurar niveles específicos para algunas bibliotecas
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    
    # Crear logger para la aplicación
    logger = logging.getLogger("somaflow")
    logger.setLevel(level_map.get(log_level, logging.INFO))
    
    logger.info(f"Logger configurado con nivel: {log_level}")
    return logger
