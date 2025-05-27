 Employee Retention Analysis - HR Analytics

This project performs exploratory data analysis and builds a Logistic Regression model to predict employee retention based on HR data.

 Dataset

Dataset Source: [Kaggle - HR Analytics](https://www.kaggle.com/giripujar/hr-analytics)  
File used: `HR.csv`

 Tasks Performed

1. Exploratory Data Analysis (EDA)  
   - Checked the correlation between `salary` and employee retention.
   - Analyzed the impact of `Department` on employee retention.

2. Visualizations
   - Bar chart showing the relation between salary and employee attrition.
   - Bar chart showing the relation between department and employee attrition.

3. Model Building
   - Used `Logistic Regression` to predict if an employee will leave the company.
   - Selected features: `satisfaction_level`, `average_montly_hours`, `promotion_last_5years`, and `salary`.
   - One-hot encoded the `salary` column.

4. Model Evaluation
   - Split the dataset into training and testing sets (80:20 split).
   - Evaluated the model using `.score()` method for accuracy.

 Output

The model was trained and tested successfully.  
Accuracy score indicates how well the model predicts employee retention based on selected variables.

---

 How to Run

```bash
pip install pandas matplotlib scikit-learn
python hr_task.py
