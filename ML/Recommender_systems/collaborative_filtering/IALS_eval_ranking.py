import numpy as np

# the lower the mean_rank, the better the model

# Step 1: Define the watch_times_test array for two users
watch_times_user1 = [0.3, 0.5, 1.7, 0.7, 1.0, 1.2, 0.4, 0.8, 1.3]
watch_times_user2 = [0.4, 1.1, 0.2, 0.6, 0.9, 0.5, 1.3, 0.7, 1.4]

# Define the list of recommended items for both users
recommended_items_user1 = [2, 5, 3, 8, 6]
recommended_items_user2 = [0, 1, 4, 7, 3]

# Calculate rankings for both users
rankings_user1 = {item: idx / (len(recommended_items_user1) - 1) for idx, item in enumerate(recommended_items_user1)}
rankings_user2 = {item: idx / (len(recommended_items_user2) - 1) for idx, item in enumerate(recommended_items_user2)}

# Step 2: Calculate the mean_rank for both users combined
numerator = 0.0
denominator = 0.0

# User 1
for i in recommended_items_user1:
    watch_time_ui = watch_times_user1[i]
    rank_ui = rankings_user1[i]
    numerator += watch_time_ui * rank_ui
    denominator += watch_time_ui

# User 2
for i in recommended_items_user2:
    watch_time_ui = watch_times_user2[i]
    rank_ui = rankings_user2[i]
    numerator += watch_time_ui * rank_ui
    denominator += watch_time_ui

# Calculate mean_rank
mean_rank = numerator / denominator if denominator != 0 else float('nan')

print(f"Mean Rank for both users: {mean_rank:.4f}")

