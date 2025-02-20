from typing import List

from project.task import Task


class Section:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        completed_task = next((t for t in self.tasks if t.name == task_name), None)
        if completed_task:
            completed_task.completed = True
            return f"Completed task {completed_task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        amount = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                amount += 1
        return f"Cleared {amount} tasks."

    def view_section(self) -> str:
        info = f"Section {self.name}:\n"
        for task in self.tasks:
            info += f"{task.details()}\n"
        return info
