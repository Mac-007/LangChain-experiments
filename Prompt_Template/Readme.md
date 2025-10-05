# Different types of prompt templates in LangChain

LangChain provides a structured way to manage prompts through the `PromptTemplate` class. A prompt template is a blueprint for how you interact with a language model, supporting **static text, dynamic variables, chaining, few-shot learning, and conditional logic**. Let’s explore the types of prompts you mentioned:

## **1. Static Prompt**
- A **static prompt** is a fixed string with no placeholders or no dynamic content.
- Every time it is sent to the model, the same exact text is used.
- This type of prompt is useful for repetitive tasks where the query doesn’t depend on external variables, such as asking the model to summarize a fixed paragraph or provide a definition.
- Example - [Static Prompt Code](1.static_prompt.py)


## **2. Dynamic Prompt with a Single Variable**

- A **dynamic prompt with a single variable** allows you to insert **one piece of runtime data** into the prompt.
- This makes the prompt flexible while keeping the structure simple.
- It is useful when you want the same instruction to adapt to different contexts, such as translating sentences, defining a word, or summarizing text.

## **3. Dynamic Prompt with Multiple Variables**

- A **dynamic prompt with multiple variables** includes **two or more placeholders** that are filled dynamically at runtime.
- This allows prompts to be highly customizable, adapting to complex tasks that require multiple inputs such as instructions, context, and user preferences.


## **4. Chained / Composed Prompts**

- Chained or composed prompts involve **connecting multiple prompt templates sequentially**, where the output of one template serves as input for another.
- This approach is more advanced and allows breaking complex tasks into smaller, manageable sub-tasks.

## **5. Few-shot Prompt**

- A **few-shot prompt** provides the model with **examples** to guide its behavior. This can be combined with static or dynamic variables.
- Few-shot prompting is especially effective in tasks requiring a specific style, reasoning pattern, or structured output.


## **6. Conditional / Programmatic Prompt (Advanced)**

- Conditional or programmatic prompts allow **dynamic modification of the template itself** based on runtime logic.
- Instead of a static template, you can decide which sections, examples, or instructions appear depending on certain conditions.
- This is advanced because it introduces programmatic control over the prompt structure.