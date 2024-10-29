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

    # Ensure price is int
    data['price'] = data['price'].astype(int)

    return data
