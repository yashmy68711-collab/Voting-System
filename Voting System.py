class VotingSystem:
    def __init__(self):
        self.candidates = {}

    def add_candidate(self, name):
        if name in self.candidates:
            print("Candidate already exists")
        else:
            self.candidates[name] = 0
            print(f"{name} added successfully")

    def cast_vote(self, name):
        found = False

        for candidate in self.candidates:
            if candidate.lower() == name.lower():
                self.candidates[candidate] += 1
                print("Vote counted successfully!")
                found = True
                break

        if not found:
            print("Candidate not found")

    def show_results(self):
        if len(self.candidates) == 0:
            print("No candidates available")
        else:
            print("\nVote Count:")
            for name, votes in self.candidates.items():
                print(f"{name}: {votes} votes")

    def show_winner(self):
        if len(self.candidates) == 0:
            print("No candidates available")
            return

        winner = max(self.candidates, key=self.candidates.get)
        votes = self.candidates[winner]

        print(f"Winner: {winner} with {votes} votes")


system = VotingSystem()

while True:
    print("\n--- Voting System ---")
    print("1. Add Candidate")
    print("2. Cast Vote")
    print("3. Show Results")
    print("4. Show Winner")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter candidate name: ")
        system.add_candidate(name)

    elif choice == "2":
        name = input("Vote for candidate: ")
        system.cast_vote(name)

    elif choice == "3":
        system.show_results()

    elif choice == "4":
        system.show_winner()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")