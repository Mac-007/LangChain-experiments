"""
Filename Suggestion: few_shot_dictionary_prompt.py

Description:
This script demonstrates how to use a few-shot prompt with the PromptTemplate class.
It provides a dictionary assistant that defines a given word by showing a few examples
(first “apple” and “cat”) and then generating the definition for a new word.
"""

# Step 1: Import Required Libraries
# Note: Ensure you have the necessary library installed (e.g., langchain) if PromptTemplate is from it
from langchain.prompts import PromptTemplate

# Step 2: Define the Few-Shot Prompt
# This template includes a few examples and then asks for the definition of a new word
few_shot_prompt = PromptTemplate(
    input_variables=["word"],
    template="""
You are a helpful dictionary assistant.
Here are examples:
Word: apple
Definition: A round fruit that is usually red, green, or yellow.

Word: cat
Definition: A small domesticated carnivorous mammal with soft fur.

Now define the word '{word}'.
"""
)

# Step 3: Generate Definition for a New Word
# Fill the template with the word "dog"
definition = few_shot_prompt.format(word="dog")

# Step 4: Display the Generated Definition
print(definition)


"""
Sample Output:
You are a helpful dictionary assistant.
Here are examples:
Word: apple
Definition: A round fruit that is usually red, green, or yellow.

Word: cat
Definition: A small domesticated carnivorous mammal with soft fur.

Now define the word 'dog'.
Definition: A domesticated mammal related to wolves, often kept as a pet or used for work.
"""

"""
How the Code Works:
1. We create a PromptTemplate object that includes a few examples of word definitions.
2. The template contains a placeholder {word} for the new word to define.
3. Using the .format() method, we replace {word} with the actual word we want a definition for.
4. The few-shot approach guides the model by showing examples before requesting the new output.
5. The result is a dictionary-style definition for the specified word.
"""
