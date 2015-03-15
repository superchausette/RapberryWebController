import time

class MPD:
  def __init__(self):
    self.lastRestart = time.time()
    
  def restart(self):
    currentTime = time.time()
    if currentTime - self.lastRestart < 15:
      err = "Waiting for at least 15 s since last restart, only %d s" %(currentTime - self.lastRestart)
      return False, err

    self.lastRestart = time.time()
    return True, "MDP restarted"
