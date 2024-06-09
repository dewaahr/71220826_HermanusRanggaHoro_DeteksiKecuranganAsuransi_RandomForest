import pandas as pd
import joblib

# Memuat dataset
df = pd.read_csv('Clean_Data.csv')

# Memuat model yang telah dilatih sebelumnya
loaded_model = joblib.load('random_forest_model0.pkl')

# Mengambil satu data dari dataset (misalnya baris pertama)
data_to_predict = df.iloc[[0]]
print(data_to_predict)

# Menghilangkan kolom 'fraud_reported' dari data yang akan diprediksi
X_pred = data_to_predict.drop(columns=['fraud_reported'])

# Melakukan prediksi pada data yang dimuat
prediction = loaded_model.predict(X_pred)

# Menampilkan hasil prediksi
print("Hasil Prediksi:", prediction)
