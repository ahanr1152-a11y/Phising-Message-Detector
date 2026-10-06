# Phising-Message-Detector
# 🛡️ Phishing Message Detector

A beginner-friendly Machine Learning project that detects whether a text message is potentially **phishing** or **safe**.

The project combines **Python, Scikit-learn, TF-IDF, Logistic Regression, and Tkinter** to create a simple desktop-based phishing message detection system.

---

## 📌 Project Overview

Phishing messages are designed to trick users into clicking malicious links or sharing sensitive information such as passwords, OTPs, bank details, or personal information.

This project demonstrates how Machine Learning can be used to classify text messages based on patterns learned from training data.

The user enters a message into the application, and the trained ML model predicts whether the message is:

- ✅ Likely Safe
- ⚠️ Potentially Phishing

---

## 🎯 Features

- 🔍 Detect potentially phishing messages
- 🤖 Machine Learning based classification
- 📊 TF-IDF text feature extraction
- 🧠 Logistic Regression model
- 📈 Model accuracy evaluation
- 🖥️ User-friendly Tkinter GUI
- 📊 Prediction confidence
- ⚠️ Basic safety recommendations
- 🧹 Clear input and results
- ℹ️ Model information window

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Tkinter | Graphical User Interface |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Classification algorithm |

---

## 🧠 How It Works

The project follows a simple Machine Learning pipeline:

```text
                    User Message
                         │
                         ↓
                  Text Processing
                         │
                         ↓
                   TF-IDF Vectorizer
                         │
                         ↓
                Numerical Features
                         │
                         ↓
                Logistic Regression
                         │
                    ┌────┴────┐
                    ↓         ↓
                 Safe      Phishing
                    │         │
                    └────┬────┘
                         ↓
                   Tkinter GUI
                         │
                         ↓
                  Display Result
🔬 Machine Learning Workflow
1. Training Data
The project starts with example messages labelled as:
0 → Safe
1 → Phishing
2. TF-IDF Vectorization
Text cannot be directly understood by most traditional Machine Learning algorithms.
TF-IDF converts text into numerical features.
Text
 ↓
TF-IDF
 ↓
Numerical Features
3. Train/Test Split
The dataset is divided into training and testing data.
Dataset
   │
   ├── Training Data
   │
   └── Testing Data
4. Model Training
A Logistic Regression classifier learns patterns from the training data.
5. Prediction
When the user enters a new message, the trained model predicts its class.
0 → Likely Safe
1 → Potentially Phishing
6. Evaluation
The model's predictions are compared with the actual test labels using accuracy.
🖥️ Application Interface
The application provides:
Message input area
Check Message button
Clear button
About Model button
Prediction result
Confidence score
Safety advice
Example:
┌──────────────────────────────────────┐
│     🛡️ Phishing Message Detector     │
│                                      │
│ Enter a message                     │
│ ┌──────────────────────────────────┐ │
│ │ Your account has been blocked... │ │
│ └──────────────────────────────────┘ │
│                                      │
│       [ CHECK MESSAGE ]              │
│                                      │
│       ⚠️ POTENTIAL PHISHING          │
│                                      │
│       Model Confidence: 94%          │
└──────────────────────────────────────┘
⚙️ Installation
Step 1: Clone the repository
git clone https://github.com/YOUR-USERNAME/phishing-message-detector.git
Step 2: Open the project
cd phishing-message-detector
Step 3: Install dependencies
python -m pip install scikit-learn
Tkinter is normally included with Python on Windows.
Step 4: Run the application
python phishing.py
🧪 Example Messages
Phishing Example
Congratulations! You have won ₹50,000.
Click this link immediately to claim your prize.
Expected result:
⚠️ POTENTIAL PHISHING
Safe Example
Hey, are you coming to college tomorrow?
We have a project meeting.
Expected result:
✅ LIKELY SAFE
📂 Project Structure
phishing-message-detector/
│
├── phishing.py
│
├── README.md
│
└── screenshots/
    └── application.png
📚 Concepts Learned
Through this project, I practiced:
Python programming
Text classification
Natural Language Processing basics
TF-IDF
Logistic Regression
Training and testing datasets
Model prediction
Accuracy evaluation
Tkinter GUI development
Basic cybersecurity concepts
🚀 Future Improvements
The current version is a beginner/learning implementation.
Future versions can include:
[ ] Larger real-world phishing dataset
[ ] Multiple Machine Learning models
[ ] Precision, Recall and F1-score
[ ] Confusion Matrix
[ ] URL/link analysis
[ ] Suspicious keyword highlighting
[ ] Message history
[ ] CSV report generation
[ ] Improved GUI
[ ] Better model evaluation
[ ] Real-time email/message analysis
⚠️ Disclaimer
This project is created for educational purposes.
The current model is trained on a small sample dataset and should not be considered a professional cybersecurity or phishing detection solution.
A message classified as "Safe" should not automatically be trusted.
Always verify suspicious messages independently and avoid sharing sensitive information.
👨‍💻 Author
Ahan Raj
B.Tech CSE (AIML) Student
Interested in:
Artificial Intelligence
Machine Learning
Python
Cybersecurity
AI Engineering
⭐ If you found this project useful
Consider giving the repository a ⭐ on GitHub!