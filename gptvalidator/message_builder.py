from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str

    def to_dict(self):
        return {"role": self.role, "content": self.content}


class MessageBuilder:
    def __init__(self):
        self.messages = []

    def add_user_message(self, content: str):
        self.messages.append(Message("user", content))

    def add_system_message(self, content: str):
        self.messages.append(Message("system", content))

    def add_assistant_message(self, content: str):
        self.messages.append(Message("assistant", content))

    def get_messages(self):
        return [message.to_dict() for message in self.messages]
