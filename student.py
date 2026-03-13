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

data_sorted = data.sort_values(by=['Gender', 'Exam_Score'], ascending=[True, False])
print(data_sorted)

data.to_excel('student_summary.xlsx',index=False)
