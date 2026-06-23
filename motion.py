from argument import Argument
from research import ResearchPoint
from speech import Speech

class Motion:
    def __init__(self, title):
        self.title = title                  # Motion topic
        self.arguments = []                 # List of Argument objects
        self.research_points = []           # List of ResearchPoint objects
        self.speeches = []                  # List of Speech objects

    def add_argument(self, content, side):
        arg = Argument(content, side)
        self.arguments.append(arg)

    def add_research_point(self, fact, source):
        rp = ResearchPoint(fact, source)
        self.research_points.append(rp)

    def add_speech(self, title, content):
        sp = Speech(title, content)
        self.speeches.append(sp)

    def to_dict(self):
        return {
            "title": self.title,
            "arguments": [arg.to_dict() for arg in self.arguments],
            "research_points": [rp.to_dict() for rp in self.research_points],
            "speeches": [sp.to_dict() for sp in self.speeches]
        }

    @classmethod
    def from_dict(cls, data):
        motion = cls(data["title"])
        motion.arguments = [Argument.from_dict(a) for a in data["arguments"]]
        motion.research_points = [ResearchPoint.from_dict(r) for r in data["research_points"]]
        motion.speeches = [Speech.from_dict(s) for s in data["speeches"]]
        return motion

    def __str__(self):
        return f"📋 Motion: {self.title} | Arguments: {len(self.arguments)} | Research: {len(self.research_points)} | Speeches: {len(self.speeches)}"