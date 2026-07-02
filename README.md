# AI-Based Network Intrusion Detection System (IDS)

An AI-based Intrusion Detection System developed as a final-year Computer Engineering project. This project analyzes live network traffic using machine learning techniques to identify malicious activities and classify network packets as normal or malicious.

---

# Project Overview

With the increasing number of cyber attacks, traditional rule-based security systems often fail to detect unknown threats. This project uses machine learning algorithms to analyze network traffic and detect suspicious activities in real time.

The system captures network packets, extracts important features, preprocesses the data, and predicts whether the traffic is normal or malicious.

---

# Objectives

- Detect malicious network traffic
- Improve network security using Machine Learning
- Analyze live network packets
- Classify packets into Normal or Attack
- Reduce manual monitoring

---

# Features

- Live network traffic monitoring
- Machine Learning based detection
- Data preprocessing
- Real-time prediction
- Packet classification
- Performance evaluation

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning |
| Matplotlib | Data Visualization |
| Joblib | Model Saving |
| Jupyter Notebook | Model Development |

---

# Project Architecture

```
Network Traffic
        │
        ▼
Packet Capture
        │
        ▼
Feature Extraction
        │
        ▼
Data Preprocessing
        │
        ▼
Machine Learning Model
        │
        ▼
Prediction
        │
        ▼
Normal / Malicious
```

---

# Workflow

### Step 1

Capture live network traffic.

### Step 2

Extract useful packet features.

### Step 3

Clean and preprocess the data.

### Step 4

Load the trained Machine Learning model.

### Step 5

Predict whether incoming traffic is malicious.

### Step 6

Display the prediction result.

---

# Dataset

The project uses a network traffic dataset containing normal and attack records.

Example features include:

- Source IP
- Destination IP
- Protocol
- Packet Length
- Flow Duration
- Bytes Sent
- Bytes Received

*(Replace this section with your actual dataset name if applicable.)*

---

# Machine Learning Model

The model was trained using network traffic data and evaluated using standard machine learning metrics.

Performance was measured using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# Project Structure

```
AI-Based-Network-Intrusion-Detection-System
│
├── dataset/
├── model/
├── notebooks/
├── screenshots/
├── src/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/AI-Based-Network-Intrusion-Detection-System.git
```

Go to the project folder.

```bash
cd AI-Based-Network-Intrusion-Detection-System
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the project.

```bash
python app.py
```

(Change this command if your main file has a different name.)

---

# Screenshots

## System Architecture
<img width="1536" height="940" alt="ChatGPT Image Jun 28, 2026, 08_4asd4_44 PM" src="https://github.com/user-attachments/assets/d4c02d72-357f-4ce2-bacf-4136f9d9b20c" />


---

## Output
<img width="596" height="418" alt="image" src="https://github.com/user-attachments/assets/c4e5a126-4663-4bfa-936e-9e5f322a357f" />


---


# Results

The system successfully classified live network traffic into normal and malicious categories.

The project demonstrates how machine learning can assist in identifying suspicious network activities and improve intrusion detection.

---

# Challenges Faced

- Processing live network packets
- Handling different traffic types
- Feature extraction
- Reducing false positives
- Evaluating model performance

---

# Future Improvements

- Deep Learning models
- Real-time dashboard
- Cloud deployment
- Larger datasets
- Explainable AI
- Better attack detection

---

# My Contribution

This project was completed as part of my final-year Computer Engineering curriculum.

My contributions included:

- Implementing and testing the project on a live Wi-Fi network
- Understanding and validating the machine learning workflow
- Running experiments on network traffic
- Evaluating prediction results
- Documenting the implementation and findings

---

# Skills Demonstrated

- Python
- Machine Learning
- Data Analysis
- Data Preprocessing
- Network Traffic Analysis
- Scikit-learn
- Pandas
- NumPy

---

