import logging

# Configurar o logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def log_error(message: str):
    """Função para registrar erros"""
    logger.error(message)
