import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.color("black")
pen.hideturtle()
pen.penup()


num_correct = 0

# read in the CSV data
data = pd.read_csv("50_states.csv")
state_column = data["state"].tolist()
guessed_states = []


game_is_on = True

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [states for states in state_column if states not in guessed_states]
        data = pd.DataFrame(missing_states)
        data.to_csv("missing_states.csv")
        break
    if answer_state in state_column and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        row = data[data.state == answer_state]
        pen.goto(int(row.x), int(row.y))
        pen.write(f"{answer_state}", align="center", font=("Arial", 11, "normal"))
        num_correct += 1




turtle.exitonclick()
# create a list of all the states to compare

