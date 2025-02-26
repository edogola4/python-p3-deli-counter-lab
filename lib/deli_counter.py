def line(deli):
    if len(deli) == 0:
        print("The line is currently empty.")
    else:
        positions = [f"{i+1}. {name}" for i, name in enumerate(deli)]
        print("The line is currently: " + " ".join(positions))


def take_a_number(deli, name):
    deli.append(name)
    position = len(deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(deli):
    if len(deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving = deli.pop(0)
        print(f"Currently serving {serving}.")
