# 🏏 IPL Match Win Probability Predictor

An end-to-end **Machine Learning + Streamlit** application that predicts the **winning probability of the batting team in an IPL match** based on the current match situation.

This project demonstrates how to take an ML model from a notebook and deploy it as an **interactive, rule-aware web application**.

---

## 📌 Project Overview

Cricket match outcomes depend on multiple dynamic factors such as:

- Runs left  
- Balls remaining  
- Wickets in hand  
- Current and required run rate  
- Teams and venue  

This project uses a **trained machine learning classification model** to estimate the probability of winning, while also applying **cricket domain rules** to handle impossible or completed match states.

---

## 🎯 Key Features

- 📊 Real-time win & loss probability prediction  
- 🧠 Machine Learning–based inference using `predict_proba()`  
- 🧩 Rule-based logic for impossible states (e.g. 0 balls left)  
- 🖥️ Interactive Streamlit UI  
- ⚡ Fast, lightweight, and data-science focused  

---

## 🧠 Machine Learning Details

- **Problem Type**: Binary Classification (Win / Loss)  
- **Model Output**: Probability of winning  
- **Model Interface**: `predict_proba()`  
- **Preprocessing**: Handled inside the trained pipeline (categorical + numerical)  
- **Deployment**: Serialized using `pickle`  

> ⚠️ The ML model is only used for **valid match states**.  
> Cricket rules are enforced using deterministic logic **before prediction**.

---

## 🧱 Project Structure
User (Browser)
│
▼
Streamlit UI (app.py)
│
▼
Rule-Based Logic
(cricket constraints check)
│
├── Match Decided?
│ ├── Yes → Direct Result (0% / 100%)
│ └── No
▼
ML Model (match_win_model.pkl)
│
▼
predict_proba()
│
▼
Win / Lose Probability
│
▼
Result Displayed to User

## 💡 Why This Project Stands Out

✔ Not just a notebook — a deployed ML app
✔ Proper handling of edge cases
✔ Clear separation of ML and business logic
✔ Interview-ready architecture
✔ Practical sports analytics use case

## 🔮 Future Improvements

📊 Probability visualization (progress bar / gauge)

🧠 Model explainability (feature impact)

💾 Save prediction history

🌐 Cloud deployment (Streamlit Cloud / Render)

🔐 User login and match tracking


# 👤 Author

Saurav Kumar
Aspiring Data Scientist | Machine Learning | Python


