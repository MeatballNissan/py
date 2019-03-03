
import os
import sys
print(os.path.abspath(__file__))#相对路径
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#import conf,core
from conf import settings
from core import main
main.login()
