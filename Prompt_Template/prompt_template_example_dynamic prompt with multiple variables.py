"""
==========================================================
LangChain PromptTemplate Example - dynamic prompt with multiple variables
----------------------------------------------------------
This script demonstrates how to use LangChain's PromptTemplate
to create a reusable prompt with placeholders that can be
formatted dynamically at runtime.

We'll define a simple template, fill it with user inputs, and
print the generated prompt. This is useful for building
consistent and structured prompts for LLM applications.
==========================================================
"""

# Step 1: Import necessary class from LangChain
from langchain.prompts import PromptTemplate

# Step 2: Define a template string with placeholders
# Here, {product} and {audience} will be filled dynamically
template_str = "Write a catchy marketing slogan for a {product} targeting {audience}."

# Step 3: Create a PromptTemplate object
# - input_variables: list of placeholder variable names used in the template
# - template: the actual template string
prompt = PromptTemplate(
    input_variables=["product", "audience"],
    template=template_str
)

# Step 4: Format the template with actual values
# You can imagine these values coming from user input or a dataset
filled_prompt = prompt.format(
    product="eco-friendly water bottle",
    audience="college students"
)

# Step 5: Print the formatted prompt
print("=== Generated Prompt ===")
print(filled_prompt)

"""
======================== SAMPLE OUTPUT ========================
=== Generated Prompt ===
Write a catchy marketing slogan for a eco-friendly water bottle targeting college students.
================================================================
"""

"""
======================== HOW THIS WORKS ========================
1. We define a text template with variables wrapped in curly braces.
2. We create a PromptTemplate object, specifying which variables appear in the template.
3. Using the .format() method, we substitute actual values into the placeholders.
4. The result is a fully formatted prompt string that can be passed to an LLM.
================================================================
"""
