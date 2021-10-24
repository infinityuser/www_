bind = '127.0.0.1:4000'
backlog = 64

workers = 3
worker_class = 'sync'
worker_connections = 1024
timeout = 30
keepalive = 2

raw_env = []

spew = False
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None
proc_name = None
