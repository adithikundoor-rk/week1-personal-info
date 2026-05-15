# Personal Information Manager
# My first Python project

# --- STEP 1: WELCOME MESSAGE ---
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# --- STEP 2: STORE STATIC INFORMATION ---
# Using the variables from your instruction sheet
name = "Alex Johnson"
age = 22
city = "San Francisco"
hobby = "playing guitar"

# --- STEP 3: GET USER INPUT ---
print("Please tell me about yourself:")
print("-" * 30)

# The space after the '?' makes the output look clean
favorite_food = input("What's your favorite food? ")
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

# --- STEP 4: CALCULATE AGE IN MONTHS ---
age_in_months = age * 12

# --- STEP 5: DISPLAY INFORMATION ---
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# --- STEP 6: GOODBYE MESSAGE ---
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)