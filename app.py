import time
import sys

def countdown(t, label):
    """Displays a countdown timer in the terminal."""
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        sys.stdout.write(f"\r{label}: {timer}")
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    print()

def main():
    """Main function to run the study session timer."""
    print("🚀 Welcome to the Smart Study Session Timer! 🚀")
    
    try:
        work_duration = int(input("Enter work session duration in minutes (e.g., 25): ")) * 60
        break_duration = int(input("Enter break duration in minutes (e.g., 5): ")) * 60
        sessions = int(input("Enter number of sessions to complete: "))
        
        print("\nLet's get started!")
        
        for i in range(1, sessions + 1):
            print(f"\n--- Session {i} of {sessions} ---")
            
            # Work Session
            countdown(work_duration, "💪 Focus Time")
            print("🎉 Work session complete! Time for a break. 🎉")
            
            # Break Session (if not the last session)
            if i < sessions:
                countdown(break_duration, "🧘 Break Time")
                print("✅ Break's over! Let's get back to it. ✅")

        print("\n✨ Congratulations! You've completed all your study sessions! ✨")

    except ValueError:
        print("\n❌ Invalid input. Please enter numbers only. Exiting. ❌")
    except KeyboardInterrupt:
        print("\n\n👋 Timer stopped. See you next time! 👋")

if __name__ == "__main__":
    main()