# Data Science Practicals (1 to 10)

This repository contains all 10 Data Science practical scripts along with their required input datasets. Each practical is completely self-contained and ready to be opened and run in **Python IDLE** or from the terminal on any PC.

---

## 📁 Repository Structure

```text
pc/
├── practicals/
│   ├── practical_1.py              # Q1) CSV to HORUS Format
│   ├── practical_2.py              # Q2) JSON to HORUS Format
│   ├── practical_3.py              # Q3) XML to HORUS Format
│   ├── practical_4.py              # Q4) Fixers Utilities
│   ├── practical_5.py              # Q5) Averaging of Data
│   ├── practical_6.py              # Q6) Create Sample Dataset
│   ├── practical_7.py              # Q7) Retrieve Attributes of Data
│   ├── practical_8.py              # Q8) Fix Problematic Column Names
│   ├── practical_9.py              # Q9) Network Routing Diagram
│   ├── practical_10.py             # Q10) Error Management with Pandas
│   ├── run_all.py                  # Script to run and test all practicals
│   ├── requirements.txt            # Required Python packages
│   ├── Country_Code.csv            # Dataset for Practical 1
│   ├── Country_Code.json           # Dataset for Practical 2
│   ├── Country_Code.xml            # Dataset for Practical 3
│   ├── IP_DATA_CORE.csv            # Dataset for Practical 5
│   ├── IP_DATA_ALL.csv             # Dataset for Practical 7 & 8
│   ├── sample1.csv                 # Dataset for Practical 10
│   └── sample2.csv                 # Dataset for Practical 9
├── .gitignore
└── README.md
```

---

## 🚀 Setup & Installation (On Any PC)

### 1. Clone the repository
```bash
git clone https://github.com/tushaljadhav/pc.git
cd pc
```

### 2. Install Dependencies
Ensure Python is installed, then install required libraries:
```bash
pip install -r practicals/requirements.txt
```
*(Required packages: `pandas`, `networkx`, `matplotlib`)*

---

## 🖥️ How to Run in Python IDLE

1. Open the `practicals` folder.
2. **Right-click** on any script (e.g., `practical_1.py`) and select **"Edit with IDLE"**.
3. In the IDLE window, press **`F5`** (or go to menu: `Run` ➔ `Run Module`).
4. The output will immediately appear in the Python IDLE Shell!

---

## ⚡ How to Run from Terminal / Command Prompt

Navigate to the `practicals` folder and run any practical:
```bash
cd practicals
python practical_1.py
python practical_2.py
python practical_3.py
python practical_4.py
python practical_5.py
python practical_6.py
python practical_7.py
python practical_8.py
python practical_9.py
python practical_10.py
```

Or run all practicals at once:
```bash
python run_all.py
```
