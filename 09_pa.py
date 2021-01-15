# 9: Script to ping and check whether any given IPs are active, also whether given set of software are installed in the existing system ( like java, kubectl, aws etc)

import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in range(1, 10):
                ip="192.168.0.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, "inactive")
                else:
                        print (ip, "active") 