from flask import Flask, jsonify, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# df = pd.read_csv('Clean_Data.csv')

loaded_model = joblib.load('random_forest_model5.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()

        waktu = int(data['waktu'])
        kendaraan_terlibat = int(data['jumlahKendaraanTerlibat'])
        klaim = int(data['klaimDiajukan'])
        pekerjaan = data['pekerjaan']
        tipe_kecelakaan = data['tipeKecelakaan']
        tipe_kerusakan = data['tipeKerusakan']
        jenis_kerusakan = data['tingkatKeparahan']
        otoritas_dihubungi = data['otoritasDihubungi']
        umur = int(data['umur'])
        lama_aa = int(data['lamaAnggotaAsuransi'])
        kategori_premi = data['kategoriPremi']
        saksi = data['jumlahSaksi']
        df=pd.DataFrame()
        df['incident_hour_of_the_day'] = [waktu]
        df['number_of_vehicles_involved'] = [kendaraan_terlibat]
        df['witnesses'] = [saksi]
        df['total_claim_amount'] = [klaim]

        df['insured_occupation_adm-clerical'] = [1 if pekerjaan == 'Pekerjaan1' else 0]
        df['insured_occupation_armed-forces'] = [1 if pekerjaan == 'Pekerjaan2' else 0]
        df['insured_occupation_craft-repair'] = [1 if pekerjaan == 'Pekerjaan3' else 0]
        df['insured_occupation_exec-managerial'] = [1 if pekerjaan == 'Pekerjaan4' else 0]
        df['insured_occupation_farming-fishing'] = [1 if pekerjaan == 'Pekerjaan5' else 0]
        df['insured_occupation_handlers-cleaners'] = [1 if pekerjaan == 'Pekerjaan6' else 0]
        df['insured_occupation_machine-op-inspct'] = [1 if pekerjaan == 'Pekerjaan7' else 0]
        df['insured_occupation_other-service'] = [1 if pekerjaan == 'Pekerjaan8' else 0]
        df['insured_occupation_priv-house-serv'] = [1 if pekerjaan == 'Pekerjaan9' else 0]
        df['insured_occupation_prof-specialty'] = [1 if pekerjaan == 'Pekerjaan10' else 0]
        df['insured_occupation_protective-serv'] = [1 if pekerjaan == 'Pekerjaan11' else 0]
        df['insured_occupation_sales'] = [1 if pekerjaan == 'Pekerjaan12' else 0]
        df['insured_occupation_tech-support'] = [1 if pekerjaan == 'Pekerjaan13' else 0]
        df['insured_occupation_transport-moving'] = [1 if pekerjaan == 'Pekerjaan14' else 0]

        df['incident_type_Multi-vehicle Collision'] = [1 if tipe_kecelakaan == 'tipeKecelakaan1' else 0]
        df['incident_type_Parked Car'] = [1 if tipe_kecelakaan == 'tipeKecelakaan2' else 0]
        df['incident_type_Single Vehicle Collision'] = [1 if tipe_kecelakaan == 'tipeKecelakaan3' else 0]
        df['incident_type_Vehicle Theft'] = [1 if tipe_kecelakaan == 'tipeKecelakaan4' else 0]

        df['collision_type_other'] = [1 if tipe_kerusakan == 'tipekerusakan4' else 0]
        df['collision_type_Front Collision'] = [1 if tipe_kerusakan == 'tipekerusakan1' else 0]
        df['collision_type_Rear Collision'] = [1 if tipe_kerusakan == 'tipekerusakan2' else 0]
        df['collision_type_Side Collision'] = [1 if tipe_kerusakan == 'tipekerusakan3' else 0]

        df['incident_severity_Major Damage'] = [1 if jenis_kerusakan == 'jeniskerusakan1' else 0]
        df['incident_severity_Minor Damage'] = [1 if jenis_kerusakan == 'jeniskerusakan2' else 0]
        df['incident_severity_Total Loss'] = [1 if jenis_kerusakan == 'jeniskerusakan3' else 0]
        df['incident_severity_Trivial Damage'] = [1 if jenis_kerusakan == 'jeniskerusakan4' else 0]

        df['authorities_contacted_Ambulance'] = [1 if otoritas_dihubungi == 'otoritasdihubungi3' else 0]
        df['authorities_contacted_Fire'] = [1 if otoritas_dihubungi == 'otoritasdihubungi2' else 0]
        df['authorities_contacted_None'] = [1 if otoritas_dihubungi == 'otoritasdihubungi5' else 0]
        df['authorities_contacted_Other'] = [1 if otoritas_dihubungi == 'otoritasdihubungi4' else 0]
        df['authorities_contacted_Police'] = [1 if otoritas_dihubungi == 'otoritasdihubungi1' else 0]

        df['age_group_15-20'] = [1 if umur in range(15, 21) else 0]
        df['age_group_21-25'] = [1 if umur in range(21, 26) else 0]
        df['age_group_26-30'] = [1 if umur in range(26, 31) else 0]
        df['age_group_31-35'] = [1 if umur in range(31, 36) else 0]
        df['age_group_36-40'] = [1 if umur in range(36, 41) else 0]
        df['age_group_41-45'] = [1 if umur in range(41, 46) else 0]
        df['age_group_46-50'] = [1 if umur in range(46, 51) else 0]
        df['age_group_51-55'] = [1 if umur in range(51, 56) else 0]
        df['age_group_56-60'] = [1 if umur in range(56, 61) else 0]
        df['age_group_61-65'] = [1 if umur in range(61, 66) else 0]

        df['months_as_customer_groups_0-50'] = [1 if lama_aa in range(0, 51) else 0]
        df['months_as_customer_groups_101-150'] = [1 if lama_aa in range(101, 151) else 0]
        df['months_as_customer_groups_151-200'] = [1 if lama_aa in range(151, 201) else 0]
        df['months_as_customer_groups_201-250'] = [1 if lama_aa in range(201, 251) else 0]
        df['months_as_customer_groups_251-300'] = [1 if lama_aa in range(251, 301) else 0]
        df['months_as_customer_groups_301-350'] = [1 if lama_aa in range(301, 351) else 0]
        df['months_as_customer_groups_351-400'] = [1 if lama_aa in range(351, 401) else 0]
        df['months_as_customer_groups_401-450'] = [1 if lama_aa in range(401, 451) else 0]
        df['months_as_customer_groups_451-500'] = [1 if lama_aa in range(451, 501) else 0]
        df['months_as_customer_groups_51-100'] = [1 if lama_aa in range(51, 101) else 0]

        df['policy_annual_premium_groups_high'] = [1 if kategori_premi == 'kategoripremi2' else 0]
        df['policy_annual_premium_groups_low'] = [1 if kategori_premi == 'kategoripremi4' else 0]
        df['policy_annual_premium_groups_medium'] = [1 if kategori_premi == 'kategoripremi3' else 0]
        df['policy_annual_premium_groups_very high'] = [1 if kategori_premi == 'kategoripremi1' else 0]
        df['policy_annual_premium_groups_very low'] = [1 if kategori_premi == 'kategoripremi5' else 0]


        # prediction = loaded_model.predict(df)
        # print(prediction)
        # result = {'prediction': prediction[0]}
        prediction = loaded_model.predict(df)
        probability = loaded_model.predict_proba(df)[:, 1]
        result = {'prediksi': int(prediction[0]), 'persentase': float(probability[0])}

        # result = {'prediction': int(prediction[0])}
        if result['prediksi'] == 1:
            result['pesan'] = 'Kemungkinan Terjadi Kecurangan'
        else:
            result['pesan'] = 'Tidak Terjadi Kecurangan'
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
