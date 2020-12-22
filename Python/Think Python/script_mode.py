#!/bin/python3

import math
import os
import random
import re
import sys



def is_leap(year):
    leap = False
    if year % 4 == 0: #is
        if year%100 == 0: #is not
            if year%400 == 0: #is
                print("divisible by 400")
                return leap
            print("divisible by 100 but not by 400")
            return leap
        leap = True
        print("divisible by 4 but not by 100")
        return leap
    return leap
year = int(input())
print(is_leap(year))
print("hi")