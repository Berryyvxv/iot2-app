from flask import Flask


app = Flask(__name__)
# Route for seeing a data
@app.route('/noiseLevel')
def get_noiseLevel():
    # Returning an api for showing in  reactjs
    return {
        'tableID':1, 
        "noiseLevel":"First",
        "tableAvailability":"Not Available", 
        }


# @app.route("/")
# def Home():
#     render_template('index.js')


# @app.route('/listen', methods=['GET'])
# def listen():

#     def stream():
#         messages = announcer.listen()  
#         while True:
#             msg = messages.get()  
#             yield msg

#     return Response(stream(), mimetype='text/event-stream')


# @app.route('/noiseLevel')
# def noiseLevel():
#     msg = format_sse(data={
#         'tableID': request.args.get('tableID', 1),
#         'noiseLevel': request.args.get('noiseLevel', 'First'),
#         'tableAvailability': request.args.get('tableAvailability', 'Not Available')
#     })
#     announcer.announce(msg=msg)
#     return {}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

