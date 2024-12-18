# CompetitorAnalyst Crew

Welcome to the CompetitorAnalyst Crew project, powered by crewAI! This project serves as a robust template to set up a multi-agent AI system effortlessly, leveraging crewAI's powerful and flexible framework. The goal is to enable seamless collaboration among AI agents to tackle complex tasks, maximizing their collective intelligence and efficiency.

## Installation
Ensure your system has Python version >=3.10 and <=3.13 installed. This project uses UV for dependency and package management, ensuring a smooth setup process.

## Step 1: Install UV
If UV is not already installed, run the following command:
First, if you haven't already, install uv:

```bash
pip install uv
```
## Step 2: Install Project Dependencies
Navigate to the project directory and install the required packages:
```bash
pip install -r requirements.txt
```
## Step 3: Download the Ollama Model
Download the necessary Ollama model locally:

```bash
ollama pull llama3.2:3b
```
## Customization
Set Your API Key
Add your OPENAI_API_KEY to the .env file located in the root directory.

## Modify Configuration
- Agents Configuration: Customize src/competitor_analyst/config/agents.yaml to define your agents' roles, goals, and tools.
- Tasks Configuration: Update src/competitor_analyst/config/tasks.yaml to define the tasks your agents will execute.
- Crew Logic: Extend or modify the logic in src/competitor_analyst/crew.py to include additional tools, logic, or specific arguments.
- Main Workflow: Customize src/competitor_analyst/main.py to adjust input parameters or overall task flow for your agents.

## Running the Project
Launch your AI agents and start task execution with a single command:

```bash
$ python main.py
```

## Understanding Your Crew
The CompetitorAnalyst Crew comprises multiple AI agents, each assigned unique roles, goals, and tools. These agents work collaboratively to execute a sequence of tasks defined in config/tasks.yaml. The config/agents.yaml file specifies each agent's capabilities and configuration. Together, they combine their skills and insights to achieve complex objectives efficiently.


