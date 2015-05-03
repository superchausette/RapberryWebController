import time
import subprocess

class LightDM:
    def __init__(self):
        self.lastStop = time.time()
        self.lastStart = time.time()

    def stop(self):
        currentTime = time.time()
        if currentTime - self.lastStop < 5:
            err = "Waiting for at least 5 s sinc last stop, only %d s" (currentTime - self.lastStop)
            return False, err
        cmd = ["service", "lightdm", "stop"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
            stderr =subprocess.PIPE,stdin  = subprocess.PIPE)
        out, err = p.communicate()
        rc = p.returncode
        if rc != 0:
            err = "Error during stop out:\'%s\' err:\'%s\'" %(out,err)
            return False, err
 
        self.lastStop = time.time()
        return True, "LightDM Stop"

    def start(self):
        currentTime = time.time()
        if currentTime - self.lastStart < 5:
            err = "Waiting for at least 5 s sinc last start, only %d s" (currentTime - self.lastStart)
            return False, err
        cmd = ["service", "lightdm", "start"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
            stderr =subprocess.PIPE,stdin  = subprocess.PIPE)
        out, err = p.communicate()
        rc = p.returncode
        if rc != 0:
            err = "Error during start out:\'%s\' err:\'%s\'" %(out,err)
            return False, err
 
        self.lastStart = time.time()
        return True, "LightDM Start"
