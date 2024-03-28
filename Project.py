name = input("Enter your characters name: ")
age = int(input("Enter your characters starting age: (1,18)"))
print(name)
print(age)
def colonies():
    colony = input("Enter the colony you want to start off at:(North America/South America/Europe/Africa/Asia/Australia) ")
    for colony in colonies:
        if colony== "North America":
            print(colony)
            print("Welcome to your new adventure!")
        if colony == "South America":
            print(colony)
            print("Good luck escaping the walls!")
        if colony == "Europe":
            print("Get geared up for your new journey!")
        if colony == "Africa":
            print("Don't try and become dehydrated!")
        if colony == "Asia":
            print("Welcome to the largest continent in the world!")
        if colony == "Australia":
            print("Don't let the kangaroos hurt you!")
colonies()