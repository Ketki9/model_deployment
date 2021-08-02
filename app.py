import pickle
import joblib
from flask import Flask,render_template,request


#initiate the app
app=Flask(__name__)

#load the model
model=joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return render_template('form.html')

# @app.route('/home')
# def home():
#     return render_template('index.html')

# @app.route('/contact')
# def contact():
#     return 'contact pag'

@app.route('/submit' , methods = ["POST"])
def form_data():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    #insert in db query
    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    print(output)

    if output[0] == 1:
        out = 'diabatic'
    else:
        out = 'not diabatic'

    return render_template('predict.html' , data = f'person is {out}')




print(__name__)

if __name__ == '__main__':
    app.run(debug=True)