import json

# Load the recipes from the JSON file
with open('recipes.json', 'r') as file:
    recipes = json.load(file)

# Get user input and convert it to a set of ingredients
user_ingredients = set(input("Enter a list of ingredients, separated by commas: ").lower().replace(" ", "").split(','))
print(user_ingredients)

# Find matching recipes
matching_recipes = []

for recipe in recipes:
    recipe_ingredients = set(ingredient.lower() for ingredient in recipe['ingredients'])

    # Only add the recipe if all recipe ingredients are in the user’s list
    if recipe_ingredients.issubset(user_ingredients):
        matching_recipes.append(recipe)

# Display results
if matching_recipes:
    print("Here are some recipes you can make:")
    for recipe in matching_recipes:
        print(f"\nRecipe: {recipe['name']}")
        print("Ingredients:", ", ".join(recipe['ingredients']))
        print("Instructions:", recipe['instructions'])
else:
    print("No matching recipes were found.")