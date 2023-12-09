from flask import Flask, jsonify
from flask_cors import CORS
import pyrebase

app = Flask(__name__)
CORS(app)

firebaseConfig = {
    "apiKey": "AIzaSyC5Ql__00x7m10GTAi-znW1QgK7BJGFWRw",
    "authDomain": "noise-detector-cd802.firebaseapp.com",
    "databaseURL": "https://noise-detector-cd802-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "noise-detector-cd802",
    "storageBucket": "noise-detector-cd802.appspot.com",
    "messagingSenderId": "263064507685",
    "appId": "1:263064507685:web:9af0b69f0c9ffd3adff6cc"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)

# Getting reference to the Firebase database
DB = firebase.database()

def get_data():
    # Retrieve data from Firebase
    data1 = DB.child('test/float').get().val() #Warning Type
    data2 = DB.child('test/int').get().val() #Table ID

    return {'tableID1': data1, 'noiseLevel1': data2}

# Route for seeing data including Firebase data
@app.route('/noiseLevel')
def get_noiseLevel():
    # Get the data from the Firebase database
    firebase_data = get_data()

    # Construct the response dictionary
    response_data = {
        'tableID': 1,
        'noiseLevel': "First",
        'tableAvailability': "Not Available",
        'tableID1': firebase_data['tableID1'],
        'noiseLevel1': firebase_data['noiseLevel1'],
    }

    # Returning the combined data as a JSON response
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
