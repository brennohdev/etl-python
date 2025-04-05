# 📊 ETL Project with Visual Report - Student Performance and Attendance

This project implements a full ETL (Extract, Transform, Load) pipeline using Python and SQLite, based on a dataset of student academic performance. After the ETL process, the project generates visual reports to analyze trends and insights.

---

## 🚀 Features

- **Extraction** of data from a CSV file (`attendance.csv`)
- **Transformation** for data cleaning, normalization, and enrichment
- **Loading** into a SQLite database
- **Visual reports** using `matplotlib` and `seaborn`

---

## 📂 Project Structure

```
etl/
├── etl/
│   ├── __init__.py
│   ├── extract.py       # Handles CSV reading
│   ├── transform.py     # Data cleaning and processing
│   └── load.py          # Loads data into SQLite
│
├── report/
│   ├── __init__.py
│   ├── generate.py      # Main report generation script
│   └── plots.py         # Graph plotting functions
│
├── attendance.csv       # Raw dataset
├── attendance.db        # Generated SQLite database
├── main.py              # Runs the ETL pipeline
└── report_main.py       # Runs the visual report generator
```

---

## 🛠️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-user/your-repo.git
cd your-repo
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### 3. Install dependencies
```bash
pip install pandas matplotlib seaborn
```

### 4. Run the ETL pipeline
```bash
python main.py
```

### 5. Generate the visual report
```bash
python report_main.py
```

---

## 📈 Visualizations Included

- Average attendance by course (bar chart)
- Pass rate (pie chart)
- Final grade distribution (histogram)
- Attendance vs Final grade correlation (scatter plot)

---

## 📊 Dataset

Based on the [Student Performance and Attendance Dataset](https://www.kaggle.com/datasets/marvyaymanhalim/student-performance-and-attendance-dataset/data), which includes:

- Student ID and name
- Course
- Attendance percentage
- Final grade
- Approval status (passed or not)

---

## 🧼 Best Practices Followed

- Modular codebase for maintainability
- Clear and descriptive function and file names
- Following Clean Code and Clean Architecture principles

---

## 🧠 Author

Developed by Brenno Henrique

---