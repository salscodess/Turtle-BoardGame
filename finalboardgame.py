# Salcodess
# 10/12/26
# Turtle Board Game
import turtle, math, random

screen = turtle.Screen()
screen.title("Chemistry INC.")

# Config
speed = 3

board_forward = 125
number_forward = board_forward  # does spacing
screen.bgcolor("#e8eef5")
screen.tracer(1)
number_font = max(1, round(number_forward * 0.45))
label_font = max(1, round(number_forward * 0.22))

#Stats
stats_rolled = 0
myst_amount = 0

# Create all the turtles
def make_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.speed(speed)
    return new_turtle
player_turtle = make_turtle()
board_turtle = make_turtle()
button_turtle = make_turtle()
stats_turtle = make_turtle()
dice_turtle = make_turtle()
deco_turtle = make_turtle()
title_turtle = make_turtle()
number_turtle = make_turtle()

player_turtle.color("Blue")
player_turtle.right(180)
player_turtle.shapesize(2,2,2)
# Spaces
spaces = {
    0: (5 * board_forward, -2 * board_forward),
    1: (4 * board_forward, -2 * board_forward),
    2: (3 * board_forward, -2 * board_forward),
    3: (2 * board_forward, -2 * board_forward),
    4: (board_forward, -2 * board_forward),
    5: (0, -2 * board_forward),
    6: (-board_forward, -2 * board_forward),
    7: (-2 * board_forward, -2 * board_forward),
    8: (-3 * board_forward, -2 * board_forward),
    9: (-4 * board_forward, -2 * board_forward),
    10: (-4 * board_forward, -board_forward),
    11: (-4 * board_forward, 0),
    12: (-4 * board_forward, board_forward),
    13: (-4 * board_forward, 2 * board_forward),
    14: (-3 * board_forward, 2 * board_forward),
    15: (-2 * board_forward, 2 * board_forward),
    16: (-board_forward, 2 * board_forward),
    17: (0, 2 * board_forward),
    18: (board_forward, 2 * board_forward),
    19: (2 * board_forward, 2 * board_forward),
    20: (3 * board_forward, 2 * board_forward),
    21: (4 * board_forward, 2 * board_forward),
    22: (5 * board_forward, 2 * board_forward),
    23: (5 * board_forward, board_forward),
    24: (5 * board_forward, 0),
    25: (5 * board_forward, -board_forward)
}

def output_draw():
    board_turtle.setheading(0)
    board_turtle.speed(200)
    board_turtle.goto(250,150)
    board_turtle.pendown()
    board_turtle.forward(250) #long
    board_turtle.right(90)
    board_turtle.forward(285) #wide
    board_turtle.right(90)
    board_turtle.forward(250) #long
    board_turtle.right(90)
    board_turtle.forward(285) #wide
    board_turtle.penup()
    board_turtle.goto(375, 0) #(250, 150) to (500, -150)
    board_turtle.setheading(0)
    board_turtle.goto(265, -100)
    board_turtle.pendown()

    new_x =265
    new_y = -100
    for lines in range(5):
        board_turtle.forward(35)
        board_turtle.penup()
        new_y += 50
        board_turtle.goto(new_x,new_y)
        board_turtle.pendown()
    board_turtle.penup()

updates = []
displayed_updates = 0

def stats_manager():
    global displayed_updates

    if len(updates) == displayed_updates:
        return

    stats_turtle.clear()
    stats_turtle.penup()

    y = -110
    index = len(updates) - 1
    messages_shown = 0

    while index >= 0 and messages_shown < 9:
        stats_turtle.goto(375, y)
        stats_turtle.write(
            updates[index],
            align="center",
            font=("Arial", 13, "bold")
        )

        y = y + 25
        index = index - 1
        messages_shown = messages_shown + 1

    displayed_updates = len(updates)

#Evil or good spaces
random_spaces = [4,7,10,13,16]
current_space = 0

player_space = 0

def move(next_space):
    global player_space

    if next_space > player_space:
        direction = 1
    else:
        direction = -1

    for spot in range(
        player_space + direction,
        next_space + direction,
        direction
    ):
        player_turtle.setheading(
            player_turtle.towards(spaces[spot])
        )
        player_turtle.goto(spaces[spot])
        player_space = spot

def event_manager():
    global current_space,myst_amount
    myst_amount = 0
    while current_space in random_spaces:
        updates.append('Mystery Space ' + str(current_space))
        random_event_num = random.randint(1, 4)

        if random_event_num == 1:
            current_space += 2
            myst_amount +=1
            updates.append("Forward 2 spaces!")
            print("You gained two spaces!")
        elif random_event_num == 2:
            current_space -= 3
            myst_amount +=1
            updates.append("Back 3 spaces :{")
            print("You lost three spaces ;{")
        elif random_event_num == 3:
            current_space = 0
            myst_amount += 1
            updates.append("Back to the start! ahah")
            print("You are back at the start! haha")
        elif random_event_num == 4:
            current_space = 25
            myst_amount += 1
            updates.append("skip to the end!")
            print("Congrats you magicly won (Roll the lottery next)")
        else:
            print("it failed :{")
        current_space = max(0, min(current_space, 25))
        move(current_space)
    # Win condition
    if current_space == 25:
        board_turtle.goto(20, 65)
        board_turtle.width(5)
        board_turtle.write(
            "You Win",
            align="center",
            font=("Arial", number_font, "bold")
        )
        print("Done")

def roll_dice():
    global current_space, stats_rolled

    if current_space == 25:
        return


    rolled = random.randint(1, 6)
    print(rolled)
    #updates.append("Rolled " + str(rolled))

    dice_turtle.clear()
    dice_turtle.goto(25, -125)
    dice_turtle.write(
        "You rolled: " + str(rolled),
        align="center",
        font=("Arial", 20, "bold")
    )

    current_space = min(current_space + rolled, 25)
    move(current_space)

    event_manager()
    stats_manager()
    stats_rolled += 1


def color_factory():
    colors = [
        "red", "orange", "yellow", "green", "blue",
        "purple", "pink", "cyan", "magenta", "lime",
        "turquoise", "gold", "violet", "coral",
        "salmon", "navy", "teal", "maroon"
    ]
    return random.choice(colors)
    #colors = random.choice

# Draw the board
board_turtle.goto(5.5 * board_forward, -2.5 * board_forward)
board_turtle.showturtle()
board_turtle.setheading(180)
board_turtle.speed(0)
# Draw Start to the right


color_factory()
board_turtle.pendown()
board_turtle.fillcolor(color_factory())
board_turtle.begin_fill()
for side in range(4):
    board_turtle.forward(board_forward)
    board_turtle.right(90)
board_turtle.penup()
board_turtle.end_fill()
board_turtle.forward(board_forward)


def draw_blocks(amount):
    for block in range(amount):
        board_turtle.fillcolor(color_factory())
        board_turtle.pendown()
        board_turtle.begin_fill()

        for side in range(4):
            board_turtle.forward(board_forward)
            board_turtle.right(90)

        board_turtle.end_fill()
        board_turtle.penup()
        board_turtle.forward(board_forward)

# Bottom middle
draw_blocks(9)

# Left column
board_turtle.right(90)
board_turtle.forward(board_forward)
draw_blocks(4)

# Top middle
board_turtle.right(90)
board_turtle.forward(board_forward)
draw_blocks(8)

# Right column
board_turtle.right(90)
board_turtle.goto(5.5 * board_forward, 2.5 * board_forward)
draw_blocks(4)

board_turtle.hideturtle()

# Numbers
# Apply the numbers

number_turtle.goto(5 * number_forward, -2.15 * number_forward)
number_turtle.write(
    "Start", align="center", font=("Arial", label_font, "bold")
)

number_turtle.goto(4 * number_forward, -2.3 * number_forward)
number_turtle.showturtle()
number_turtle.penup()
number_turtle.setheading(180)
number_turtle.speed(0)

next_number = 1

for numbers in range(9):
    number_turtle.write(
        next_number, align="center", font=("Arial", number_font, "bold")
    )

    if next_number in random_spaces:
        old_y = number_turtle.ycor()
        number_turtle.sety(old_y - 18)
        number_turtle.write(
            "Mystery Space", align="center", font=("Arial", 11, "bold")
        )
        number_turtle.sety(old_y)

    next_number += 1
    if next_number == 10:
        number_turtle.right(90)
    number_turtle.forward(number_forward)
for numbers in range(4):
    number_turtle.write(
        next_number, align="center", font=("Arial", number_font, "bold")
    )

    if next_number in random_spaces:
        old_y = number_turtle.ycor()
        number_turtle.sety(old_y - 18)
        number_turtle.write(
            "Mystery Space", align="center", font=("Arial", 11, "bold")
        )
        number_turtle.sety(old_y)

    next_number += 1
    if next_number == 14:
        number_turtle.right(90)
    number_turtle.forward(number_forward)
for numbers in range(8):
    number_turtle.write(
        next_number, align="center", font=("Arial", number_font, "bold")
    )

    if next_number in random_spaces:
        old_y = number_turtle.ycor()
        number_turtle.sety(old_y - 18)
        number_turtle.write(
            "Mystery Space", align="center", font=("Arial", 11, "bold")
        )
        number_turtle.sety(old_y)

    next_number += 1
    if next_number == 22:
        number_turtle.right(90)
        number_turtle.goto(5 * number_forward, 1.7 * number_forward)
    else:
        number_turtle.forward(number_forward)
for numbers in range(4):
    if next_number == 25:
        number_turtle.write(
            "Finish!", align="center", font=("Arial", label_font, "bold")
        )
    else:
        number_turtle.write(
            next_number, align="center", font=("Arial", number_font, "bold")
        )
    next_number += 1
    if next_number == 25:
        number_turtle.goto(5 * number_forward, -1.15 * number_forward)
    else:
        number_turtle.forward(number_forward)
    if next_number > 25:
        number_turtle.hideturtle()
        break

# Button
button_turtle.showturtle()
button_turtle.speed(50)
button_turtle.goto(-125, 75)
button_turtle.pendown()
button_turtle.forward(300)
button_turtle.right(90)
button_turtle.forward(150)
button_turtle.right(90)
button_turtle.forward(300)
button_turtle.right(90)
button_turtle.forward(150)
button_turtle.penup()
button_turtle.goto(25, -45)
button_turtle.write("Roll Dice!",align="center",font=("Arial", 32, "bold"))

def click(x, y):
    if -125 <= x <= 175 and -100 <= y <= 50:
        roll_dice()
screen.onclick(click)

player_turtle.shape("turtle")
player_turtle.goto(spaces[0])
player_turtle.showturtle()
output_draw()
stats_manager()
screen.onkey(roll_dice, "space")
screen.listen()

screen.update()
screen.mainloop()
