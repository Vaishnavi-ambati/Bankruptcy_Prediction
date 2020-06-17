from Modules.appLogger import application_logger
from Modules.DataLoader import predictionDataLoader
from Modules.SaveLoadModel import saveLoadModel
from Modules.DataPreprocessor import dataPreprocessor
from Modules.DbInsertion import DbInsertion
import pandas as pd

class predictData:
    """
                            Class Name: predictData
                            Description: Predicts the rating of a restaurant based on the inputs.
                            Input: None
                            Output: CSV file containing the ratings of the restaurants given in the input file.
                            On Failure: Raise Exception

                            Written By: Murali Krishna Chintha
                            Version: 1.0
                            Revisions: None
    """

    def __init__(self):

        try:
            self.prediction_logs = pd.read_csv('Logs\\Prediction Logs\\prediction_logs.csv')
            self.prediction_logs.drop('Unnamed :0', axis = 1, inplace= True)

        except:
            self.prediction_logs = pd.DataFrame(columns=['date','time','logs'])

        self.db_insertion_obj = DbInsertion.db_insertion('Logs\\Prediction Logs\\prediction_logs.csv','PredLogs')
        self.loggerObj = application_logger.logger()
        self.data_loaderObj = predictionDataLoader.predictionDataLoader(logger_obj= self.loggerObj, log_file = self.prediction_logs)
        self.load_modelObj = saveLoadModel.saveLoadModel(loggerObj= self.loggerObj, log_file = self.prediction_logs)
        self.preprocessObj = dataPreprocessor.processData(logger_object= self.loggerObj, log_file = self.prediction_logs)


    def predict_data(self, filename, year):
        """
                                Class Name: predict_data
                                Description: Predicts the rating of a restaurant based on the inputs.
                                Input: None
                                Output: CSV file containing the ratings of the restaurants given in the input file.
                                On Failure: Raise Exception

                                Written By: Murali Krishna Chintha
                                Version: 1.0
                                Revisions: None
        """

        try:
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs, "Prediction of data has started")
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs,"Entered predict_data of predictData class")

            prediction_data = self.data_loaderObj.load_prediction_data(filename)

            print("prediction_data")
            print(prediction_data)

            #preprocess the data before loading the model
            preprocessed_prediction_data = self.preprocessObj.preprocess_prediction_data(prediction_data)

            print("preprocessed_prediction_data")
            print(preprocessed_prediction_data)

            #loading the model.
            model = self.load_modelObj.load_model(year)

            #predciting using the loaded model.
            predictions = model.predict(preprocessed_prediction_data)

            predictions_dataframe = pd.concat([preprocessed_prediction_data,pd.DataFrame(predictions,columns= ['Class'])], axis=1)
            predictions_dataframe['Class'] = predictions_dataframe['Class'].map({0: 'No', 1: 'Yes'})

            predictions_dataframe.to_csv('Prediction_Output_Files\\predictions.csv')

            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs, "Prediction of Data is a success.")
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs, "Exiting the predict_data method of predictData class.")

            self.prediction_logs.to_csv("Logs\\Prediction Logs\\prediction_logs.csv", index= False)

            # self.db_insertion_obj.db_insert_query()


            return "Success"

        except Exception as e:

            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs, "Exception occured in predict_data method of predictData class. The exception is " + str(e))
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs,'Exiting the predict_data method of predictData class.')
            self.prediction_logs.to_csv("Logs\\Prediction Logs\\prediction_logs.csv", index= False)

            self.db_insertion_obj.db_insert_query()
            raise Exception

    def predict_single_manual(self, features_list,year):
        """
                                        Method Name: predict_single_manual
                                        Description: Predicts the rating of a restaurant based on the inputs entered manually.
                                        Input: None
                                        Output: Rating of the restaurant
                                        On Failure: Raise Exception

                                        Written By: Murali Krishna Chintha
                                        Version: 1.0
                                        Revisions: None
                """

        try:
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs, "Prediction of data has started")
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs,"Entered predict_single_manual of predictData class")

            preprocessed_dataframe = self.preprocessObj.preprocess_single_predict_manual(features_list)

            # loading the model.
            model = self.load_modelObj.load_model(year)

            # predciting using the loaded model.
            predictions = model.predict(preprocessed_dataframe)

            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs, "Prediction of Data is a success.")
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs, "Exiting the predict_single_manual method of predictData class.")

            self.prediction_logs.to_csv("Logs\\Prediction Logs\\prediction_logs.csv", index=False)

            return predictions

        except Exception as e:

            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs,"Exception occured in predict_single_manual method of predictData class. The exception is " + str(
                                                                e))
            self.prediction_logs = self.loggerObj.write_log(self.prediction_logs,
                                                            'Exiting the predict_single_manual method of predictData class.')
            self.prediction_logs.to_csv("Logs\\Prediction Logs\\prediction_logs.csv", index=False)

            raise Exception

