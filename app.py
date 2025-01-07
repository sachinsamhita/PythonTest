from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Sachin, Abhishek and Suhel are working on AI Projects - It requires machine learning  expertise "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
