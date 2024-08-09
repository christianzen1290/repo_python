import turtle

# Function to draw a text input box
def draw_input_box(t, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Function to draw text
def draw_text(t, text, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, font=("Arial", 12, "normal"))

# Main function to draw the login form
def draw_login_form():
    screen = turtle.Screen()
    screen.title("Login Form")
    screen.setup(width=400, height=300)

    # Create turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed (0 is the fastest)

    # Draw username input box
    draw_text(t, "Username:", -150, 50)
    draw_input_box(t, -50, 50, 200, 20)

    # Draw password input box
    draw_text(t, "Password:", -150, 0)
    draw_input_box(t, -50, 0, 200, 20)

    # Draw login button
    draw_input_box(t, -50, -50, 100, 30)
    draw_text(t, "Login", -20, -35)

    t.hideturtle()  # Hide turtle after drawing

    turtle.done()

# Call the function to draw the login form
draw_login_form()
