def vacuum_agent(percept):
    table = {('A', 'Clean'): 'Move Right',
             ('A', 'Dirty'): 'Suck',
             ('B', 'Clean'): 'Move Left',
             ('B', 'Dirty'): 'Suck'}

    room, condition = percept
    action = table.get((room, condition), 'No Operation')
    return action


def main():
    while True:
        room = input("Enter the room to clean (A/B) or 'exit' to quit: ")
        if room.lower() == 'exit':
            break

        condition = input("Is the room dirty? (Clean/Dirty): ")

        action = vacuum_agent((room, condition))
        print(f"Action: {action}")

        if action == 'No Operation':
            print("Invalid input. Please try again.")

        print()

    print("Vacuum cleaner agent exited.")


if __name__ == '__main__':
    main()
