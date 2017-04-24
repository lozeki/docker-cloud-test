from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "UNH698 Website"

@app.route('/marvel')
def marvel():
    return render_template('marvel.html')

@app.route('/character')
def marvel():
    return render_template('character.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
