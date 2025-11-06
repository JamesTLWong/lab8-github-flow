from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console
#Choice color = Yellow, Exit color = Red, Question color = cyan, Event color = green

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    Console().print("You wake up in a dark forest. You can go left or right.", style = "green")
    while True:
        choice = Console().input("[cyan]Which direction do you choose?[/cyan] ([yellow]left/right/[/yellow][red]exit[/red]): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            Console().print("You have escaped the forest. Goodbye.", style="red")
            break
        
        Console().print(step(choice, events), style="green")
