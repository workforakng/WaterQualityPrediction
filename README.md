# 💧 Water Quality Prediction

This AI-powered project predicts six major **water pollutants** using historical station-based monitoring data and the year. The goal is to support environmental analysis and forecasting using machine learning techniques.

---

## 🚀 Run the App

### ▶️ In Google Colab  
Click below to launch the prediction app:

👉 **[Run on Colab](https://colab.research.google.com/github/workforakng/WaterQualityPrediction/blob/main/WaterQualityPred_Week3_.ipynb)**

## By: AKSHAR NATH GORAIN 
Registration ID: 
STU6829b3f24d2691747563506 
AICTE Internship ID: 
INTERNSHIP_1746416864681834e0e35d8
# Water Quality Prediction

A reproducible machine-learning project that predicts major water pollutant concentrations (O₂, NO₃, NO₂, SO₄, PO₄, Cl⁻) for monitoring stations using historical data (2000–2021).

## Quick Links

- **Notebook (analysis & training):** `WaterQualityPred_Week3_.ipynb`
- **Prediction app:** `app.py` (Gradio interface)
- **Primary dataset:** `PB_All_2000_2021.csv`

---

## Project Summary

This repository demonstrates the full pipeline from data preparation and exploratory analysis to model training and a lightweight web interface for inference. The model is a multi-output regressor trained to predict pollutant levels from a small set of features (year and station id). The project is intended for educational and exploratory use in environmental data science.

---

**Dataset**: `PB_All_2000_2021.csv` — station-based monitoring records spanning 2000–2021.

**Targets (predicted pollutants):** O₂ (dissolved oxygen), NO₃, NO₂, SO₄, PO₄, Cl⁻

**Model files:** `pollution_model.pkl`, `model_columns.pkl`

---

**File Structure (important files):**

- `app.py`: Gradio app to run predictions locally or in Colab.
- `PB_All_2000_2021.csv`: Main dataset used for training and EDA.
- `WaterQualityPred_Week2.ipynb`, `WaterQualityPred_Week3_.ipynb`: Notebooks with EDA and model training.
- `model_columns.pkl`: Column order used for model input alignment.
- `pollution_model.pkl`: Trained model (not tracked in repo? check .gitignore or storage).
- `requirements.txt`: Python dependencies.
- `images/`: Supporting visualizations and screenshots.

---

## Setup

1. Create a Python environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. If you have the model artifacts (`pollution_model.pkl`, `model_columns.pkl`) in the project root, run the Gradio app:

```powershell
python app.py
```

The Gradio interface will open locally and provide a simple JSON output of predicted pollutant concentrations.

---

## Usage (examples)

- To run predictions locally using the included interface: `python app.py` and open the provided local URL.
- To reproduce training and analysis, open the notebooks in Jupyter/Colab: `WaterQualityPred_Week3_.ipynb`.

---

## Notes & Recommendations

- Ensure `pollution_model.pkl` and `model_columns.pkl` are present at the project root before running `app.py`.
- If you intend to re-train the model, follow the steps in the notebooks and export model artifacts using `joblib`.
- Consider versioning model artifacts (DVC, cloud storage) for reproducibility.

---

## Author

AKSHAR NATH GORAIN

Contact / Identifier:

- Registration ID: `STU6829b3f24d2691747563506`
- AICTE Internship ID: `INTERNSHIP_1746416864681834e0e35d8`

---

## License

This repository does not include an explicit license. Add a `LICENSE` file if you intend to allow reuse.

---

