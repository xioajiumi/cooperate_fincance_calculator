#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    : 
# @File    : toys.py
import time

def timer(func):
    def wrapper(*args,**kwargs):
        t0=time.clock()
        ret=func(*args,**kwargs)
        t1=time.clock()
        elapsed=t1-t0
        print(F"{round(elapsed,10)} passed")
        return ret
    return wrapper

