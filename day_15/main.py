# start to python day-14 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 07-03-2022

import random
import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
screen_clear()