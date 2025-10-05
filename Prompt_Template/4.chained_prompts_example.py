"""
Filename Suggestion: chained_prompts_example.py

Description:
This script demonstrates how to use chained or composed prompts with the PromptTemplate class.
It first generates a summary of a given text and then extracts key points from that summary.
The approach shows how multiple prompts can be linked together to perform sequential tasks.
"""

# Step 1: Import Required Libraries
# Note: Ensure you have the necessary library installed (e.g., langchain) if PromptTemplate is from it
from langchain.prompts import PromptTemplate

# Step 2: Define the Summary Prompt
# This prompt will summarize a given text in one paragraph
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in one paragraph:\n{text}"
)

# Step 3: Define the Key Points Prompt
# This prompt will extract 5 key points from a summary
key_points_prompt = PromptTemplate(
    input_variables=["summary"],
    template="List the 5 key points from the following summary:\n{summary}"
)

# Step 4: Input Text to Summarize
text_to_summarize = (
    "Recursion is a programming concept where a function calls itself "
    "to solve smaller instances of a problem."
)

# Step 5: Generate the Summary
summary = summary_prompt.format(text=text_to_summarize)  # Fill the summary prompt

# Step 6: Extract Key Points from the Summary
key_points = key_points_prompt.format(summary=summary)  # Fill the key points prompt

# Step 7: Display the Results
print("Summary:", summary)
print("Key Points:", key_points)


"""
Sample Output:
Summary: Recursion is a programming technique in which a function calls itself 
to solve smaller parts of a problem, enabling the solution of complex problems 
by breaking them down into simpler, repetitive steps.

Key Points: 
1. Recursion is a programming technique.
2. A function calls itself.
3. It solves smaller parts of a problem.
4. Helps tackle complex problems.
5. Breaks problems into simpler, repetitive steps.
"""

"""
How the Code Works:
1. Two PromptTemplate objects are created: one for summarizing text, one for extracting key points.
2. The summary_prompt is filled with the original text, generating a concise summary.
3. The key_points_prompt is then filled with the generated summary, producing a list of key points.
4. This chaining demonstrates how outputs from one prompt can serve as inputs for another, 
   enabling sequential text-processing tasks.
"""
