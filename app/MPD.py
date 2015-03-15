import time

class MPD:
  def __init__(self):
    self.lastRestart = time.time()
    
  def restart(self):
    currentTime = time.time()
    print("print last restart: %d - %d : %d" %(currentTime,self.lastRestart, currentTime - self.lastRestart))
    if currentTime - self.lastRestart < 30:
      err = "Waiting for at least 30s since last restart, only %d s" %(currentTime - self.lastRestart)
      return False, err

    self.lastRestart = time.time()
    return True, "MDP restarted"
