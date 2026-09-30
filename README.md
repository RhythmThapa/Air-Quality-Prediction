# Air Quality Prediction

Predicts carbon monoxide concentration (**CO(GT)**) from air-quality sensor readings, weather variables and time features, using the [UCI Air Quality dataset](https://archive.ics.uci.edu/dataset/360/air+quality).

## Results

Three regression models were compared; Linear Regression performed best on the held-out test set.

| Metric | Value  |
|--------|--------|
| MAE    | 0.3196 |
| RMSE   | 0.4837 |
| R²     | 0.8706 |

Models compared: Linear Regression, Random Forest, Gradient Boosting. See [`results/metrics.json`](results/metrics.json).

## Preprocessing

- Removed duplicate records
- Replaced invalid `-200` sensor values and handled missing values
- Extracted `Hour`, `Month` and `DayOfWeek` from the timestamp
- Scaled input features with `StandardScaler`

## Input features

`PT08.S1(CO)`, `C6H6(GT)`, `PT08.S2(NMHC)`, `NOx(GT)`, `PT08.S3(NOx)`, `NO2(GT)`, `PT08.S4(NO2)`, `PT08.S5(O3)`, `T`, `RH`, `AH`, `Hour`, `Month`, `DayOfWeek`

## Project structure

```
Air-Quality-Prediction/
├── models/
│   ├── air_quality_model.joblib   # trained Linear Regression
│   ├── scaler.joblib              # fitted StandardScaler
│   └── feature_names.json         # feature order expected by the model
├── notebooks/                     # analysis and training notebooks
├── results/
│   └── metrics.json
├── cli.py                         # interactive prediction prototype
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting started

```bash
git clone https://github.com/RhythmThapa/Air-Quality-Prediction.git
cd Air-Quality-Prediction
pip install -r requirements.txt
python cli.py
```

The CLI asks for each feature in the order above and prints the predicted CO(GT).

> **Note:** predictions depend on the quality and units of the input measurements (same units as the UCI dataset).
> The saved model was trained with scikit-learn 1.8; other versions may show a version warning when loading.
