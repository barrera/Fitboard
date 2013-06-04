import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'default'
SESSION_COOKIE_NAME = 'FITBITSTATUSAPP'

DEBUG_TB_INTERCEPT_REDIRECTS = False