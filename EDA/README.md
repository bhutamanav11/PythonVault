
---

```markdown
 📊 Amazon Bestsellers EDA

An exploratory data analysis (EDA) project on the "Amazon Bestsellers with Categories" dataset.  
This project dives deep into trends across ratings, prices, reviews, genres, years, and authors.

---

 📁 Dataset Info

- Source: Amazon Bestsellers dataset (2009–2019)
- Features: Title, Author, Genre, User Rating, Reviews, Price, Year

---

 📌 Key Analyses

1. Data Cleaning  
   - Removed duplicates  
   - Handled missing/zero prices  
   - Corrected column types

2. Distributions  
   - Price and reviews visualized (log scale + box plots)  
   - Rating distribution explored

3. Top & Bottom Insights  
   - Top reviewed, highest rated, and most expensive books

4. Frequency Analysis  
   - Most frequent authors  
   - Most common genre  
   - Book releases by year

5. Comparative Trends  
   - Genre-wise average price, rating, and review count  
   - Yearly trends across all metrics

6. Author Analysis  
   - Top authors by frequency  
   - Best-rated authors (with 3+ books)

7. Correlation Heatmap  
   - Numeric feature relationships: Rating, Price, Reviews

8. Custom Score  
   - Custom formula: `(Rating × Reviews) / Price`  
   - Ranked books based on overall value

---

 📈 Visualizations

The notebook includes bar plots, line charts, correlation heatmaps, and dual-axis trend plots using `matplotlib` and `seaborn`.

---

 🧠 Conclusion

This analysis reveals:
- Fiction dominates quantity, but both genres show similar ratings.
- Ratings have improved over the years, while prices have declined.
- Authors like Jeff Kinney and J.K. Rowling lead both in presence and performance.
- A custom score effectively highlights high-value books by balancing quality, popularity, and cost.

---

 🚀 Technologies Used

- Python (Pandas, NumPy)
- Visualization: Matplotlib, Seaborn
- Jupyter Notebook

---

---

 🧩 Future Ideas

- Genre + Year heatmaps  
- Sentiment analysis on book reviews (if text data is available)  
- Predictive modeling (e.g. rating prediction)

---

 📬 Contact

Feel free to reach out via [LinkedIn](https://www.linkedin.com/) if you'd like to collaborate or have questions!

---
```

