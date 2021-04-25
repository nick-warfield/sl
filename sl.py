#!/usr/bin/python3

import sys
import subprocess
import random

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

#subprocess.run(["./train_animation"])
print(selection)


