import os
import shutil
import pickle

class saveLoadModel:
    """
                            Class Name: saveLoadModel

                            Written By: Murali Krishna Chintha
                            Version: 1.0
                            Revisions: None
    """

    def __init__(self, loggerObj, log_file):
        self.loggerObj = loggerObj
        self.log_file = log_file
        self.model_directory = 'models/'

    def save_model(self,model,folder_name,filename):
        """
                                Module Name: save_model
                                Description: Saves the model into a pickle file.
                                Input: model, filename
                                Output: Pickle file containing the model.
                                On Failure: Raise Exception

                                Written By: Murali Krishna Chintha
                                Version: 1.0
                                Revisions: None
        """

        try:
            self.log_file = self.loggerObj.write_log(self.log_file,'Entered save_model module of the saveLoadModel class.')
            path = os.path.join(self.model_directory,folder_name)
            if os.path.isdir(path):
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path) #
            with open(path +'/' + filename+'.pickle','wb') as f:
                pickle.dump(model, f) # save the model to file
            self.log_file = self.loggerObj.write_log(self.log_file,'Model has been saved Successfully.')
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting save_model')

            return 'success'

        except Exception as e:
            self.log_file = self.loggerObj.write_log(self.log_file,'An exception has occured in save_model module of the saveLoadModel class.')
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting save_model module')
            self.log_file.to_csv("Logs\\TrainingLogs\\training_logs.csv")
            raise Exception()

    def find_model_name(self,year):

        directory_path = 'models'

        folder_name = str(year) + ' year'

        file_name = 'Year' + str(year) + 'XGB'

        return folder_name, file_name

    def load_model(self,year):
        """
                                Module Name: load_model
                                Description: loads the model from a pickle file.
                                Input: filename
                                Output: model
                                On Failure: Raise Exception

                                Written By: Murali Krishna Chintha
                                Version: 1.0
                                Revisions: None
        """

        self.log_file = self.loggerObj.write_log(self.log_file, "Model loading has started")
        self.log_file = self.loggerObj.write_log(self.log_file, "Entered load_model method of saveLoadModel class.")

        folder_name,file_name = self.find_model_name(year)
        try:
            print("Inside load model")
            with open(self.model_directory + folder_name + '/' + file_name + '.pickle', 'rb') as f:
                print("before pickle load model")
                model = pickle.load(f)
                print("after pickle load model")
                self.log_file = self.loggerObj.write_log(self.log_file, "Model" + file_name + "has loaded Succesfully.")
                self.log_file = self.loggerObj.write_log(self.log_file, "Exiting load_model method of saveLoadModel class.")
                return model

        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file, "Model" + file_name + " has not loaded. The exception is " + str(e))
            self.log_file = self.loggerObj.write_log(self.log_file, "Exiting load_model method of saveLoadModel class.")
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception()
