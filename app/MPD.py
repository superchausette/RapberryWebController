import time
import subprocess

class MPD:
  def __init__(self):
    self.lastRestart = time.time()
    
  def restart(self):
    currentTime = time.time()
    if currentTime - self.lastRestart < 15:
      err = "Waiting for at least 15 s since last restart, only %d s" %(currentTime - self.lastRestart)
      return False, err

    cmd = ["service", "mpd", "restart"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                              stderr =subprocess.PIPE,
                              stdin  = subprocess.PIPE)

    out, err = p.communicate()
    rc = p.returncode
    if rc != 0:
        err = "Error during restart out:\'%s\' err:\'%s\'" %(out,err)
        return False, err
    self.lastRestart = time.time()
    return True, "MDP restarted"
