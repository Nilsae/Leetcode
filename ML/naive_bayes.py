#  how the code is implementing

# [
# \hat{A} = \arg\max_A P(B \mid A),P(A)
# ]

# Let’s connect the **math symbols → code lines** very clearly.

# ---

# ## Step 1. What the formula means

# We want to predict the class (A) that maximizes:

# * prior of the class
# * times likelihood of the observed features

# So conceptually:

# ```
# score(class) = P(class) * P(features | class)
# ```

# Then choose the class with largest score.

# ---

# ## Step 2. Where the code sets (P(A))

# This line:

# ```python
# class_probabilities[class_] = priors[class_]
# ```

# This is exactly:

# [
# P(A)
# ]

# So for each class we start the score with its prior probability.

# ---

# ## Step 3. Where the code builds (P(B \mid A))

# This loop:

# ```python
# for feature in X_test.columns:
#     feature_probs = likelihoods[feature][class_]
#     class_probabilities[class_] *= feature_probs.get(...)
# ```

# This is doing:

# [
# \prod_i P(x_i \mid A)
# ]

# because:

# * each feature probability is multiplied
# * multiplication accumulates the likelihood

# So after the loop finishes:

# ```
# class_probabilities[class_] =
# P(A) * P(x1|A) * P(x2|A) * ... * P(xn|A)
# ```

# And under Naive Bayes assumption:

# [
# P(B \mid A) = \prod_i P(x_i \mid A)
# ]

# So now the code has computed:

# [
# P(B \mid A)P(A)
# ]

# Exactly the numerator of Bayes rule.

# ---

# ## Step 4. Where the code does the **argmax**

# This line:

# ```python
# max(class_probabilities, key=class_probabilities.get)
# ```

# means:

# 👉 find the class whose score is largest.

# Mathematically:

# [
# \arg\max_A P(B \mid A)P(A)
# ]

# That is precisely the prediction rule.

# ---

# ## Step 5. Why the denominator is missing

# The real Bayes formula is:

# [
# P(A \mid B)
# ===========

# \frac{P(B \mid A)P(A)}{P(B)}
# ]

# But in classification:

# * (P(B)) is the same for all classes
# * so it does not change which class is largest

# Therefore:

# [
# \arg\max_A P(A \mid B)
# ======================

# \arg\max_A P(B \mid A)P(A)
# ]

# So the code correctly ignores the denominator.

# ---

# ## Step 6. Put it all together in one mapping

# Math step → Code step

# Start score with prior

# ```python
# class_probabilities[class_] = priors[class_]
# ```

# Multiply likelihoods

# ```python
# class_probabilities[class_] *= feature_probs.get(...)
# ```

# Choose best class

# ```python
# max(class_probabilities, key=class_probabilities.get)
# ```

# This is literally:

# [
# \hat{A} = \arg\max_A P(B \mid A)P(A)
# ]

# ---

# ## Intuition picture

# For each class the code is asking:

# > “If this sample really belonged to this class, how probable would its feature values be?”

# Then:

# > “Also, how common is this class overall?”

# Multiply those.

# Then:

# > “Which class makes this sample most plausible?”

# That class wins.

# ---

# ## Very important insight

# The code is **not computing true posterior probabilities.**

# It is computing **unnormalized scores**.

# But argmax does not need normalization.

# This is a key ML trick.

import pandas as pd

def calculate_prior_probabilities(y):
    return y.value_counts(normalize=True)

def calculate_likelihoods_with_smoothing(X, y):
    likelihoods = {}
    for column in X.columns:
        likelihoods[column] = {}
        for class_ in y.unique():
            # Calculate normalized counts with smoothing
            class_data = X[y == class_][column]
            counts = class_data.value_counts()
            total_count = len(class_data) + len(X[column].unique())  # total count with smoothing
            likelihoods[column][class_] = (counts + 1) / total_count  # add-1 smoothing
    return likelihoods

def naive_bayes_classifier(X_test, priors, likelihoods):
    predictions = []
    for _, data_point in X_test.iterrows():
        class_probabilities = {}
        for class_ in priors.index:
            class_probabilities[class_] = priors[class_]
            for feature in X_test.columns:
                # Use .get to safely retrieve probability and get a default of 1/total to handle unseen values
                feature_probs = likelihoods[feature][class_]
                class_probabilities[class_] *= feature_probs.get(data_point[feature], 1 / (len(feature_probs) + 1))

        # Predict class with maximum posterior probability
        predictions.append(max(class_probabilities, key=class_probabilities.get))

    return predictions

weather_data = {
    'Temperature': ['Hot', 'Cold', 'Cold', 'Hot', 'Hot'],
    'Wind': ['Strong', 'Weak', 'Strong', 'Strong', 'Weak'],
    'Forecast': ['Rain', 'Rain', 'Sunny', 'Sunny', 'Sunny']
}

df = pd.DataFrame(weather_data)

new_day = pd.DataFrame([{'Temperature': 'Hot', 'Wind': 'Weak'}])
priors = calculate_prior_probabilities(df['Forecast'])
likelihoods = calculate_likelihoods_with_smoothing(df[['Temperature', 'Wind']], df['Forecast'])
weather_prediction = naive_bayes_classifier(new_day, priors, likelihoods)
print("Forecast for the new day is:", weather_prediction)