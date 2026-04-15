



import numpy as np

def read_users_items_matrix(file_path):
    users_items_matrix = {}
    with open(file_path, 'r') as file:
        for line in file:
            user, item, rating = line.strip().split(',')
            if user not in users_items_matrix:
                users_items_matrix[user] = {}
            users_items_matrix[user][item] = int(rating)
    return users_items_matrix

def pearson_correlation(ratings1, ratings2):
    n = len(ratings1)
    assert n == len(ratings2)

    mean1 = np.mean(ratings1)
    mean2 = np.mean(ratings2)

    diff1 = ratings1 - mean1
    diff2 = ratings2 - mean2

    numerator = np.sum(diff1 * diff2)
    denominator = np.sqrt(np.sum(diff1 ** 2) * np.sum(diff2 ** 2))

    if denominator == 0:
        return 0
    else:
        return numerator / denominator

def predict_rating(target_user, target_item, user_ratings):
    weighted_sum = 0
    sum_of_weights = 0
    
    target_ratings = np.array([rating for item, rating in user_ratings[target_user].items() if item != target_item])
    
    for user, ratings in user_ratings.items():
        if user != target_user and target_item in ratings:
            other_ratings = np.array([rating for item, rating in ratings.items() if item != target_item])
            user_similarity = pearson_correlation(target_ratings, other_ratings)
            weighted_sum += user_similarity * ratings[target_item]  
            sum_of_weights += abs(user_similarity) # because pearson can be negative and for the denominator we need the magnitude for it not to cancel out

    if sum_of_weights == 0:
        return 0
    else:
        return weighted_sum / sum_of_weights

file_path = 'user_items_matrix.txt'
users_items_matrix = read_users_items_matrix(file_path)

predicted_rating = predict_rating('User3', 'ItemC', users_items_matrix)
print(f"Predicted Rating for User3 on ItemC (To Be Changed): {predicted_rating}")