import os

# specify the directory name
directory = 'chapter 1'

# list all files and directories in the specified directory
for item in os.listdir(directory):

# print each file and directory name   
 print(item)
