import random
import tkinter as tk

# Recipe categories and their corresponding ingredients
recipe_categories = {
    "Italian": ["pasta", "tomatoes", "olive oil", "basil", "garlic", "parmesan cheese"],
    "Mexican": ["tortillas", "beans", "rice", "salsa", "avocado", "cheese"],
    "Asian": ["rice", "soy sauce", "ginger", "garlic", "vegetables", "chicken"],
    # Add more recipe categories and ingredients as needed
}

# Ingredient prices
ingredient_prices = {
    "pasta": 2.99,
    "tomatoes": 1.99,
    "olive oil": 4.99,
    "basil": 1.49,
    "garlic": 0.99,
    "parmesan cheese": 3.49,
    "tortillas": 2.49,
    "beans": 1.99,
    "rice": 1.99,
    "salsa": 2.99,
    "avocado": 1.99,
    "cheese": 2.99,
    "soy sauce": 2.49,
    "ginger": 1.99,
    "vegetables": 2.99,
    "chicken": 5.99,
    # Add more ingredients and their prices as needed
}

# Generate a random recipe with estimated cost
def generate_recipe():
    recipe = "Recipe: \n"
    
    # Select a random recipe category
    recipe_category = random.choice(list(recipe_categories.keys()))
    recipe += "Category: " + recipe_category + "\n"
    
    # Select ingredients based on the recipe category
    recipe += "Ingredients: \n"
    ingredients = recipe_categories[recipe_category]
    recipe += ", ".join(ingredients) + "\n"
    
    # Calculate the estimated cost of ingredients
    total_cost = sum(ingredient_prices[ingredient] for ingredient in ingredients)
    recipe += "Estimated Cost: $" + str(round(total_cost, 2)) + "\n"
    
    return recipe

# Function to print the recipe
def print_recipe():
    recipe = generate_recipe()
    print(recipe)
    
# Create a GUI window
window = tk.Tk()
window.title("Recipe Generator - Manike Grocery")
window.geometry("400x300")

# Create a label with the grocery store name
store_name_label = tk.Label(window, text="Manike Grocery", font=("Arial", 16))
store_name_label.pack(pady=10)

# Create a button to generate and print a recipe
generate_button = tk.Button(window, text="Generate Recipe", command=print_recipe)
generate_button.pack(pady=10)

# Run the GUI event loop
window.mainloop()
