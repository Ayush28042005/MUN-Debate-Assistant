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

    def generate_dossier(self):
        lines = [
            "=" * 60,
            f"MUN & DEBATE DOSSIER: {self.title.upper()}",
            "=" * 60,
            "",
            "--- ARGUMENTS IN FAVOR (FOR) ---"
        ]

        for_args = [arg for arg in self.arguments if arg.side.lower() == "for"]
        if for_args:
            for i, arg in enumerate(for_args, 1):
                lines.append(f"  {i}. {arg.content}")
        else:
            lines.append("  (No 'FOR' arguments added yet)")

        lines.append("")
        lines.append("--- ARGUMENTS AGAINST ---")
        against_args = [arg for arg in self.arguments if arg.side.lower() == "against"]
        if against_args:
            for i, arg in enumerate(against_args, 1):
                lines.append(f"  {i}. {arg.content}")
        else:
            lines.append("  (No 'AGAINST' arguments added yet)")

        lines.append("")
        lines.append("--- RESEARCH FACTS & EVIDENCE ---")
        if self.research_points:
            for i, rp in enumerate(self.research_points, 1):
                lines.append(f"  {i}. {rp.fact}")
                lines.append(f"     Source: {rp.source}")
        else:
            lines.append("  (No research points added yet)")

        lines.append("")
        lines.append("--- PREPARED SPEECHES ---")
        if self.speeches:
            for i, sp in enumerate(self.speeches, 1):
                lines.append(f"\n[Speech {i}: {sp.title}]")
                lines.append(f"{sp.content}")
        else:
            lines.append("  (No speeches saved yet)")

        lines.append("")
        lines.append("=" * 60)
        return "\n".join(lines)

    def __str__(self):
        return f"📋 Motion: {self.title} | Arguments: {len(self.arguments)} | Research: {len(self.research_points)} | Speeches: {len(self.speeches)}"