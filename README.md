# Bankruptcy_Prediction

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask)
[![Website myfakewebsitethatshouldnotexist.at.least.i.hope](https://img.shields.io/website-up-down-green-red/http/myfakewebsitethatshouldnotexist.at.least.i.hope.svg)](https://www.google.com/url?q=https%3A%2F%2Fta-restaurant-ratings.el.r.appspot.com)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


#### -- Project Status: Completed

## Project Intro

Bankruptcy prediction is the task of predicting bankruptcy and various measures of financial distress of firms. It is a vast area of finance and accounting research. The importance of the area is due in part to the relevance for creditors and investors in evaluating the likelihood that a firm may go bankrupt. The aim of predicting financial distress is to develop a predictive model that combines various econometric parameters which allow foreseeing the financial condition of a firm. The purpose of the bankruptcy prediction is to assess the financial condition of a company and its future perspectives within the context of long-term operation on the market . It is a vast area of finance and econometrics that combines expert knowledge about the phenomenon and historical data of prosperous and unsuccessful companies. Typically, enterprises are quantified by numerous indicators that describe their business condition that are further used to induce a mathematical model using past observation


To skip the description and get started :) [cilck here!](https://github.com/Vaishnavi-ambati/Bankruptcy_Prediction/blob/master/README.md#getting-started)

### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
* Hyperparameter Tuning
* Flask integration

##### Technologies Used:
Type | Used
--- | --- 
Language | Python 3.7
IDE |	PyCharm
Database	|MySQL
Frontend	| HTML5, CSS3, Bootstrap
Integration	| Flask
Deployment |	Google Cloud Platform


## Project Description

The dataset is about bankruptcy prediction of Polish companies. The data was collected from Emerging Markets Information Service (EMIS]), which is a database containing information on emerging markets around the world. The bankrupt companies were analysed in the period 2000-2012, while the still operating companies were evaluated from 2007 to 2013.

Based on the collected data five classification cases were distinguished, that depends on the forecasting period:
1. 1st year: The data contains financial rates from 1st year of the forecasting period and corresponding class label that indicates bankruptcy status after 5 years. The data contains 7027 instances (financial statements), 271 represents bankrupted companies, 6756 firms that did not bankrupt in the forecasting period.
2. 2nd year: The data contains financial rates from 2nd year of the forecasting period and corresponding class label that indicates bankruptcy status after 4 years. The data contains 10173 instances (financial statements), 400 represents bankrupted companies, 9773 firms that did not bankrupt in the forecasting period.
3. 3rd year: The data contains financial rates from 3rd year of the forecasting period and corresponding class label that indicates bankruptcy status after 3 years. The data contains 10503 instances (financial statements), 495 represents bankrupted companies, 10008 firms that did not bankrupt in the forecasting period.
4. 4th year: The data contains financial rates from 4th year of the forecasting period and corresponding class label that indicates bankruptcy status after 2 years. The data contains 9792 instances (financial statements), 515 represents bankrupted companies, 9277 firms that did not bankrupt in the forecasting period.
5. 5th year: The data contains financial rates from 5th year of the forecasting period and corresponding class label that indicates bankruptcy status after 1 years.
The data contains 5910 instances (financial statements), 410 represents bankrupted companies, 5500 firms that did not bankrupt in the forecasting period.

* All the dataset have 64 independent and 1 dependent features.

The aim of predicting financial distress is to develop a predictive model that combines various econometric parameters which allow foreseeing the financial condition of a firm. In this project we document our observations as we explore, build, and compare, some of the widely used classification models:

* Random Forests
* Extreme Gradient Boosting
* Balanced Bagging

I have chosen the Polish companies’ bankruptcy data set where synthetic features were used to reflect higher-order statistics.
 

The Process flow of the project:
![flow](https://user-images.githubusercontent.com/50202237/84906666-e088c500-b0cf-11ea-99eb-8ae5e366254e.png)


## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](https://github.com/Vaishnavi-ambati/Bankruptcy_Prediction/tree/master/Data)
3. Data processing/transformation scripts are being kept [here](https://github.com/Vaishnavi-ambati/Bankruptcy_Prediction/tree/master/Modules).
4. After cloning the repo, open an editor of your choice and create a new environment.(for help see this [tutorial](https://realpython.com/lessons/creating-virtual-environment/))
5. Install the required modules in the environment using the requirements.txt file. (for help see this [tutorial](https://note.nkmk.me/en/python-pip-install-requirements/))
6. Open the script.sql file in Mysql and run the script to create database and tables
7. Open DbInsertion.py file and change the connection to your values (line 36)
   Ex: connection = mysql.connector.connect(host="127.0.0.1", user="your username", password="your password",
                                                 database="databaseName")
8. After installing the required modules. You are all set! Run the 'main.py' file and the app will be hosted in your local server.

Note: If you have any issues with project or with the setup. You can always contact me or raise an issue. :)
