from flask import Flask
app = Flask(__name__)

@app.route("/noiseLevel")
def noiseLevel():
    return {"noiseLevel:": ["tableID","warningType", "tableAvailability"]}

if __name__=="__main__":
    app.run(debug=True)