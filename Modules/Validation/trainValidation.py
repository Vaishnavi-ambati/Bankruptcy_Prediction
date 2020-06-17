from Modules.appLogger import application_logger
import pandas as pd
from Modules.RawDataValidation import validateRawTrainingData
from Modules.DataLoader import trainingDataLoader
from Modules.DbInsertion import DbInsertion

class train_validation:
    """
                  Class Name: validate_train
                  Description: Validates the training data.
                  Input: None

                  Written By: Murali Krishna Chintha
                  Version: 1.0
                  Revisions: None
     """

    def __init__(self):
        # self variables
        try:
            self.train_validation_logs = pd.read_csv('Logs\\Training Validation\\train_validation_logs.csv')
        except:
            self.train_validation_logs = pd.DataFrame(columns=['date', 'time', 'logs'])
        self.db_insertion_obj = DbInsertion.db_insertion('Logs\\Training Validation\\train_validation_logs.csv', 'TrainValidLogs')
        self.logger_object = application_logger.logger()
        self.raw_validate = validateRawTrainingData.validate_raw_data(self.logger_object,self.train_validation_logs)
        self.data_loader = trainingDataLoader.data_loader(self.logger_object,self.train_validation_logs)

    def validate_train(self, filename):
        """
                     Method Name: validate_train
                     Description: Validates the training data.
                     Input: None

                     Written By: Murali Krishna Chintha
                     Version: 1.0
                     Revisions: None
        """
        try:
            self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs, 'Entered validate_train class of trainValidation')
            self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs, 'Training Data Validation has started.')

            dataframe = self.data_loader.load_data(filename)

            # columns names and no. of columns check
            validate = self.raw_validate.column_validate(dataframe)

            self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs, 'Entered validateRawData')

            if validate:
                self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs, 'Columns are Valid in the Training Data.')
            else:
                self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs, 'Columns are not valid in the Training Data.')


            # entire column null values check.
            null_values = self.raw_validate.entire_column_null_value_check(dataframe)

            if not null_values:
                self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs, 'No column in the dataset has complete null values.')
            else:
                self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs,  'Dataset cannot be accepted.')

            if not null_values and validate:
                self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs,'Exiting validate_train of trainValidation class.')
                self.train_validation_logs.to_csv('Logs\\Training Validation\\train_validation_logs.csv',index=False)
                self.db_insertion_obj.db_insert_query()

                return True
            else:
                self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs,'Exiting validate_train of trainValidation class.')
                self.train_validation_logs.to_csv('Logs\\Training Validation\\train_validation_logs.csv',index=False)
                self.db_insertion_obj.db_insert_query()

                return False

        except Exception as e:
            self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs,'An Exception has occured in validate_train of trainValidation class. The Exception is ' + str(e))
            self.train_validation_logs = self.logger_object.write_log(self.train_validation_logs,'Exting validate_train of trainValidation class.')
            self.train_validation_logs.to_csv('Logs\\Training Validation\\train_validation_logs.csv', index=False)
            self.db_insertion_obj.db_insert_query()
            raise Exception
