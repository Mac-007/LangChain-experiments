"""
Filename Suggestion: dynamic_prompt_single_var.py

Description:
This script demonstrates how to create and use a dynamic prompt template
with a single variable using the `PromptTemplate` class. The template
is designed to explain any given topic in simple terms suitable for a
10-year-old. The user provides the topic, and the script outputs a
formatted explanation prompt.
"""

# Step 1: Import Required Library
# Assuming `PromptTemplate` comes from a library such as `langchain.prompts`
from langchain.prompts import PromptTemplate

# Step 2: Define the Dynamic Prompt Template
# We define a template with a single input variable 'topic'.
Dynamic_single_var_prompt = PromptTemplate(
    input_variables=["topic"],  # Variable to replace in the template
    template="Explain the topic '{topic}' in simple terms suitable for a 10-year-old."
)

# Step 3: Format the Prompt with a Specific Topic
# Here we provide the topic "quantum physics" to the template.
formatted_prompt = Dynamic_single_var_prompt.format(topic="quantum physics")

# Step 4: Output the Formatted Prompt
print(formatted_prompt)

"""
Sample Output:
Explain the topic 'quantum physics' in simple terms suitable for a 10-year-old.
"""

"""
How the Code Works:
1. Import the PromptTemplate class from the langchain.prompts library.
2. Create a template string with a placeholder for 'topic'.
3. Format the template by replacing the placeholder with an actual topic.
4. Print the final prompt which can be used as input for an AI model
   or further processing.
"""
