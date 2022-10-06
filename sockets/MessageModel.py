class MessageModel:
    def __init__(self, pa_from_user, pa_to_user, pa_text, pa_action) -> None:
        self.pa_from_user = pa_from_user
        self.pa_to_user = pa_to_user
        self.pa_text = pa_text
        self.pa_action = pa_action
        pass

    @staticmethod
    def from_json(obj):
        return MessageModel(obj["from_user"],obj["to_user"],obj["text"],obj["action"])