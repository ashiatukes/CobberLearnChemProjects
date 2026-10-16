
AlkaneBoilingPoints This simple code plots the number of car-
bon atoms in the alkane on the x-axis and the bollins points o that alkane on they-axis. It generates a properly labeled graph using Matplotlib.
This is part of the CobberLearChem Machine Learning course through Concordia College.

Alongside my public coding projects, I'm keeping a private ethics portfolio where I reflect on what I'm learning and how it's shaping the kind of scientist I want to become.

Molecule Explorer: This Python program uses RDKit to convert a SMILES string into a molecule and calculate molecular descriptors, including exact molecular weight, hydrogen bond donors, TPSA, LogP, and rotatable bonds. I tested the program using alanine and cysteine and added an invalid SMILES check and an option to analyze multiple molecules. This project helped me understand how molecular structures can be represented as data and how chemical properties can be calculated using Python.
# Chapter 7: Mind the Gaps: Learning to Impute with Insight and Integrity

For Chapter 7, I explored how machine learning can help predict missing values in a chemistry dataset. The goal was to compare different models, evaluate their accuracy, and understand how molecular structure affects predictions.

I completed this project in Python using PyCharm, working with a dataset of 250 alkane molecules.

## Dataset and Preparation

The dataset contained information about each molecule, including carbon count, molecular weight, boiling point, viscosity, thermal conductivity, heat capacity, and number of branches.

Some measurements were missing:

- **Viscosity had 50 missing values
- **Heat capacity had 25 missing values
- **Thermal conductivity had 55 missing values

Instead of removing every molecule with missing information, I explored how machine learning could estimate those values.

I used carbon count and branch number as the main input variables and trained the models using molecules with known measurements.

## Machine Learning Models

I tested four approaches:

1. **Log-Linear Regression:** Uses a mathematical relationship between molecular structure and the property being predicted.
2. **K-Nearest Neighbors (KNN):** Makes predictions based on molecules with similar carbon counts and branching patterns. I tested different numbers of neighbors.
3. **Random Forest:** Uses multiple decision trees to recognize patterns. I compared tree depths of 5 and 15.
4. **Ensemble:** Combines predictions from multiple models to see whether their combined results improve accuracy.

I used five-fold cross-validation to test how well the models predicted known measurements.

Model accuracy was measured using Mean Absolute Error (MAE), where a lower value indicates more accurate predictions.

## Results

**Viscosity:** Log-linear regression performed best, with an MAE of **0.0109**. The Ensemble model was close behind at 0.0116.

**Heat Capacity:** Random Forest with a maximum depth of 15 performed best, with an MAE of **6.9788**. Log-linear regression had much larger errors for this property.

**Thermal Conductivity:** KNN with 10 neighbors was one of the best-performing models, with an MAE of **0.0024**.

These results showed that different chemical properties benefit from different prediction methods.

## Graphs and Bias Analysis

I created prediction-quality graphs to compare actual measurements with predicted values. The red dashed line represented a perfect prediction, making it easier to see how closely each model followed the real data.

I also created bias plots showing relative prediction error against carbon count and branch number.

For viscosity, log-linear regression showed relatively consistent performance across molecular structures.

For heat capacity, Random Forest was generally more accurate for larger molecules, while smaller molecules showed greater variation in errors.

For thermal conductivity, KNN produced relatively small errors across different carbon counts and branching patterns, although some overprediction and underprediction occurred.

None of the examined bias plots showed errors exceeding ±100%.

## What I Learned


This project helped me understand that machine learning models do not perform equally well for every chemical property. A more complicated model is not necessarily more accurate.

I also learned why it is important to evaluate both numerical accuracy and prediction bias. A model may have a low overall error but still struggle with certain types of molecules.

Another important part of the process was making sure predictions were converted back to their original measurement scale after using logarithmic transformations.

Overall, this chapter helped me better understand how to work with incomplete scientific data and evaluate which prediction methods are most appropriate.

## Tools Used

- Python and PyCharm
- pandas and NumPy
- scikit-learn
- Matplotlib

## Running the Project

To reproduce the analysis, open the project in PyCharm and make sure `alkane_dataset.csv` is available to the scripts.

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib
```

Run the three Python files:

- `ImputeViscosity.py`
- `ImputeHeatCapacity.py`
- `ImputeThermalConductivity.py`

Each script evaluates models for its corresponding property. The results appear in the Run window, and the generated graphs help visualize prediction accuracy and bias.

## Conclusion

Chapter 7 demonstrated how machine learning can be used to evaluate methods for estimating missing chemical measurements. By comparing four approaches across three properties, I found that the best-performing model depended on the property being predicted.

The main takeaway was that choosing an imputation method requires more than finding the lowest error. It also involves understanding the data, checking for bias, and making sure the predictions are scientifically reasonable.