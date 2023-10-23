import shutil 
import os

folder=os.listdir(R'F:')
print(folder)
for file in folder:
    ext=os.path.splitext(file)
    if file=='System Volume Information':
        continue
    elif ext[1]=='':
        shutil.copytree(Rf"F:\{file}",R'E:\data')
    else:
        shutil.copy(Rf"F:\{file}",R'E:\data')
