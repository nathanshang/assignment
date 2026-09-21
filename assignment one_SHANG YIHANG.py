# Name: [SHANG YIHANG]
# Assignment One
# ddl is 22/9/2026 23:59pm

# Assignment 1: a calculator, a small keyword bot, and a turtle design.

def read_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, such as 12 or 3.5.")


def calculator():
    """Run the four-operation calculator required by Task A."""
    print("\n--- Simple Calculator ---")
    first = read_number("First number: ")
    second = read_number("Second number: ")
    symbol = input("Operation (+, -, *, /): ").strip()

    if symbol == "+":
        answer = first + second
    elif symbol == "-":
        answer = first - second
    elif symbol == "*":
        answer = first * second
    elif symbol == "/":
        if second == 0:
            print("A number cannot be divided by zero.")
            return
        answer = first / second
    else:
        print("That operation is not supported.")
        return

    print(f"Result: {answer:g}")


def qa_bot():
    """Answer the five required keywords in a case-insensitive way."""
    print("\n--- Question Answering Bot ---")
    print("Try: hello, python, jetson, ai, or name. Type quit to leave.")

    replies = {
        "hello": "Hello! It is nice to meet you.",
        "python": "Python is a programming language.",
        "jetson": "Jetson Nano is a small AI computer.",
        "ai": "AI stands for Artificial Intelligence.",
        "name": "My name is Python Bot.",
    }

    while True:
        query = input("Ask me something: ").strip().lower()
        if query == "quit":
            print("Bot: Goodbye!")
            break
        if query in replies:
            print("Bot:", replies[query])
        else:
            print("Bot: Sorry, I do not understand that yet.")


def turtle_drawing():
    """Draw a colourful repeating pattern with Python's turtle module."""
    import turtle

    screen = turtle.Screen()
    screen.title("Colourful Turtle Pattern")
    screen.bgcolor("midnight blue")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.pensize(2)
    artist.penup()
    artist.goto(-180, 0)
    artist.pendown()

    colours = ["cyan", "magenta", "gold", "spring green", "orange"]
    for round_number in range(36):
        artist.pencolor(colours[round_number % len(colours)])
        artist.forward(70 + round_number * 2)
        artist.left(144)
        if round_number % 6 == 5:
            artist.right(12)

    artist.hideturtle()
    screen.mainloop()


def main():
    """Let the user choose which assignment task to demonstrate."""
    while True:
        print("\n=== Assignment One ===")
        print("1. Simple Calculator")
        print("2. QA Bot")
        print("3. Turtle Drawing")
        print("4. Exit")
        choice = input("Choose a task: ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            turtle_drawing()
        elif choice == "4":
            print("Thanks for trying the program!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
