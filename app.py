from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Namaste! Aapka Python app Docker mein chal raha hai! 🎉"

@app.route('/about')
def about():
    return "Ye ek simple Flask application hai"

if __name__ == '__main__':
    # 0.0.0.0 isliye taaki container ke bahar se bhi access ho sake
    app.run(host='0.0.0.0', port=5000, debug=True)