# 🌦️ Project Samarth — Rainfall Chat Assistant

An interactive chatbot that compares rainfall across Indian states and suggests suitable crops based on rainfall type.

---

## 🧩 **Architecture**

**User (asks question)**  
⬇️  
**Chat Interface (Streamlit)**  
⬇️  
**Reasoning Engine (`qa_engine.py`)**  
⬇️  
**Data Layer (`rainfall.csv` + `crops.csv`)**  
⬇️  
**Result + Source Citation**

---

### 💡 **Features**
- Compare rainfall between two states  
- Identify crops suited for high or low rainfall  
- Explain monsoon rainfall  
- Friendly responses for general chat  

---

### 🧰 **Tech Stack**
- **Python (Flask)**  
- **HTML, CSS, JavaScript**  
- **Pandas**  
- **CSV datasets**

---

### 📂 **Dataset**
Includes:  
- `rainfall.csv`: Annual rainfall by Indian states  
- `crops_clean.csv`: Crops and their rainfall requirements  

---

### 👩‍💻 **Developer**
Built by **Saraswathi (alias Velzy)** for **Bharat Fellowship 2025**.

---

### ⚙️ **Run Locally**
```bash
pip install -r requirements.txt
python app.py


