#main.py
import fileinput # biblioteka datnju ievadisanai

with fileinput.FileInput(files=('kl10.txt', 'kl11.txt')) as datne:
 for idx, line in enumerate(datne):
    print('=== Lasa datni === ', datne.filename())
    print(idx, line,end='' )
