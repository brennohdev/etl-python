from report.data_loader import load_data
from report.plots import (
    plot_attendance_by_course,
    plot_passed_pie,
    plot_grade_distribution,
    plot_attendance_vs_grade,
)

def generate_report():
    # Load data
    df = load_data()

    # Generate plots
    plot_attendance_by_course(df)
    plot_passed_pie(df)
    plot_grade_distribution(df)
    plot_attendance_vs_grade(df)