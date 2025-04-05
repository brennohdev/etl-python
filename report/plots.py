import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def plot_attendance_by_course(df):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x='Course', y='Attendance')
    plt.title('Average Attendance by Course')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_passed_pie(df):
    counts = df['Passed'].value_counts()
    labels = ['Approved', 'Not Approved']
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=['#4CAF50', '#F44336'])
    plt.title('Approval Rate')
    plt.show()

def plot_grade_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Final Grade'], bins=10, kde=True)
    plt.title('Final Grade Distribution')
    plt.xlabel('Final Grade')
    plt.ylabel('Frequency')
    plt.show()

def plot_attendance_vs_grade(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Attendance', y='Final Grade', hue='Passed')
    plt.title('Correlation: Attendance vs Final Grade')
    plt.show()
