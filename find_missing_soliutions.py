import glob
import os
import pickle

SOLUTION_MASK = "solutions/*.cpp"

solved = [int(os.path.basename(os.path.splitext(x)[0])) for x in glob.glob(os.path.abspath(SOLUTION_MASK))]
missing = list(set(range(1, 1000)).difference(solved))

print(missing)
with open("missing_solutions", "wb+") as f:
    pickle.dump(missing, f)
