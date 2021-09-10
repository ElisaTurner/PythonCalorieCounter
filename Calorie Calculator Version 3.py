# Elisa Turner
# September 7, 2021
# Calorie Calculator Version 1
# Calculates how many calories someone has consumed based on number of cookies
# eaten 


# Define main function
def main():
    # Declare constants before variables
    # 40 cookies in a bag
    # 10 servings in a bag
    # 300 calories per serving
    COOKIES_PER_BAG = 40
    SERVINGS_PER_BAG = 10
    CALORIES_PER_SERVING = 300
    CALORIES_PER_COOKIE = 75
    # Calculate calories per cookie
    CALORIES_PER_COOKIE = CALORIES_PER_SERVING / (COOKIES_PER_BAG / SERVINGS_PER_BAG)
    # Declare and initialize variables.
    # String for name
    userName = ""
    # Whole number variable for cookies eaten
    cookiesEaten = 0
    # Real number variable for calories consumed
    caloriesConsumed = 0.0
    # Display "Welcome to the Calorie Counter!!"
    print(f"Welcome to the Calorie Counter!!\n\n")
    # Prompt/ask user for name
    userName = input(f"Please enter your name: ")
    # Prompt/ask for cookies eaten by displaying "Please enter number of cookies eaten"
    # Use int to make sure input turns into a number
    # Have to use int before input to make a number instead of printing 75 times
    cookiesEaten = int(input(f"How many cookies have you eaten: "))
    # Calculate/set calories consumed = cookies eaten * caloriespercookie
    caloriesConsumed = cookiesEaten * CALORIES_PER_COOKIE
    # Display calories consumed
    # the f in front of the quotes makes sure the variables are called instead of printed
    print(f"\nOk {userName}, you've consumed {caloriesConsumed} calories")



main()


