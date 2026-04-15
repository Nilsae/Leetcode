import numpy as np
# Sample item profiles: described by song genres
item_profiles = {
    'Song1': {'Pop': 0.8, 'Rock': 0.2, 'Jazz': 0.1},
    'Song2': {'Pop': 0.1, 'Rock': 0.9, 'Jazz': 0.4},
    'Song3': {'Pop': 0.3, 'Rock': 0.3, 'Jazz': 0.8},
}

# Sample user profile: representing preferences for genres
# User has listened and liked past music mostly in 'Pop' and 'Jazz'
user_profile = {'Pop': 0.7, 'Rock': 0.2, 'Jazz': 0.6}

# Compute similarity using a dot product for songs
def compute_similarity(user, item):
    print([i for i in item_profiles[item].values()])
    print([i for i in user.values()])
    return np.dot([i for i in user.values()],  [i for i in item_profiles[item].values()])

# Recommend songs based on similarity to user profile
def recommend_songs(user_profile, item_profiles):
    d = {item : compute_similarity(user_profile, item) for item in item_profiles.keys()}
    return sorted(d.items(), key = lambda x: x[1], reverse=True)

# Get recommendations
recommendations = recommend_songs(user_profile, item_profiles)
print("Recommendations:", recommendations)