from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/goal')
def goal():
    return render_template('goal.html')
@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)