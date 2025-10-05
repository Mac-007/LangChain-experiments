from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

# 1. Create a local text-generation (instruction-following) pipeline
local_model = pipeline(
    "text2text-generation",         # flan-t5 uses this task, not "text-generation"
    model="google/flan-t5-small",   # tiny model (~80MB)
    max_new_tokens=100
)

# 2. Wrap the pipeline with LangChain
model = HuggingFacePipeline(pipeline=local_model)

# 3. Create a prompt template
prompt = PromptTemplate.from_template("Tell me a joke about {topic}")

# 4. Chain prompt → model
chain = prompt | model

# 5. Invoke the chain
response = chain.invoke({"topic": "cats"})

# 6. Print the model's output
print(response)
