import requests
import numpy as np
import pandas as pd
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import pickle
from flask import Flask
from flask import request
from flask import jsonify


url = "https://github.com/AndresLDF/ML-Zoomcamp-Midterm-Project/raw/main/DataSet/Concrete_Data_Yeh.csv"

response = requests.get(url)

if response.status_code==200:
  file = StringIO(response.text)
  df = pd.read_csv(file)

#Set all the columns labels to lower case
df.columns = df.columns.str.lower()

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=4)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=4)
df_full_train.shape, df_train.shape, df_val.shape, df_test.shape

y_fulltrain = df_full_train["csmpa"].values
y_train = df_train["csmpa"].values
y_val = df_val["csmpa"].values
y_test = df_test["csmpa"].values

del df_full_train["csmpa"]
del df_train["csmpa"]
del df_val["csmpa"]
del df_test["csmpa"]

X_fulltrain = df_full_train.values
X_train = df_train.values
X_val = df_val.values
X_test = df_test.values

features = df_train.columns.to_list()
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)
dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)

watchlist = [(dtrain, 'train'), (dval, 'val')]

features = df_full_train.columns.to_list()
dfulltrain = xgb.DMatrix(X_fulltrain, label=y_fulltrain, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

model_filename = 'xgb_model.pkl'

with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

y_test_pred = loaded_model.predict(dtest)

error = mean_squared_error(y_test, y_test_pred, squared=False)
print(f"The loaded model mean squared error is {np.round(error,2)}")

app = Flask('csmp')
@app.route('/predict', methods=['POST'])
def predict():
    concrete_mixture = request.get_json()
    X = list(concrete_mixture.values())
    X_reshaped = np.array(X).reshape(1, -1)
    dX = xgb.DMatrix(X_reshaped, feature_names=features)
    y_pred = np.round(loaded_model.predict(dX), 2)

    result = {
        'Compression_Strenght': float(y_pred)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)