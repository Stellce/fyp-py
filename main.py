import data_preparation as dp
import model_training as mt
import pickle

# Load and preprocess data
file_path = input("File path: ") or 'data.xlsx'
print(file_path)
data = dp.load_data(file_path)
data = dp.preprocess_data(data)


# Load the trained model
with open("trained_model.pkl", "rb") as file:
    algo = pickle.load(file)

# Get recommendations for a specific user
user_id = input('User ID: ') or '1'
print(user_id)
recommendations = mt.get_recommendations(user_id, data, algo, top_n=5)
print(f"Recommendations for user {user_id}: {recommendations}")
