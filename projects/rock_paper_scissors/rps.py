import random
import json

# File name for saving scores
SCORES_FILE = "rps_v5.json"

# ---------------- FILE HANDLING ---------------- #
def load_data():
    """Load previous scores and history from file, if exists."""
    try:
        with open(SCORES_FILE, "r") as f:
            data = json.load(f)
            return data.get("scores", {"user": 0, "computer": 0, "tie": 0}), data.get("history", [])
    except FileNotFoundError:
        return {"user": 0, "computer": 0, "tie": 0}, []

def save_data(scores, history):
    """Save current scores and history to file."""
    data = {"scores": scores, "history": history}
    with open(SCORES_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- MAIN GAME ---------------- #
def rps_v5():
    choices = ["rock", "paper", "scissors"]
    scores, history = load_data()

    print("🎮 Welcome to Rock–Paper–Scissors!")
    print(f"Previous Scores => You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}\n")

    while True:
        # Input handling
        while True:
            try:
                user = input("Enter rock, paper, or scissors: ").strip().lower()
                if user not in choices:
                    raise ValueError("Invalid choice! Please enter rock, paper, or scissors.")
                break
            except ValueError as ve:
                print(ve)

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        # Game logic
        if user == computer:
            print("It's a Tie!")
            scores["tie"] = scores.get("tie", 0) + 1
            history.append("tie")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("You Win!")
            scores["user"] = scores.get("user", 0) + 1
            history.append("user")
        else:
            print("Computer Wins!")
            scores["computer"] = scores.get("computer", 0) + 1
            history.append("computer")

        print(f"Scores => You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}\n")

        replay = input("Play again? (y/n): ").strip().lower()
        if replay != "y":
            # Save data
            save_data(scores, history)

            # Show stats
            total_rounds = len(history)
            user_wins = history.count("user")
            comp_wins = history.count("computer")
            ties = history.count("tie")

            print("\n📊 FINAL STATS 📊")
            print(f"Total Rounds: {total_rounds}")
            print(f"Your Wins: {user_wins} ({user_wins/total_rounds*100:.1f}%)")
            print(f"Computer Wins: {comp_wins} ({comp_wins/total_rounds*100:.1f}%)")
            print(f"Ties: {ties} ({ties/total_rounds*100:.1f}%)")

            print("\nThanks for playing! 👋")
            break

# Run Game
if __name__ == "__main__":
    rps_v5()
