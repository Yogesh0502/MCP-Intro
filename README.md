# MCP Intro

This repository demonstrates an MCP agentic AI project that interacts with a local MCP server, fetches weather data, and saves notes.

## Overview

- **MCP Agentic AI**: This project showcases how to use an agentic AI system to interact with an MCP server, fetch weather information, and store notes.
- **Weather Notes**: The agent can fetch weather data for any city and save it to notes files.
- **Server Configuration**: The MCP server is configured via mcp.json.

## Project Structure

- main.py: Main script to interact with the MCP agent and perform actions.
- test_mcp.py: Test cases for MCP agent functionality.
- pyproject.toml, uv.lock: Project dependencies and lock file for reproducible environments.
- mcp.json: MCP server configuration file.
- mynotes.txt, another_notes.txt: Files where weather notes are saved.

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/Yogesh0502/MCP-Intro.git
cd MCP-Intro
```

### 2. Install Dependencies with uv

[uv](https://github.com/astral-sh/uv) is a fast Python package manager.  
To install dependencies, run:

```sh
uv pip install -r requirements.txt
```
Or, if using pyproject.toml:

```sh
uv pip install -r pyproject.toml
```

### 3. MCP Server Configuration

Edit mcp.json to configure your MCP server. Example:

```json
{
  "servers": {
    "hello_mcp": {
      "url": "http://127.0.0.1:8000/sse",
      "type": "http"
    }
  },
  "inputs": []
}
```

- Ensure your MCP server is running and accessible at the specified URL.

### 4. Running the Program

To run the main agentic AI script:

```sh
python main.py
```

- The agent will interact with the MCP server, fetch weather data, and save notes.
- You can customize the agent's actions in main.py.

### 5. Notes

- Weather data is saved in mynotes.txt and another_notes.txt.
- You can fetch, add, or read notes using the agent.

## Author

Yogesh0502