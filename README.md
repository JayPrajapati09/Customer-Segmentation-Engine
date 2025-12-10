# German Credit Risk: Customer Segmentation & Profiling

## 📌 Project Overview
This project uses **Unsupervised Machine Learning** to identify distinct customer segments within the German Credit dataset. 

The goal was to move beyond simple data analysis and create actionable **Business Personas**. By grouping customers based on credit history, demographics, and behavior, this analysis helps banks tailor their **Risk Management** and **Marketing Strategies** for specific groups.

## 📊 Key Results: The 4 Customer Personas
After optimizing the clustering algorithm, we identified four distinct customer profiles:

| Cluster | Persona Name | Financial Profile | Business Strategy (Bank View) |
| :--- | :--- | :--- | :--- |
| **0** | **The VIP Investors** | High Credit, Long Duration | **High Risk / High Reward.** Needs personalized relationship management. |
| **1** | **The Young Starters** | Low Credit, Young, Female-Leaning | **Future Growth.** Target with student/starter products to build loyalty. |
| **2** | **The Middle-Class Core** | Medium Credit, Established Jobs | **Cash Cow.** The stable backbone of the portfolio; focus on retention. |
| **3** | **The Cautious Seniors** | Low Credit, Safe Repayment | **Safe Harbor.** Low profit margin, but almost zero risk exposure. |

## 🛠️ Technical Approach
This project solves the "Curse of Dimensionality" often found in mixed categorical/numerical datasets.

1.  **Data Preprocessing:**
    * Handled missing values and performed Feature Scaling (`StandardScaler`).
    * Applied One-Hot Encoding to categorical variables (Sex, Job, Purpose).

2.  **Dimensionality Reduction (PCA):**
    * Initially, K-Means struggled with the sparse data (Silhouette Score: ~0.15).
    * Implemented **Principal Component Analysis (PCA)** to retain 95% of variance while reducing noise.
    * **Result:** Improved cluster separation and stability (Silhouette Score increased to **0.35**).

3.  **Modeling & Evaluation:**
    * Algorithm: **K-Means Clustering**.
    * Optimization: Used **Optuna** and Elbow Method to determine the optimal number of clusters ($k=4$).

4.  **Interpretation (The "Human" Layer):**
    * Mapped mathematical centroids to real-world attributes.
    * Created a "Value Matrix" to assess Revenue vs. Risk for each group.

## 💻 Technologies Used
* **Language:** Python
* **Libraries:** Scikit-Learn, Pandas, NumPy, Optuna
* **Visualization:** Seaborn, Matplotlib, Plotly (Radar Charts)
* **Techniques:** Clustering, PCA, Feature Engineering, Data Visualization

