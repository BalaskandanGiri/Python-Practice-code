import os
path="C:\\Users\\I346330\\Documents\\Work\\test"
PO=""
for files in os.listdir(path):
    print(files)
    with open(os.path.join(path,files),'r') as file:
        buf = file.readlines()
    with open(os.path.join(path,files),'w') as outfile:
        for line in buf:
            potag="&lt;PO_NUMBER&gt;"
            if potag in line:
                print(line)
                PO = line[line.index(potag)+len(potag):line.index(potag)+len(potag)+10]
                print(PO)
            if "&lt;/PO_ITEM&gt;&#13;" in line and PO.startswith("4"):
                print(line)
                line = line + "\t\t\t&lt;REF_DOC_TYPE&gt;PO&lt;/REF_DOC_TYPE&gt;&#13;\n"
            elif "&lt;/PO_ITEM&gt;&#13;" in line and PO.startswith("5"):
                print(line)
                line = line + "\t\t\t&lt;REF_DOC_TYPE&gt;SAR&lt;/REF_DOC_TYPE&gt;&#13;\n"
            outfile.write(line)

