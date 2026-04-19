# Coverage calculation
# Coverage is the proportion of all possible items that appear at least once in the recommendation results across users.
# Intuition: it tells you how much of your catalog your model is actually using—low coverage means it keeps recommending the same few items, while high coverage means it explores and recommends a wider variety of items.

def coverage(predictions, all_items):
    # s = set()
    # for item_list in predictions.values():
    #     for item in item_list:
    #         s.add(item)
    s = {item for item_list in predictions.values() for item in item_list}
    return len(s) / len(all_items) if all_items else None
    # Use a set comprehension to gather all unique recommended items
    # Return the coverage by dividing unique items by total items

# Example data
all_possible_items = [1, 2, 3, 4, 5, 6, 7]
user_predictions = {
    'User1': [1, 2, 3],
    'User2': [3, 4, 5],
    'User3': [5, 6, 7]
}
cove = coverage(user_predictions, all_possible_items)
print(f"{cove:.2f}")
# Call the coverage function and print the coverage score with two decimal precision








# 2
import xgboost as xgb
import numpy as np

# Load dataset
# For a more diverse and realistic dataset, let's create data for 4 users and 15 unique items
# Each data point represents a user-item interaction with features (item_id, ...) and corresponding rating

# Example user-item interactions for training
X_train = np.array([
    [1, 1], [1, 3], [1, 4], [1, 5],
    [2, 2], [2, 5], [2, 6], [2, 7],
    [3, 2], [3, 3], [3, 8], [3, 9],
    [4, 1], [4, 6], [4, 10], [4, 11]
])
y_train = np.array([
    5, 3, 4, 4,  # Ratings for User 1
    3, 4, 5, 2,  # Ratings for User 2
    4, 3, 5, 5,  # Ratings for User 3
    2, 5, 4, 3   # Ratings for User 4
])

# Sample test data for user predictions (items each user hasn't interacted with)
X_test = np.array([
    [1, 6], [1, 7], [1, 12], [1, 13],  # Predictions needed for User 1
    [2, 8], [2, 9], [2, 12], [2, 13],  # Predictions needed for User 2
    [3, 10], [3, 11], [3, 12], [3, 14],  # Predictions needed for User 3
    [4, 8], [4, 9], [4, 14], [4, 15]   # Predictions needed for User 4
])

# Train the model
model = xgb.XGBRegressor(objective='reg:squarederror')
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Determine top items for each user
num_users = 4
user_prediction_counts = 3  # Number of top recommendations for each user
top_items = []

for user_idx in range(num_users):
    start_idx = user_idx * len(X_test) // num_users
    end_idx = (user_idx + 1) * len(X_test) // num_users
    user_predictions = predictions[start_idx:end_idx]
    user_top_indices = np.argsort(user_predictions)[-user_prediction_counts:]
    print(f"indices of predicted items for user {user_idx}: {user_top_indices}")
    user_items = X_test[start_idx:end_idx][user_top_indices]
    top_items.extend(user_items[:, 1])  # Take the item_id, which is the second feature

# Example all items (all unique items from training/testing data)
all_possible_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(top_items)
# Calculate and print coverage score
coverage = len(set(top_items)) / len(all_possible_items)
print(coverage)
# All the predictions are stored in top_items list