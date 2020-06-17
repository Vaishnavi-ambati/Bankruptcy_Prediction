from Modules.appLogger import application_logger
import pandas as pd
import numpy as np


class validate_raw_data():

    def __init__(self, logger_object,log_file):
        self.log_file = log_file
        self.logger_object = logger_object

    def column_validate(self,dataframe):
        """
                                Module Name: column_validate
                                Description: Validates the number of columns and the column names.
                                Input: dataframe
                                Output: True/False
                                On Failure: Raise Exception

                                Written By: Murali Krishna Chintha
                                Version: 1.0
                                Revisions: None
        """
        try:
            self.log_file = self.logger_object.write_log(self.log_file, 'Data Validation has Stared.')

            columns = list(dataframe.columns)
            length_of_columns = len(columns)

            actual_columns = ['Attr1', 'Attr2', 'Attr3', 'Attr4', 'Attr5', 'Attr6', 'Attr7', 'Attr8',
                              'Attr9', 'Attr10', 'Attr11', 'Attr12', 'Attr13', 'Attr14', 'Attr15',
                              'Attr16', 'Attr17', 'Attr18', 'Attr19', 'Attr20', 'Attr21', 'Attr22',
                              'Attr23', 'Attr24', 'Attr25', 'Attr26', 'Attr27', 'Attr28', 'Attr29',
                              'Attr30', 'Attr31', 'Attr32', 'Attr33', 'Attr34', 'Attr35', 'Attr36',
                              'Attr37', 'Attr38', 'Attr39', 'Attr40', 'Attr41', 'Attr42', 'Attr43',
                              'Attr44', 'Attr45', 'Attr46', 'Attr47', 'Attr48', 'Attr49', 'Attr50',
                              'Attr51', 'Attr52', 'Attr53', 'Attr54', 'Attr55', 'Attr56', 'Attr57',
                              'Attr58', 'Attr59', 'Attr60', 'Attr61', 'Attr62', 'Attr63', 'Attr64','class']

            # checking for column data types
            object_column_list = ['Attr1', 'Attr2', 'Attr3', 'Attr4', 'Attr5', 'Attr6', 'Attr7', 'Attr8',
                                  'Attr9', 'Attr10', 'Attr11', 'Attr12', 'Attr14', 'Attr15', 'Attr16',
                                  'Attr17', 'Attr18', 'Attr21', 'Attr22', 'Attr24', 'Attr25', 'Attr26',
                                  'Attr27', 'Attr28', 'Attr29', 'Attr32', 'Attr33', 'Attr34', 'Attr35',
                                  'Attr36', 'Attr37', 'Attr38', 'Attr40', 'Attr41', 'Attr45', 'Attr46',
                                  'Attr47', 'Attr48', 'Attr50', 'Attr51', 'Attr52', 'Attr53', 'Attr54',
                                  'Attr57', 'Attr59', 'Attr60', 'Attr61', 'Attr63', 'Attr64']

            float_column_list = ['Attr13', 'Attr19', 'Attr20', 'Attr23', 'Attr30', 'Attr31', 'Attr39',
                                 'Attr42', 'Attr43', 'Attr44', 'Attr49', 'Attr55', 'Attr56', 'Attr58',
                                 'Attr62','class']

            object_columns = list(dataframe.dtypes[dataframe.dtypes == np.object].index)
            float_columns = list(dataframe.dtypes[(dataframe.dtypes == np.float64) | (dataframe.dtypes == np.int64)].index)


            if object_columns == object_column_list and float_columns == float_column_list:
                data_type_validate = True
            else:
                data_type_validate = False


            if columns == actual_columns and data_type_validate:
                self.logger_object.write_log(self.log_file, 'Columns in the data are valid.')
                self.log_file = self.logger_object.write_log(self.log_file,'Exited column_validate module of validateRawTrainingData class.')

                return True


            elif columns == actual_columns and not data_type_validate:
                self.logger_object.write_log(self.log_file, 'Columns in the dataset are valid but the column data types are not valid.')
                self.log_file = self.logger_object.write_log(self.log_file,'Exited column_validate module of validateRawTrainingData class.')

                return False
            else:
                self.logger_object.write_log(self.log_file, 'Columns in the data are not valid.')
                self.log_file = self.logger_object.write_log(self.log_file,'Exited column_validate module of validateRawTrainingData class.')

                return False


        except Exception as e:
            self.log_file = self.logger_object.write_log(self.log_file, 'An Exception has occured in column_validate of validateRawTrainingData class. The Exception is ' + str(e))
            self.log_file = self.logger_object.write_log(self.log_file,'Exting column_validate of validateRawTrainingData class.')
            self.log_file.to_csv('Logs\\Training Validation\\train_validation_logs.csv')



    def entire_column_null_value_check(self, dataframe):
        """
                                Module Name: entire_column_null_value_check
                                Description: Validates the number of columns and the column names.
                                Input: dataframe
                                Output: True/False
                                On Failure: Raise Exception

                                Written By: Murali Krishna Chintha
                                Version: 1.0
                                Revisions: None
        """


        try:

            self.log_file = self.logger_object.write_log(self.log_file, 'Null Values Check has started.')

            null_values_counts = dataframe.isnull().sum()
            length_of_dataframe = dataframe.shape[0]

            column_null_check = []

            for column,null_value_count in null_values_counts.items():
                if null_value_count >= 0.75 * length_of_dataframe:
                    self.raw_prediction_validation_logs = self.logger_object.write_log(self.raw_prediction_validation_logs,'The Column ' + str(column) + ' has only values. The Dataset Cannot be Accepted.')
                    self.raw_prediction_validation_logs = self.logger_object.write_log(self.raw_prediction_validation_logs,'Entire Row null value check has completed.')
                    self.raw_prediction_validation_logs = self.logger_object.write_log(self.raw_prediction_validation_logs,'Exting entireColumnNullValueCheck of validateRawPredicitonData class.')

                    column_null_check.append(True)
                else:
                    self.raw_prediction_validation_logs = self.logger_object.write_log(self.raw_prediction_validation_logs,'No column in the Dataset has complete null values.')
                    self.raw_prediction_validation_logs = self.logger_object.write_log(self.raw_prediction_validation_logs,'Exting entire_column_null_value_check of validateRawPredicitonData class.')

                    column_null_check.append(False)

            if False in column_null_check:
                return False
            else:
                return True


        except Exception as e:
            self.log_file = self.logger_object.write_log(self.log_file,'An Exception has occured in entire_column_null_value_check of validateRawTrainingData class. The Exception is ' + str(e))
            self.log_file = self.logger_object.write_log(self.log_file,'Exting entire_column_null_value_check of validateRawPredicitonData class.')
            self.log_file.to_csv('Logs\\Training Validation\\train_validation_logs.csv')

