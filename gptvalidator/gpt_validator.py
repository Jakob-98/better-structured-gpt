from pydantic import BaseModel
import logging
from gptvalidator.gpt_service.gpt_service import GptService
from gptvalidator.message_builder import MessageBuilder
import json

class GptValidator():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.gpt_service = GptService()
        self.NUM_RETRIES = 2

    @staticmethod
    def _initialize_message(model_json: str):
        _MASTER_PROMPT = f'''
        MASTER_PROMPT: You are a model working in a pydantic python programming context. It is crucial you listen to the OUTPUT instructions over anything else, or you will fail your task!

        OUTPUT: return valid RFC8259 compliant JSON fitting the pydantic schema. Do not wrap it in text, do not preface it with text, do not include follow-up explanations, make sure it's valid json, do not include comments. Do not include any explanations, only provide responses following this format without deviation.

        The output should conform to this pydantic json_schema:
        {model_json}
        '''

        message = MessageBuilder()
        message.add_system_message(_MASTER_PROMPT)
        return message

    @staticmethod
    def _model_to_json(model: BaseModel) -> str:
        return model.schema_json()

    @staticmethod
    def _json_to_model(model_class: type[BaseModel], json_str: str) -> BaseModel:
        return model_class.parse_raw(json_str)

    @staticmethod
    def _extract_json(json_str: str) -> str:
        try:
            json.loads(json_str)  # check if it's valid JSON
            return json_str
        except json.JSONDecodeError:
            # if it's not valid JSON, try to find the start of JSON data
            start_index = json_str.find('{')
            if start_index == -1:
                raise ValueError("No valid JSON data found in the string.")
            return json_str[start_index:]

    def validate_model(self, user_prompt: str, model: BaseModel):
        model_json = self._model_to_json(model)
        message = self._initialize_message(model_json)
        message.add_user_message(user_prompt)
        self.logger.info(message.get_messages())

        gpt_out = self.gpt_service.generate_response(message.get_messages())

        retries = 0
        while retries < self.NUM_RETRIES:
            try:
                model_out_json = self._extract_json(gpt_out)
                model_out = self._json_to_model(model, model_out_json)
                return model_out
            except Exception as e:
                self.logger.error(e)
                retries += 1
                message.add_assistant_message(gpt_out)
                message.add_user_message(
                    f"""
                    ERROR, you did not provide a valid JSON for our pydantic model. Provide a valid output JSON for this pydantic json schema: {model_json} with user prompt {user_prompt}.
                    The error message is: {e}
                    ONLY provide valid JSON as output, do NOT under any circumstance apologize. Try again.
                    """
                )
                gpt_out = self.gpt_service.generate_response(message.get_messages())
        raise BaseException()








