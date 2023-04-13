import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []

all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state name?" ).title()
    
    if answer_state == "Exit":
        break

    if (answer_state in all_states) and (answer_state not in guessed_states):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(state_data.state.item())

missed_states = [item for item in all_states if item not in guessed_states]

pd_data = pandas.DataFrame(missed_states)
pd_data.to_csv("missed_states.csv")