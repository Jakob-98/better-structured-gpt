import pytest
from unittest.mock import patch, MagicMock
from gptvalidator.gpt_service.gpt_service import GptService

def test_generate_response():
    # Mock OpenAI API response
    mock_response = {
        "choices": [
            {"message": {"content": "Hello, I am an AI assistant."}}
        ]
    }

    # Mock the openai.ChatCompletion.create method
    with patch('openai.ChatCompletion.create', return_value=mock_response) as mock_create:
        gpt_service = GptService()
        messages = [{"role": "system", "content": "I am a chatbot"}, {"role": "user", "content": "Hi"}]

        response = gpt_service.generate_response(messages)

        # Check that the API was called with the correct parameters
        mock_create.assert_called_once_with(
            model=gpt_service.model,
            messages=messages,
            temperature=gpt_service.temperature,
        )

        # Check that the response is as expected
        assert response == "Hello, I am an AI assistant."

def test_input_validation():
    gpt_service = GptService()

    # Test with non-list messages
    with pytest.raises(TypeError):
        gpt_service.generate_response("invalid input")

    # Test with list of non-dict messages
    with pytest.raises(TypeError):
        gpt_service.generate_response(["invalid", "input"])

    # Test with dict messages without 'role' or 'content'
    with pytest.raises(ValueError):
        gpt_service.generate_response([{"invalid": "input"}])

    # Test with invalid temperature
    gpt_service.temperature = -0.1
    with pytest.raises(ValueError):
        gpt_service.generate_response([{"role": "system", "content": "I am a chatbot"}])
