import glob
import shutil

myfiles = glob.glob("files/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath) as file:
        print(file.read())

shutil.make_archive("output", "zip", "files")
