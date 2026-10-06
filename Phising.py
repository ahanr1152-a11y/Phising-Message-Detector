# ============================================================
# PHISHING MESSAGE DETECTOR
# Python + Machine Learning + Tkinter
# ============================================================

import tkinter as tk
from tkinter import messagebox

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ============================================================
# 1. TRAINING DATA
# ============================================================

messages = [

    # ---------------- PHISHING ----------------

    "Congratulations you won 50000 rupees click this link to claim your prize",
    "Your bank account has been blocked click here to verify your account",
    "Urgent your account will be suspended verify your information now",
    "You have won a lottery send your bank details to receive money",
    "Click this link immediately to claim your free reward",
    "Your ATM card has been blocked call this number immediately",
    "Congratulations you have won an iPhone click the link to claim",
    "Your account needs verification click the link immediately",
    "You have received a cash reward verify your bank details",
    "Your bank account will be closed today click here to verify",
    "Free recharge available click this link now",
    "You won a prize provide your OTP to receive the money",
    "Your KYC has expired click here to update it immediately",
    "Urgent payment required click this link to avoid account suspension",
    "Congratulations you are selected for a cash prize send your details",
    "Your credit card has been blocked verify your information now",
    "Click here to receive your refund immediately",
    "You have won a lucky draw send your account information",
    "Your mobile number will be disconnected verify your details",
    "Important security alert login through this link immediately",

    # ---------------- SAFE ----------------

    "Hey are you coming to college tomorrow",
    "Please send me the notes from today's class",
    "The project meeting is scheduled for tomorrow",
    "Can you help me with my Python assignment",
    "I will reach college at ten in the morning",
    "Please remember to bring your laptop tomorrow",
    "The teacher uploaded the assignment on the college portal",
    "Our group presentation is next Monday",
    "Can you send me the project file",
    "Let's meet in the library after class",
    "The examination schedule has been announced",
    "I finished my Python project today",
    "Please remind me about the meeting",
    "We have a computer networks lecture tomorrow",
    "Can you explain this programming question",
    "I will call you after reaching home",
    "The college event starts at nine tomorrow",
    "Please share the presentation with me",
    "Our team needs to complete the project this week",
    "I am studying machine learning today"
]


# ============================================================
# 2. LABELS
# ============================================================

labels = [

    # Phishing = 1
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,

    # Safe = 0
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
]


# ============================================================
# 3. CONVERT TEXT INTO NUMBERS
# ============================================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X = vectorizer.fit_transform(messages)

y = labels


# ============================================================
# 4. SPLIT DATA
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# ============================================================
# 5. CREATE MACHINE LEARNING MODEL
# ============================================================

model = LogisticRegression()

model.fit(
    X_train,
    y_train
)


# ============================================================
# 6. CHECK MODEL ACCURACY
# ============================================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Model Accuracy:", round(accuracy * 100, 2), "%")


# ============================================================
# 7. PREDICT MESSAGE
# ============================================================

def check_message():

    message = message_box.get(
        "1.0",
        tk.END
    ).strip()

    if message == "":

        messagebox.showwarning(
            "No Message",
            "Please enter a message first."
        )

        return

    # Convert message into TF-IDF numbers
    message_vector = vectorizer.transform(
        [message]
    )

    # Prediction
    prediction = model.predict(
        message_vector
    )[0]

    # Probability
    probabilities = model.predict_proba(
        message_vector
    )[0]

    confidence = max(probabilities) * 100


    # ========================================================
    # PHISHING RESULT
    # ========================================================

    if prediction == 1:

        result_label.config(
            text="⚠️ POTENTIAL PHISHING",
            fg="#ef4444"
        )

        confidence_label.config(
            text=f"Model Confidence: {confidence:.2f}%"
        )

        advice_label.config(
            text=(
                "Safety Advice:\n"
                "Do not click unknown links, share OTPs, "
                "passwords, or bank information."
            )
        )


    # ========================================================
    # SAFE RESULT
    # ========================================================

    else:

        result_label.config(
            text="✅ LIKELY SAFE",
            fg="#22c55e"
        )

        confidence_label.config(
            text=f"Model Confidence: {confidence:.2f}%"
        )

        advice_label.config(
            text=(
                "The model did not detect strong phishing "
                "patterns in this message.\n"
                "Still avoid sharing sensitive information."
            )
        )


# ============================================================
# 8. CLEAR FUNCTION
# ============================================================

def clear_message():

    message_box.delete(
        "1.0",
        tk.END
    )

    result_label.config(
        text="Result will appear here",
        fg="#cbd5e1"
    )

    confidence_label.config(
        text="Model Confidence: --"
    )

    advice_label.config(
        text="Safety advice will appear here."
    )


# ============================================================
# 9. SHOW MODEL INFORMATION
# ============================================================

def show_model_info():

    messagebox.showinfo(
        "About the Model",
        f"""
Phishing Message Detector

Machine Learning Algorithm:
Logistic Regression

Text Processing:
TF-IDF Vectorization

Training Messages:
{len(messages)}

Test Size:
25%

Model Accuracy:
{accuracy * 100:.2f}%

This is a beginner machine-learning
project for educational purposes.
"""
    )


# ============================================================
# 10. MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Phishing Message Detector"
)

root.geometry(
    "950x650"
)

root.minsize(
    850,
    600
)

root.configure(
    bg="#0f172a"
)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg="#111827"
)

header.pack(
    fill="x"
)


title = tk.Label(
    header,
    text="🛡️ Phishing Message Detector",
    font=("Arial", 25, "bold"),
    bg="#111827",
    fg="white"
)

title.pack(
    pady=(25, 5)
)


subtitle = tk.Label(
    header,
    text="Machine Learning based message security analyzer",
    font=("Arial", 11),
    bg="#111827",
    fg="#94a3b8"
)

subtitle.pack(
    pady=(0, 25)
)


# ============================================================
# MAIN CONTENT
# ============================================================

main_frame = tk.Frame(
    root,
    bg="#0f172a"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=25
)


# ============================================================
# INPUT CARD
# ============================================================

input_card = tk.Frame(
    main_frame,
    bg="#1e293b"
)

input_card.pack(
    fill="x"
)


input_title = tk.Label(
    input_card,
    text="Enter a message",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="white"
)

input_title.pack(
    anchor="w",
    padx=20,
    pady=(20, 10)
)


message_box = tk.Text(
    input_card,
    height=6,
    font=("Arial", 12),
    bg="#0b1220",
    fg="white",
    insertbackground="white",
    relief="flat",
    wrap="word"
)

message_box.pack(
    fill="x",
    padx=20,
    pady=(0, 20)
)


# ============================================================
# BUTTON AREA
# ============================================================

button_frame = tk.Frame(
    input_card,
    bg="#1e293b"
)

button_frame.pack(
    pady=(0, 20
)
)


check_button = tk.Button(
    button_frame,
    text="🔍 CHECK MESSAGE",
    command=check_message,
    font=("Arial", 11, "bold"),
    bg="#7c3aed",
    fg="white",
    activebackground="#6d28d9",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)

check_button.grid(
    row=0,
    column=0,
    padx=5
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_message,
    font=("Arial", 11, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)

clear_button.grid(
    row=0,
    column=1,
    padx=5
)


info_button = tk.Button(
    button_frame,
    text="ABOUT MODEL",
    command=show_model_info,
    font=("Arial", 11, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)

info_button.grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# RESULT CARD
# ============================================================

result_card = tk.Frame(
    main_frame,
    bg="#1e293b"
)

result_card.pack(
    fill="both",
    expand=True,
    pady=(20, 0)
)


result_title = tk.Label(
    result_card,
    text="Analysis Result",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="white"
)

result_title.pack(
    pady=(20, 15)
)


result_label = tk.Label(
    result_card,
    text="Result will appear here",
    font=("Arial", 24, "bold"),
    bg="#1e293b",
    fg="#cbd5e1"
)

result_label.pack(
    pady=10
)


confidence_label = tk.Label(
    result_card,
    text="Model Confidence: --",
    font=("Arial", 12),
    bg="#1e293b",
    fg="#94a3b8"
)

confidence_label.pack(
    pady=5
)


advice_label = tk.Label(
    result_card,
    text="Safety advice will appear here.",
    font=("Arial", 11),
    bg="#1e293b",
    fg="#cbd5e1",
    wraplength=700,
    justify="center"
)

advice_label.pack(
    pady=20
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="Python • Scikit-learn • TF-IDF • Logistic Regression • Tkinter",
    font=("Arial", 9),
    bg="#0f172a",
    fg="#64748b"
)

footer.pack(
    pady=(0, 12)
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()
