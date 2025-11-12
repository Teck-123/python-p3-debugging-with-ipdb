#!/usr/bin/env python3

import ipdb

def tracing_the_function():
    inside = "We're inside the function"
    print(inside)
    print("We're about to stop because of ipdb!")
    ipdb.set_trace()
    later = "The program froze before it could read me!"
    print(later)

tracing_the_function()
