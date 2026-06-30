# ML Classifier Comparison

Trains and compares three classifiers on the Titanic survival dataset: Logistic Regression, Decision Tree, and Random Forest.

## What it does

1. Loads the Titanic dataset directly from a public GitHub CSV.
2. Fills missing `Age` values with the median, builds `FamilySize` and `IsAlone` features, and encodes `Sex` numerically.
3. Splits data 80/20 into train and test sets.
4. Trains all three models on `Pclass`, `Sex`, `Age`, `Fare`, `FamilySize`, `IsAlone`, predicting `Survived`.
5. Reports accuracy, F1 score, and confusion matrix for each model.
6. Prints a final comparison table.

## Results

| Model | Accuracy | F1 Score |
|---|---|---|
| Logistic Regression | 0.7989 | 0.7465 |
| Decision Tree | 0.7654 | 0.7237 |
| Random Forest | 0.7933 | 0.7483 |

Logistic Regression and Random Forest perform similarly and both outperform the Decision Tree on this split.

## Files

- `code.ipynb` — the original notebook, unmodified.
- `code.html` — static HTML export of the executed notebook (generated via `jupyter nbconvert --to html code.ipynb`), used for the live demo page.

## Stack

Python, Pandas, scikit-learn (`LogisticRegression`, `DecisionTreeClassifier`, `RandomForestClassifier`).

## Notes

This notebook pulls a fixed dataset and takes no dynamic input, so the live demo page embeds a static export rather than re-executing on every load.
