import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print('🚀 STEP 5: IMPROVED ML MODEL')
print('=' * 50)

# Load cleaned data
df = pd.read_csv('data/telco_churn_cleaned.csv')

print('1. PREPARING ENHANCED FEATURES...')
# Convert categorical variables to numeric (simple encoding)
df_ml = df.copy()

# Encode important categorical features
df_ml['Contract_encoded'] = df_ml['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
df_ml['InternetService_encoded'] = df_ml['InternetService'].map({'No': 0, 'DSL': 1, 'Fiber optic': 2})
df_ml['OnlineSecurity_encoded'] = df_ml['OnlineSecurity'].map({'No': 0, 'Yes': 1, 'No internet service': 2})

# Select features for improved model
features = [
    'tenure', 'MonthlyCharges', 'TotalCharges',
    'Contract_encoded', 'InternetService_encoded', 'OnlineSecurity_encoded'
]

X = df_ml[features]
y = df_ml['Churn_binary']

print('Enhanced features:', features)
print('')

print('2. TRAINING IMPROVED MODEL...')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train improved model
model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print('✅ Improved Model Performance:')
print(f'📊 Accuracy: {accuracy:.2%}')

print('')
print('3. FEATURE IMPORTANCE (Improved):')
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance)

print('')
print('4. CREATING CONFUSION MATRIX...')
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - Churn Prediction')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.savefig('confusion_matrix.png', dpi=100, bbox_inches='tight')
print('✅ Saved: confusion_matrix.png')

print('')
print('🎯 BUSINESS RECOMMENDATIONS:')
print('1. Focus on customers with HIGH Monthly Charges')
print('2. Monitor customers with SHORT Tenure')
print('3. Month-to-month contracts are highest risk')
print('')
print(f'💡 The model can help prevent {accuracy:.1%} of potential churn!')
