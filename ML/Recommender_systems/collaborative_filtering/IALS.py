# Implicit Alternating Least Squares


# l: regularization weight 
# p: the preference of user u for item i, which is 1 for observed interactions and 0 otherwise.
# c: the confidence level associated with each interaction.
# We are trying to minimize c(p - U @ V)^2 + l(|U|^2 + |V|^2)
# derivative with respect to U: 2cV(p - U @ V) + 2lU = 0
# cVp - cVUV + lU = 0
# cVp = (cVV + lI) U
# b = A x




import numpy as np

# Initialize user-item interaction matrix with normalized watch times
watch_times_matrix = np.array(
    [[0.0, 0.0, 0.0, 0.9, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7, 0.0, 0.95, 0.0],
    [0.0, 0.65, 1.1, 0.0, 0.85, 0.0, 0.0, 0.6, 0.7, 0.0, 0.0],
    [0.0, 1.2, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.75, 0.0, 0.0, 0.9, 0.0],
    [0.0, 0.0, 0.85, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.95],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.1, 0.0, 0.0, 0.0, 0.0, 0.8],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 0.0, 0.0, 0.75, 0.0],
    [0.0, 0.0, 0.0, 0.7, 0.0, 0.0, 0.0, 0.0, 0.85, 1.2, 0.0]]
)

num_users, num_items = watch_times_matrix.shape
num_factors = 32
lambda_reg = 40
alpha_conf = 40
num_iterations = 15

# Initialize user and item feature matrices with better initial values
user_features = np.random.normal(0, 0.01, (num_users, num_factors))
item_features = np.random.normal(0, 0.01, (num_items, num_factors))

# Create preference and confidence matrices
preference_matrix = (watch_times_matrix > 0).astype(np.float32)
confidence_matrix = 1 + alpha_conf * watch_times_matrix

# Pre-compute identity matrix
lambda_identity = lambda_reg * np.eye(num_factors, dtype=np.float32)

def update_user_features(user_feat, item_feat, confidence, preference, num_usrs, num_feats, reg_param):
    item_features_T = item_feat.T
    for user in range(num_usrs):
        conf_u = confidence[user]
        conf_u_mat = np.diag(conf_u)
        print(item_feat.shape)
        print(conf_u_mat.shape)
        A = item_features_T  @ conf_u_mat @ item_feat + lambda_identity
        b = item_features_T @ conf_u_mat @ preference[user]
        user_feat[user] = np.linalg.solve(A, b)

def update_item_features(user_feat, item_feat, confidence, preference, num_items, num_feats, reg_param):
    user_features_T = user_feat.T
    for item in range(num_items):
        conf_i = confidence[:, item]
        conf_i_mat = np.diag(conf_i)
        A = user_features_T @ conf_i_mat @ user_feat + lambda_identity
        b = user_features_T @ conf_i_mat @ preference[:, item]
        item_feat[item] = np.linalg.solve(A, b)

def train_ials():
    global user_features, item_features
    
    for _ in range(num_iterations):
        update_user_features(user_features, item_features, confidence_matrix, preference_matrix, num_users, num_factors, lambda_reg)
        update_item_features(user_features, item_features, confidence_matrix, preference_matrix, num_items, num_factors, lambda_reg)

    return user_features @ item_features.T

prediction_matrix = train_ials()
print('Final Predicted Ratings Matrix:')
print(prediction_matrix)




# 2
import numpy as np

# Initialize user-item interaction matrix with normalized watch times
watch_times_matrix = np.array(
    [[0.0, 0.0, 0.0, 0.9, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7, 0.0, 0.95, 0.0],
     [0.0, 0.65, 1.1, 0.0, 0.85, 0.0, 0.0, 0.6, 0.7, 0.0, 0.0],
     [0.0, 1.2, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.75, 0.0, 0.0, 0.9, 0.0],
     [0.0, 0.0, 0.85, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.95],
     [0.0, 0.0, 0.0, 0.0, 0.0, 1.1, 0.0, 0.0, 0.0, 0.0, 0.8],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 0.0, 0.0, 0.75, 0.0],
     [0.0, 0.0, 0.0, 0.7, 0.0, 0.0, 0.0, 0.0, 0.85, 1.2, 0.0]],
    dtype=np.float32
)

num_users, num_items = watch_times_matrix.shape

# Reduced number of latent factors
num_factors = 32

lambda_reg = 40.0
alpha_conf = 40.0
num_iterations = 15

# Initialize user and item feature matrices (float32 for speed/consistency)
user_features = np.random.normal(0, 0.01, (num_users, num_factors)).astype(np.float32)
item_features = np.random.normal(0, 0.01, (num_items, num_factors)).astype(np.float32)

# Create preference and confidence matrices
preference_matrix = (watch_times_matrix > 0).astype(np.float32)
confidence_matrix = 1.0 + alpha_conf * watch_times_matrix

# Pre-compute identity matrix
lambda_identity = (lambda_reg * np.eye(num_factors, dtype=np.float32))

def update_user_features(user_feat, item_feat, confidence, preference, num_usrs, num_feats, reg_param):
    item_features_T = item_feat.T  # (F, I)
    for user in range(num_usrs):
        cu = confidence[user]               # (I,)
        # Avoid diag(cu): scale rows of item_feat by cu
        A = item_features_T @ (item_feat * cu[:, None]) + lambda_identity
        b = item_features_T @ (preference[user] * cu)
        user_feat[user] = np.linalg.solve(A, b)

def update_item_features(user_feat, item_feat, confidence, preference, num_items, num_feats, reg_param):
    user_features_T = user_feat.T  # (F, U)
    for item in range(num_items):
        ci = confidence[:, item]         # (U,)
        # Avoid diag(ci): scale rows of user_feat by ci
        A = user_features_T @ (user_feat * ci[:, None]) + lambda_identity
        b = user_features_T @ (preference[:, item] * ci)
        item_feat[item] = np.linalg.solve(A, b)

def train_ials():
    global user_features, item_features
    for _ in range(num_iterations):
        update_user_features(user_features, item_features, confidence_matrix, preference_matrix, num_users, num_factors, lambda_reg)
        update_item_features(user_features, item_features, confidence_matrix, preference_matrix, num_items, num_factors, lambda_reg)
    return user_features @ item_features.T

prediction_matrix = train_ials()
print('Final Predicted Ratings Matrix:')
# print(prediction_matrix)

# Extract predicted values for a specific user (e.g., user 0)
user_id = 0
user_predictions = prediction_matrix[user_id]
# print(user_predictions)

# Find indices of the top 5 items with the largest predicted values
recommended_indices = np.argsort(user_predictions)[-5:]


print(f'Recommended Items for user {user_id}: {recommended_indices}')