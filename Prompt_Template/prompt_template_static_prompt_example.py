"""
===============================================================================
FILE: prompt_template_static_prompt_local.py

DESCRIPTION:
    Modern LangChain (0.2+) example:
    - Uses a STATIC PROMPT (no placeholders)
    - Runs a local Hugging Face model (google/flan-t5-small) with Transformers
    - Uses the new `Runnable` interface (prompt | llm), not LLMChain or run()
===============================================================================
"""

# =============================================================================
# Step 1: Imports
# =============================================================================
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline  # Updated import

# =============================================================================
# Step 2: Load Local Model with Hugging Face Transformers
# =============================================================================
local_model = pipeline(
    "text2text-generation",        # correct task for flan-t5
    model="google/flan-t5-small",  # tiny model (~80MB)
    max_new_tokens=100
)

# Wrap the pipeline for LangChain compatibility
llm = HuggingFacePipeline(pipeline=local_model)

# =============================================================================
# Step 3: Define Static Prompt
# =============================================================================
prompt_text = "Explain the concept of gravity in simple terms suitable for a 10-year-old."

prompt = PromptTemplate(
    input_variables=[],  # no variables since static
    template=prompt_text
)

# =============================================================================
# Step 4: Create Chain Using Runnable Interface
# =============================================================================
# This replaces the old LLMChain(prompt=..., llm=...)
# It creates a pipeline where the prompt feeds into the model.
chain = prompt | llm

# =============================================================================
# Step 5: Invoke the Chain
# =============================================================================
# Since there are no input variables, pass an empty dict.
response = chain.invoke({})

# =============================================================================
# Step 6: Display Result
# =============================================================================
print("=== Model Response ===")
print(response)

"""
===============================================================================
SAMPLE OUTPUT:
-------------------------------------------------------------------------------
=== Model Response ===
Gravity is a force that pulls everything toward the Earth. 
It keeps us on the ground and makes things fall when dropped.
-------------------------------------------------------------------------------

===============================================================================
HOW THIS CODE WORKS:
-------------------------------------------------------------------------------
1. Loads a local flan-t5-small model using Hugging Face's pipeline.
2. Wraps it with HuggingFacePipeline for LangChain compatibility.
3. Creates a PromptTemplate with no variables (static prompt).
4. Uses the modern Runnable syntax (prompt | llm) to build the chain.
5. Invokes the chain with an empty dict, since there are no inputs.
6. Prints the model’s response — fully offline, no API key needed.

===============================================================================
"""
