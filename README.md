# MUN & Debate Preparation Assistant

A Python-based command-line application designed to help students prepare for Model United Nations (MUN) and debate competitions by organizing motions, arguments, research points and speeches - all in one place.

---

## Features

- Add debate motions/topics
- Store arguments for and against each motion
- Save research points with their sources
- Write and save speeches for each motion
- View all motions at a glance
- View detailed information for any motion
- Persistent storage using JSON - data is never lost
- Duplicate motion prevention

---

## 🧠 OOP Concepts Used

| Concept | Where Used |
|---|---|
| Classes & Objects | Argument, ResearchPoint, Speech, Motion, MUNAssistant |
| Constructors | Every class uses `__init__` to initialize data |
| Encapsulation | All data stored inside class attributes |
| Composition | Motion class contains Argument, ResearchPoint and Speech objects |
| Abstraction | MUNAssistant hides all file handling and data logic |
| Single Responsibility | Each class and file has one clear job |

---

## Project Structure

```
MUN-Debate-Assistant/
│
├── argument.py        → Argument class
├── research.py        → ResearchPoint class
├── speech.py          → Speech class
├── motion.py          → Motion class
├── mun_assistant.py   → MUNAssistant class
├── main.py            → Entry point and menu
└── data.json          → Persistent JSON data storage
```

---

## 🚀 How To Run

```bash
python main.py
```

No external libraries required. Just Python 3.x!

---

## 👨‍💻 Author

**Ayush Saini**

