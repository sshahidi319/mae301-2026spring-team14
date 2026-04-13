# ShelfAware Phase 2

## Overview
ShelfAware is a meal recommendation prototype that helps users turn available pantry ingredients into practical meal suggestions. The current Phase 2 version accepts pantry ingredients and nutrition preferences, then ranks recipe suggestions and shows estimated calories, protein, carbs, fat, and missing ingredients needed to complete each meal.

For Phase 2, we focused on building a narrow but working end-to-end prototype rather than trying to complete every long-term feature at once. This version is meant to demonstrate meaningful MVP progress, reproducibility, and clear evidence of what currently works and what still remains to be built.

## Current MVP Definition
The current prototype workflow:

1. The user enters pantry ingredients manually.
2. The user enters a maximum calorie preference and minimum protein preference.
3. The system normalizes pantry ingredient names.
4. The system compares the pantry against a local recipe dataset.
5. The system ranks recipe suggestions based on pantry matches and nutrition preference alignment.
6. The system displays estimated macros and missing ingredients for each recipe.

## Current Features
- Manual pantry input
- Basic ingredient normalization
- Nutrition-aware recipe ranking
- Estimated calories, protein, carbs, and fat
- Missing ingredient output for grocery planning
- Reproducible terminal-based demo

## Current Prototype Behavior
The current prototype treats calorie and protein goals as ranking preferences, not strict exclusion rules. Recipes that better match the user’s targets are ranked higher, but recipes outside the targets may still appear lower in the results.

This behavior was chosen for Phase 2 so the system can still return useful suggestions when pantry options are limited. In a later version, we may change this behavior to completely exclude recipes that do not meet the user’s calorie or protein targets once we have the running pantry inventory setup as well as a larger recipe database.

## Repository Contents
This Phase 2 folder includes:
- `demo.py` — main working prototype
- `README.md` — setup and run instructions
- `report.md` — Phase 2 progress report
- `artifacts/` — screenshots, logs, and other proof of progress

The repository also contains a separate `nanogpt/` folder from an earlier experimental direction. That work explored recipe text generation, but it is not the main Phase 2 MVP.

## Requirements
This prototype currently uses standard Python only.

- Python 3.x

No external Python packages are required for the current `demo.py`.

## How to Run
From the repository root, open a terminal and run
- Mac:
  
 cd phase2

 python3 demo.py
  
- Windows:

 cd phase2
 
 python demo.py

