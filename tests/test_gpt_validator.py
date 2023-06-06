import pytest
from gptvalidator.gpt_validator import GptValidator
from pydantic import BaseModel
from typing import Optional, List

# Define a simple Pydantic model for testing.
class TestModel(BaseModel):
    name: str
    age: int

def test_validate_model_live_gpt():
    validator = GptValidator()

    # We will test with a simple user prompt.
    user_prompt = "Hello, I am a user named test. My age is 20"

    # Call the function to test.
    model_out = validator.validate_model(user_prompt, TestModel)

    # The GptService should return a valid TestModel object.
    # Here we're assuming that the GptService works correctly.
    assert model_out.name == "test"
    assert model_out.age == 20


class SubModel(BaseModel):
    name: str
    age: int

class ComplexModel(BaseModel):
    name: str
    age: int
    friends: Optional[List[SubModel]]


def test_validate_complex_model_live_gpt():
    validator = GptValidator()

    # We will test with a simple user prompt.
    user_prompt = "Hello, I am a user named test. My age is 20. I have two friends, one named friend1 who is 30 years old, and another named friend2 who is 40 years old."

    # Call the function to test.
    model_out = validator.validate_model(user_prompt, ComplexModel)

    # The GptService should return a valid TestModel object.
    # Here we're assuming that the GptService works correctly.
    assert model_out.name == "test"
    assert model_out.age == 20
    assert model_out.friends[0].name == "friend1"
    assert model_out.friends[0].age == 30
    assert model_out.friends[1].name == "friend2"
    assert model_out.friends[1].age == 40

