from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy


def train_model(data):
    """Train the recommendation model using SVD."""
    reader = Reader(rating_scale=(0, 1))
    surprise_data = Dataset.load_from_df(data[['customer_id', 'product_id', 'is_on_wishlist']], reader)

    trainset, testset = train_test_split(surprise_data, test_size=0.2)

    algo = SVD()
    algo.fit(trainset)

    # Evaluate model
    predictions = algo.test(testset)
    accuracy.rmse(predictions)

    return algo


def get_recommendations(user_id, data, algo, top_n=5):
    """Generate product recommendations for a specific user."""
    product_list = data['product_id'].unique()
    user_data = data[data['customer_id'] == user_id]
    user_products = user_data['product_id'].unique()

    products_to_predict = [x for x in product_list if x not in user_products]
    predictions = [algo.predict(user_id, product) for product in products_to_predict]

    predictions.sort(key=lambda x: x.est, reverse=True)
    top_predictions = predictions[:top_n]

    recommended_products = [pred.iid for pred in top_predictions]
    return recommended_products
