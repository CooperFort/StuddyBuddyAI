import json

class DataManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name

    def save_tasks(self, tasks):
        with open(self.file_name, "w") as file:
            json.dump(tasks, file)

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
