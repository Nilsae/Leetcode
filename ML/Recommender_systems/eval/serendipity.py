# Serendipity measures how many recommended items are both:
# 1) relevant (the user actually likes them)
# 2) unexpected (not among popular/common items)
#
# It captures "pleasant surprises" in recommendations.
# High serendipity means the model is not just accurate,
# but also helping users discover less obvious items.
#
# Formula:
# serendipity = (# relevant AND not popular recommendations) / (total recommendations)


# Serendipity calculation

def serendipity(true_items, predicted_items, popular_items):
    serendipitous_recommendations = sum(1 for item in predicted_items if item in true_items and item not in popular_items)
    total_recommendations = len(predicted_items)
    return serendipitous_recommendations / total_recommendations

# Data for 5 users
users = {
    'User1': {'true_items': [1, 3, 5], 'predicted_items': [5, 6, 7]},
    'User2': {'true_items': [2, 4, 6], 'predicted_items': [4, 6, 8]},
    'User3': {'true_items': [7, 9, 10], 'predicted_items': [7, 9, 11]},
    'User4': {'true_items': [3, 5, 10], 'predicted_items': [5, 10, 12]},
    'User5': {'true_items': [1, 8, 9], 'predicted_items': [9, 10, 1]}
}

popular_items = [1, 2, 5]
average_serendipity = 0

# Calculate and print serendipity score for each user
for user, items in users.items():
    s = serendipity(items['true_items'], items['predicted_items'], popular_items)
    print(s)
    average_serendipity += s

average_serendipity /= len(users)
print(average_serendipity)
# Calculate and print average serendipity score for all users