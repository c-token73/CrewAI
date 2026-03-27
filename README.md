# CrewAI Multi-Agent System

## Project Overview

This project implements a fully working AI multi-agent system using CrewAI framework with Google Gemini integration. The system features two specialized agents that collaborate on system design and security auditing tasks, demonstrating advanced agent orchestration and automated workflows.

## Features

- **Multi-Agent Architecture**: Two specialized AI agents working in sequence
- **Google Gemini Integration**: Powered by Gemini 1.5 Flash model
- **Secure Environment Handling**: Environment variable management with validation
- **Automated Git Workflow**: Automatic commit and push after execution
- **DevContainer Support**: Ready-to-use development environment
- **Production-Ready Code**: Clean architecture with error handling

## Setup Instructions

1. **Clone the repository** in GitHub Codespaces
2. **Add Google API Key**:
   - Go to Settings → Secrets → Codespaces → New Secret
   - Name: `GOOGLE_API_KEY`
   - Value: Your Google AI API key
3. **Rebuild the container** (if needed) to install dependencies
4. **Run the system**: `python main.py`

## How to Run

Execute the main script to start the multi-agent system:

```bash
python main.py
```

The system will:
1. Load environment configuration
2. Initialize AI agents with Google Gemini
3. Execute sequential tasks (Architecture Design → Security Audit)
4. Display results
5. Automatically commit and push changes to git

## Agents

### Architect Agent
- **Role**: Low-Level Systems Architect
- **Expertise**: Rust, Go, Memory optimization, Semantic compression
- **Goal**: Design ultra-efficient backend systems

### Senior Auditor Agent
- **Role**: Security Auditor (Memory Safety Specialist)
- **Expertise**: Memory safety, Race conditions, Vulnerability detection
- **Goal**: Identify security flaws in system designs

## Dependencies

- crewai
- langchain-google-genai
- python-dotenv
- gitpython

All dependencies are automatically installed via the devcontainer post-create command.