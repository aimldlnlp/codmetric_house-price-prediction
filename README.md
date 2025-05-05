# House Price Prediction

## Project Description
This project implements a machine learning pipeline to predict house prices based on various features from a housing dataset. The pipeline includes data loading, preprocessing, model training using linear regression, and evaluation of the model's performance. The project also includes exploratory data analysis (EDA) and visualization to better understand the data and model results.

## Installation
To set up the project environment, install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage
Run the main script to execute the full pipeline of loading data, preprocessing, training the model, and evaluating its performance:

```bash
python main.py
```

## Project Structure
- `main.py`: Entry point of the project that orchestrates the pipeline.
- `src/`: Contains modularized source code for different pipeline stages:
  - `data_loader.py`: Loads the housing dataset.
  - `preprocessing.py`: Cleans and preprocesses the data, including feature engineering.
  - `model.py`: Defines and trains the linear regression model.
  - `evaluate.py`: Evaluates the trained model and visualizes results.
- `data/`: Contains the housing dataset CSV file (`housing.csv`).
- `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA).
- `reports/`: Contains generated plots and visualizations from the analysis and evaluation.

## Data
The dataset used is `housing.csv`, which contains various features related to houses and their corresponding median prices. The target variable for prediction is `median_house_value`.

## Preprocessing
The preprocessing step involves:
- Dropping rows with missing values.
- Splitting the dataset into features and target variable.
- Applying one-hot encoding to categorical features.
- Splitting the data into training and testing sets.

## Model
A linear regression model is trained on the preprocessed training data using scikit-learn's `LinearRegression` implementation.

## Evaluation
The model is evaluated on the test set using:
- Mean Squared Error (MSE)
- R² Score

Additionally, a scatter plot visualizes the actual vs predicted house prices to assess model performance visually.

## Additional Resources
- The `notebooks/EDA.ipynb` notebook contains exploratory data analysis and insights.
- The `reports/` folder contains plots and visualizations generated during analysis and evaluation.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Zidan - z.zidan9123@gmail.com
