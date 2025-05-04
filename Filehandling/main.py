from datetime import datetime


def feedback_collecting():
    feedback = input("Enter your feedback: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("feedback.txt", "a") as file:
        file.write(f"{timestamp} {feedback}\n")
    print("thanks for your feedback")


def view_feedback():
    with open("feedback.txt", "r") as file:
        content = file.read()
        if content:
            print(content)
        else:
            print("No feedback available.")


def main():
    while True:
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            feedback_collecting()
        elif choice == '2':
            view_feedback()
        elif choice == '3':
            print("you can close now!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")



main()
