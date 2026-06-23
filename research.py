class ResearchPoint:
    def __init__(self, fact, source):
        self.fact = fact         # The research fact or data point
        self.source = source     # Where you got it from
    
    def to_dict(self):
        return{
            "fact":self.fact,
            "source":self.source
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["fact"], data["source"])
    
    def __str__(self):
        return f"📌{self.fact} (Source: {self.source})"