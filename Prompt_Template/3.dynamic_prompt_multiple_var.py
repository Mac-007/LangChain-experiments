"""
Filename Suggestion: dynamic_story_prompt.py

Description:
This script demonstrates how to create and use a dynamic prompt with multiple variables 
using the PromptTemplate class. It allows you to define a template with placeholders 
for variables like 'name', 'age', and 'hobby', and then generate a customized story 
by filling in these variables.
"""

# Step 1: Import Required Libraries
# Note: Ensure you have the necessary library (e.g., langchain) installed if PromptTemplate is from it
from langchain.prompts import PromptTemplate

# Step 2: Define the Dynamic Prompt
# The template has placeholders for 'name', 'age', and 'hobby'
multi_var_prompt = PromptTemplate(
    input_variables=["name", "age", "hobby"],
    template="Write a short story about a person named {name}, who is {age} years old and loves {hobby}."
)

# Step 3: Generate a Story by Filling in the Variables
# Here we provide values for the placeholders
story = multi_var_prompt.format(name="Alice", age=12, hobby="painting")

# Step 4: Display the Generated Story
print(story)


"""
Sample Output:
Write a short story about a person named Alice, who is 12 years old and loves painting.
"""

"""
How the Code Works:
1. We import the PromptTemplate class which allows us to create text templates with variables.
2. We define a template string with placeholders {name}, {age}, and {hobby}.
3. Using the .format() method, we replace the placeholders with actual values.
4. The result is a dynamically generated story that is printed to the console.
"""
