import pandas as pd
data=pd.read_csv('StudentPerformanceFactors.csv')
print(data)

print(data.head(10))
print(data.tail())
print(data.info())
print(data.describe())
print(data.isnull())  

#Total Gender count Male and Female
gender_counts = data['Gender'].value_counts()
print(gender_counts)

#Groupby gender by size 
gender_counts = data.groupby('Gender').size()
print(gender_counts)

#percentage by Gender
gender_percent = data['Gender'].value_counts(normalize=True) * 100
print(gender_percent)

#performance score by Gender
performance_score=data.groupby('Gender')['Exam_Score'].mean()
print(performance_score)

#Total Education Level
education_category= data.groupby('Parental_Education_Level')['Gender'].count()
print(education_category)

#Attendance rate by gender
attendance_rate=data.groupby("Gender")['Attendance'].value_counts(normalize=True)*100
print(attendance_rate)

#gender sorted by exam score
data_sorted = data.sort_values(by=['Gender', 'Exam_Score'], ascending=[True, False])
print(data_sorted)

data.to_excel('student_summary.xlsx',index=False)

# Export all summaries into one Excel file
with pd.ExcelWriter("student_summary_report.xlsx") as writer:
    gender_counts.to_excel(writer, sheet_name="1_Gender_Count")
    gender_counts.to_excel(writer, sheet_name="2_Group_Size")
    gender_percent.to_excel(writer, sheet_name="3_Percentage")
    performance_score.to_excel(writer, sheet_name="4_Performance_Score")
    education_category.to_excel(writer, sheet_name="5_Education_Level")
    attendance_rate.to_excel(writer, sheet_name="6_Attendance_Rate")
    data_sorted.to_excel(writer, sheet_name="7_Sorted_Scores", index=False)
    print("✅ Report exported to student_summary_report.xlsx")