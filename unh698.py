from flask import Flask, render_template

import prometheus_metrics

app = Flask(__name__)

from prometheus_metrics import setup_metrics
setup_metrics(app)

@app.route('/')
def home():
    return render_template('marvel.html',unh698_image_version='0.0.4')

@app.route('/movie')
def movie():
    filmlist = (
                 {'name':'Doctor Strange','release':'Nov 4, 2016','image':'https://i.annihil.us/u/prod/marvel/i/mg/3/50/57fd2d2084523/portrait_incredible.jpg'},
                 {'name':'Captain America: Civil War','release':'May 6, 2016','image':'https://i.annihil.us/u/prod/marvel/i/mg/c/30/521f6f84ecba1/portrait_incredible.jpg'},
                 {'name':'Ant-Man','release':'Jul 17, 2015','image':'https://i.annihil.us/u/prod/marvel/i/mg/d/60/5553932315f24/portrait_incredible.jpg'},                 
               )
    return render_template('movie.html',list=filmlist)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

