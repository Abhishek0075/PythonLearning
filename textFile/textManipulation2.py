myfile = open(r"C:\Users\abhir\OneDrive\Documents\GitHub\PythonLearning\files\textFile.txt")

content= myfile.read()

print (content)
print()
print (content)
myfile.close()
print(myfile.read()) # Cause error due to closing the file

# see the closing and reading in readingText.py