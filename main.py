import turtle
import pandas
NUM_STATES = 50
state_data = pandas.read_csv('50_states.csv')

# print(state_data[state_data.state == 'Ohio'])

screen = turtle.Screen()
screen.title('U.S. States Game')

img = 'blank_states_img.gif'
screen.addshape(img)
screen.setup(800, 600)
turtle.shape(img)

states = []

while len(states) < NUM_STATES:
    state_is_used = False
    # Get input from player
    state_choice = screen.textinput(title=f"{len(states)}/{NUM_STATES} State's Correct",
                                    prompt="What's another state's name?").title()
    # Exit game
    if state_choice == 'Exit':
        # Create list of missed states
        missed_states = [state for state in state_data.state if state not in states]
        break
    # Check if state has been used
    for check in states:
        if state_choice == check:
            state_is_used = True
    if state_is_used:
        continue
    else:
        # Check if choice is a state
        for state in state_data.state:
            if state_choice == state:
                # Create turtle obj and move it to correct position
                state_obj = state_data[state_data.state == state_choice]
                new_text = turtle.Turtle()
                new_text.hideturtle()
                new_text.penup()
                new_text.goto(int(state_obj.x), int(state_obj.y))
                new_text.write(state, align="center", font=('Courier', 8, 'bold'))
                states.append(state_choice)
new_data = pandas.DataFrame(missed_states)
new_data.to_csv('states_to_learn.csv')