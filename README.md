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

## Sample Data
Load	Material Density	Young's Modulus	Length	Width	Height	Deformation
3807.947177	2295.930502	115.4264209	6.759759643	2.902779804	2.028814049	0.000519718
9512.071633	4793.306632	111.7446998	7.987145832	4.046618414	2.419834731	0.001412607
7346.740024	7110.620851	276.5636451	2.579632198	3.824788556	4.287282227	0.000172577
6026.718994	6125.574205	112.38655	6.286253586	0.854109533	1.766021492	0.0001309
1644.58454	6645.928035	117.9874315	5.760285233	0.831322402	4.361283456	4.26E-06
1644.345751	5611.483567	239.8495656	8.34502073	1.414054402	0.531858712	9.37E-06
675.0277605	5845.935952	162.4349606	9.070261899	1.869266159	3.906312342	-2.12E-05
8675.143843	6944.369561	244.1776392	0.220352038	2.101432349	4.252983402	4.52E-05
6051.038616	2747.676062	66.34153939	6.772797199	3.430516362	0.990906499	0.0007902
7109.91852	4425.974746	171.8927984	0.613174411	0.377734118	2.208698009	2.96E-05
303.7864935	2548.466093	58.40340005	5.533700784	0.269896251	0.910948896	2.86E-06
9702.107536	7913.676056	65.66330086	2.947564018	2.020361758	3.562360232	0.00041683

## Sample Web Interface
![alt text](<interface 1.PNG>)

## License
This project is licensed under the MIT License.
   
