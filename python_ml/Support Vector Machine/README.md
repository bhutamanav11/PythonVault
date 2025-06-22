---

```
# 🔍 Support Vector Machines with Scikit-Learn

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Active-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> 📁 Folder: `python_ml/svm/`  
> 🧠 Purpose: Practice & apply SVMs for classification on **Iris** and **Digits** datasets.

---

## ✨ Project Overview

This folder contains two hands-on Jupyter Notebooks using **Support Vector Machines (SVM)** to solve classification problems.

📘 **iris_dataset_svm.ipynb**  
🔢 **digit_dataset_svm.ipynb**

Through these notebooks, the goal is to:
- Understand the working of SVM
- Explore **different kernels**: `linear`, `rbf`
- Experiment with `C` (regularization) and `gamma` (kernel flexibility)
- Visualize how different settings affect accuracy

---

## 📂 Contents

| Notebook | Dataset | Objective |
|----------|---------|-----------|
| `iris_dataset_svm.ipynb` | Iris Dataset 🌸 | Classify flower species using sepal/petal features |
| `digit_dataset_svm.ipynb` | Digits Dataset 🔢 | Classify handwritten digits using pixel data |

---

## 📘 iris_dataset_svm.ipynb — *Getting Started with SVM*

- Uses `load_iris()` from `sklearn.datasets`
- Applies SVM to classify flowers into 3 species
- Tests `kernel='linear'` and `kernel='rbf'`
- Experiments with:
  - **C parameter** to control regularization
  - **Train-test split** to check generalization
- Outcome: Understand when linear separation works well

---

## 🧠 digit_dataset_svm.ipynb — *Advanced Exercise with Image Data*

- Uses `load_digits()` from `sklearn.datasets`
- Classifies images (0–9 digits) using SVM
- Visualizes digits using `matplotlib`
- Tries:
  - `kernel='rbf'` and `kernel='linear'`
  - Tuning `C` and `gamma` for max accuracy
- Outcome: Builds intuition on complex decision boundaries

---

## 🛠️ Concepts Practiced

- Support Vector Machines
- Kernel Trick (non-linear separation)
- Hyperparameter tuning
- Accuracy evaluation
- Visualization & feature engineering

---

## 🚀 Tools Used

| Tool | Purpose |
|------|---------|
| `Python 3.8+` | Programming language |
| `scikit-learn` | ML algorithms & datasets |
| `matplotlib` | Data visualization |
| `pandas` | Data handling |

## 💡 Author Notes

This is a personal ML practice repo focused on mastering core algorithms by working with real datasets and visualizations. These notebooks are intentionally simple and self-explanatory, great for students and beginners.

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

### 👨‍💻 Made by [Manav](https://github.com/bhutamanav11) — Learning ML by doing 🔁

```

---
