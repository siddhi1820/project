import numpy as np
from flask import Flask,request,render_template
import joblib
app=Flask(__name__)
model=joblib.load('loandata.pkl')


@app.route('/')
def home():
    return render_template('vhg.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender=1
        Gender=0
        Married=request.form['Married']
        if(Married=='No'):
            Married=0
        Married=1
        Dependents = request.form['Dependents']
        Education=request.form['Education']
        if (Education == 'Graduate'):
            Education= 0
        Education = 1
        Self_Employed = request.form['Self_Employed']
        if (Self_Employed == 'No'):
            Self_Employed = 0
        Self_Employed = 1

        Property_Area=request.form['Property_Area']
        if (Property_Area == 'Rural'):
            Property_Area = 0
        elif (Property_Area=='Semiurban'):
            Property_Area=1
        else:
            Property_Area=2

        History=(request.form['Credit_History'])
        if History == '':
            return render_template('vhg.html', val2='Enter credict History eigther 0 or 1')
        Amount=(request.form['Amount'])
        if Amount=='':
            return render_template('vhg.html',val='Please Enter Amount')

        sample_data=np.array([[Gender,Married,Dependents,Education,Self_Employed,History,Property_Area,Amount]])
        y_pred=model.predict(sample_data)
        if y_pred==0:
            return render_template('vhg.html',predict1='Sorry !! Your loan is not approval')
        else:
            return render_template('vhg.html',predict1='Congradution your loan is approval')


if __name__=='__main__':
    app.run(debug=True)

