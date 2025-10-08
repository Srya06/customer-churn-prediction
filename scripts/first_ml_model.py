import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print('🤖 STEP 4: BUILDING MACHINE LEARNING MODEL')
print('=' * 60)

# Load cleaned data
df = pd.read_csv('data/telco_churn_cleaned.csv')

print('1. PREPARING DATA FOR ML...')
# Select features for the model (simple version)
features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn_binary']
ml_df = df[features].copy()

# Separate features (X) and target (y)
X = ml_df[['tenure', 'MonthlyCharges', 'TotalCharges']]
y = ml_df['Churn_binary']

print('Features used:', list(X.columns))
print('Target variable: Churn_binary')

print('')
print('2. SPLITTING DATA...')
# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f'Training set: {X_train.shape[0]} samples')
print(f'Testing set: {X_test.shape[0]} samples')

print('')
print('3. TRAINING RANDOM FOREST MODEL...')
# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print('✅ Model trained successfully!')

print('')
print('4. MAKING PREDICTIONS...')
# Predict on test set
y_pred = model.predict(X_test)

print('')
print('5. MODEL PERFORMANCE:')
accuracy = accuracy_score(y_test, y_pred)
print(f'📊 Accuracy: {accuracy:.2%}')

print('')
print('6. FEATURE IMPORTANCE:')
# See which features are most important
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance)

print('')
print('🎯 BUSINESS INSIGHTS:')
print('- Most important factor for churn:', feature_importance.iloc[0]['feature'])
print('- Model can predict churn with', f'{accuracy:.1%}', 'accuracy')

print('')
print('✅ FIRST ML MODEL COMPLETE!')
