import pytest
from unittest.mock import patch, MagicMock
from gptvalidator.gpt_service.gpt_service import GptService

def test_generate_response():
    gpt_service = GptService(temperature=0)
    messages = [{"role": "system", "content": "I am a chatbot"}, {"role": "user", "content": "Hi, please return ONLY the exact string 'lorem ipsum'"}]

    response = gpt_service.generate_response(messages)

    # Check that the response is as expected
    assert response == "lorem ipsum"