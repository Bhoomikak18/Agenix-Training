from flask import Flask, request, jsonify
import pandas as pd
import joblib

#  Load the improved model, scaler, and RFM data (after capping)
model = joblib.load('kmeans_model_capped.pkl')
scaler = joblib.load('scaler_capped.pkl')
rfm = pd.read_csv('rfm_data_capped.csv', index_col='CustomerID')

#  Segment mapping from your final clustering
segment_map = {
    0: 'Regular Buyers',
    1: 'Inactive',
    2: 'VIPs'
}

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict_segment():
    try:
        customer_id = int(request.args.get('customer_id'))
        
        if customer_id not in rfm.index:
            return jsonify({'error': 'Customer ID not found'}), 404

        # Select customer data
        customer_data = rfm.loc[[customer_id]]

        #  Drop unnecessary columns just in case
        customer_data = customer_data.drop(columns=['Segment', 'Cluster', 'Hierarchical_Cluster'], errors='ignore')


        # Scale and predict
        customer_scaled = scaler.transform(customer_data)
        segment = model.predict(customer_scaled)[0]

        return jsonify({
            'CustomerID': customer_id,
            'Predicted_Segment': int(segment),
            'Segment_Name': segment_map[int(segment)]
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
