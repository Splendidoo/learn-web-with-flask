from flask import Flask #imports Flask class from the flask module

app = Flask(__name__) #Creates a Flask object

@app.route("/")
def hello_world():
  return "Hello World!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)