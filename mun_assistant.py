import json
from motion import Motion

class MUNAssistant:
    def __init__(self, filename="data.json"):
        self.filename = filename            # JSON file name
        self.motions = []                   # List of Motion objects
        self.load_data()                    # Load existing data on startup

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.motions = [Motion.from_dict(m) for m in data["motions"]]
        except (FileNotFoundError, json.JSONDecodeError):
            self.motions = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({"motions": [m.to_dict() for m in self.motions]}, f, indent=4)

    def add_motion(self, title):              
        if self.get_motion(title):
            print(f"❌ Motion '{title}' already exists!")
            return
        motion = Motion(title)
        self.motions.append(motion)
        self.save_data()
        print(f"✅ Motion '{title}' added successfully!")

    def get_motion(self, title):
        for motion in self.motions:
            if motion.title.lower() == title.lower():
                return motion
        return None

    def view_all_motions(self):
        if not self.motions:
            print("❌ No motions found!")
            return
        print("\n=== All Motions ===")
        for i, motion in enumerate(self.motions, 1):
            print(f"{i}. {motion}")

    def add_argument(self, title, content, side):
        motion = self.get_motion(title)
        if motion:
            motion.add_argument(content, side)
            self.save_data()
            print(f"✅ Argument added to '{title}'!")
        else:
            print(f"❌ Motion '{title}' not found!")

    def add_research_point(self, title, fact, source):
        motion = self.get_motion(title)
        if motion:
            motion.add_research_point(fact, source)
            self.save_data()
            print(f"✅ Research point added to '{title}'!")
        else:
            print(f"❌ Motion '{title}' not found!")

    def add_speech(self, title, speech_title, content):
        motion = self.get_motion(title)
        if motion:
            motion.add_speech(speech_title, content)
            self.save_data()
            print(f"✅ Speech added to '{title}'!")
        else:
            print(f"❌ Motion '{title}' not found!")

    def view_motion_details(self, title):
        motion = self.get_motion(title)
        if not motion:
            print(f"❌ Motion '{title}' not found!")
            return
        print(f"\n=== {motion.title} ===")
        print("\n-- Arguments --")
        for arg in motion.arguments:
            print(arg)
        print("\n-- Research Points --")
        for rp in motion.research_points:
            print(rp)
        print("\n-- Speeches --")
        for sp in motion.speeches:
            print(sp)