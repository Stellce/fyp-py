import data_preparation as dp
import model_training as mt

# Load and preprocess data
file_path = 'data.xlsx'
data = dp.load_data(file_path)
data = dp.preprocess_data(data)

# Train the model
algo = mt.train_model(data)

# Get recommendations for a specific user
user_id = 'user1'  # Replace with an actual user ID
recommendations = mt.get_recommendations(user_id, data, algo, top_n=5)
print(f"Recommendations for user {user_id}: {recommendations}")
