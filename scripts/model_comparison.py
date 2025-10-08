import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import xgboost as xgb

print('🤖 MODEL COMPARISON - MULTIPLE ALGORITHMS')
print('=' * 60)

# Load cleaned data
df = pd.read_csv('data/telco_churn_cleaned.csv')

print('1. PREPARING DATA...')
# Select features
features = ['tenure', 'MonthlyCharges', 'TotalCharges']
X = df[features]
y = df['Churn_binary']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print('Training samples:', X_train.shape[0])
print('Testing samples:', X_test.shape[0])
print('')

print('2. TRAINING MULTIPLE MODELS...')
# Define models to compare
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'XGBoost': xgb.XGBClassifier(random_state=42),
    'SVM': SVC(random_state=42)
}

# Train and evaluate each model
results = {}

for name, model in models.items():
    print('Training', name, '...')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy
    print('   ', name, 'Accuracy:', f'{accuracy:.2%}')
    print('')

print('3. MODEL COMPARISON RESULTS:')
print('=' * 40)
# Sort by accuracy
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

for name, accuracy in sorted_results:
    print('   ', f'{name:<20}: {accuracy:.2%}')

print('')
print('4. CREATING COMPARISON CHART...')
# Create bar chart
plt.figure(figsize=(10, 6))
models_names = list(results.keys())
accuracies = list(results.values())

bars = plt.bar(models_names, accuracies, color=['blue', 'green', 'orange', 'red', 'purple'])
plt.title('Model Comparison - Accuracy Scores', fontsize=14, fontweight='bold')
plt.ylabel('Accuracy', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 1)

# Add value labels on bars
for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
             f'{accuracy:.2%}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('model_comparison.png', dpi=100, bbox_inches='tight')
print('Saved: model_comparison.png')

print('')
print('5. BEST MODEL ANALYSIS:')
best_model_name, best_accuracy = sorted_results[0]
print('Best Model:', best_model_name, f'({best_accuracy:.2%} accuracy)')

# Get feature importance for tree-based models
if hasattr(models[best_model_name], 'feature_importances_'):
    print('Feature Importance:')
    feature_imp = pd.DataFrame({
        'feature': features,
        'importance': models[best_model_name].feature_importances_
    }).sort_values('importance', ascending=False)
    
    for index, row in feature_imp.iterrows():
        feature_name = row['feature']
        importance_val = row['importance']
        print('   ', f'{feature_name:<15}: {importance_val:.3f}')

print('')
print('MODEL COMPARISON COMPLETE!')
