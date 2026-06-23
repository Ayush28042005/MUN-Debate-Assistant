class Speech:
    def __init__(self, title, content):
        self.title = title      # Title of the speech
        self.content = content  # Full speech text

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["content"])

    def __str__(self):
        return f"🎤 {self.title}\n{self.content}"