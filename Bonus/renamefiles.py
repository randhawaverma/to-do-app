filenames = ["1.Doc", "1.Report", "1.Presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)