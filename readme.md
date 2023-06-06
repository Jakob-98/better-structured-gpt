# Better Structured GPT with Pydantic models

Better Structured GPT is a Python library designed to provide structured outputs from the OpenAI GPT model. It uses Pydantic models to shape the text responses generated by GPT into structured data. 

## Powerful and Reliable Structured Outputs with Better Structured GPT

Here, we demonstrate a user input, the GPT output, and the final Pydantic model populated with the structured output.

**Step 1: User Input**
```python
user_prompt = "Generate a brief profile for a fictional character."
```

**Step 2: Define a Pydantic Model**
```python
from pydantic import BaseModel
from typing import List

class CharacterProfile(BaseModel):
    name: str
    age: int
    profession: str
    hobbies: List[str]
```

**Step 3: Populate the Model with Structured Output**
```python
character_profile = validator.validate_model(user_prompt, CharacterProfile)
print(character_profile)
```

**Result**
```python
name='John Doe' age=30 profession='Space Explorer' hobbies=['Astrophotography', 'Alien Languages']
```

Better Structured GPT enables you to convert unstructured GPT outputs into structured data.


## Prerequisites
This project requires Python 3.8 or newer. It makes use of the OpenAI API, so make sure to obtain your API key. This API key needs to be provided through an environment variable named `OPENAI_API_KEY`.

## Installation
You'll need Poetry, a tool for dependency management in Python projects. If you haven't installed Poetry yet, you can do so by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Once Poetry is installed, clone the repository and navigate into the project's root directory:

```
git clone https://github.com/Jakob-98/better-structured-gpt.git
cd better-structured-gpt
```

Next, use Poetry to install the project's dependencies:

```
poetry install
```

## Usage
After installing the project, you can use the `GptValidator` class to validate and structure GPT outputs. 

You first need to import the necessary classes and create an instance of `GptValidator`:

```python
from pydantic import BaseModel
from better_structured_gpt import GptValidator


validator = GptValidator()
```

Next, you can use the `validate_model` method to generate a structured output:

```python
# define your Pydantic model
class MyModel(BaseModel):
    ...

# define your user prompt
user_prompt = "Your user prompt here"

# generate and validate the GPT output
model_out = validator.validate_model(user_prompt, MyModel())
```

The `validate_model` method will return an instance of your Pydantic model, with the data structured according to the model's definition.

Please read the source code and example files for more detailed usage instructions.

## Tests

The tests currently do live calls to the OpenAI API. This is not best practice, instead I should probably add some mocking tests. TODO.

## Contributing

Contributions are welcome! Please read our [contributing guide](CONTRIBUTING.md).
