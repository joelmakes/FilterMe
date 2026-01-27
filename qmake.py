#allow the use od the system path
import sys
#allow run commands in the system vs
import subprocess
#allow to create paths
import os

# setup up python path and find pyside6 ( converts files to py files)
uic  = os.path.join(os.path.dirname(sys.executable), 'PySide6-uic.exe')

#set ui file (using file name) to py file (given name)
subprocess.run([uic, 'Form/main_window.ui', '-o', 'gen/gen_main_window.py'])