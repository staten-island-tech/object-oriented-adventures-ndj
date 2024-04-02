import turtle 

name = input("Enter your characters name: ")
age = int(input("Enter your characters starting age: (1,18)"))
print(name)
print(age)
screen = turtle.Screen()
screen.screensize(2600, 1400)
screen.title("Conquest")
image = "world_map.gif"
screen.addshape(image)
turtle.shape(image)
# screen.textinput(title="How to use map", prompt="Utilize the scrollbars on the right and bottom of the screen to scroll up/down and left/right respectively.")
# starting_location = screen.textinput(title="Starting country", prompt="Enter starting location: ")
turtler = turtle.Turtle("square")
turtler.hideturtle()
turtler.penup()
turtler.goto(-940, 290)
turtler.shapesize(5, 5)
turtler.color("red")

x = []
def colonies():
    colony = input("Enter the colony you want to start off at:(North America/South America/Europe/Africa/Asia/Australia) ")
    for i in colony:
        if i == "North America":
            print("Welcome to your new adventure!")
            x.append(colony)
        elif i == "South America":
            print("Good luck escaping the walls!")
            x.append(colony)
        elif colony == "Europe":
            print("Get geared up for your new journey!")
            x.append(colony)
        elif colony == "Africa":
            print("Don't try and become dehydrated!")
            x.append(colony)
        elif colony == "Asia":
            print("Welcome to the largest continent in the world!")
            x.append(colony)
        elif colony == "Australia":
            print("Don't let the kangaroos hurt you!")
            x.append(colony)
colonies()