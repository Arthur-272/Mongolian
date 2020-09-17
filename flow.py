from get_ip import getIP
from get_os import getos
import coloredlogs, logging

logger = logging.getLogger()
coloredlogs.install(level='DEBUG', logger=logger)

ips = getIP()

for ip in ips:
    try:
        logger.info(ip + ' --> '+ getos(ip))
    except:
        logger.error('Failed for ' + ip)
