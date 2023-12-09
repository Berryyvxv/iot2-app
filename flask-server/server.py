from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Route for seeing a data
@app.route('/noiseLevel')
def get_noiseLevel():
    # Returning an api for showing in  reactjs
    return {
        'tableID': 1, 
        "noiseLevel":"First",
        "tableAvailability":"Not Available", 
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

