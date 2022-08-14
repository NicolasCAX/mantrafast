from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['root'] = os.getenv('MYSQL_USER') or 'root'
app.config['FAXW6HBRPqsGIfi3bdK4'] = os.getenv('MYSQL_PASSWORD') or 'faztpassword'
app.config['containers-us-west-74.railway.app'] = os.getenv('MYSQL_HOST') or '127.0.0.1' # localhost
app.config['railway'] = os.getenv('MYSQL_DB') or 'flaskcrud'
app.config['railway'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)
