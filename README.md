
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

1. Log-Linear Regression: Uses a mathematical relationship between molecular structure and the property being predicted.
2. K-Nearest Neighbors (KNN): Makes predictions based on molecules with similar carbon counts and branching patterns. I tested different numbers of neighbors.
3. Random Forest: Uses multiple decision trees to recognize patterns. I compared tree depths of 5 and 15.
4. Ensembleij : Combines predictions from multiple models to see whether their combined results improve accuracy.

I used five-fold cross-validation to test how well the models predicted known measurements.

Model accuracy was measured using Mean Absolute Error (MAE), where a lower value indicates more accurate predictions.

## Results

Viscosity: Log-linear regression performed best, with an MAE of **0.0109**. The Ensemble model was close behind at 0.0116.

Heat Capacity: Random Forest with a maximum depth of 15 performed best, with an MAE of **6.9788**. Log-linear regression had much larger errors for this property.

Thermal Conductivity: KNN with 10 neighbors was one of the best-performing models, with an MAE of **0.0024**.

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

## Chapter 12: Evolutionary Algorithms

In Chapter 12, I explored how evolutionary algorithms can solve problems through repeated improvements over time. I recreated the Weasel program in Python using PyCharm to demonstrate how random mutations and selection can gradually produce a target phrase.

The goal was to evolve a randomly generated string into the phrase "METHINKS IT IS LIKE A WEASEL" by selecting changes that improved its fitness score.


### How the Algorithm Works

I created a Python program called Weasel.py that uses random mutations and fitness scores to evolve a string of letters.

The program begins with a randomly generated string and compares it to the target phrase.

For each generation, the algorithm:

1. Creates 100 mutated versions of the current string.
2. Calculates a fitness score based on how many characters match the target phrase.
3. Selects the version with the highest fitness score.
4. Keeps the new version only if its fitness score improves.
5. Repeats until the target phrase is matched or 1,000 generations have been attempted.

A perfect match has a fitness score of 28 out of 28.



### Results and Fitness Graph

The evolutionary algorithm successfully reached the target phrase, "METHINKS IT IS LIKE A WEASEL," with a final fitness score of 28/28.

The program used:
- Population size: 100 offspring per generation
- Mutation probability: 5% per character
- Maximum generations: 1,000
- Final fitness: 28/28

The number of generations needed to reach the target varied between runs because mutations were random.

I created a fitness evolution graph using Matplotlib and saved it as fitness_evolution.png.

The graph showed that fitness increased as the algorithm selected better candidates. Some generations showed no improvement, but the overall fitness continued increasing until the target phrase was reached.

This demonstrates how mutation introduces variation while selection preserves improvements.



### Program Improvements

I made two improvements to the original evolutionary algorithm:

1. **Fitness Tracking:** I added a list called fitness_history to record improvements in the fitness score as the algorithm progressed.

2. **Data Visualization:** I used Matplotlib to create a graph showing how the fitness score increased over time. The graph was saved as fitness_evolution.png.

These additions made it easier to observe and understand how the algorithm gradually improved its results.

### Conclusion

This project helped me understand how evolutionary algorithms use mutation, selection, and fitness scores to solve problems.

By recreating the Weasel program in Python, I demonstrated how repeated selection of better candidates can eventually produce a specific target phrase.

I also gained more experience using Python functions, loops, lists, and Matplotlib to analyze and visualize results.



