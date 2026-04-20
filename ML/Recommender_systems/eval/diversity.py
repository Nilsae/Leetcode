# Diversity measures how different the recommended items are from each other
# based on their vector representations (e.g., embeddings, features).

# IMPORTANT:
# - We compare ITEM vectors, not user vectors
# - For each user, we compute pairwise similarity between their recommended items

# For a given user with k recommended items:
# - we compute cosine similarity for all item pairs → O(k^2)
# - high similarity → items are similar → low diversity
# - low similarity → items are different → high diversity

# Overall complexity:
# O(num_users * k^2)

# So:
# - each user conceptually has their own diversity score
# - but we average across all users to get one system-level diversity metric

# Final formula:
# diversity = 1 - average pairwise cosine similarity

# Intuition:
# - if recommendations are all similar → diversity ≈ 0
# - if recommendations are varied → diversity ≈ 1

# NOTE:
# This function assumes item_vectors are meaningful (e.g., learned embeddings);
# otherwise, diversity scores will not reflect real item differences.





# How cosine_similarity(X) works if only one input X is provided:
# 1. It takes a list of vectors (X) as input.
# 2. It calculates the similarity between every pair of vectors in X.
# 3. It returns a matrix where the element at [i, j] is the 
#    similarity between vector i and vector j.
# 4. The diagonal [i, i] is always 1.0 because an item is identical to itself.


# How cosine_similarity(X, Y) works if provided with both inputs:
# 1. X and Y are both lists of vectors.
# 2. It calculates the similarity between each vector in X and each vector in Y.
# 3. The resulting matrix has dimensions (len(X), len(Y)).
# 4. If Y is not provided, it defaults to Y=X, comparing X to itself.







from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def diversity(predictions, item_vectors):
    item_indices = [[item_vectors[item] for item in items if item in item_vectors] for items in predictions.values()]

    total_similarity = 0
    count = 0
    for items in item_indices:
        if len(items) < 2:
            continue
        similarities = cosine_similarity(items)
        # Calculate sum of similarities while excluding self-similarity (diagonal)
        sum_similarities = np.sum(similarities) - len(items)
        total_similarity += sum_similarities
        # N * N - N (because all the matrix elements minus the diagonals)
        count += (len(items) * (len(items) - 1))
    

    if count != 0:
        average_similarity = total_similarity / count
        return 1 - average_similarity
    return 0

# Example data
user_predictions = {
    'user1': ['item1', 'item2', 'item3'],
    'user2': ['item2', 'item3', 'item4'],
    'user3': ['item1', 'item4', 'item5']
}

# Assuming item_vectors is pre-defined with relevant dimensional vectors
item_vectors = {
    'item1': np.array([1, 0, 0]),
    'item2': np.array([0, 1, 0]),
    'item3': np.array([0, 0, 1]),
    'item4': np.array([1, 1, 0]),
    'item5': np.array([0, 1, 1]),
}

# Calculate the diversity score
diversity_score = diversity(user_predictions, item_vectors)
print(f"Diversity: {diversity_score:.2f}")