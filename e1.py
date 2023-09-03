import glob
import shutil
import webbrowser

# 1
myfiles = glob.glob("files/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath) as file:
        print(file.read())

# 2
shutil.make_archive("output", "zip", "files")

# 3
search = input("Enter search term: ").replace(" ", "+")
webbrowser.open("https://google.com/search?q=" + search)
