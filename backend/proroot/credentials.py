from decouple import config

secret_key = config("SECRET_KEY", default="")
# debug      = config("DEBUG", default=True, cast = bool)
allowed_hosts = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

db_name = config("DB_NAME", default="db.sqlite3")
db_user = config("DB_USER", default="admin")
db_password = config("DB_PASSWORD", default="fls_2022")
db_port = config("DB_PORT", default=5432, cast=int)
db_host = config("DB_HOST", default='locahost')
