from flask import render_template , flash, redirect, session, url_for, request, g

from app import app

def mpd_restart():
  flash("MPD restarted")
  app.logger.info("MPD restarted",'message')
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


@app.errorhandler(401)
def internal_error(error):
  return redirect(url_for('index'))

@app.errorhandler(404)
def internal_error(error):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
  return render_template('500.html'), 500



