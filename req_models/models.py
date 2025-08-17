import json
import pandas as pd
import pickle
import joblib



with open('req_models/XGB_Fractal_ExportData.pkl','rb') as f:
    model = pickle.load(f)

def load_model():
    scaler = joblib.load('req_models/scaler.pkl')
    return  scaler

scaler = load_model()