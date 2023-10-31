from flask import Flask, request

app = Flask(__name__)

@app.route('/crud/espresso', methods=['GET', 'POST'])
def espresso_drinks():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of espresso drinks',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an espresso drink',
            'method': request.method,
		'body': request.json
        }

@app.route('/crud/espresso/<int:drink_id>', methods=['GET', 'PUT', 'DELETE'])
def espresso(drink_id):
    if request.method == "GET":
        return {
            'id': drink_id,
            'message': 'This endpoint should return the drink {} details'.format(drink_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': drink_id,
            'message': 'This endpoint should update the drink {}'.format(drink_id),
            'method': request.method,
		'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': drink_id,
            'message': 'This endpoint should delete the drink {}'.format(drink_id),
            'method': request.method
        }

if __name__ == "__main__":
    app.run(debug=True)     
