import tkinter as tk
from tkinter import messagebox

class StudentGradeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Tracker")

        self.students = {}
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Student Name:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.label_grades = tk.Label(self.root, text="Enter Grades (comma-separated):")
        self.label_grades.grid(row=1, column=0, padx=10, pady=10)

        self.grades_entry = tk.Entry(self.root)
        self.grades_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_grades_button = tk.Button(self.root, text="Add Grades", command=self.add_grades)
        self.add_grades_button.grid(row=1, column=2, padx=10, pady=10)

        self.report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def add_student(self):
        name = self.name_entry.get()
        if name:
            self.students[name] = []
            self.name_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Student '{name}' added successfully.")
        else:
            messagebox.showerror("Error", "Please enter a student name.")

    def add_grades(self):
        name = self.name_entry.get()
        grades = self.grades_entry.get()
        if name in self.students and grades:
            self.students[name].extend(map(int, grades.split(',')))
            self.grades_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Grades added for student '{name}' successfully.")
        elif not name:
            messagebox.showerror("Error", "Please enter a student name.")
        else:
            messagebox.showerror("Error", "Student not found.")

    def generate_report(self):
        report = "Grade Report:\n"
        for name, grades in self.students.items():
            average_grade = sum(grades) / len(grades) if grades else 0
            report += f"\n{name}:\nGrades: {', '.join(map(str, grades))}\nAverage Grade: {average_grade:.2f}\n"
        messagebox.showinfo("Grade Report", report)

def main():
    root = tk.Tk()
    app = StudentGradeTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
