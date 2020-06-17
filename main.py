from flask import Flask,render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import os
from Modules.PredictData import predictData
from Modules.Validation import trainValidation, predictionValidation
from Modules.TrainModel import trainModel
from flask import send_file
from wsgiref import simple_server

app = Flask(__name__)

class data:
    name: str
    rating: int


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/bulk.html')
def bulk():
    return render_template('bulk.html')

def prediction(filename, year):

    predict_valid_obj = predictionValidation.prediction_validation()
    validation = predict_valid_obj.validate_predict_data(filename)

    if validation:
        predict_obj = predictData.predictData()
        message = predict_obj.predict_data(filename, year)

        print(message)
        return message
    else:
        message = "Failure"
        print(message)
        return message

@app.route('/bulk_results', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['filename']
      filename = secure_filename(f.filename)
      # f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      print(app.instance_path)
      f.save(os.path.join(app.instance_path, 'files', secure_filename(f.filename)))

      print("Filename is ", f.filename)
      year = request.form["year"]
      message = prediction(f.filename, year)

      if message == 'Success':
          return render_template('bulk_results.html')

      else:
          return render_template('errors.html')



@app.route('/retrain.html', methods = ['GET', 'POST'])
def retrain():

    return render_template("retrain.html")

@app.route('/single.html', methods = ['GET', 'POST'])
def single():

    return render_template("single.html")


@app.route('/single_csv.html', methods = ['GET', 'POST'])
def single_csv():

    return render_template("single_csv.html")

@app.route('/single_inputs.html', methods = ['GET', 'POST'])
def single_inputs():

    return render_template("single_inputs.html")

@app.route('/single_results_manual.html', methods = ['GET', 'POST'])
def single_results_manual():
    if request.method == "POST":

        features_list = []
        for i in range(1,65):
            value = request.form['Attr'+ str(i)]
            features_list.append(value)

        year = request.form["year"]

        prediction_obj = predictData.predictData()
        result = prediction_obj.predict_single_manual(features_list,year)

        print(result)

    return render_template("single_results_manual.html", result = result)

def train(filename, year):

    train_val_obj = trainValidation.train_validation()  # object initialization

    validation = train_val_obj.validate_train(filename)  # calling the training_validation function

    if validation:
        train_model_obj = trainModel.trainModel()  # object initialization
        train_model_obj.train_model(filename, year)  # training the model for the files in the table

        return 'Model has been trained successfully.'
    else:
        print('Model training is a failure.')
        return 'Data is not valid'


@app.route('/retrain_results', methods = ['GET', 'POST'])
def retrain_results():

    if request.method == 'POST':
        f = request.files['filename']
        filename = secure_filename(f.filename)
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        print(app.instance_path)
        f.save(os.path.join(app.instance_path, 'files', secure_filename(f.filename)))

        print("Filename for Train is ",f.filename)
        year = request.form["year"]
        message = train(f.filename, year)

        if message == 'success':
            return render_template('retrain_results.html')

        else:
            return render_template('errors.html')


@app.route('/errors.html', methods = ['GET', 'POST'])
def errors():

    return render_template("errors.html")
#
# @app.route('/main.html', methods = ['GET', 'POST'])
# def home():
#
#     return render_template("home.html")
#
# @app.route('/home.html', methods = ['GET', 'POST'])
# def home():

    # return render_template("home.html")

@app.route('/downloadFile')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "Prediction_Output_Files/predictions.csv"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     host = '127.0.0.1'
#     port = 8000
#     httpd = simple_server.make_server(host, port, app)
#     print("Serving on %s %d" % (host, port))
#     httpd.serve_forever()