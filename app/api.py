from src import app
from logging.handlers import RotatingFileHandler
import logging,os

if __name__ == '__main__':
    log_format      = f"%(asctime)s [%(levelname)s] %(message)s"
    log_date_format = "%Y-%m-%d %H:%M:%S"
    project_path    = os.path.abspath(os.path.dirname(__file__))
    os.makedirs(project_path+'/log', exist_ok=True)
    log_file        = project_path+'/log/report.log'
    handler         = RotatingFileHandler(log_file, maxBytes=1000, backupCount=4)
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format, datefmt=log_date_format)
    app.run(host="localhost", port=8000, debug=True)