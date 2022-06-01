# Demonstrate how to use dictionary comprehensions
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # TODO: Use a comprehension to build a dictionary

    # TODO: Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}


if __name__ == "__main__":
    main()
