
---

```markdown
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

- 📘 `iris_dataset_svm.ipynb`  
- 🔢 `digit_dataset_svm.ipynb`

Through these notebooks, the goal is to:
- Understand the working of SVM
- Explore **different kernels**: `linear`, `rbf`
- Experiment with `C` (regularization) and `gamma` (kernel flexibility)
- Visualize how different settings affect accuracy

---

## 📂 Contents

| Notebook                 | Dataset        | Objective                                              |
|--------------------------|----------------|--------------------------------------------------------|
| `iris_dataset_svm.ipynb` | Iris Dataset 🌸 | Classify flower species using sepal/petal features     |
| `digit_dataset_svm.ipynb`| Digits Dataset 🔢| Classify handwritten digits using pixel image data     |

---

## 📘 iris_dataset_svm.ipynb — *Getting Started with SVM*

- Uses `load_iris()` from `sklearn.datasets`
- Applies SVM to classify flowers into 3 species
- Tests `kernel='linear'` and `kernel='rbf'`
- Experiments with:
  - `C` parameter to control regularization
  - Train-test split to check generalization

> 🎯 **Outcome:** Build intuition on how linear vs non-linear kernels behave on structured numeric data.

---

## 🧠 digit_dataset_svm.ipynb — *Advanced Exercise with Image Data*

- Uses `load_digits()` from `sklearn.datasets`
- Visualizes digit images using `matplotlib`
- Applies SVM for handwritten digit classification (0–9)
- Tests:
  - `kernel='rbf'` and `kernel='linear'`
  - Tuning `C` and `gamma` to boost performance

> 🎯 **Outcome:** Gain hands-on experience with hyperparameter tuning for complex data.

---

## 🛠️ Concepts Practiced

- Support Vector Machines (SVM)
- Kernel Trick for non-linear separation
- Hyperparameter tuning: `C`, `gamma`
- Model evaluation using accuracy
- Feature exploration + visualization

---

## 🚀 Tools Used

| Tool            | Purpose                       |
|------------------|-------------------------------|
| `Python 3.8+`     | Programming language           |
| `scikit-learn`    | ML algorithms & datasets       |
| `matplotlib`      | Data visualization             |
| `pandas`          | Data preprocessing & analysis  |

---

## 💡 Author Notes

This is part of my personal ML practice series, designed to **strengthen algorithm intuition** using real datasets. The code is clean, beginner-friendly, and ideal for hands-on learning.

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

### 👨‍💻 Made by [Manav](https://github.com/bhutamanav11) — Learning ML by doing 🔁
```

---
