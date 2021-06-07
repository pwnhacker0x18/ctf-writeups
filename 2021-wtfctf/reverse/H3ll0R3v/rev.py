import uncompyle6
import os

os.system('cp Hello flag.pyc')
file = open('decompiled.py', 'w')
data = uncompyle6.decompile_file("flag.pyc", file)

