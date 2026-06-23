from mun_assistant import MUNAssistant

def main():
    assistant = MUNAssistant()

    while True:
        print("\n=== MUN & Debate Preparation Assistant ===")
        print("1. Add a Motion")
        print("2. View all Motions")
        print("3. Add Argument (For/Against)")
        print("4. Add Research Point")
        print("5. Save a Speech")
        print("6. View Motion Details")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter motion title: ").strip()
            assistant.add_motion(title)

        elif choice == "2":
            assistant.view_all_motions()

        elif choice == "3":
            title = input("Enter motion title: ").strip()
            side = input("Is this argument 'for' or 'against'? ").lower()
            while side not in ["for", "against"]:
                print("❌ Please enter 'for' or 'against' only!")
                side = input("Is this argument 'for' or 'against'? ").lower()
            content = input("Enter your argument: ")
            assistant.add_argument(title, content, side)

        elif choice == "4":
            title = input("Enter motion title: ").strip()
            fact = input("Enter research fact: ")
            source = input("Enter source: ")
            assistant.add_research_point(title, fact, source)

        elif choice == "5":
            title = input("Enter motion title: ").strip()
            speech_title = input("Enter speech title: ")
            content = input("Enter your speech: ")
            assistant.add_speech(title, speech_title, content)

        elif choice == "6":
            title = input("Enter motion title: ").strip()
            assistant.view_motion_details(title)

        elif choice == "7":
            print("👋 Goodbye! Good luck with your MUN!")
            break

        else:
            print("❌ Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()