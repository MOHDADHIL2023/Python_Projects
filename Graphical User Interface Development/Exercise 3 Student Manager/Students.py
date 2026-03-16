import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.load_records()

    def load_records(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                num_students = int(file.readline().strip())
                for _ in range(num_students):
                    data = file.readline().strip().split(',')
                    student = {
                        'code': int(data[0]),
                        'name': data[1],
                        'coursework1': int(data[2]),
                        'coursework2': int(data[3]),
                        'coursework3': int(data[4]),
                        'exam': int(data[5])
                    }
                    self.students.append(student)
        else:
            messagebox.showerror("Error", f"File {self.filename} not found!")

    def save_records(self):
        with open(self.filename, 'w') as file:
            file.write(f"{len(self.students)}\n")
            for student in self.students:
                file.write(f"{student['code']},{student['name']},"
                           f"{student['coursework1']},{student['coursework2']},"
                           f"{student['coursework3']},{student['exam']}\n")

    def calculate_marks(self, student):
        coursework_total = sum([student['coursework1'], student['coursework2'], student['coursework3']])
        total_marks = coursework_total + student['exam']
        percentage = (total_marks / 160) * 100
        grade = self.determine_grade(percentage)
        return coursework_total, total_marks, percentage, grade

    def determine_grade(self, percentage):
        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        return 'F'

    def create_window(self):
        self.root = tk.Tk()
        self.root.title("Student Records Manager")
        self.root.geometry("400x500")
        self.root.resizable(0, 0)

        buttons = [
            ("View All Records", self.view_all_records),
            ("View Individual Record", self.view_individual_record),
            ("Highest Total Score", self.show_highest_score),
            ("Lowest Total Score", self.show_lowest_score),
            ("Sort Records", self.sort_records),
            ("Add Student", self.add_student),
            ("Delete Student", self.delete_student),
            ("Update Student", self.update_student)
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, command=command, width=30).pack(pady=10)

        self.root.mainloop()

    def view_all_records(self):
        records_window = tk.Toplevel(self.root)
        records_window.title("All Student Records")
        text_widget = tk.Text(records_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        total_percentage = 0
        for student in self.students:
            coursework_total, total_marks, percentage, grade = self.calculate_marks(student)
            record = (f"Name: {student['name']} (Code: {student['code']})\n"
                      f"Coursework Total: {coursework_total}/60\n"
                      f"Exam Mark: {student['exam']}/100\n"
                      f"Overall Percentage: {percentage:.2f}%\n"
                      f"Grade: {grade}\n\n")
            text_widget.insert(tk.END, record)
            total_percentage += percentage

        avg_percentage = total_percentage / len(self.students) if self.students else 0
        summary = (f"\nTotal Students: {len(self.students)}\n"
                   f"Average Percentage: {avg_percentage:.2f}%")
        text_widget.insert(tk.END, summary)
        text_widget.config(state=tk.DISABLED)

    def view_individual_record(self):
        student_names = [student['name'] for student in self.students]
        selected_name = simpledialog.askstring("Select Student", "Select Student Name:", initialvalue=student_names[0])
        
        if selected_name:
            student = next((s for s in self.students if s['name'] == selected_name), None)
            if student:
                coursework_total, total_marks, percentage, grade = self.calculate_marks(student)
                messagebox.showinfo("Individual Record", 
                    f"Name: {student['name']} (Code: {student['code']})\n"
                    f"Coursework Total: {coursework_total}/60\n"
                    f"Exam Mark: {student['exam']}/100\n"
                    f"Overall Percentage: {percentage:.2f}%\n"
                    f"Grade: {grade}")
            else:
                messagebox.showerror("Error", "Student not found")

    def show_highest_score(self):
        if not self.students:
            messagebox.showinfo("No Students", "No students in the record")
            return

        highest_student = max(self.students, key=lambda s: self.calculate_marks(s)[1])
        coursework_total, total_marks, percentage, grade = self.calculate_marks(highest_student)
        
        messagebox.showinfo("Highest Score", 
            f"Name: {highest_student['name']} (Code: {highest_student['code']})\n"
            f"Coursework Total: {coursework_total}/60\n"
            f"Exam Mark: {highest_student['exam']}/100\n"
            f"Overall Percentage: {percentage:.2f}%\n"
            f"Grade: {grade}")

    def show_lowest_score(self):
        if not self.students:
            messagebox.showinfo("No Students", "No students in the record")
            return

        lowest_student = min(self.students, key=lambda s: self.calculate_marks(s)[1])
        coursework_total, total_marks, percentage, grade = self.calculate_marks(lowest_student)
        
        messagebox.showinfo("Lowest Score", 
            f"Name: {lowest_student['name']} (Code: {lowest_student['code']})\n"
            f"Coursework Total: {coursework_total}/60\n"
            f"Exam Mark: {lowest_student['exam']}/100\n"
            f"Overall Percentage: {percentage:.2f}%\n"
            f"Grade: {grade}")

    def sort_records(self):
        order = simpledialog.askstring("Sort Order", "Enter 'asc' for ascending or 'desc' for descending:")
        
        if order:
            self.students.sort(key=lambda s: self.calculate_marks(s)[1], reverse=(order.lower() == 'desc'))
            self.view_all_records()

    def add_student(self):
        code = simpledialog.askinteger("Add Student", "Enter Student Code (1000-9999):")
        name = simpledialog.askstring("Add Student", "Enter Student Name:")
        coursework1 = simpledialog.askinteger("Add Student", "Enter Coursework 1 Mark (0-20):")
        coursework2 = simpledialog.askinteger("Add Student", "Enter Coursework 2 Mark (0-20):")
        coursework3 = simpledialog.askinteger("Add Student", "Enter Coursework 3 Mark (0-20):")
        exam = simpledialog.askinteger("Add Student", "Enter Exam Mark (0-100):")

        if all([code, name, coursework1 is not None, coursework2 is not None, 
                coursework3 is not None, exam is not None]):
            new_student = {
                'code': code,
                'name': name,
                'coursework1': coursework1,
                'coursework2': coursework2,
                'coursework3': coursework3,
                'exam': exam
            }
            self.students.append(new_student)
            self.save_records()
            messagebox.showinfo("Success", "Student record added successfully!")

    def delete_student(self):
        student_names = [student['name'] for student in self.students]
        selected_name = simpledialog.askstring("Delete Student", "Select Student Name to Delete:", initialvalue=student_names[0])
        
        if selected_name:
            self.students = [s for s in self.students if s['name'] != selected_name]
            self.save_records()
            messagebox.showinfo("Success", f"Student {selected_name} deleted successfully!")

    def update_student(self):
        student_names = [student['name'] for student in self.students]
        selected_name = simpledialog.askstring("Update Student", "Select Student Name to Update:", initialvalue=student_names[0])
        
        if selected_name:
            student = next((s for s in self.students if s['name'] == selected_name), None)
            if student:
                update_options = [
                    "Student Code",
                    "Student Name", 
                    "Coursework 1 Mark", 
                    "Coursework  2 Mark", 
                    "Coursework 3 Mark", 
                    "Exam Mark"
                ]
                
                selected_option = simpledialog.askstring(
                    "Update Options", 
                    "Select what to update:\n" + "\n".join(
                        f"{i+1}. {option}" for i, option in enumerate(update_options)
                    )
                )
                
                if selected_option:
                    try:
                        option_index = int(selected_option) - 1
                        new_value = simpledialog.askstring("New Value", f"Enter new {update_options[option_index]}:")
                        
                        if new_value:
                            if option_index == 0:
                                student['code'] = int(new_value)
                            elif option_index == 1:
                                student['name'] = new_value
                            elif option_index == 2:
                                student['coursework1'] = int(new_value)
                            elif option_index == 3:
                                student['coursework2'] = int(new_value)
                            elif option_index == 4:
                                student['coursework3'] = int(new_value)
                            elif option_index == 5:
                                student['exam'] = int(new_value)
                            
                            self.save_records()
                            messagebox.showinfo("Success", "Record updated successfully!")
                    except (ValueError, IndexError):
                        messagebox.showerror("Error", "Invalid selection")

def main():
    filename = "A1 - Skills Portfolio/Exercise 3 Student Manager/studentMarks.txt"
    app = StudentManager(filename)
    app.create_window()

if __name__ == "__main__":
    main()
