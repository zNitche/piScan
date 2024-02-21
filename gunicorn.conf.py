import multiprocessing
from config import Config, PROJECT_ROOT


bind = f"{Config.APP_HOST}:{Config.APP_PORT}"


workers = 4
threads = multiprocessing.cpu_count()
worker_class = "gthread"

timeout = 10
keepalive = 5

loglevel = "error"
# accesslog = os.path.join(PROJECT_ROOT, "logs", "access.log")
# errorlog = os.path.join(PROJECT_ROOT, "logs", "error.log")
