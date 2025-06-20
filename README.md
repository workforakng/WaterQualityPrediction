## Week 1
https://colab.research.google.com/github/workforakng/WaterQualityPrediction/blob/main/WaterQualityPrediction.ipynb.txt

# Water Quality Prediction

This project focuses on predicting key water quality parameters using historical data from 2000 to 2021 in Punjab, India.

## Dataset

The dataset `PB_All_2000_2021.csv` contains monthly water quality measurements from multiple locations. It includes features such as:

- NH4
- BSK5
- Suspended solids
- O2, NO3, NO2, SO4, PO4, CL

## How to Run

1. Open the notebook in **Google Colab**.
2. The dataset is automatically downloaded from GitHub using `wget`.
3. Required libraries are installed using `pip`.
4. Run all cells to preprocess data, analyze, and train a basic prediction model using `RandomForestRegressor`.

## Requirements

- Python 3.x
- pandas, numpy, matplotlib, seaborn
- scikit-learn

## Output

The model evaluates performance using **R² Score** and **Mean Squared Error**, giving insights into how well water quality parameters can be predicted.

---

**Author**: [@workforakng](https://github.com/workforakng)
