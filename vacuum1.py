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
        room = input("\nWhich room to clean? (A/B/Exit): ")
        
        if room.lower() == 'exit':
            print("Vacuum cleaner agent exited.")
            break
            
        if room not in ['A', 'B']:
            print("Invalid input, please enter 'A', 'B', or 'Exit'.")
            continue

        while True:
            condition = input(f"\nIs the room {room} dirty? (Clean/Dirty/Stop): ")
            if condition.lower() == 'stop':
                print("Vacuum cleaner agent stopped.")
                break

            if condition not in ['Clean', 'Dirty']:
                print("Invalid input, please enter 'Clean', 'Dirty', or 'Stop'.")
                continue

            action = vacuum_agent((room, condition))
            print(f"Action: {action}")
            
            if room == 'A':
                room = 'B'
            elif room == 'B':
                room = 'A'

        # print()


main()
