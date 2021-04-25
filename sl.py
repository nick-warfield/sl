#!/usr/bin/python3

import sys
import subprocess
import random
import time

def get_selection(lower_bound, upper_bound) -> int:
    selection = random.randint(lower_bound, upper_bound)
    if len(sys.argv) == 3 and sys.argv[1] == '-n':
        try:
            temp = int(sys.argv[2])
            if temp >= lower_bound and temp <= upper_bound:
                selection = temp
        except:
            pass

    return selection

selection = get_selection(0, 2)
path = sys.path[0] + '/resources/'

if selection == 0:
    subprocess.run([path + "0_train_animation"])
else:
    with open(path + str(selection) + "_train.txt", "r") as train:
        for line in train.readlines():
            print(line, end="")

    # timer to preserve the original intent of punishing the user
    time.sleep(1.5)


