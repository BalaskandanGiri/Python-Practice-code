import os
path='C:\AUTOMATION\TEMP'
for file in os.listdir('C:\AUTOMATION\TEMP'):
    if "_base" not in file and file.endswith(".xml"):
        #print(file[:-4]+"_base.xml")
        os.rename(os.path.join(path,file),os.path.join(path,file[:-4]+"_target.xml"))
