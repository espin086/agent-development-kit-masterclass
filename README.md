# Agent Development Kit Masterclass 🚀

Follow-along code for the Google Agent Development Kit (ADK) masterclass. Each numbered
folder is one step of the course, built up as the class goes. Right now there is a single
step: a minimal ADK agent defined in Python, wired to a Gemini model, with its API key read
from a local `.env` file. The repo exists as a working reference for the class, not as a
library to install.

**Class video:** [Watch the recording on YouTube](https://www.youtube.com/watch?v=P4VFL9nIaIA)

## Contents

| Folder | What it covers |
|---|---|
| `1-basic-agent/greeting_agent/` | The smallest ADK unit: a single `Agent` with a name, description, model, and instruction. `__init__.py` re-exports the module so ADK's loader can discover `root_agent`. `.env.example` shows the two environment variables the agent needs. |

More agents are planned as the course continues.

Note on the current state of `1-basic-agent/greeting_agent/agent.py`: it imports from
`google.adk.agent`, passes `description` twice, and uses `instructions`. Recent ADK releases
use `google.adk.agents` and an `instruction` argument, so the file as committed will not run
without those fixes. Left as is here since the README documents what the code contains.

## Requirements

- Python 3.11 or newer
- [Poetry](https://python-poetry.org/) for dependency management
- A Google AI Studio API key (Gemini)

Dependencies declared in `pyproject.toml`: `google-adk`, `google-generativeai`, `litellm`,
`yfinance`, `psutil`, `python-dotenv`. `yfinance` and `psutil` are pinned for agent tools
used later in the course; nothing in the current code imports them yet.

## Installation

```bash
git clone https://github.com/espin086/agent-development-kit-masterclass.git
cd agent-development-kit-masterclass
poetry install
```

## Usage

Create the agent's `.env` from the example and add your key:

```bash
cp 1-basic-agent/greeting_agent/.env.example 1-basic-agent/greeting_agent/.env
```

```
GOOGLE_GENAI_USER_VERTEXAI=FALSE
GOOGLE_API_KEY=your-key-here
```

`GOOGLE_API_KEY` comes from [Google AI Studio](https://aistudio.google.com/apikey).
Setting the Vertex flag to `FALSE` tells ADK to call the Gemini API directly instead of
going through Vertex AI. The `.env` file is gitignored.

ADK discovers agents by directory, so run its CLI from the folder that holds the agent
package:

```bash
cd 1-basic-agent
poetry run adk web        # browser UI at http://localhost:8000
poetry run adk run greeting_agent   # terminal chat
```

`adk web` lists every agent package under the current directory in a dropdown. `adk run`
takes the package name and talks to it in the terminal.

## License

No LICENSE file in this repo.
