# import pickle mode
import pickle
import os
# create pickle file
cur_path = os.path.abspath(os.curdir)
test_list = [123, 3.14, "wm", ["another list"]]
fp = open(cur_path + "\\" + "test_list.pkl", "wb")

pickle.dump(test_list, fp)
fp.close()

# Use the pickle file restore list
fp = open(cur_path + "\\" + "test_list.pkl", "rb")
pickle_list = pickle.load(fp)

print(pickle_list)


