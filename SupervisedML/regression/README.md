# House Price Prediction Model

## Overview
This project focuses on predicting house prices using machine learning. It involves exploring and implementing various regression models and evaluating their performance on a house price dataset.

## Dataset
[Specify the dataset you used, e.g., Melbourne Housing Dataset from Kaggle](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot)

## Models Implemented
* Linear Regression
* Ridge Regression
* Lasso Regression
* Support Vector Regression
* Random Forest Regressor
* Gradient Boosting Regressor

## Key Libraries
* scikit-learn
* pandas
* numpy
* pickle

## Performance Evaluation
### Models without Optimized Parameters:
| Model                      | RMSE                    | R-squared                     |
|--------------------------- |-------------------------|-------------------------------|
| Linear Regression          | $599681907430005120.00  | -873467188889441206796288.0000|
| Ridge Regression           | $364853.64              | 0.6767                        |
| Lasso Regression           | $364731.20              | 0.6769                        |
| Support Vector Regression  | $666261.94              | -0.0782                       |
| Random Forest Regressor    | $285085.78              | 0.8026                        |
| Gradient Boosting Regressor| $305397.92              | 0.7735                        |

### Models with Specified Hyperparameters:

| Model                      | RMSE                  | R-squared                      |
|----------------------------|-----------------------|--------------------------------|
| Linear Regression          | $599681907430005120.00| -873467188889441206796288.0000 |
| Ridge Regression           | $369658.02  | 0.6681  |                                |
| Lasso Regression           | $364716.64  | 0.6769  |                                |
| Support Vector Regression  | $547372.91  | 0.2723  |                                |
| Random Forest Regressor    | $284010.78  | 0.8041  |                                |
| Gradient Boosting Regressor| $305397.92  | 0.7735  |                                |

## Key Findings
Significant performance differences were observed across models, with Linear Regression struggling notably. While Random Forest Regressor consistently achieved the highest R-squared, reaching 0.8041 after applying specified hyperparameters, Support Vector Regression showed the most substantial improvement upon hyperparameter adjustment. Other models like Ridge and Lasso remained relatively stable. Random Forest's superior performance highlights its effectiveness for this prediction task.

## Next Steps
* Develop a user interface using Gradio for interactive predictions.
* Explore deployment options using Streamlit or AWS.
* Further optimize model hyperparameters.

## Author
Marcel Ambo Ndowah
