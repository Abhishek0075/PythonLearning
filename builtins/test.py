import time
with open(r"C:\Users\abhir\OneDrive\Documents\GitHub\PythonLearning\files\newfile.txt","a+") as myfile:
        content=myfile.read()
        myfile.write(content)
        myfile.write(content)
        # myNew.seek(0)
        # time.sleep(1)