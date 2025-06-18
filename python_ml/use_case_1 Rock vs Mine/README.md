
## 🪨 Rock vs Mine Predictor using Logistic Regression

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Sklearn](https://img.shields.io/badge/Made%20with-Scikit--Learn-F7931E.svg?logo=scikit-learn)](https://scikit-learn.org/)
[![Platform](https://img.shields.io/badge/Platform-Jupyter-lightgrey?logo=Jupyter)](https://jupyter.org)

This project uses a Machine Learning model to classify sonar signals as either **rock** or **mine** based on signal intensity features. It uses the [Sonar Dataset from UCI](https://archive.ics.uci.edu/ml/datasets/connectionist+bench/sonar/sonar) and implements **Logistic Regression** for binary classification.

---

### 📁 Project Structure

```bash
rock_mine_predictor/
│
├── rock_mine_predictor.ipynb   # Jupyter Notebook with all code
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── sonar.csv                   # (Optional) Dataset file
```

---

### 🚀 Features

* 📊 Exploratory Data Analysis
* 🧠 Logistic Regression model
* 🔄 One-hot encoding of target
* 🧪 Train-test split (80/20)
* 📉 Accuracy evaluation

---

### 🔧 Tech Stack

* Python 🐍
* Jupyter Notebook
* NumPy
* Pandas
* Scikit-learn

---

### 📂 Dataset Info

* **Source:** UCI ML Repository
* **Samples:** 208
* **Features:** 60 continuous values
* **Target Labels:** `'R'` for Rock, `'M'` for Mine

---

### 🧪 Model

* **Type:** Supervised ML
* **Algorithm:** Logistic Regression
* **Evaluation:** Accuracy Score

---

### 📌 How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/rock_mine_predictor.git
   cd rock_mine_predictor
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the notebook**

   ```bash
   jupyter notebook rock_mine_predictor.ipynb
   ```

---

### 📈 Results

| Metric   | Value                        |
| -------- | ---------------------------- |
| Accuracy | \~85–90% (varies with split) |

---

### 📃 requirements.txt

```txt
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.1
jupyter==1.0.0
```

> 📌 You can generate this using:

```bash
pip freeze > requirements.txt
```

---

### ✅ Future Enhancements

* 🔍 Add confusion matrix and classification report
* 🔄 Try more ML models (SVM, Random Forest, etc.)
* 🌐 Deploy via Streamlit or Flask

---

### 📃 License

This project is open-sourced under the [MIT License](LICENSE).

---

### 🙋‍♂️ Author

* **Name:** Manav Bhuta
* **Education:** Computer Engineering, Mumbai
* **LinkedIn:** \[www.linkedin.com/in/manav-bhuta]

---
