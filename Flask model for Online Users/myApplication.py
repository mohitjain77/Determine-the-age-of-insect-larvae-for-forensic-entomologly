from flask import Flask, render_template, request
from graphviz import render
import age as a
import os
from joblib import load

app = Flask(__name__)
picfolder = os.path.join('static','uploaded_viz')
app.config['UPLOADED_FOLDER'] = picfolder
@app.route('/viz', methods=["GET","POST"])
def predict_age():
    pict = ''
    tree = ''
    la = ''
    age_of_larvae = ''
    if request.method == "POST":
        
        temperature = request.form.get('temperature',False)
        length = request.form.get('length',False)
        weight = request.form.get('weight', False)
        larvelStage = request.form.get('larvelStage',False)
        a.LarvaeAge().path_view(float(length), float(weight), float(larvelStage), float(temperature))
        a.LarvaeAge().tree_view(float(length), float(weight), float(larvelStage), float(temperature))
        age_of_larvae = a.LarvaeAge().age_prediction(float(length), float(weight), float(larvelStage), float(temperature))
        la = round((age_of_larvae)/24,2)
        pict = os.path.join(app.config['UPLOADED_FOLDER'], f'path_view{float(length)}-{float(weight)}-{float(larvelStage)}-{float(temperature)}.svg')
        tree = os.path.join(app.config['UPLOADED_FOLDER'], f'tree_view{float(length)}-{float(weight)}-{float(larvelStage)}-{float(temperature)}.svg')
        return render_template("index.html", path_v= str(pict), tree_v = str(tree), larvae_age=f'The Predicted Age of Larvae is {age_of_larvae} hours({la} days approx.).')
    else:
        return render_template("index.html", path_v = str(pict), tree_v = str(tree), larvae_age=f'The Predicted Age of Larvae is..')


if __name__=="__main__":
    app.run(debug=True)
    