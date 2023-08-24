from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/temprature')
def temp():
    return render_template('temprature.html')

@app.route('/light')
def light():
    return render_template('light.html')

@app.route('/button')
def button():
    return render_template('button.html')

if __name__ == "__main__":
    app.run(debug=True)
