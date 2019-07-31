import os

# Get Current working directory

# -> print(os.getcwd())

#Create Folder
# -> os.mkdir("C:\\Folder1_new")

#for i in range(10):
#    os.mkdir("C:\\Folder_loop"+str(i))

# create multiple folder
# ->os.makedirs("C:\\folder1\\folder2\\folder3")

#get list of directory adn files

#-> fileslit = os.listdir("C:\\")
#-> print(fileslit)

#-> os.rename("C:\\folder1" , "C:\\folder_renamed")

# change current working directory

# print(os.getcwd())
# print(os.listdir("."))
# os.chdir("C:\\")
# print(os.getcwd())
# print(os.listdir("."))

# remove directory
#os.remove("C:\\DataFile1")
#  -> os.removedirs("C:\\folder_renamed")

# run windows commmand using python
# ->data = os.system("dir")
#-> print("data:", data)

#output= os.popen("dir", 'r')
#print("data1:", output)

import shutil

#shutil.copy("C:\\DataFile1\\File1.txt", "C:\\Folder1_new")

#shutil.rmtree("C:\\folder1")

