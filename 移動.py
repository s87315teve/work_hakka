import shutil
import os



path_now = os.path.abspath('.')
path_new = os.path.abspath('..')
path_now = path_now+'\\test_remove.py'
path_new = path_new+'\\test_remove.py'
print(path_now)
print(path_new)

shutil.move(path_now,path_new)
