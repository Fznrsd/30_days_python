from math import *
import math
from statistics import *

class mth:
    def __init__(self, lst):
        self.lst = lst    
    
    def info(self):
        print("Count:", len(self.lst))
        print('Sum: ', sum(self.lst)) # 744
        print('Min: ', min(self.lst)) # 24
        print('Max: ', max(self.lst)) # 38
        print('Mean: ', mean(self.lst)) # 30
        print('Median: ', median(self.lst)) # 29
        print('Mode: ', mode(self.lst)) # 'mode': 26

lst = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
p = mth(lst)
p.info()

###########
