import pandas as pd
import joblib

model = joblib.load('Model/best_model.pkl')

features = [
    'order_year',
    'order_month',
    'order_weekday_name',
    'order_hour',
    'is_weekend',
    'total_price',
    'total_freight',
    'order_total_value',
    'total_items',
    'average_item_price',
    'number_of_sellers',
    'freight_ratio',
    'customer_state'
]
input_data = pd.DataFrame(columns=features)

for col in features:
    if col in ['order_year', 'order_month', 'order_hour', 'is_weekend', 'total_items', 'number_of_sellers']:
        input_data[col] = [int(input(f"Enter value for {col}: "))]
    elif col in ['total_price', 'total_freight', 'order_total_value', 'average_item_price', 'freight_ratio']:
        input_data[col] = [float(input(f"Enter value for {col}: "))]
    elif col == 'order_weekday_name':
        input_data[col] = [input(f"Enter value for {col} (e.g., Monday, Tuesday): ")]
    elif col == 'customer_state':
        input_data[col] = [input(f"Enter value for brazilian {col} (e.g., AL, MA): ")]

prediction = model.predict(input_data)
probability = model.predict_proba(input_data)[:, 1]

label = 'Late' if prediction[0] == 1 else 'On Time / Early'
print(f'\nPrediction: {label}')
print(f'Probability of late delivery: {probability[0]:.4f}')