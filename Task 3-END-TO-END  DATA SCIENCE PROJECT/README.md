**TASK 3: END-TO-END DATA SCIENCE PROJECT**

**House Price Prediction using Machine Learning and Flask**

**OBJECTIVE**

To develop a complete data science project from data collection and preprocessing to model deployment using Flask.

**DATASET**

California Housing Dataset from Scikit-Learn.

* Total Samples: 20,640
* Features: 8
* Target Variable: House Price

**TECHNOLOGIES USED**

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Flask
* Joblib

**WORKFLOW**

**1. Data Collection**

* Loaded California Housing Dataset using Scikit-Learn.

**2. Data Exploration**

* Examined dataset structure and features.
* Performed basic analysis.

**3. Data Preprocessing**

* Split dataset into training and testing sets.
* Applied feature scaling using StandardScaler.

**4. Model Training**

* Trained a Linear Regression model.

**5. Model Evaluation**

* Generated predictions on test data.
* Calculated evaluation metrics.

**6. Visualization**

* Created prediction graph comparing actual and predicted values.

**7. Model Saving**

* Saved trained model using Joblib.
* Generated file: house_price_model.pkl

**8. Model Deployment using Flask**

* Developed a Flask web application.
* Users can enter housing features and receive predicted house prices.

**MODEL PERFORMANCE**

* Mean Squared Error (MSE): Generated during execution
* R² Score: Generated during execution

**OUTPUT FILES**

* house_price_model.pkl
* prediction_graph.png
* app.py
* templates/index.html

**HOW TO RUN**

Install Dependencies:

pip install pandas numpy matplotlib scikit-learn flask joblib

Train Model:

python house_price_prediction.py

Run Flask Application:

python app.py

Open Browser:

http://127.0.0.1:5000

**RESULT**

The machine learning model successfully predicts house prices using housing features. The trained model was deployed using Flask, allowing users to interact with the model through a web interface.

**AUTHOR**

Bonthala Supriya Sindhu
