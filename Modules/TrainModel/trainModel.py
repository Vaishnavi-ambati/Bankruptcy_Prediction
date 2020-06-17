# trains different models and finds the best model based the metrics given and dumps the model into a pickle file.
import pandas as pd
from Modules.DataLoader import trainingDataLoader
from Modules.appLogger import application_logger
from Modules.DataPreprocessor import dataPreprocessor
from Modules.ModelFinder import modelFinder
from sklearn.model_selection import train_test_split
from Modules.SaveLoadModel import saveLoadModel
from Modules.DbInsertion import DbInsertion

class trainModel:

    def __init__(self):
        try:
            self.train_model_logs = pd.read_csv('Logs\\TrainingLogs\\train_model_logs.csv')
        except:
            self.train_model_logs = pd.DataFrame(columns=['date', 'time', 'logs'])

        self.db_insertion_obj = DbInsertion.db_insertion('Logs\\TrainingLogs\\train_model_logs.csv',
                                                         'TrainLogs')
        self.loggerObj = application_logger.logger()
        self.data_loader = trainingDataLoader.data_loader(self.loggerObj,self.train_model_logs)
        self.preprocess = dataPreprocessor.processData(self.loggerObj,self.train_model_logs)
        self.model_finder_obj = modelFinder.modelFinder(self.loggerObj,self.train_model_logs)
        self.save_modelObj = saveLoadModel.saveLoadModel(self.loggerObj,self.train_model_logs)

    def train_model(self, filename, year):
        """
                                Method Name: train_model
                                Description: Trains the models with the input.
                                Output: saves the best model the specified directory.
                                On Failure: Raise Exception

                                Written By: Murali Krishna Chintha
                                Version: 1.0
                                Revisions: None
        """


        try:
            print('entered train_model')
            self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'Entered the train_model method of the modelFinder class.')
            self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'Training the model with input data has started.')

            # loading the data.
            data = self.data_loader.load_data(filename)

            # preprocessing the data

            preprocessed_data = self.preprocess.preprocess_training_data(data)
            print("Preprocess done")

            null_value_dict, value = self.preprocess.null_value_check(preprocessed_data)

            if value:
                self.train_model_logs = self.loggerObj.write_log((self.train_model_logs,'There are null in the data set.' + 'The null value counts are' + str(null_value_dict)))
                self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'Dealing with null values has started.')
                #dropping the null values
                preprocessed_data.dropna(inplace=True)
                self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'Null values have been dealt with.')


            else:
                self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'There are no null values in the data.')

            # seperating independent and dependent features.
            X, y = self.preprocess.separate_label_feature(preprocessed_data, 'class')

            # splitting the data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            features_list = ['Attr1', 'Attr2', 'Attr3', 'Attr4', 'Attr5', 'Attr6', 'Attr7', 'Attr8',
                           'Attr9', 'Attr10', 'Attr11', 'Attr12', 'Attr13', 'Attr14', 'Attr15',
                           'Attr16', 'Attr17', 'Attr18', 'Attr19', 'Attr20', 'Attr21', 'Attr22',
                           'Attr23', 'Attr24', 'Attr25', 'Attr26', 'Attr27', 'Attr28', 'Attr29',
                           'Attr30', 'Attr31', 'Attr32', 'Attr33', 'Attr34', 'Attr35', 'Attr36',
                           'Attr37', 'Attr38', 'Attr39', 'Attr40', 'Attr41', 'Attr42', 'Attr43',
                           'Attr44', 'Attr45', 'Attr46', 'Attr47', 'Attr48', 'Attr49', 'Attr50',
                           'Attr51', 'Attr52', 'Attr53', 'Attr54', 'Attr55', 'Attr56', 'Attr57',
                           'Attr58', 'Attr59', 'Attr60', 'Attr61', 'Attr62', 'Attr63', 'Attr64']

            df_train = X_train
            df_train['class'] = y_train

            df_test = X_test
            df_test['class'] = y_test

            df_train.reset_index(drop=True, inplace=True)
            df_test.reset_index(drop=True, inplace=True)

            df_train_features = df_train[features_list]
            df_test_features = df_test[features_list]

            # Set labels
            df_train_label = df_train['class']
            df_test_label = df_test['class']

            reduced_train_df = self.preprocess.scaling_training_data_columns(df_train_features,features_list)
            df_train_complete = pd.concat([reduced_train_df, df_train_label], axis=1)

            reduced_test_df = self.preprocess.scaling_training_data_columns(df_test_features, features_list)
            df_test_complete = pd.concat([reduced_test_df, df_test_label], axis=1)


            # start of feeding the data to different models.
            best_model, folder_name, best_model_name  = self.model_finder_obj.get_best_model(df_train_complete, df_test_complete, year)

            # dump the best model in a pickle file

            save_model = self.save_modelObj.save_model(best_model, folder_name, best_model_name)

            print(save_model)

            self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'Model has been trained succesfully.')
            self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'Exiting the train_model module of the trainModel Class.')
            self.train_model_logs.to_csv('Logs\\TrainingLogs\\training_logs.csv', index= False)

            self.db_insertion_obj.db_insert_query()

            return save_model

        except Exception as e:
            self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'An Exception has occured in the train_model method of trainModel class. The Exception is '+ str(e))
            self.train_model_logs = self.loggerObj.write_log(self.train_model_logs,'Exiting the train_model module of the trainModel Class.')
            self.train_model_logs.to_csv('Logs\\TrainingLogs\\training_logs.csv', index=False)
            self.db_insertion_obj.db_insert_query()
            raise Exception

        # todo implement oversampling and KFold.

        # get the data - create a .py file for data loading -check

        # create a .py file preprocessing
        # remove the unnecessary columns based on EDA -check
        # check for null values -check
        # deal with null values - yet to be done.

        # create a python file for training different models with the data.
        # use different models -check
        # get the best model - check

        # create a python file for dumping the model into pickl file
        # dump the best model into a pickl file to use it for future prediction.
