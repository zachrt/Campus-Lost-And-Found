import csv
import random
from datetime import datetime, timedelta

categories = ['Electronics', 'Clothing', 'Books', 'Keys', 'Wallets']
locations = ['Library', 'Student Union', 'Gym', 'Science Building', 'Cafeteria']
statuses = ['Lost', 'Found', 'Claimed']

with open('synthetic_items.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['item_id', 'category', 'description', 'location', 'status', 'date_reported'])
    
    for i in range(1, 10001):
        date = datetime.now() - timedelta(days=random.randint(0, 365))
        writer.writerow([
            i,
            random.choice(categories),
            f"Synthetic item {i} for load testing",
            random.choice(locations),
            random.choice(statuses),
            date.strftime('%Y-%m-%d')
        ])
