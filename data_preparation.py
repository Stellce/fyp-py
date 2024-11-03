import pandas as pd


def load_data(file_path):
    """Load data from an Excel file."""
    data = pd.read_excel(file_path)
    return data


def preprocess_data(data):
    """Clean and preprocess the data."""
    # Convert 'purchased_at' to datetime
    data['purchased_at'] = pd.to_datetime(data['purchased_at'], errors='coerce')

    # Ensure is_on_wishlist, and is_in_cart are booleans
    data['is_on_wishlist'] = data['is_on_wishlist'].astype(bool)
    data['is_in_cart'] = data['is_in_cart'].astype(bool)

    # Ensure price is float
    data['price'] = data['price'].astype(float)

    data['interaction_score'] = data.apply(calculate_interaction_score, axis=1, current_date=pd.Timestamp.now())

    return data


def calculate_interaction_score(row, current_date):
    # Assign base scores and weights for each factor
    score = row['price'] * 0.5  # base score from price

    # Wishlist and cart adjustments
    if row['is_on_wishlist']:
        score += 1  # add weight if in wishlist
    if row['is_in_cart']:
        score += 2  # higher weight if in cart

    # Recency adjustment
    days_since_purchase = (current_date - row['purchased_at']).days if pd.notnull(row['purchased_at']) else 0
    recency_score = max(1, 30 - days_since_purchase // 30)
    score += recency_score

    return score
