"""
File: static_prompt_example.py

Description:
This script demonstrates how to create and use a static prompt with LangChain's 
PromptTemplate. The prompt is static, meaning it does not require any input 
variables and always returns the same text.
"""

# Step 1: Import required library
from langchain.prompts import PromptTemplate

# Step 2: Define a static prompt
# The template contains fixed text and does not use any dynamic input variables.
static_prompt = PromptTemplate(
    input_variables=[],  # No dynamic variables needed
    template="This is a static prompt example using LangChain's PromptTemplate."
)

# Step 3: Display the static prompt
# The format() method generates the final prompt string.
print(static_prompt.format())

"""
Sample Output:
This is a static prompt example using LangChain's PromptTemplate.
"""

"""
How the code works:
1. Import the PromptTemplate class from LangChain.
2. Create a PromptTemplate object with no input variables, providing a fixed template string.
3. Call the `format()` method of the PromptTemplate to get the static prompt text.
4. Print the generated prompt.
"""
