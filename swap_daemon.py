# -*- coding: utf-8 -*-

import os
import subprocess
import time


def clean_swap():
    user = str(subprocess.check_output("whoami"), encoding="utf-8")[0:-1]
    if user == "root":
        while 1 == 1:
            try:
                output = str(subprocess.check_output("free"), encoding="utf-8").split()

                mem_total = int(output[7])
                mem_used = int(output[8])
                mem_used_percent = mem_used / mem_total * 100

                swp_used = int(output[-2])

                if swp_used > 0 and mem_used_percent < 90:
                    os.system("swapoff -a")
                    os.system("swapon -a")
                time.sleep(1)
            except:
                pass

            time.sleep(1)
    else:
        print("You are not root")


if __name__ == '__main__':
    clean_swap()
