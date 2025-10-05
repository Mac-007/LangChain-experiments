"""
Filename Suggestion: conditional_prompt_example.py

Description:
This script demonstrates how to create a conditional or programmatic prompt using the 
PromptTemplate class. The prompt can optionally include an example to guide the response. 
Depending on the 'include_examples' flag, the prompt either includes or omits a sample 
question-answer pair to provide context.
"""

# Step 1: Import Required Libraries
# Note: Ensure you have the necessary library installed (e.g., langchain) if PromptTemplate is from it
from langchain.prompts import PromptTemplate

# Step 2: Define a Function to Create Conditional Prompt
def create_conditional_prompt(include_examples: bool):
    """
    Create a PromptTemplate with optional examples.
    
    Args:
        include_examples (bool): Whether to include an example question-answer pair.
        
    Returns:
        PromptTemplate: A dynamically created prompt template.
    """
    # Base template with a placeholder for the question
    base_template = "Answer the following question clearly:\n{question}"

    # Optionally add an example question-answer to guide the model
    if include_examples:
        base_template += "\nExample:\nQuestion: What is 2+2?\nAnswer: 4"

    # Return the PromptTemplate object
    return PromptTemplate(
        input_variables=["question"],
        template=base_template
    )

# Step 3: Use the Conditional Prompt
# Set include_examples=True to include the guiding example
conditional_prompt = create_conditional_prompt(include_examples=True)

# Step 4: Provide a Question and Generate the Prompt
question = "What is the capital of France?"
output = conditional_prompt.format(question=question)

# Step 5: Display the Generated Prompt
print(output)


"""
Sample Output:
Answer the following question clearly:
What is the capital of France?
Example:
Question: What is 2+2?
Answer: 4
"""

"""
How the Code Works:
1. We define a function 'create_conditional_prompt' that builds a prompt template dynamically.
2. The template always includes a placeholder for the user's question.
3. If 'include_examples' is True, an example question-answer pair is appended to guide the response.
4. The function returns a PromptTemplate object that can be filled using .format().
5. When we provide a real question, the template generates a prompt with or without the example.
"""
