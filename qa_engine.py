import pandas as pd

rainfall_df = pd.read_csv("data/rainfall.csv")
crops_df = pd.read_csv("data/crops_clean.csv")

def answer_question(user_input):
    user_input = user_input.lower().strip()

    if "compare" in user_input and "rainfall" in user_input:
        parts = user_input.replace("compare rainfall in", "").split("and")
        if len(parts) == 2:
            s1, s2 = parts[0].strip().title(), parts[1].strip().title()
            if s1 in rainfall_df["state"].values and s2 in rainfall_df["state"].values:
                r1 = rainfall_df.loc[rainfall_df["state"] == s1, "annual_rainfall"].values[0]
                r2 = rainfall_df.loc[rainfall_df["state"] == s2, "annual_rainfall"].values[0]
                more = s1 if r1 > r2 else s2
                less = s2 if r1 > r2 else s1
                return f"{more} received more rainfall ({max(r1, r2)} mm) than {less} ({min(r1, r2)} mm)."
            else:
                return "Sorry, I couldn't find rainfall data for one of those states."

    elif "low rainfall" in user_input:
        crops = crops_df[crops_df["rainfall_type"].str.lower() == "low"]["crop"].tolist()
        return f"Crops that need low rainfall include: {', '.join(crops)}."

    elif "monsoon" in user_input:
        return "Monsoon rainfall refers to the seasonal rains between June and September in India, brought by southwest monsoon winds."

    elif any(word in user_input for word in ["hi", "hello", "hey", "yo", "hola", "namaste"]):
        return "Hi there! 👋 You can ask me things like: Compare rainfall in Kerala and Karnataka."

    elif any(word in user_input for word in ["yes", "yep", "ok", "okay", "sure", "hmm", "alright"]):
        return "Got it 👍! You can ask about rainfall comparisons or crops next if you like."

    else:
        return "Hmm, I didn’t quite get that 😅. You can ask:\n- Compare rainfall in Kerala and Karnataka\n- Crops that grow in low rainfall\n- What is monsoon rainfall?"
