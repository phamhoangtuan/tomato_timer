Simple Tomato Timer using Python 3

# Purpose

- Improve productivity by separate focus time to many little chunks
- Practice TDD

# Installation

```
virtualenv .venv --python=python3
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

# Notes:

- By default, the timer will run 10 pomodoro phases, each phase lasts 25 minutes. Each short break phase lasts 5 minutes. Each long break phase lasts 10 minutes for every 4 pomodoro phases

# Know issues:

- <b>_simpleaudio.SimpleaudioError: Unable to start queue. -- CODE: -66681</b>: Library error that can't play sound more than 4 times. Will investigate more
