
import numpy as np

R = []
with open('explicit-ratings.txt', 'r') as file:
    users = file.readlines()
    for user in users:
        # Split the string into a list of strings using space as a delimiter
# Then convert each string in that list into an integer
        ratings = list(map(int, user.split(' ')))
        R.append(ratings)

R = np.array(R)

print(R)  