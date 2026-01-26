import sys
import subprocess
import os

uic  = os.path.join(os.path.dirname(sys.executable), 'PySide6-uic.exe')

subprocess.run([uic, 'Form/mainwindow.ui', '-o', 'gen/gen_mainwindow.py'])