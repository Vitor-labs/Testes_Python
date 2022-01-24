import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - \
                    %(levelname)s - %(message)s', datefmt='%d/%M/%Y %H:%M:%S')

# logging.debug('Menssagem de DEBUG')
# logging.info('Menssagem de INFORMAÇÃO')
# logging.critical('Menssagem CRITICA')

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
file = logging.FileHandler('arq.log')

handler.setLevel(logging.WARNING)
file.setLevel(logging.ERROR)

formato = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formato)
file.setFormatter(formato)

logger.addHandler(handler)
logger.addHandler(file)

logger.warning('Menssagem de WARNING')
logger.error('Menssagem de ERROR')
logger.critical('Menssagem de CRITICAL')
logger.debug('Menssagem de DEBUG')
logger.info('Menssagem de INFO')
