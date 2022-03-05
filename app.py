#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get('loan')
        print(income, age, loan)
        model = joblib.load('CCD_LR')
        pred = model.predict([[float(income), float(age), float(loan)]])
        print(pred)
        if pred[0] == 0:
            decision = 'No'
        elif pred[0] == 1:
            decision = 'Yes'
        print(decision)
        s_lr = 'Predicted default possibility based on Logistics Regression is: ' + str(decision)
        model = joblib.load('CCD_DT')
        pred = model.predict([[float(income), float(age), float(loan)]])
        print(pred)
        if pred[0] == 0:
            decision = 'No'
        elif pred[0] == 1:
            decision = 'Yes'
        print(decision)
        s_dt = 'Predicted default possibility based on Decision Tree is: ' + str(decision)
        model = joblib.load('CCD_RF')
        pred = model.predict([[float(income), float(age), float(loan)]])
        print(pred)
        if pred[0] == 0:
            decision = 'No'
        elif pred[0] == 1:
            decision = 'Yes'
        print(decision)
        s_rf = 'Predicted default possibility based on Random Forest is: ' + str(decision)
        model = joblib.load('CCD_XGB')
        pred = model.predict([[float(income), float(age), float(loan)]])
        print(pred)
        if pred[0] == 0:
            decision = 'No'
        elif pred[0] == 1:
            decision = 'Yes'
        print(decision)
        s_xgb = 'Predicted default possibility based on XGBoost is: ' + str(decision)
        model = joblib.load('CCD_NN')
        pred = model.predict([[float(income), float(age), float(loan)]])
        print(pred)
        if pred[0] == 0:
            decision = 'No'
        elif pred[0] == 1:
            decision = 'Yes'
        print(decision)
        s_nn = 'Predicted default possibility based on Neural Network is: ' + str(decision)
        return(render_template("index.html", result1=s_lr, result2=s_dt, result3=s_rf, result4=s_xgb, result5=s_nn))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2", result4="2", result5="2"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




