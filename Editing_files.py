import os
import filecmp
path='C:\AUTOMATION'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file)):
        print(file)
        with open(os.path.join(path,file),'r') as f:
            data = f.read()
            print(data)
            data=data.replace('_-ARBA_-','ARBCIG_')
            print(data)
        with open(os.path.join(path, file), 'w') as f:
            f.write(data)