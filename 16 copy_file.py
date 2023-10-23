import shutil 
import os
folder=os.listdir(R'C:\Users\Ansham\Desktop\New')
for file in folder:
    ext=os.path.splitext(file)
    if ext[1]=='.pdf':
        shutil.copy(Rf"C:\Users\Ansham\Desktop\New\{file}",R'C:\Users\Ansham\Desktop\New folder')
