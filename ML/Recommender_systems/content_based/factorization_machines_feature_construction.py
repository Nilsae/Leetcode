import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Reading JSON files
with open('tracks.json', 'r') as tracks_file:
    tracks = json.load(tracks_file)
    
with open('users.json', 'r') as users_file:
    users = json.load(users_file)
    
with open('interactions.json', 'r') as interactions_file:
    interactions = json.load(interactions_file)


genre_encodings = {"Jazz": [1, 0, 0], "Pop": [0, 1, 0], "Rock": [0, 0, 1]}


# Prepare data
data = []

for interaction in interactions:
    user_id = interaction['user_id']
    track_id = interaction['track_id']
    rating = interaction['rating']

    user_dummies = [1 if i == user_id else 0 for i in range(1, len(users) + 1)]
    track_dummies = [1 if i == track_id else 0 for i in range(1, len(tracks) + 1)]

    # Extract user and track features
    user = next(user for user in users if user['id'] == user_id)
    track = next(track for track in tracks if track['id'] == track_id)

    track_likes = track['likes']
    user_listening_avg = user['time_listening_avg']

    user_genre_array = np.array(list(user['genre_preferences'].values()))
    track_genre_array = np.array(genre_encodings[track['genre']])
    genre_similarity = cosine_similarity([user_genre_array], [track_genre_array])[0, 0]

    # Combine all features and append to data
    row = user_dummies + track_dummies + [track_likes, user_listening_avg, genre_similarity, rating]
    data.append(row)

# Define column names
columns = ['user1', 'user2', 'user3', 'track1', 'track2', 'track3', 
           'track_likes', 'user_listening_avg', 'genre_similarity', 'rating']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

print(df)