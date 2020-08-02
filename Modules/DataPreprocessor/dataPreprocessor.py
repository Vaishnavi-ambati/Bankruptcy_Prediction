import ast
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import resample
from sklearn.impute import KNNImputer

class processData:
    """
                            Class Name: processData
                            Description: Preprocess the data.
                            Input: logger_obj, log_file
                            On Failure: Raise Exception

                            Written By: Vaishnavi Ambati
                            Version: 1.0
                            Revisions: None
    """

    def __init__(self, logger_object, log_file):

        self.loggerObj = logger_object
        self.log_file = log_file

    def set_new_headers(self, dataframe, train_bool):
        """
             Method Name: set_new_headers
             Description: Changes the column headings
             Input: dataframe
             Input Type: dataframe
             Output: Returns a dataframe with changed column names.

             Written By:Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """
        try:

            self.log_file = self.loggerObj.write_log(self.log_file, 'Entered set_new_headers of dataProcessor class')
            self.log_file = self.loggerObj.write_log(self.log_file, 'Dataframe with changed column names has been initiated.')

            if train_bool == True:
                cols = ['X' + str(i + 1) for i in range(len(dataframe.columns) - 1)]
                cols.append('Y')
                dataframe.columns = cols
            else:
                cols = ['X' + str(i + 1) for i in range(len(dataframe.columns))]
                dataframe.columns = cols

            return dataframe

        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file,'An error occured in the set_new_headers method of dataPreprocessor class. The exception is ' + str(e))
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting the set_new_headers method of dataPreprocessor class.')
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception


    def convert_columns_type(self, dataframe, train_bool):
        """
                     Method Name: set_new_headers
                     Description: Changes the column headings
                     Input: dataframe
                     Input Type: dataframe
                     Output: Returns a dataframe with changed column names.

                     Written By: Vaishnavi Ambati
                     Version: 1.0
                     Revisions: None
                """

        try:
            self.log_file = self.loggerObj.write_log(self.log_file, 'Entered convert_columns_type of dataProcessor class')
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Dataframe with changed column types has been initiated.')

            if train_bool == True:
                index = 1
                while (index <= 63):
                    colname = dataframe.columns[index]
                    col = getattr(dataframe, colname)
                    dataframe[colname] = col.astype(float)
                    index += 1
                col = getattr(dataframe, 'Y')
                dataframe['Y'] = col.astype(int)
            else:
                index = 1
                while (index <= 63):
                    colname = dataframe.columns[index]
                    col = getattr(dataframe, colname)
                    dataframe[colname] = col.astype(float)
                    index += 1


            return dataframe
        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file,'An error occured in the convert_columns_type method of dataPreprocessor class. The exception is ' + str(e))
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting the convert_columns_type method of dataPreprocessor class.')
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception


    def preprocess_training_data(self, dataframe):
        """
             Method Name: preprocess_training_data
             Description: Preprocess the training data.
             Input: dataframe
             Input Type: dataframe
             Onput: Returns a processsed dataframe.

             Written By: Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """

        try:

            self.log_file = self.loggerObj.write_log(self.log_file, 'Entered preprocess_training_data of dataProcessor class')
            self.log_file = self.loggerObj.write_log(self.log_file, 'Data preprocessing has been initiated.')

            dataframe = self.set_new_headers(dataframe, True)
            print("dataframe columns after set_new_headers")
            print(dataframe.columns)

            if '?' in dataframe.values:
                clms_name_replaced_df = dataframe.replace(to_replace='?', value=np.NaN)
                clms_converted_df = self.convert_columns_type(clms_name_replaced_df, True)
                knn_imputed = KNNImputer(n_neighbors=2).fit_transform(clms_converted_df)
                knn_imputed_df = pd.DataFrame(data=knn_imputed)
            else:
                clms_converted_df = self.convert_columns_type(dataframe, True)
                knn_imputed = KNNImputer(n_neighbors=2).fit_transform(clms_converted_df)
                knn_imputed_df = pd.DataFrame(data=knn_imputed)


            self.log_file = self.loggerObj.write_log(self.log_file,'Data Preprocessing has completed. Exiting the preprocess_training_data method of dataPreprocessor class.')

            return knn_imputed_df

        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file,'An error occured in the preprocess_training_data method of dataPreprocessor class. The exception is ' + str(e))
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting the preprocess_training_data method of dataPreprocessor class.')
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception


    def scaling_training_data_columns(self, dataframe,features_list):
        """
             Method Name: scaling_training_data_columns
             Description: scales columns of training data.
             Input: dataframe
             Input Type: dataframe
             Output: Returns a scaled dataframe.

             Written By:Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """

        try:

            self.log_file = self.loggerObj.write_log(self.log_file, 'Entered scaling_training_data_columns of dataProcessor class')
            self.log_file = self.loggerObj.write_log(self.log_file, 'Scaling training data has been initiated.')

            pp_method = MinMaxScaler()
            pp_method.fit(dataframe)

            reduced_df = pp_method.transform(dataframe)
            reduced_df = pd.DataFrame(reduced_df, columns=features_list)

            self.log_file = self.loggerObj.write_log(self.log_file,'Scaling training data has completed. Exiting the scaling_training_data_columns method of dataPreprocessor class.')

            return reduced_df

        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file,'An error occured in the scaling_training_data_columns method of dataPreprocessor class. The exception is ' + str(e))
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting the scaling_training_data_columns method of dataPreprocessor class.')
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception

    def up_and_down_sampling(self, dataframe,multiply_factor,target_clm):
        """
             Method Name: scaling_training_data_columns
             Description: scales columns of training data.
             Input: dataframe
             Input Type: dataframe
             Output: Returns a scaled dataframe.

             Written By: Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """

        try:

            self.log_file = self.loggerObj.write_log(self.log_file, 'Entered up_and_down_sampling of dataProcessor class')
            self.log_file = self.loggerObj.write_log(self.log_file, 'Up sampling and down sampling training data has been initiated.')

            # Downsampling
            target = target_clm
            df_majority = dataframe[dataframe[target] == 0]
            df_minority = dataframe[dataframe[target] == 1]
            n_samples = len(dataframe) - (len(df_minority) * multiply_factor)
            # Downsample majority class
            df_majority_undersampled = resample(df_majority,
                                                replace=True,
                                                n_samples=n_samples,
                                                random_state=2)

            # Combine minority class with Downsampled df
            df_undersampled = pd.concat([df_majority_undersampled, df_minority])

            # Display new class counts
            print("Target value counts after downsampling: \n", df_undersampled[target].value_counts())

            # Upsampling
            df_majority = df_undersampled[df_undersampled[target] == 0]
            df_minority = df_undersampled[df_undersampled[target] == 1]
            n_samples = len(df_minority) * multiply_factor
            # Upsample minority class
            df_minority_upsampled = resample(df_minority,
                                             replace=True,
                                             n_samples=n_samples,
                                             random_state=2)

            # Combine majority values with upsampled minority df
            df_upsampled = pd.concat([df_majority, df_minority_upsampled])

            # Display new class counts
            print("\nTarget value counts after upsampling: \n", df_upsampled[target].value_counts())

            self.log_file = self.loggerObj.write_log(self.log_file,'Up sampling and down sampling of training data has completed. Exiting the up_and_down_sampling method of dataPreprocessor class.')

            return df_upsampled

        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file,'An error occured in the up_and_down_sampling method of dataPreprocessor class. The exception is ' + str(e))
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting the up_and_down_sampling method of dataPreprocessor class.')
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception


    def remove_columns(self, dataframe, columns):
        """
             Method Name: remove_columns
             Description: Drops the specified columns
             Input: dataframe, columns
             Input Type: dataframe - dataframe, columns - list
             Output: Returns a dataframe without the specified columns.

             Written By: Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """

        dataframe_dropped = dataframe.drop(columns, axis=1)
        self.log_file = self.loggerObj.write_log(self.log_file,
                                                 'Columns ' + columns + ' have been removed succesfully.')

        return dataframe_dropped

    def null_value_check(self, dataframe):
        """
             Method Name: null_value_check
             Description: Checks for null values in the dataset.
             Input: dataframe
             Input Type: dataframe - dataframe
             Output: Null Value dictionary containing the columns in which null values are present and its value, True/False

             Written By:Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """

        self.log_file = self.loggerObj.write_log(self.log_file,
                                                 'Entered null_value_check method of dataPreprocessor class.')
        self.log_file = self.loggerObj.write_log(self.log_file, 'Null value check has started.')

        try:
            null_value_dict = dict()

            for column, value in dataframe.isnull().sum().items():
                if value != 0:
                    null_value_dict[column] = value

            if len(null_value_dict) > 0:
                self.log_file = self.loggerObj.write_log(self.log_file,
                                                         'Null values been checked. There are null values in the data.')
                self.log_file = self.loggerObj.write_log(self.log_file,
                                                         'Exiting the null_value_check method of the dataPreprocessor class.')
                return null_value_dict, True
            else:
                self.log_file = self.loggerObj.write_log(self.log_file,
                                                         'Null values been checked. There are no null values in the data.')
                self.log_file = self.loggerObj.write_log(self.log_file,
                                                         'Exiting the null_value_check method of the dataPreprocessor class.')
                return null_value_dict, False

        except Exception as e:
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'An Exception has occured in the null_value_check method of dataPreprocessor class. The Exception is ' + str(
                                                         e))
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Exting the null_value_check method of the dataProcessor class.')
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception

    def separate_label_feature(self, dataframe, label_column_name):
        """
             Method Name: separate_label_feature
             Description: Separates the input dataframe into two dataframe. One containing the only the specified column.
             Input: dataframe, label_column_name
             Input Type: dataframe - dataframe, label_column_name - string
             Output: Returns two dataframes X,Y

             Written By: Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """

        try:
            self.log_file = self.loggerObj.write_log(self.log_file, 'Seperating labels has started.')
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Entered seperate_label_feature of the dataPreprocessor class.')

            X = dataframe.drop(labels=label_column_name, axis=1)
            Y = dataframe[label_column_name]

            self.log_file = self.loggerObj.write_log(self.log_file, 'Data has been seperated succesfully.')
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Exiting the seperate_label_feature method of the dataPreprocessor class.')

            return X, Y
        except Exception as e:
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'An exception occured in seperate_label_feature method of the dataPreprocessor class. The Exception is ' + str(
                                                         e))
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Exiting the seperate_label_feature method of the dataPreprocessor class.')
            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception()

    def preprocess_prediction_data(self, dataframe):
        """
             Method Name: preprocess_prediction_data
             Description: Preprocesses the prediction data.
             Input: dataframe
             Input Type: dataframe - dataframe
             Output: Returns dataframe

             Written By: Vaishnavi Ambati
             Version: 1.0
             Revisions: None
        """

        try:

            print("Inside preprocess_prediction_data")
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Entered preprocess_prediction_data of dataProcessor class')
            self.log_file = self.loggerObj.write_log(self.log_file, 'Data preprocessing has been initiated.')

            dataframe = self.set_new_headers(dataframe, False)
            print("dataframe columns after set_new_headers")
            print(dataframe.columns)

            if '?' in dataframe.values:
                clms_name_replaced_df = dataframe.replace(to_replace='?', value=np.NaN)
                clms_converted_df = self.convert_columns_type(clms_name_replaced_df, False)
                knn_imputed = KNNImputer(n_neighbors=2).fit_transform(clms_converted_df)
                knn_imputed_df = pd.DataFrame(data=knn_imputed)
                knn_imputed_changed_headers_df = self.set_new_headers(knn_imputed_df, False)
            else:
                clms_converted_df = self.convert_columns_type(dataframe, False)
                knn_imputed = KNNImputer(n_neighbors=2).fit_transform(clms_converted_df)
                knn_imputed_df = pd.DataFrame(data=knn_imputed)
                knn_imputed_changed_headers_df = self.set_new_headers(knn_imputed_df, False)

            self.log_file = self.loggerObj.write_log(self.log_file,'Data Preprocessing has completed. Exiting the preprocess_prediction_data method of dataPreprocessor class.')

            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            return knn_imputed_changed_headers_df

        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file, "Exception occured in preprocess_prediction_data method of dataPreprocessor class. Exception is " + str(e))
            self.log_file = self.loggerObj.write_log(self.log_file,'Exiting the preprocess_prediction_data method of dataPreprocessor class.')

            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception

    def preprocess_single_predict_manual(self, feature_list):
        """
                     Method Name: preprocess_single_predict_manual
                     Description: Preprocesses the prediction data entered manually.
                     Input: feature_list
                     Input Type: list
                     Output: Returns dataframe

                     Written By: Vaishnavi Ambati
                     Version: 1.0
                     Revisions: None
                """

        try:
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Entered preprocess_single_predict_manual of dataProcessor class')
            self.log_file = self.loggerObj.write_log(self.log_file, 'Data preprocessing has been initiated.')

            columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14',
                       'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22', 'X23', 'X24', 'X25', 'X26', 'X27',
                       'X28', 'X29', 'X30', 'X31', 'X32', 'X33', 'X34', 'X35', 'X36', 'X37', 'X38', 'X39', 'X40',
                       'X41', 'X42', 'X43', 'X44', 'X45', 'X46', 'X47', 'X48', 'X49', 'X50', 'X51', 'X52', 'X53',
                       'X54', 'X55', 'X56', 'X57', 'X58', 'X59', 'X60', 'X61', 'X62', 'X63', 'X64']

            feature_dic = dict(zip(columns, feature_list))

            df = pd.DataFrame(feature_dic, index=[0])

            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Data Preprocessing has completed. Exiting the preprocess_single_predict_manual method of dataPreprocessor class.')
            print(df)
            return df

        except Exception as e:

            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     "Exception occured in preprocess_single_predict_manual method of dataPreprocessor class. Exception is " + str(
                                                         e))
            self.log_file = self.loggerObj.write_log(self.log_file,
                                                     'Exiting the preprocess_single_predict_manual method of dataPreprocessor class.')

            self.log_file.to_csv("Logs\\Prediction Logs\\prediction_logs.csv")

            raise Exception

