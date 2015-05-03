from flask import render_template , flash, redirect, session, url_for, request, g

from app import app, MDPImpl, LightDMImpl

def mpd_restart():
  suc, error = MDPImpl.restart()
  if suc == True:
    flash("MPD restarted",'info')
    app.logger.info("MPD restarted")
  else:
    flashMsg = "Unable to restart MPD: %s" % error
    flash(flashMsg,('error'))
    app.logger.info(flashMsg)
  return redirect(url_for('index'))


def lightm_cmd(cmd):
    if cmd == "start":
        suc, error = LightDMImpl.start()
        if suc == True:
            flash("LightDM started")
            app.logger.info("LightDM started")
        else:
            flashMsg = "Unable to start LightDM: %s" % error
            flash(flashMsg,('error'))
            app.logger.info(flashMsg)
    elif cmd == "stop":
        suc, error = LightDMImpl.stop()
        if suc == True:
            flash("LightDM stopped")
            app.logger.info("LightDM stopped")
        else:
            flashMsg = "Unable to stop LightDM: %s" % error
            flash(flashMsg,('error'))
            app.logger.info(flashMsg)
    else:
        flashMsg = "Invalid LightDM cmd: %s" % cmd
        flash(flashMsg,('error'))
        app.logger.info(flashMsg)

    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route("/mpd/",methods = ['POST'])
def mpd():
  if request.form['mpd'] == 'Restart MPD':
    return mpd_restart()

  flash("Unknown request",'error')
  return redirect(url_for('index'))

@app.route("/lightdm/", methods = ['POST'])
def lightdm():
    if request.form['lightdm'] == 'Stop lightdm':
        return lightm_cmd("start")
    elif request.form['lightdm'] == 'Start lightdm':
        return lightm_cmd("stop")

    flash("Unknown request",'error')
    return redirect(url_for('index'))

@app.errorhandler(401)
def internal_error(error):
  return redirect(url_for('index'))

@app.errorhandler(404)
def internal_error(error):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
  return render_template('500.html'), 500



