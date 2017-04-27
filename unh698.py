from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('marvel.html',unh698_image_version='0.0.4')

@app.route('/movie')
def movie():
    filmlist = (
                 {'name':'Doctor Strange','release':'Nov 4, 2016','image':'doctor.jpg'},
                 {'name':'Captain America: Civil War','release':'May 6, 2016','image':'captain.jpg'},
                 {'name':'Ant-Man','release':'Jul 17, 2015','image':'ant.jpg'},                 
               )
    return render_template('movie.html',list=filmlist)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

