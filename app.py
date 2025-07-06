import pandas as pd
import numpy as np
import joblib
import gradio as gr

# Load the model and column structure
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

# Prediction function
def predict_pollutants(year, station_id):
    try:
        input_df = pd.DataFrame({'year': [year], 'id': [station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Align columns with training columns
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        prediction = model.predict(input_encoded)[0]
        result = {p: round(val, 2) for p, val in zip(pollutants, prediction)}
        return result

    except Exception as e:
        return {"Error": str(e)}

# Gradio Interface
inputs = [
    gr.Number(label="Year", value=2022, minimum=2000, maximum=2100),
    gr.Textbox(label="Station ID", placeholder="e.g., 1")
]

outputs = gr.JSON(label="Predicted Pollutant Levels")

app = gr.Interface(
    fn=predict_pollutants,
    inputs=inputs,
    outputs=outputs,
    title="💧 Water Pollutants Predictor",
    description="Predict levels of O₂, NO₃, NO₂, SO₄, PO₄, and Cl⁻ based on year and station ID."
)

if __name__ == "__main__":
    app.launch()