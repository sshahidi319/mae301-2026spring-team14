# ShelfAware Phase 2 Report

## 1. Objective and Current MVP Definition
The goal of ShelfAware is to help users turn the ingredients they already have into realistic meal suggestions that fit their nutrition goals. For Phase 2, we narrowed the scope of the project to a smaller but functional MVP that could be demonstrated clearly and reproducibly.

The current MVP focuses on the following workflow:
1. accept pantry ingredients as manual input,
2. accept a maximum calorie target and minimum protein target,
3. normalize ingredient names into a cleaner pantry list,
4. compare the pantry against a recipe dataset,
5. rank recipe suggestions based on pantry overlap and nutrition preference alignment,
6. display macros and missing ingredients for each suggested recipe.

This version does not yet represent the full ShelfAware vision. Instead, it is meant to show that the core recommendation loop can work in a simple and reproducible way.

## 2. What Has Been Built So Far
At this stage, the project includes a working `phase2/demo.py` prototype that runs in the terminal and produces recipe suggestions from pantry input. The demo currently supports:
- manual pantry ingredient entry,
- calorie and protein preference entry,
- ingredient normalization using simple aliases,
- recipe ranking,
- macro output including calories, protein, carbs, and fat,
- missing ingredient output for grocery planning.

This gives the project a working end-to-end flow from user input to ranked recipe output. The current prototype is intentionally narrow, but it demonstrates a meaningful portion of the intended ShelfAware functionality.

In parallel, the repository also contains an earlier `nanogpt/` experiment. That work explored recipe-text generation using a small character-level NanoGPT model trained on a very limited recipe set. While this was a useful technical experiment, it does not yet solve the main ShelfAware task of matching pantry contents with nutrition-aware meal recommendations. For that reason, the Phase 2 submission focuses on the rule-based pantry recommendation prototype rather than the generative model.

## 3. Technical Approach
The current prototype uses a small local recipe dataset stored directly in the code. Each recipe includes:
- a title,
- a set of ingredients,
- calories,
- protein,
- carbs,
- fat.

The first step of the demo is pantry parsing. The user enters ingredients as a comma-separated list, and the system cleans the entries by converting them to lowercase, removing punctuation, trimming spacing, and applying a small alias dictionary so similar ingredient names can map to the same normalized item. For example, “chicken breast” can be treated as “chicken,” and “white rice” can be treated as “rice.”

After the pantry is normalized, each recipe is scored using two main ideas:
1. how many recipe ingredients match the pantry,
2. how well the recipe aligns with calorie and protein preferences.

The current system treats calorie and protein goals as ranking preferences rather than strict exclusion rules. Recipes that better satisfy the targets are ranked higher, but recipes that do not fully satisfy the targets may still appear lower in the output. This was intentionally chosen for Phase 2 so the program can still produce suggestions even when the pantry is limited. In a later version, this may be changed so recipes that do not meet the nutrition targets are completely excluded.

The final output shows the top-ranked recipes along with macro information and the ingredients that are still missing. This makes the prototype useful both as a meal suggestion tool and as a basic grocery-planning aid.

## 4. Evidence of Progress
The current prototype can be run from the `phase2/` folder using `python3 demo.py`. A successful run prompts the user for pantry ingredients, maximum calories, and minimum protein, then prints ranked recipe suggestions with macros and missing ingredients.

Evidence of progress for this phase includes:
- a working `demo.py` file,
- a screenshot of a successful terminal run in `phase2/artifacts/`,
- a saved run log such as `phase2/artifacts/demo_run.txt`,
- a repository structure that separates the current Phase 2 MVP from earlier experimental work.

This evidence shows that the project has progressed from a broad concept into a reproducible prototype with a clear input-output flow.

## 5. Current Limitations and Open Risks
The current prototype has several important limitations.

1. the recipe dataset is very small and is currently hard-coded into the script. That means the recommendation space is limited and does not yet reflect the variety needed for a realistic user-facing product.

2. pantry input is still manual. A major part of the long-term ShelfAware idea is a running pantry inventory that persists over time and updates as groceries are added and meals are consumed. That feature is not yet built in the current Phase 2 version.

3. the system does not yet include real receipt parsing or OCR in the main demo flow. The user must type ingredients manually rather than uploading a grocery receipt and automatically updating inventory.

4. the nutrition values are approximate and attached to whole recipes rather than generated dynamically from a full nutrition database. 

5. the current recommendation logic is simple and transparent, but not especially advanced. It uses a small scoring system rather than a larger learned model or more robust recommendation engine.

6. the earlier NanoGPT experiment remains limited by a very small training set and does not yet support structured pantry-aware, nutrition-aware recommendations. Because of that, it is better treated as an exploratory side experiment rather than the main solution at this point.

## 6. Plan for Phase 3
The next major step is to expand the recipe dataset significantly. A likely path is to incorporate a much larger recipe source from Kaggle so the system can recommend from a broader and more realistic recipe collection. This would improve variety, make ranking more meaningful, and better support different user preferences.

Another major priority is adding a running pantry inventory. Instead of relying on one-time manual entry each time the demo is used, the system should maintain a saved pantry state that updates over time. This would move the project much closer to the original ShelfAware idea described in the proposal.

Additional Phase 3 goals include:
- adding receipt parsing so groceries can be converted into pantry items automatically,
- improving ingredient normalization and substitution logic,
- improving macro and nutrition accuracy,
- testing stricter filtering behavior so recipes that fail calorie or protein requirements can be fully excluded if desired,
- improving the user interface beyond a terminal-only prototype.

Overall, the Phase 2 result is a working prototype that demonstrates the core ShelfAware recommendation loop. While it is still limited, it establishes a strong base for expanding into a larger dataset, a persistent pantry system, and more realistic nutrition-aware recommendations in the next phase.
