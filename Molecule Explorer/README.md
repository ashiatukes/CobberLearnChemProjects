Chapter 6: Molecular Similarity and Molecule Explorer

Project Overview
In Chapter 6, I explored how molecules can be compared using different chemical properties, including molecular weight, polarity, solubility, and flexibility.

Because I did not have access to CobberLearnChem on my computer, I used Python to explore molecular properties and generate similarity matrices.

Molecule Explorer
I created a Python program using RDKit that allows users to enter a molecule's SMILES string and analyze its chemical properties.

The program:
- Converts SMILES strings into molecular structures.
- Generates an image of the molecule.
- Calculates exact molecular weight, hydrogen bond donors, TPSA, LogP, and rotatable bonds.
- Allows users to analyze multiple molecules without restarting the program.
- Displays numerical results rounded to two decimal places for easier reading.
 
- What I Learned
I learned that molecular similarity depends on which chemical properties are being compared. Two molecules can be similar in molecular weight but different in polarity or flexibility.

I also learned how to use RDKit to calculate molecular descriptors, organize Python output, and improve my code using loops and explanatory comments.

Challenges
One challenge was completing the activities without access to CobberLearnChem. I worked around this by using Python and RDKit to explore molecular properties and create my own comparisons.

Chapter 8: Error Analysis and Model Evaluation

Objective
The goal of this chapter was to evaluate how closely
predicted values matched actual values using error
metrics and visualizations.

Methods
Python was used with NumPy, pandas, matplotlib, and
scikit-learn to analyze prediction errors.

Four simulated datasets were created to demonstrate
low scatter, high scatter, positive deviation, and
negative deviation. MAE, MSE, and R² were calculated
for each dataset.

Predicted-vs-actual and residual plots were generated
to examine prediction accuracy and systematic bias.

A separate ErrorMetrics.py script was used to calculate
MAE, MSE, and R² manually using NumPy. The calculations
were then verified using scikit-learn.

Results: Dataset Comparison

| Dataset | MAE | MSE | R² |
|---|---:|---:|---:|
| Low Scatter | 1.2484 | 2.3471 | 0.9967 |
| High Scatter | 9.8111 | 137.8530 | 0.8038 |
| Positive Deviation | 9.8975 | 101.9131 | 0.8549 |
| Negative Deviation | 9.9401 | 102.4389 | 0.8542 |

The low-scatter dataset performed best overall.
The high-scatter dataset showed the largest squared
errors and the lowest R².

The positive- and negative-deviation datasets showed
systematic overprediction and underprediction.

Results: Manual Error Metrics

MAE: 0.8571
MSE: 0.7857
R²: 0.8218

The NumPy calculations matched the scikit-learn results.

Improvements
1. Printed a table displaying actual values, predicted
   values, and residuals.
2. Highlighted the largest prediction errors in red
   on the predicted-vs-actual graph.

Conclusion
This chapter demonstrated that evaluating a model
requires more than looking at its R² value. MAE and
MSE help measure the size of prediction errors, while
residual plots reveal patterns such as systematic bias.

The results showed that a model can follow the overall
trend of the data while consistently overpredicting
or underpredicting actual values.

The four comparison datasets were simulated
because the original CobberResidue CSV files were
not available.
