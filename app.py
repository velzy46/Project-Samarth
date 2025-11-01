from flask import Flask, render_template, request, jsonify
import pandas as pd
from qa_engine import answer_question

app = Flask(__name__)


# Load datasets
try:
    rainfall_df = pd.read_csv("data/rainfall.csv")
    crops_df = pd.read_csv("data/crops_clean.csv")
except Exception as e:
    rainfall_df = pd.DataFrame()
    crops_df = pd.DataFrame()
    print("Error loading CSVs:", e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("question", "")
    answer = answer_question(user_input)
    return jsonify({"answer": answer})

    user_input = request.json.get("question", "").lower().strip()

    try:
        # 1️⃣ Compare rainfall
        if "compare" in user_input and "rainfall" in user_input:
            parts = user_input.replace("compare rainfall in", "").split("and")
            if len(parts) == 2:
                s1, s2 = parts[0].strip().title(), parts[1].strip().title()
                if s1 in rainfall_df["state"].values and s2 in rainfall_df["state"].values:
                    r1 = rainfall_df.loc[rainfall_df["state"] == s1, "annual_rainfall"].values[0]
                    r2 = rainfall_df.loc[rainfall_df["state"] == s2, "annual_rainfall"].values[0]
                    more = s1 if r1 > r2 else s2
                    less = s2 if r1 > r2 else s1
                    return jsonify({
                        "answer": f"{more} received more rainfall ({max(r1, r2)} mm) than {less} ({min(r1, r2)} mm)."
                    })
                else:
                    return jsonify({
                        "answer": "Sorry, I couldn't find rainfall data for one of those states."
                    })

        # 2️⃣ High rainfall crops
        elif "high rainfall" in user_input:
            crops = crops_df[crops_df["rainfall_type"].str.lower() == "high"]["crop"].tolist()
            return jsonify({"answer": f"Crops that grow well in high rainfall areas include: {', '.join(crops)}."})

        # 3️⃣ Low rainfall crops
        elif "low rainfall" in user_input:
            crops = crops_df[crops_df["rainfall_type"].str.lower() == "low"]["crop"].tolist()
            return jsonify({"answer": f"Crops that need low rainfall include: {', '.join(crops)}."})

        # 4️⃣ Monsoon meaning
        elif "monsoon" in user_input:
            return jsonify({
                "answer": "Monsoon rainfall refers to the seasonal rains between June and September in India, brought by southwest monsoon winds."
            })

        # 5️⃣ General chat fallback
        elif any(word in user_input for word in ["hi", "hello", "hey", "how are you", "namaste"]):
            return jsonify({
                "answer": "Hi there! 👋 I'm your rainfall assistant. You can ask things like:\n- Compare rainfall in Kerala and Karnataka\n- Crops that grow in low rainfall\n- What is monsoon rainfall?"
            })

        else:
            return jsonify({
                "answer": "Hmm, I didn’t quite get that 😅. You can ask:\n- Compare rainfall in Kerala and Karnataka\n- Crops that grow in low rainfall\n- What is monsoon rainfall?"
            })

    except Exception as e:
        print("Error:", e)
        return jsonify({"answer": "Sorry, something went wrong."})


if __name__ == "__main__":
    app.run(debug=True)
