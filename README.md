# House Price Prediction App (ML + Streamlit)

A machine learning web app that predicts house prices based on user input features.  
Built using Linear Regression and deployed with Streamlit for real-time interaction.

---

## Features

- Predict house price based on input features
- Interactive UI using Streamlit
- Uses real dataset (train.csv)
- Handles categorical features using one-hot encoding
- Automatically aligns input features with trained model

---

## How It Works

1. Dataset is loaded using pandas  
2. Selected features are extracted:
   - HouseStyle
   - OverallQual
   - RoofStyle
   - GrLivArea
   - GarageCars
   - TotalBsmtSF  
3. Categorical features are encoded using `get_dummies`  
4. Data is split into training and testing sets  
5. Linear Regression model is trained  
6. User inputs are collected via Streamlit UI  
7. Input is encoded and aligned with training columns  
8. Model predicts house price  

---

## Input Features

- Overall Quality (slider)
- Ground Living Area (slider)
- Garage Capacity (slider)
- Basement Area (slider)
- Roof Style (dropdown)
- House Style (dropdown)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
