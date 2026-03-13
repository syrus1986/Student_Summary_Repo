# 📊 Student Summary Report

This project analyzes student performance factors using **Python + Pandas** and exports results into a multi‑sheet Excel file (`student_summary_report.xlsx`).

---

## 📂 Report Highlights

1. **Total Gender Count**  
   - Shows the number of male and female students in the dataset.

2. **Group Size by Gender**  
   - Displays how many records belong to each gender group.

3. **Percentage by Gender**  
   - Calculates the percentage distribution of male vs female students.

4. **Performance Score by Gender**  
   - Provides the average performance score for each gender.

5. **Total Education Level**  
   - Summarizes the counts of different education levels.

6. **Attendance Rate by Gender**  
   - Shows the average attendance rate for male and female students.

7. **Gender Sorted by Exam Score**  
   - Lists exam scores sorted within each gender group for comparison.

---

## ✅ Output
Running the script generates:

- `student_summary_report.xlsx` → A polished Excel file with **7 sheets**, each containing one of the summaries above.

---

## 📊 Example Code
```python
import pandas as pd

df = pd.read_csv("StudentPerformanceFactors.csv")

# Example: Average performance score by gender
performance_by_gender = df.groupby("gender")["performance_score"].mean()
print(performance_by_gender)
