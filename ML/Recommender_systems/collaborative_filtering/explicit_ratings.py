
import numpy as np
import random

R = []
with open('explicit-ratings.txt', 'r') as file:
    users = file.readlines()
    for user in users:
        # Split the string into a list of strings using space as a delimiter
        # Then convert each string in that list into an integer
        ratings = list(map(int, user.split(' ')))
        R.append(ratings)

R = np.array(R)



num_users, num_items = R.shape
original_R = R.copy()  # Create a copy to track original values
missing_ratio = 0.1  # Fraction of entries to exclude
num_missing = int(missing_ratio * np.count_nonzero(R != -1))
missing_indices = random.sample(list(zip(*np.where(R != -1))), num_missing)
# np.where(R != -1) returns a tuple of arrays: (rows, cols)
# Example: ([0, 1, 1], [0, 0, 1])
#
# The * (asterisk) is the unpacking operator:
# It "unpacks" the tuple into separate arguments.
#
# So:
#   zip(*np.where(R != -1))
# is equivalent to:
#   rows, cols = np.where(R != -1)
#   zip(rows, cols)
#
# This lets zip pair corresponding elements:
#   [(row1, col1), (row2, col2), ...]
#
# Without *, zip would receive a single tuple and not pair rows and cols correctly.

for (u, i) in missing_indices:
    R[u, i] = -1  # Mark selected original values as missing