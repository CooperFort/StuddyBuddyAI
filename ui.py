import tkinter as tk
from tkinter import messagebox
import datetime
from task_manager import TaskManager
from recommendation_engine import RecommendationEngine
from data_manager import DataManager
from calendar_integration import CalendarIntegration
from ml_prioritizer import TaskPrioritizer
import matplotlib.pyplot as plt

class StudyBuddyUI:
    def __init__(self):
        self.task_manager = TaskManager()
        self.recommendation_engine = RecommendationEngine()
        self.data_manager = DataManager()
        self.calendar_integration = CalendarIntegration()
        self.prioritizer = TaskPrioritizer()
        self.task_manager.tasks = self.data_manager.load_tasks()

        self.root = tk.Tk()
        self.root.title("StudyBuddy AI")

    def run(self):
        self.create_ui()
        self.root.mainloop()

    def create_ui(self):
        tk.Label(self.root, text="Task Name:").pack()
        self.task_name_entry = tk.Entry(self.root, width=50)
        self.task_name_entry.pack()

        tk.Label(self.root, text="Deadline (YYYY-MM-DD):").pack()
        self.deadline_entry = tk.Entry(self.root, width=50)
        self.deadline_entry.pack()

        tk.Label(self.root, text="Importance (1-5):").pack()
        self.importance_entry = tk.Entry(self.root, width=50)
        self.importance_entry.pack()

        tk.Button(self.root, text="Add Task", command=self.add_task).pack()

        tk.Label(self.root, text="Your Tasks:").pack()
        self.task_list = tk.Listbox(self.root, width=70, height=10)
        self.task_list.pack()

        tk.Button(self.root, text="Delete Task", command=self.delete_task).pack()
        tk.Button(self.root, text="Get Recommendations", command=self.get_recommendations).pack()
        tk.Button(self.root, text="Visualize Tasks", command=self.visualize_tasks).pack()

        self.update_task_list()

    def add_task(self):
        name = self.task_name_entry.get()
        deadline = self.deadline_entry.get()
        importance = self.importance_entry.get()
        if name and deadline and importance:
            try:
                deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
                self.task_manager.add_task(name, deadline, importance)
                self.calendar_integration.add_event(name, deadline)
                self.update_task_list()
                self.data_manager.save_tasks(self.task_manager.get_tasks())
                messagebox.showinfo("Task Added", f"Task '{name}' added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format or importance level.")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            self.task_manager.delete_task(index)
            self.update_task_list()
            self.data_manager.save_tasks(self.task_manager.get_tasks())
        else:
            messagebox.showerror("Error", "No task selected!")

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.task_list.insert(tk.END, f"{task['Task']} - {task['Deadline']}")

    def get_recommendations(self):
        next_task = self.task_manager.get_next_task()
        if next_task:
            deadline = next_task['Deadline']
            days_to_deadline = (datetime.datetime.strptime(deadline, "%Y-%m-%d") - datetime.datetime.now()).days
            importance = int(next_task.get('Importance', 3))
            recommendation = self.recommendation_engine.get_recommendation(days_to_deadline, importance)
            messagebox.showinfo(
                "Personalized Recommendations",
                f"Next Task: {next_task['Task']} (Due: {next_task['Deadline']})\n\n"
                f"Suggestion: {recommendation}"
            )
        else:
            messagebox.showinfo("No Tasks", "No tasks available to analyze.")

    def visualize_tasks(self):
        tasks = self.task_manager.get_tasks()
        if not tasks:
            messagebox.showerror("Error", "No tasks to visualize!")
            return

        # Extract task details
        task_names = [task['Task'] for task in tasks]
        days_to_deadline = [
            (datetime.datetime.strptime(task['Deadline'], "%Y-%m-%d") - datetime.datetime.now()).days
            for task in tasks
        ]
        importance = [int(task['Importance']) for task in tasks]
        deadlines = [task['Deadline'] for task in tasks]

        # Create a horizontal bar graph
        plt.figure(figsize=(10, 6))
        bars = plt.barh(task_names, days_to_deadline, color='skyblue', edgecolor='black')

        # Add importance and deadline as text in the middle of the bars
        for bar, imp, deadline in zip(bars, importance, deadlines):
            bar_center = bar.get_width() / 2  # Center of the bar
            plt.text(
                bar_center,  # X-coordinate of text
                bar.get_y() + bar.get_height() / 2,  # Y-coordinate of text (centered vertically)
                f"Importance: {imp}, Due: {deadline}",  # Text to display
                ha='center', va='center', fontsize=10, color='black'
            )

        # Add titles and labels
        plt.title('Task Deadlines with Importance and Dates', fontsize=16)
        plt.xlabel('Days to Deadline', fontsize=12)
        plt.ylabel('Tasks', fontsize=12)

        # Display the graph
        plt.tight_layout()
        plt.show()




