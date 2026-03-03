# manual_review/cli.py
from manual_review.manual_review import get_queue, mark_reviewed
import os

def display_queue():
    queue = get_queue()
    if not queue:
        print("No pending prompts for manual review.")
        return

    print("Pending Manual Review Prompts:")
    for idx, item in enumerate(queue):
        print(f"{idx + 1}. User: {item['user']}")
        print(f"   Prompt: {item['prompt']}")
        print(f"   Risk Score: {item['risk_score']}")
        print(f"   Provider: {item['provider']}")
        print("-" * 50)

def review_prompt():
    queue = get_queue()
    if not queue:
        print("No pending prompts to review.")
        return

    while queue:
        item = queue[0]
        print(f"\nReviewing Prompt:")
        print(f"User: {item['user']}")
        print(f"Prompt: {item['prompt']}")
        print(f"Risk Score: {item['risk_score']}")
        print(f"Provider: {item['provider']}")
        print("-" * 50)

        action = input("Action? [a]pprove / [r]eject / [s]kip / [q]uit: ").strip().lower()

        if action == "a":
            print("Prompt approved.")
            mark_reviewed(0)
        elif action == "r":
            print("Prompt rejected and removed from queue.")
            mark_reviewed(0)
        elif action == "s":
            print("Skipping prompt for now.")
            queue = get_queue()  # reload queue
            queue.append(queue.pop(0))  # move to end
        elif action == "q":
            print("Exiting manual review CLI.")
            break
        else:
            print("Invalid action. Please enter a, r, s, or q.")

        queue = get_queue()  # reload after any changes

if __name__ == "__main__":
    display_queue()
    review_prompt()