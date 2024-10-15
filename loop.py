import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")

# Create a new turtle object
amber = turtle.Turtle()
amber.speed(2)  # Set the drawing speed

# Draw Amber's face
amber.penup()
amber.goto(0, 50)  # Move to the starting position
amber.pendown()
amber.fillcolor("white")
amber.begin_fill()
amber.circle(50)  # Draw a circle for the face
amber.end_fill()

# Draw Amber's eyes
amber.penup()
amber.goto(-15, 70)  # Move to the left eye position
amber.pendown()
amber.fillcolor("black")
amber.begin_fill()
amber.circle(10)  # Draw a circle for the left eye
amber.end_fill()

amber.penup()
amber.goto(15, 70)  # Move to the right eye position
amber.pendown()
amber.fillcolor("black")
amber.begin_fill()
amber.circle(10)  # Draw a circle for the right eye
amber.end_fill()

# Draw Amber's mouth
amber.penup()
amber.goto(-20, 40)  # Move to the mouth position
amber.pendown()
amber.color("black")
amber.width(5)
amber.goto(20, 40)  # Draw a line for the mouth

# Draw Amber's hair
amber.penup()
amber.goto(-30, 80)  # Move to the hair position
amber.pendown()
amber.color("brown")
amber.width(10)
amber.goto(30, 80)  # Draw a line for the hair

# Draw Amber's clothes
amber.penup()
amber.goto(-40, 20)  # Move to the clothes position
amber.pendown()
amber.color("orange")
amber.width(10)
amber.goto(40, 20)  # Draw a line for the clothes

# Hide the turtle and close the window
amber.hideturtle()
win.mainloop()