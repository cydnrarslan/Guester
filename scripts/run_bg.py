# -*- coding: utf-8 -*-
#
#
#
import sys
import os
import traceback

sys.path.insert(0, "C:\\Users\\cydnr\\Desktop\\guester")

try:
    import app
except Exception as e:
    with open("C:\\Users\\cydnr\\Desktop\\guester\\bg_error.log", "w") as f:
        f.write(traceback.format_exc())
