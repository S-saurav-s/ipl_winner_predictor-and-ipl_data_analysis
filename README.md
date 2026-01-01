#🏏 IPL Match Win Probability Predictor

An end-to-end Machine Learning + Streamlit application that predicts the winning probability of the batting team in an IPL match based on the current match situation.

This project demonstrates how to take an ML model from a notebook and deploy it as an interactive, rule-aware web application.

📌 Project Overview

Cricket match outcomes depend on multiple dynamic factors such as:

Runs left

Balls remaining

Wickets in hand

Current and required run rate

Teams and venue

This project uses a trained machine learning classification model to estimate the probability of winning, while also applying cricket domain rules to handle impossible or completed match states.

🎯 Key Features

📊 Real-time win & loss probability prediction

🧠 Machine Learning–based inference using predict_proba()

🧩 Rule-based logic for impossible states (e.g. 0 balls left)

🖥️ Interactive Streamlit UI

⚡ Fast, lightweight, and data-science focused

🧠 Machine Learning Details

Problem Type: Binary Classification (Win / Loss)

Model Output: Probability of winning

Model Interface: predict_proba()

Preprocessing: Handled inside the trained pipeline (categorical + numerical)

Deployment: Serialized using pickle

⚠️ The ML model is only used for valid match states.
Cricket rules are enforced using deterministic logic before prediction.

🧱 Project Structure
IPL-Win-Predictor/
│
├── app.py                   # Streamlit application
├── match_win_model.pkl      # Trained ML model
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

🖥️ User Inputs

The application takes the following inputs:

Batting Team

Bowling Team

City

Runs Left

Balls Left

Wickets Left

Current Run Rate

Required Run Rate

Target Score

✅ Rule-Based Logic (Important)

To ensure realistic predictions, the following rules are applied before ML inference:

If runs_left <= 0 → Win probability = 100%

If balls_left == 0 and runs_left > 0 → Win probability = 0%

If wickets_left == 0 and runs_left > 0 → Win probability = 0%

ML model is used only when the match state is valid

This mirrors real-world production ML systems where domain constraints are handled outside the model.

🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
streamlit run app.py


The app will open automatically in your browser.

📦 Requirements
streamlit
pandas
scikit-learn

📈 Example Output

🏆 Win Probability: 72.4%

❌ Lose Probability: 27.6%

OR

❌ Match Over: No balls left and runs still required

🏆 Win Probability: 0%

💡 Why This Project Stands Out

✔ Not just a notebook — a deployed ML app
✔ Proper handling of edge cases
✔ Clear separation of ML and business logic
✔ Interview-ready architecture
✔ Practical sports analytics use case

🧠 Interview Explanation (Quick)

I built a machine learning model to predict IPL match win probability and deployed it using Streamlit. I combined ML predictions with rule-based cricket logic to handle impossible match states, ensuring realistic and production-ready outputs.

🔮 Future Improvements

📊 Probability visualization (progress bar / gauge)

🧠 Model explainability (feature impact)

💾 Save prediction history

🌐 Cloud deployment (Streamlit Cloud / Render)

🔐 User login and match tracking

👤 Author

Saurav Kumar
Aspiring Data Scientist | Machine Learning | Python
