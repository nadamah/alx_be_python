# daily_reminder.py

# Get task details from the user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for task priority
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Add time-sensitivity details
if time_bound == "yes":
    full_message = f"Reminder: {base_message} that requires immediate attention today!"
else:
    full_message = f"Reminder: Note: {base_message}. Consider completing it when you have free time."

# Output the customized reminder
print("\n" + full_message)

