import turtle
import pandas

screen = turtle.Screen()
screen.title("States Game")

img = "./blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


answer_state = screen.textinput(title="Guess the state:", prompt="What's another state's name?")
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x, state_data.y)
    t.write(state_data.state)



screen.exitonclick()
