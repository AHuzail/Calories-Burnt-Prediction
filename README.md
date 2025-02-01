# Calories-Burnt-Prediction
This project aims to analyze the correlations between calories burnt, exercise routines, and body types, utilizing machine learning techniques to predict energy expenditure based on various factors.

## Introduction

Understanding how different exercises and body types influence calorie expenditure is crucial for personalized fitness planning. This project leverages machine learning to predict calories burnt based on individual characteristics and exercise parameters.

## Dataset

The dataset used in this project includes information on individuals' physical activities and corresponding calories burnt. Key features include:

- **Age:** Age of the individual
- **Gender:** Male or Female
- **Height:** Height in centimeters
- **Weight:** Weight in kilograms
- **Duration:** Duration of the exercise in minutes
- **Heart Rate:** Average heart rate during the exercise
- **Body Temperature:** Body temperature measured post-exercise

## Features

The project focuses on the following features:

- **Data Preprocessing:** Handling missing values, encoding categorical variables, and scaling numerical features.
- **Exploratory Data Analysis (EDA):** Visualizing data distributions and relationships between variables.
- **Feature Engineering:** Creating new features or modifying existing ones to improve model performance.
- **Model Training:** Implementing regression models to predict calories burnt.
- **Model Evaluation:** Assessing model performance using appropriate metrics.

## Modeling Approach

- **XGBoost Regression:** An advanced boosting algorithm known for its performance and efficiency.

## Results

The performance of each model was evaluated using metrics such as Mean Square Error (MSE) and R-squared (R²). The results indicate that **XGBoost Regression:** provided the most accurate predictions with an MSE of **1.58** and an R² of **0.998**.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AHuzail/Calories-Burnt-Prediction.git
   cd Calories-Burnt-Prediction
2. **Install the required packages:**
     ```bash
     pip install -r requirements.txt
3. **Run**
   ```bash
   streamlit run app.py
