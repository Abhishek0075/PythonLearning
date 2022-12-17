# with open(r"C:\Users\abhir\OneDrive\Documents\GitHub\PythonLearning\files\newfile.txt","a+") as myfile:
    # a+ is used to append and need to do other operations along with it
#         myfile.write("\nOkra")
#         content=myfile.read()
# print(content)
    # When done like above nothing will be printed
        # as the cursor is present at the end

with open(r"C:\Users\abhir\OneDrive\Documents\GitHub\PythonLearning\files\newfile.txt","a+") as myfile:
        myfile.seek(0)
        content=myfile.read()
        print(content)
        myfile.write("\n"+content)
print(content)
