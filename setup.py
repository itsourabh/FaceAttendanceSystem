import os
import sys
from setuptools import find_packages,setup

import cx_Freeze

setup(
    name='FaceAttendanceSystem',
    version='0.0.1',
    author='Sourabh',
    author_email='sg9003229@gmail.com',
    packages=find_packages(),
    install_requires=['numpy','opencv','pandas']
)

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ASUS\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ASUS\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'college_images','data','database','attendance_report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Sourabh Gupta",
    executables = executables
    )
