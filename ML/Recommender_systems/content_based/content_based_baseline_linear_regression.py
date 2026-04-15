import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


# Load data from JSON files
tracks_df = pd.read_json('tracks.json')
authors_df = pd.read_json('authors.json')


# Merge the dataframes on the common 'author_id' field
merged_df = pd.merge(tracks_df, authors_df, on='author_id', how='inner')


# Simulate user listening history or preferences
user_features = {
   "rock_preference": 5,   # On a scale of 1-5
   "pop_preference": 4,    # On a scale of 1-5
   "jazz_preference": 2,   # On a scale of 1-5
   "listens": 50,          # Total listens
   "likes": 30             # Total likes
}


# Create a profile for user
user_profile = pd.DataFrame([user_features])


# Function to map genre preferences for similarity calculation
def map_genre_to_similarity(df):
   genre_map = {
       "Rock": np.array([1, 0, 0]),
       "Pop": np.array([0, 1, 0]),
       "Jazz": np.array([0, 0, 1])
   }
   genre_features = df['genre'].apply(lambda x: genre_map[x])
   return genre_features.tolist()


# Calculate similarity between user's genre preferences and tracks' genres
track_genre_features = np.array(map_genre_to_similarity(merged_df))
user_genre_preferences = np.array([user_profile.iloc[0]['rock_preference'],
                                  user_profile.iloc[0]['pop_preference'],
                                  user_profile.iloc[0]['jazz_preference']]).reshape(1, -1)
similarities = cosine_similarity(track_genre_features, user_genre_preferences).flatten()


# Attach similarity scores to the tracks
merged_df['similarity'] = similarities


# Standardize numerical features
scaler = StandardScaler()
numeric_columns = ["likes", "clicks", "full_listens", "author_listeners", "similarity"]
track_features_scaled = scaler.fit_transform(merged_df[numeric_columns])


# Add a synthetic rating
merged_df['rating'] = [4, 5, 3]  # Mock ratings for tracks as example


# Train a linear regression model using merged_df data
model = LinearRegression()
model.fit(track_features_scaled, merged_df['rating'])


# Define test songs
test_songs = [
   {
       "likes": 120,
       "clicks": 350,
       "full_listens": 110,
       "author_listeners": 6000,
       "genre": "Rock"
   },
   {
       "likes": 130,
       "clicks": 300,
       "full_listens": 100,
       "author_listeners": 6500,
       "genre": "Pop"
   },
   {
       "likes": 110,
       "clicks": 320,
       "full_listens": 105,
       "author_listeners": 5500,
       "genre": "Jazz"
   }
]
test_df = pd.DataFrame(test_songs)
genre_vectors = map_genre_to_similarity(test_df)
test_df['similarity'] = cosine_similarity(genre_vectors, user_genre_preferences).flatten()


test_features_scaled = scaler.transform(test_df[numeric_columns])


pred = model.predict(test_features_scaled)
print(pred)

