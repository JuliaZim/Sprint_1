new_tasks = ["task_001", "task_011", "task_007", "task_015", "task_005"]
completed_tasks = ["task_002", "task_012", "task_006"]

# Переносим выполненную задачу 005 из new_task в completed_task
completed_tasks.append(new_tasks.pop(-1))

# Удаляем таску 007
new_tasks.remove("task_007")

# Вывести последнюю таску из new_tasks на экран
print(new_tasks[-1])
