import os
cur_path = os.path.abspath(os.curdir)

fp = open(cur_path + "\\" + "hello.txt", "w+")
print(fp)
fp.write("hello world\n")
txt = fp.readline()
print(txt)
fp.close()

os.remove(cur_path + "\\" + "hello.txt")
