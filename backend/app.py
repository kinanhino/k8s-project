from flask import Flask, jsonify
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://mongo-service:27017/') 
db = client['churn_predictions']
collection = db['csv_data']


@app.route('/api/<user_id>', methods=['GET'])
def api(user_id):
    # Query MongoDB for the specific user
    user = collection.find_one({"customerID": user_id})

    if user:
        user.pop('_id')  # Remove MongoDB's internal ID field if needed
        return jsonify(user)
    else:
        return jsonify({"error": f"User ID {user_id} not found"}), 404

@app.route('/api/upload', methods=['POST'])
def upload_csv():
    df = pd.read_csv('data.csv')

    data = df.to_dict(orient='records')
    result = collection.insert_many(data)
    return jsonify({'result': 'Data inserted successfully', 'inserted_ids': str(result.inserted_ids)}), 201

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data), 200



if __name__ == '__main__':
    app.run(debug=True, port=5005)
