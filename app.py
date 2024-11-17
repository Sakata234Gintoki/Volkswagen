from waitress import serve
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    query = data.get('query')

    if "Volkswagen" in query and "SUV" in query:
        response = "You should consider the Volkswagen Tiguan or the Volkswagen ID.4 for a great SUV experience!"
    else:
        response = "I'm sorry, I didn't understand your question."
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

