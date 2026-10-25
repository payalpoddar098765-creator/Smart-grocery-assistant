from urllib.parse import quote

print("===== SMART GROCERY ASSISTANT =====")

# Step 1: Number of people
try:
    people = int(input("How many people? "))

    if people <= 0:
        print("Please enter a valid number.")
        raise SystemExit

except ValueError:
    print("Please enter a valid number.")
    raise SystemExit

# Step 2: Recipe selection
print("\nChoose your recipe:")
print("1. Dosa")
print("2. Tomato Rice")

choice = input("Enter your choice (1 or 2): ").strip()

recipes = {
    "1": {
        "name": "Dosa",
        "ingredients": {
            "rice": (0.2, 60),
            "urad dal": (0.05, 120)
        }
    },
    "2": {
        "name": "Tomato Rice",
        "ingredients": {
            "rice": (0.15, 60),
            "tomato": (0.1, 40),
            "onion": (0.05, 35)
        }
    }
}

if choice not in recipes:
    print("Invalid recipe choice!")
    raise SystemExit

recipe = recipes[choice]

print("\nYour recipe:", recipe["name"])

# Step 3: Calculate ingredient quantities
print("\n===== INGREDIENTS REQUIRED =====")

for ingredient, details in recipe["ingredients"].items():
    quantity = details[0] * people
    print(f"{ingredient.title()}: {quantity:.2f} kg")

# Step 4: Find missing ingredients
available_input = input(
    "\nEnter ingredients you already have "
    "(separate them with commas): "
)

available = {
    item.strip().lower()
    for item in available_input.split(",")
    if item.strip()
}

missing = []

for ingredient, details in recipe["ingredients"].items():
    if ingredient.lower() not in available:
        missing.append((ingredient, details[1] * details[0] * people))

print("\n===== MISSING INGREDIENTS =====")

if missing:
    for ingredient, cost in missing:
        print(ingredient.title())
else:
    print("You already have all the ingredients!")

# Step 5: Calculate shopping bill
print("\n===== SHOPPING BILL =====")

total = 0

if missing:
    for ingredient, cost in missing:
        print(f"{ingredient.title()} - Rs. {cost:.2f}")
        total += cost

print("--------------------------")
print(f"Total Shopping Bill: Rs. {total:.2f}")

# Step 6: Nearby grocery shop suggestions
print("\n===== NEARBY GROCERY SHOPS =====")

area = input(
    "Enter your area or town to find grocery shops: "
).strip()

if area:
    search_query = quote("grocery shops near " + area)
    maps_link = (
        "https://www.google.com/maps/search/?api=1&query="
        + search_query
    )

    print("\nSearch for nearby grocery shops here:")
    print(maps_link)
    print("\nOpen the link in your browser to view shops.")
else:
    print("No area entered. Skipping shop suggestions.")

print("\n===== HAPPY COOKING! =====")