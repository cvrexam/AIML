import pandas as pd
import math

def id3(df, features, label):
    if len(df[label].unique()) == 1:
        return df[label].unique()[0]
    elif not features:
        return df[label].mode()[0]
    else:
        best_feature = max(features, key=lambda f: calculate_info_gain(df, f, label))
        tree = {best_feature: {}}
        for value in df[best_feature].unique():
            df_value = df[df[best_feature] == value]
            subtree = id3(df_value, [f for f in features if f != best_feature], label)
            tree[best_feature][value] = subtree
        return tree

def calculate_info_gain(df, feature, label):
    total_entropy = calculate_entropy(df, label)
    feature_entropy = 0
    total_rows = len(df)
    class_list = df[feature].unique()
    for cls in class_list:
        df_value = df[df[feature] == cls]
        p_value = len(df_value) / total_rows
        feature_entropy += p_value * calculate_entropy(df_value, label)
    return total_entropy - feature_entropy

def calculate_entropy(df, label):
    total_rows = len(df)
    class_list = df[label].unique()
    entropy = 0
    for cls in class_list:
        p_cls = len(df[df[label] == cls]) / total_rows
        entropy -= p_cls * math.log2(p_cls)
    return entropy

# Example usage:
df = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Strong', 'Weak', 'Strong', 'Weak', 'Weak', 'Weak'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'High', 'High', 'High', 'High', 'High', 'High'],
    'Play Tennis': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

features = ['Outlook', 'Wind', 'Humidity']
label = 'Play Tennis'

tree = id3(df, features, label)
print(tree)