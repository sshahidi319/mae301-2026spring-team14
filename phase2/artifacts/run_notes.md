# Demo Run Notes

## Run Example 1
Screenshot file: `demo_run_1.png`
Input:
- Pantry ingredients: chicken, eggs, spinach, rice, olive oil
- Max calories: 600
- Minimum protein: 40

Notes:
This run demonstrates the main successful use case of the current prototype. The system accepts pantry ingredients and nutrition preferences, normalizes the pantry list, and returns ranked recipe suggestions with calories, protein, carbs, fat, and missing ingredients. 
The MVP correctly lists what ingredients are missing and if the calorie goals are hit for each preset recipe.

## Run Example 2
Screenshot file: `demo_run_2.png`
Input:
- Pantry ingredients: eggs, bread, peanut butter, banana
- Max calories: 500
- Minimum protein: 10

Notes:
This run demonstrates that the system can still produce useful suggestions for a different pantry input and lower protein requirement. It shows that the prototype is not limited to one pantry example and can adapt its ranking based on different available ingredients and nutrition preferences.

## Run Example 3
Screenshot file: `demo_run_3.png`
Input:
- Pantry ingredients: chicken, spinach
- Max calories: 450
- Minimum protein: 50

Notes:
This run demonstrates behavior when the pantry is more limited and the nutrition targets are more restrictive. It helps show one of the current design choices of the prototype: calorie and protein goals are treated as ranking preferences rather than strict exclusion rules, so recipes can still appear even when they do not perfectly satisfy every target.
The MVP ranks by number of ingredients and then ranks by calorie and protein goals. The MVP is still correctly listing whats missing and is listing if calorie and protein goals will be met by the recipes.
