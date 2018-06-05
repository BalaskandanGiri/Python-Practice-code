import os
import difflib
path="C:\AUTOMATION\TEMP\Invoice"
file1=None
file1_data=None
for file in os.listdir(path):
    if file1 is None:
        file1=file
    else:
        file2=file
        print(file1)
        print(file2)
        with open(os.path.join(path, file1), 'r') as f1:
            with open(os.path.join(path, file2), 'r') as f2:
                for linea,lineb in zip(f1,f2):
                    if linea!=lineb:
                        print(linea,lineb)

        file1=None
