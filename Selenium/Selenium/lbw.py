import os
import time
from pywinauto import Application

os.startfile(r'C:\Users\sn1076327\Desktop\Teste de Projeto LBW com biblioteca compactada\Pasta Dados\Receitas_teste\11Y6212520-PC350-SAVALV01 - Copia.vi')
# Open Notepad
# app = Application().start(r'C:\Program Files\National Instruments\LabVIEW 2023\LabVIEW.exe')
time.sleep(1)  # Wait for Notepad to open

# Type some text
# app.Notepad.edit.type_keys('Hello, world!')