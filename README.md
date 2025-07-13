# Network Security Project for Phishing Data
This project focuses on detecting phishing websites using machine learning pipelines. The workflow includes data ingestion from a MongoDB Atlas database, transformation, model training, evaluation, and deployment using Docker and AWS services.

## Dataset Overview
The dataset consists of numerical features extracted from URLs to identify phishing sites. Below are some of the columns:

-having_IP_Address

-URL_Length

-Shortining_Service

-having_At_Symbol

-Prefix_Suffix

-SSLfinal_State

-web_traffic

-Statistical_report

-Result (Target: 1 for phishing, -1 for legitimate)

All features are numerical, making the dataset ready for traditional ML models like Random Forest, XGBoost, etc.

## Frontend (HTML + Jinja2)
The trained model results are rendered dynamically using Jinja2 templates.

A simple web dashboard displays prediction results, and model status directly on Chrome


## Project Architecture
### ML Pipeline Overview

 #### Data Ingestion
-Connects to MongoDB Atlas, a cloud-hosted NoSQL database.

-Extracts raw phishing URL data and saves it as .csv or .npy files.

-Output: data_ingestion_artifact.pkl (contains file paths for downstream use).

 #### Data Validation
-Ensures schema integrity (e.g., number of columns, data types).

-Checks for null values or inconsistent entries.

-Output: data_validation_artifact.pkl

 #### Data Transformation
Applies preprocessing:

-Feature scaling (e.g., StandardScaler)

-Missing value imputation (e.g., KNN Imputer)

-Saves the preprocessing pipeline as preprocessing.pkl

-Output: Transformed arrays train.npy, test.npy, and data_transformation_artifact.pkl

 #### Model Training
-Loads transformed data and initializes training.

-Uses a Model Factory to test multiple algorithms (e.g., Random Forest, XGBoost).

-Compares against a defined baseline (expected accuracy).

-Saves the best-performing model as model.pkl

-Output: model_trainer_artifact.pkl

 #### Model Evaluation
-Evaluates the newly trained model against the previously saved one (if any).

-Compares metrics such as Accuracy, Precision, Recall, and F1-score.

-Only if the new model performs better, it's marked as accepted.

-Output: model_evaluation_artifact.pkl with is_model_accepted = True/False

 #### Model Pusher
-Pushes accepted models (model.pkl, preprocessing.pkl) to a cloud storage or registry.

-Compatible with AWS S3, EC2, or Azure Blob Storage.

-Output: model_pusher_artifact.pkl

### Model Training Flow

-Input: train.npy, test.npy from transformation step

-Model Factory selects best model based on accuracy threshold

-Serialized model saved as model.pkl

## Deployment Architecture

-Containerization: Docker used to containerize the application

-ECR: Docker image pushed to AWS Elastic Container Registry

-EC2: Image pulled and deployed on EC2

-CI/CD: GitHub Actions pipeline handles automatic testing, building, and deployment

## Tech Stack
| Category       | Tools/Tech                               |
|----------------|-------------------------------------------|
| Language       | Python                                    |
| Data Storage   | MongoDB (Atlas)                           |
| ML Libraries   | scikit-learn, pandas, NumPy               |
|Web Rendering   |	HTML, Jinja2 Template Engine             |
| CI/CD          | GitHub Actions, Docker                    |
| Deployment     | AWS EC2, AWS ECR, App Runner              |
| Visualization  | Matplotlib, Seaborn                       |

## Model Artifacts
-model.pkl: Trained ML model

-preprocessing.pkl: Scaler/Encoder pipeline

-metrics.json: Evaluation scores

-All artifacts are pushed to a cloud bucket after successful evaluation.
