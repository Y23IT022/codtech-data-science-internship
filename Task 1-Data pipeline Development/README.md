**TASK 1: DATA PIPELINE DEVELOPMENT**

Customer Churn Data Pipeline using Scikit-learn

**OBJECTIVE**

This project focuses on building an automated data preprocessing pipeline for customer churn data using Pandas and Scikit-learn.

The pipeline prepares raw data into a clean and machine learning-ready format.

**WHY THIS PROJECT?**

Real-world data is often incomplete and inconsistent, making it unsuitable for machine learning models.

This project addresses that challenge by creating an automated and reusable preprocessing workflow.

**WORKFLOW**

Raw Data
↓
Data Cleaning
↓
Feature Transformation
↓
Pipeline Creation
↓
Processed Data

**IMPLEMENTATION STEPS**

**1. Data Loading**

* Loaded customer churn dataset using Pandas.
* Inspected dataset structure and columns.

**2. Data Cleaning**

* Removed unnecessary column (customerID).
* Converted TotalCharges into numeric format.
* Handled missing values.

**3. Feature Engineering**

* Separated features and target variable.
* Converted Churn into binary values (0/1).

**4. Data Transformation**

* Applied StandardScaler for numerical features.
* Applied OneHotEncoder for categorical features.

**5. Pipeline Creation**

* Built preprocessing pipelines using Scikit-learn.
* Combined transformations using ColumnTransformer.
* Automated preprocessing workflow.

**6. Pipeline Execution**

* Split dataset into training and testing data.
* Applied preprocessing pipeline.
* Generated transformed dataset.

**7. Saving Pipeline**

* Saved preprocessing pipeline using Joblib.
* Enabled future reuse and deployment.

**OUTPUT**

* Transformed dataset (`transformed_data.csv`)
* Saved preprocessing pipeline (`churn_pipeline.pkl`)
* Automated preprocessing workflow

**TECHNOLOGIES USED**

* Python
* Pandas
* Scikit-learn
* Joblib

**PROJECT FILES**

* customer_churn.csv
* data_pipeline.py
* transformed_data.csv
* churn_pipeline.pkl

**KEY LEARNING**

* Data preprocessing techniques
* Handling real-world datasets
* Feature transformation
* Pipeline automation using Scikit-learn

**CONCLUSION**

This project demonstrates the importance of preprocessing in data science workflows. A reusable data pipeline improves efficiency, ensures consistency, and prepares data for machine learning applications.

**AUTHOR**

Bonthala Supriya Sindhu
