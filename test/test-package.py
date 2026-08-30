from pathlib import Path
import pandas as pd
from model.predict import make_prediction

BASE_DIR = Path(__file__).resolve().parent

sample_input_data = pd.read_csv(BASE_DIR / "bankchurn_test.csv")

result = make_prediction(input_data=sample_input_data)
print(result)