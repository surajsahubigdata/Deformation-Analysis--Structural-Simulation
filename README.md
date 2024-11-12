# 🚀 Predicting Material Deformation with Machine Learning! 🛠️

This project aims to predict material deformation based on physical properties and applied load parameters using a machine learning model. We leverage synthetic data generated from simulated physical relationships and deploy a predictive model in a simple web-based application using Streamlit.

## Project Overview

The goal of this project is to create a machine learning model that can predict deformation (e.g., displacement, stress, or strain) in a material or structure under specified conditions. This predictive model can be valuable for engineers and researchers who need quick insights based on input parameters without running time-consuming simulations in software like ANSYS.

### Key Components
- **Synthetic Data Generation**: We simulate deformation data based on parameters such as load, material density, Young's modulus, and object dimensions.
- **Model Training**: A Random Forest regression model is trained on the synthetic dataset.
- **Streamlit App**: A web app for real-time predictions based on user inputs, hosted on a simple UI.


## Setup and Installation

### Prerequisites
- Python 3.7 or above
- Install dependencies listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/surajsahubigdata/Deformation-Analysis--Structural-Simulation.git

2. Install the required packages:
    ```cmd
    pip install -r requirements.txt

3. Train the Model: Train a Random Forest regression model on the synthetic data, save it as deformation_model.pkl, or load the provided model file.

## Project Files:
+ **syntheticdata.ipynb**: Script to generate deformation_simulation_data.csv, a synthetic dataset for model training.
+ **app.py**: Streamlit application script.
+ **deformation_model.pkl**: Pre-trained Random Forest model for deformation prediction.
+ **requirements.txt**: List of required Python packages.
+ **README.md**: Project documentation file.

## Sample Web Interface
![alt text](<interface 1.PNG>)

## License
This project is licensed under the MIT License.
   
