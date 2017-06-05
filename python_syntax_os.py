# import os mode
import os
import time

# Get the current working directory
print(os.getcwd())
# change working directory to Disk c
os.chdir("C:\\")

# Get the current working directory
print(os.getcwd())

# Return a list containing the names of the files in the directory
print(os.listdir("C:\\"))
print(os.listdir(os.curdir))
print(os.listdir(os.pardir))

# make  directory, may be used:
# os.path.exists,os.path.isdir,os.path.isfile, os.path.islink, os.path.isabs, os.path.ismount, os.path.samefile
if os.path.exists("c:\\test") is False:
    os.mkdir("c:\\test")
if os.path.exists("c:\\test\\a\\b") is False:
    os.makedirs("c:\\test\\a\\b")
print(os.listdir("C:\\"))
if os.path.exists("c:\\test\\a\\b\\c.txt") is False:
    fp = open("c:\\test\\a\\b\\c.txt", "w+")
    fp.close()
print(os.listdir("c:\\test\\a\\b"))

# get file name
print(os.path.basename("c:\\test\\a\\b\\c.txt"))

# get path
print(os.path.dirname("c:\\test\\a\\b\\c.txt"))

# Combine a and b into new paths
print(os.path.join("c:\\", "a", "b", "a_b", "c.txt"))

# split file and path
print(os.path.split("c:\\test\\a\\b\\c.txt"))

# split file names and extension names
print(os.path.splitext("c:\\test\\a\\b\\c.txt"))

# get file size
print(os.path.getsize("c:\\test\\a\\b\\c.txt"))

# Return the last access time of a file
print(os.path.getatime("c:\\test\\a\\b\\c.txt"))

# eturn the metadata change time of a file
print(os.path.getctime("c:\\test\\a\\b\\c.txt"))

# Return the last modification time of a filer
print(os.path.getmtime("c:\\test\\a\\b\\c.txt"))
GMT = os.path.getmtime("c:\\test\\a\\b\\c.txt")
print(time.localtime(GMT))

# change file name
if not os.path.exists("c:\\test\\a\\b\\test.txt"):
    os.rename("c:\\test\\a\\b\\c.txt", "c:\\test\\a\\b\\test.txt")

# You need to delete the files in the folder before deleting the folder
os.remove("c:\\test\\a\\b\\test.txt")
os.rmdir("c:\\test\\a\\b")
os.removedirs("c:\\test\\a")

print(os.name)
