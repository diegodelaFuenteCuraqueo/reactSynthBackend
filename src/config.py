class DevelopmentConfig():
  DEBUG = True
  MYSQL_HOST="127.0.0.1"
  #MYSQL_PORT=3306
  MYSQL_DB="bd_synth"
  MYSQL_USER="root"
  MYSQL_PASSWORD=""

config = {
  'development': DevelopmentConfig,
  'default': DevelopmentConfig
}