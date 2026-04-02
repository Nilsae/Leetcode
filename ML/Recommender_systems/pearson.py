# Variance: mean((x - mean_x)**2)
# std_dev: radical(Variance)
# Covariance: mean((x - mean_x) * (y - mean_y))
# Pearson: covariance(x, y) / (std_dev(x) * std_dev(y)) = sum((x - mean_x) * (y - mean_y)) / (sqrt((sum((x - mean_x)**2))) * sqrt(sum(sqrt((y - mean_y)**2))))
# Covariance depends on the scale of the data, making it hard to compare different datasets. Pearson Correlation normalizes it to a range between -1 and 1, providing a consistent measure of relationship strength regardless of the units

# The Pearson correlation coefficient ranges from -1 to 1:
# A coefficient of 1 indicates a perfect positive linear relationship.
# A coefficient of -1 indicates a perfect negative linear relationship.
# A coefficient of 0 indicates no linear correlation.

import numpy as np

# Function to calculate Pearson correlation between two users
def pearson_correlation(ratings1, ratings2):
    n = len(ratings1)
    assert n == len(ratings2)

    mean1 = np.mean(ratings1)
    mean2 = np.mean(ratings2)

    diff1 = ratings1 - mean1
    diff2 = ratings2 - mean2

    numerator = np.sum(diff1 * diff2)  # Error
    denominator = np.sqrt(np.sum(diff1 ** 2) * np.sum(diff2 ** 2))  # Error

    if denominator == 0:
        return 0
    else:
        return numerator / denominator

# Example user ratings
user1_ratings = np.array([5, 3, 4, 2, 1, 5, 3, 4, 2, 1, 5, 3, 4, 2, 1])
user2_ratings = np.array([5, 3, 3, 2, 1, 3, 3, 4, 2, 1, 5, 2, 2, 2, 1])

pearson_similarity = pearson_correlation(user1_ratings, user2_ratings)
print(f"Pearson Correlation: {pearson_similarity}")