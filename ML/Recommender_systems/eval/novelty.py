# Novelty measures how "unexpected" or "non-obvious" the recommended items are.
#
# For each recommended item, we compute:
#   -log(item_popularity / total_users)
#
# Intuition:
# - item_popularity / total_users is the probability of encountering that item
#   in the user base
# - if an item is very popular, this probability is high, so -log(prob) is small
# - if an item is rare, this probability is low, so -log(prob) is large
#
# So:
# - popular items -> low novelty
# - rare / niche items -> high novelty
#
# Information theory intuition:
# -log(p) is called "self-information"
# It measures how surprising an event is:
# - common event -> little information / little surprise
# - rare event   -> high information / high surprise
#
# In recommender systems, this means:
# - recommending blockbuster items gives low novelty
# - recommending less-known items gives high novelty
#
# We sum this value over all recommended items, then divide by len(predicted_items)
# to get the average novelty per recommendation.
#
# Why divide by len(predicted_items)?
# - without it, the score would grow just because we recommended more items
# - with it, we get a fair "novelty per item" measure
#
# Final intuition:
# novelty tells us whether the recommender is mostly suggesting obvious popular
# items, or helping the user discover less common ones.

# If an item’s popularity is unknown, we assume it is minimally popular (rare),
# so it contributes high novelty instead of breaking the calculation.


# setup 1 no missing handling
import math

def novelty(predicted_items, item_popularity, total_users):
    sum_log_probabilities = sum(
        -math.log(item_popularity.get(item, 0) / total_users)
        for item in predicted_items if item in item_popularity
    )
    return sum_log_probabilities / len(predicted_items)

def calculate_average_novelty(users_predicted_items, item_popularity, total_users):
    total_novelty = 0
    for predicted_items in users_predicted_items:
        # Calculate novelty for each user and accumulate
        user_novelty = novelty(predicted_items, item_popularity, total_users)
        total_novelty += user_novelty

    # Calculate and print average novelty
    average_novelty = total_novelty / len(users_predicted_items)
    print(f"Average Novelty: {average_novelty:.2f}")

# Example data
item_popularity = {1: 80, 2: 50, 3: 30, 4: 20, 5: 5, 6: 5, 7: 5}
users_predicted_items = [
    [1, 5, 3],
    [2, 4, 6],
    [1, 2, 5],
    [3, 4, 7],
    [5, 6, 7]
]
total_users = 100

calculate_average_novelty(users_predicted_items, item_popularity, total_users)



# setup 2 with missing handling
import math


DEFAULT_POPULARITY = 1

def calculate_item_popularity(raw_recommendations):
    item_popularity = {}
    for recommended_item in raw_recommendations:
        item_popularity[recommended_item] = item_popularity.get(recommended_item, 0) + 1
    return item_popularity

def novelty(predicted_items, item_popularity, total_users):
    sum_log_probabilities = sum(
        -math.log(item_popularity.get(item, DEFAULT_POPULARITY) / total_users) for item in predicted_items
    )
    return sum_log_probabilities / len(predicted_items)

# Example data
raw_recommendations = [1, 2, 1, 3, 4, 1, 5, 6, 7, 5, 5, 5, 5, 3, 3, 5, 5, 5, 5, 5, 1, 2, 7, 1, 2, 5, 5, 6, 5]
predicted_items = [1, 5, 3]
total_users = 10  # Example total number of users
item_popularity = calculate_item_popularity(raw_recommendations)
novelty_score = novelty(predicted_items, item_popularity, total_users)
print(f"Novelty: {novelty_score:.2f}")