import pickle
a = {"asdf":"asdassasf"}
f = file("data.txt", "wb")
pickle.dump(a, f)
f.close()