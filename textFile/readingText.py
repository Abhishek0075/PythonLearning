with open(r"C:\Users\abhir\OneDrive\Documents\GitHub\PythonLearning\files\textFile.txt") as myfile:
    content=myfile.read()
    # if we give a number as argument in read function
    # it will just read the first n characters in  the file
print(content)