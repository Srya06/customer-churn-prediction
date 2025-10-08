import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print('🚀 SIMPLE IMPROVED MODEL')
print('=' * 40)

# Load data
df = pd.read_csv('data/telco_churn_cleaned.csv')

# Simple feature engineering
features = ['tenure', 'MonthlyCharges', 'TotalCharges']
X = df[features]
y = df['Churn_binary']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print('Model Accuracy:', f'{accuracy:.2%}')
print('')
print('Feature Importance:')
for feature, importance in zip(features, model.feature_importances_):
    print(f'  {feature}: {importance:.3f}')
print('')
print('✅ Ready for dashboard!')
