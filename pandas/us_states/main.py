import turtle
import pandas as pd

def get_mouse_click(x, y):
    print(x, y)

sc = turtle.Screen()
sc.title('US States')

imgs = 'blank_states_img.gif'
sc.addshape(imgs)
turtle.shape(imgs)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = sc.textinput(title=f"{len(guess_states)}/50 states correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states =[state for state in all_states if (state) not in guess_states ]
        # for state in all_states:
        #     if state not in guess_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('state_missed.csv')
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

sc.mainloop()
