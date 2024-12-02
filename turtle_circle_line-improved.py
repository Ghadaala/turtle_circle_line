#improved code
import turtle

def setup_screen():
    """Set up the screen and general settings."""
    wn = turtle.Screen()
    wn.bgcolor("black")
    turtle.pensize(2)
    turtle.speed(0)

def draw_circle(radius, angle_step, colors):
    """Draw colorful circles with a repeating pattern."""
    for i in range(6):
        for color in colors:
            turtle.color(color)
            turtle.circle(radius)
            turtle.left(angle_step)

def move_turtle(x, y):
    """Move the turtle to a specific position."""
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

def main():
    setup_screen()

    # Main circle in the center
    draw_circle(radius=100, angle_step=10, colors=["pink", "cyan", "purple", "red", "yellow", "orange"])
    
    # Second circle at top-left position
    move_turtle(-150, 170)  # Move to top-left
    draw_circle(radius=50, angle_step=10, colors=["pink", "cyan", "purple", "red", "yellow", "orange"])
    
    # Third circle at bottom-right position
    move_turtle(150, -170)  # Move to bottom-right
    draw_circle(radius=50, angle_step=10, colors=["pink", "cyan", "purple", "red", "yellow", "orange"])
    
    turtle.hideturtle()
    turtle.mainloop()

# Run the program
main()
