import pickle 
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('linear.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():

    data=request.json['data']
    print(data)
    new_data=[list(data.values())]
    print(f"dict_values {new_data}")
    output=model.predict(new_data)[0]
    return jsonify(output)

@app.route('/predict',methods=['POST'])
def predict():

    data=[float(x) for x in request.form.values()]
    final_features= [np.array(data)]
    print(data)

    output=model.predict(final_features)[0]
    print(output)
    return render_template('home.html', prediction_text="Median house value is {}".format(output))

# if __name__=="__main__":
#     app.run(debug=True)   
