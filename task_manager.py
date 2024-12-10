class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline, importance):
        self.tasks.append({"Task": name, "Deadline": deadline, "Importance": importance})

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_tasks(self):
        return self.tasks

    def get_next_task(self):
        if not self.tasks:
            return None
        return sorted(self.tasks, key=lambda x: x["Deadline"])[0]
