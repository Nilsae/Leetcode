# We are shifting from using the raw rating to the deviation from the user's average. This ensures we're measuring how much more (or less) a neighbor liked an item compared to their usual baseline.
import numpy as np

# Read user-item rating matrix from a text file
def read_users_items_matrix(file_path):
    users_items_matrix = {}
    with open(file_path, 'r') as file:
        for line in file:
            user, item, rating = line.strip().split(',')
            if user not in users_items_matrix:
                users_items_matrix[user] = {}
            users_items_matrix[user][item] = int(rating)
    return users_items_matrix

# Updated Pearson correlation function considering only common items
def pearson_correlation(ratings1, ratings2):
    common_items = [item for item in ratings1.keys() if item in ratings2]
    if not common_items:
        return 0

    ratings1_common = np.array([ratings1[item] for item in common_items])
    ratings2_common = np.array([ratings2[item] for item in common_items])

    mean1 = np.mean(ratings1_common)
    mean2 = np.mean(ratings2_common)

    diff1 = ratings1_common - mean1
    diff2 = ratings2_common - mean2

    numerator = np.sum(diff1 * diff2)
    denominator = np.sqrt(np.sum(diff1 ** 2) * np.sum(diff2 ** 2))

    if denominator == 0:
        return 0
    else:
        return numerator / denominator

# Predicting rating without considering user's average
def raw_rating_prediction(target_user, target_item, user_ratings):
    similarities = []
    weighted_sum = 0
    sum_of_weights = 0

    target_ratings = user_ratings[target_user]

    for user, ratings in user_ratings.items():
        if user != target_user and target_item in ratings:
            similarity = pearson_correlation(target_ratings, ratings)
            similarities.append((user, similarity))
            
            rating = ratings[target_item]
            
            weighted_sum += similarity * rating
            sum_of_weights += abs(similarity)

    if sum_of_weights == 0:
        return np.mean(list(target_ratings.values()))
    return weighted_sum / sum_of_weights

# Predicting rating considering user's average
def weighted_rating_prediction(target_user, target_item, user_ratings):
    similarities = []
    weighted_sum = 0
    sum_of_weights = 0
    
    target_ratings = user_ratings[target_user]
    avg_target_user_rating = np.mean(list(target_ratings.values()))

    for user, ratings in user_ratings.items():
        if user != target_user and target_item in ratings:
            similarity = pearson_correlation(target_ratings, ratings)
            similarities.append((user, similarity))
            
            avg_user_rating = np.mean(list(ratings.values()))
            rating_diff = ratings[target_item] - avg_user_rating
            
            weighted_sum += similarity * rating_diff
            sum_of_weights += abs(similarity)

    if sum_of_weights == 0:
        return avg_target_user_rating
    return avg_target_user_rating + (weighted_sum / sum_of_weights)

# Define the path to the text file
file_path = 'user_items_matrix.txt'

# Read the user-item matrix
users_items_matrix = read_users_items_matrix(file_path)

# Calculate and print the average rating for each user
for user, ratings in users_items_matrix.items():
    avg_rating = np.mean(list(ratings.values()))
    print(f"Average rating for {user}: {avg_rating}")

print(weighted_rating_prediction('User3', 'ItemC', users_items_matrix))
print(raw_rating_prediction('User3', 'ItemC', users_items_matrix))