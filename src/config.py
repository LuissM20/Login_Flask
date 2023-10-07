class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

#Configuración para la conexión de la base de datos 
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask_login'
    MYSQL_PORT=33065


config = {
    'development': DevelopmentConfig
}
