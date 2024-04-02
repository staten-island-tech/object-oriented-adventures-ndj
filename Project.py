name = input("Enter your characters name: ")
age = int(input("Enter your characters starting age: (1,18)"))
print(name)
print(age)

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