The "Recipe Generator - Manike Grocery" is a Python project that generates random recipes based on different categories and provides an estimated cost for the ingredients. It also includes a graphical user interface (GUI) with the name of the grocery store, "Manike Grocery", to enhance the user experience.

Features:

Random Recipe Generation: The program randomly selects a recipe category from options like Italian, Mexican, Asian, etc., and generates a recipe accordingly. Each recipe includes a category, a list of ingredients, and an estimated cost based on the ingredient prices.
Ingredient Database: The project utilizes a dictionary to store the recipe categories and their corresponding ingredients. This allows for easy modification and expansion of the available recipes.
Cost Calculation: The program calculates the estimated cost of the ingredients by accessing an ingredient price database. Each ingredient is assigned a price, and the total cost is computed based on the selected ingredients for the recipe.
Graphical User Interface (GUI): The GUI window displays the name of the grocery store, "Manike Grocery", using a label. This gives the project a visually appealing and branded interface.
Recipe Printing: The GUI includes a "Generate Recipe" button that, when clicked, generates a random recipe and prints it in the console. This allows users to easily view and access the generated recipes.
How to Use:

Run the Python script using a Python interpreter with Tkinter library installed.
The GUI window will appear, titled "Recipe Generator - Manike Grocery".
The window will display the grocery store name, "Manike Grocery", using a label.
Click the "Generate Recipe" button to generate a random recipe.
The recipe will be printed in the console, displaying the category, ingredients, and estimated cost.
