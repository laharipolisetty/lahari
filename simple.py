import heapq
from collections import defaultdict

class TaskManager:
    def _init_(self):
        self.tasks = []
        self.task_dict = {}
        self.id_counter = 1
        self.recommendations = defaultdict(list)

    def add_task(self, description, priority=1):
        task_id = self.id_counter
        self.id_counter += 1
        task = {'id': task_id, 'description': description, 'priority': priority}
        heapq.heappush(self.tasks, (priority, task_id, task))
        self.task_dict[task_id] = task
        self._update_recommendations(description, task_id)
        return task

    def remove_task(self, task_id):
        if task_id in self.task_dict:
            del self.task_dict[task_id]
            self.tasks = [(p, tid, t) for (p, tid, t) in self.tasks if tid != task_id]
            heapq.heapify(self.tasks)
  return True
        return False

    def list_tasks(self):
        return [task for (_, _, task) in sorted(self.tasks)]

    def prioritize_task(self, task_id, new_priority):
        if task_id in self.task_dict:
            task = self.task_dict[task_id]
            self.remove_task(task_id)
            task['priority'] = new_priority
            heapq.heappush(self.tasks, (new_priority, task_id, task))
            self.task_dict[task_id] = task
            return task
        return None

    def recommend_tasks(self, description):
        recommendations = []
        words = description.split()
        for word in words:
            if word in self.recommendations:
                for task_id in self.recommendations[word]:
                    if task_id in self.task_dict:
                    recommendations.append(self.task_dict[task_id])
        return recommendations

    def _update_recommendations(self, description, task_id):
        words = description.split()
        for word in words:
            self.recommendations[word].append(task_id)

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Prioritize task")
        print("5. Recommend tasks")
        print("6. Exit")

        choice = input("Enter choice: ")
        
        if choice == '1':
 description = input("Enter task description: ")
            priority = int(input("Enter task priority (default is 1): ") or "1")
            task = manager.add_task(description, priority)
            print(f"Task added: {task}")
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            success = manager.remove_task(task_id)
            if success:
                print("Task removed successfully.")
            else:
                print("Task not found.")
        elif choice == '3':
            tasks = manager.list_tasks()
            print("Tasks:")
            for task in tasks:
                print(task)
        elif choice == '4':
            task_id = int(input("Enter task ID to prioritize: "))
            new_priority = int(input("Enter new priority: "))
            task = manager.prioritize_task(task_id, new_priority)
            if task:
                print(f"Task updated: {task}")
            else:
                print("Task not found.")
   elif choice == '5':
            description = input("Enter description to get recommendations: ")
            recommendations = manager.recommend_tasks(description)
            print("Recommended tasks:")
            for task in recommendations:
                print(task)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
