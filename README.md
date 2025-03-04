🚀 ML Model Deployment on AWS EC2 with Streamlit

This repository contains a KNeighborsRegressor ML model for predicting electricity bills, deployed on AWS EC2 using Streamlit.

📂 Project Structure

📦 ML-Deployment-on-EC2
├── app.py       # Streamlit app
├── model.pkl    # Trained ML model
├── requirements.txt  # Dependencies
├── README.md    # Documentation

🛠️ Setup & Deployment

1️⃣ Clone Repository


cd aws-ml-deployment

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Locally

streamlit run app.py

4️⃣ Deploy on AWS EC2

Launch an Ubuntu EC2 Instance.

Allow port 8501 in Security Groups.

Connect via SSH:

ssh -i "your-key.pem" ubuntu@your-ec2-ip

Transfer model:

scp -i "your-key.pem" model.pkl ubuntu@your-ec2-ip:/home/ubuntu/

Install dependencies:

sudo apt update && sudo apt install python3-pip -y
pip3 install streamlit pandas numpy scikit-learn

Run Streamlit:

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

