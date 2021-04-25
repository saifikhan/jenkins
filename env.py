#!/usr/bin/python

import os

def print_env():
    env = os.environ

    for k, v in env.items ():
        print (k, " : ", v)



# scope for top-level code

if __name__ == "__main__":
    print_env ()

