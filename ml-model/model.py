import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample data for task assignments (replace this with real data)
data = {
    'task_complexity': [1, 2, 3, 1, 3, 2, 1, 2],
    'employee_skill': [3, 2, 1, 2, 3, 1, 2, 1],
    'task_urgency': [1, 3, 2, 1, 2, 3, 1, 3],
    'assigned_employee': [1, 2, 1, 1, 2, 2, 1, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and labels
X = df[['task_complexity', 'employee_skill', 'task_urgency']]
y = df['assigned_employee']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save the trained model
with open('task_assignment_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("Model trained and saved.")
