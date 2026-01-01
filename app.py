import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("match_win_model.pkl", "rb"))

st.set_page_config(page_title="IPL Match Win Predictor", layout="centered")

st.title("🏏 IPL Match Win Probability Predictor")
st.write("Predict winning probability based on live match situation")

# ---------------- USER INPUTS ---------------- #

batting_team = st.selectbox(
    "Batting Team",
    ["Kolkata Knight Riders", "Sunrisers Hyderabad", "Chennai Super Kings",
     "Mumbai Indians", "Royal Challengers Bangalore", "Delhi Capitals",
     "Rajasthan Royals", "Punjab Kings"]
)

bowling_team = st.selectbox(
    "Bowling Team",
    ["Sunrisers Hyderabad", "Kolkata Knight Riders", "Chennai Super Kings",
     "Mumbai Indians", "Royal Challengers Bangalore", "Delhi Capitals",
     "Rajasthan Royals", "Punjab Kings"]
)

city = st.selectbox(
    "City",
    ["Chennai", "Mumbai", "Kolkata", "Delhi", "Bangalore", "Hyderabad", "Jaipur"]
)

runs_left = st.number_input("Runs Left", min_value=0)
balls_left = st.number_input("Balls Left", min_value=0, max_value=120)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10)
current_run_rate = st.number_input("Current Run Rate", min_value=0.0)
required_run_rate = st.number_input("Required Run Rate", min_value=0.0)
target = st.number_input("Target Score", min_value=0)

# ---------------- PREDICTION ---------------- #

if st.button("Predict Winning Probability"):

    # -------- RULE-BASED OVERRIDES (VERY IMPORTANT) -------- #

    # Case 1: Match already won
    if runs_left <= 0:
        st.success("🏆 Match already WON!")
        st.success("🏆 Win Probability: **100%**")
        st.error("❌ Lose Probability: **0%**")

    # Case 2: Match lost (no balls left)
    elif balls_left == 0 and runs_left > 0:
        st.error("❌ Match Over: No balls left and runs still required.")
        st.success("🏆 Win Probability: **0%**")
        st.error("❌ Lose Probability: **100%**")

    # Case 3: All wickets fallen
    elif wickets_left == 0 and runs_left > 0:
        st.error("❌ All wickets lost. Match LOST.")
        st.success("🏆 Win Probability: **0%**")
        st.error("❌ Lose Probability: **100%**")

    # -------- VALID MATCH STATE → USE ML MODEL -------- #
    else:
        if required_run_rate > 36:
            st.warning("⚠️ Required run rate extremely high")

        input_data = pd.DataFrame(
            [[batting_team, bowling_team, city, runs_left, balls_left,
              wickets_left, current_run_rate, required_run_rate, target]],
            columns=[
                'batting_team', 'bowling_team', 'city', 'runs_left',
                'balls_left', 'wickets_left', 'current_run_rate',
                'required_run_rate', 'target'
            ]
        )

        proba = model.predict_proba(input_data)

        win_prob = round(proba[0][1] * 100, 2)
        lose_prob = round(proba[0][0] * 100, 2)

        st.success(f"🏆 Win Probability: **{win_prob}%**")
        st.error(f"❌ Lose Probability: **{lose_prob}%**")
