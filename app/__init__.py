from flask import Flask

import MPD
import LightDM

app = Flask(__name__)
app.config.from_object('config')

MDPImpl = MPD.MPD()
LightDMImpl = LightDM.LightDM()

if not app.debug:
  import logging
  from logging.handlers import RotatingFileHandler
  file_handler = RotatingFileHandler('tmp/raspberry_web_controller.log', 'a', 1 * 1024 * 1024, 10)
  file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
  app.logger.setLevel(logging.INFO)
  file_handler.setLevel(logging.INFO)
  app.logger.addHandler(file_handler)
  app.logger.info('Raspberry Web Controller startup')



from app import views
