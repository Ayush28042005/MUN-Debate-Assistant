class Argument:
    def __init__(self, content, side):
        self.content = content  # The actual argument text
        self.side = side        # "for" or "against"

    def to_dict(self):
        return {
            "content": self.content,
            "side": self.side
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["content"], data["side"])

    def __str__(self):
        return f"[{self.side.upper()}] {self.content}"