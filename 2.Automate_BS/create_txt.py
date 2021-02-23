#!/usr/bin/env python3
import sys, os

if len(sys.argv[1]) != 0:
    file_ = open(sys.argv[1] + '.txt', 'x')
    file_.close()
