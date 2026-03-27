import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
import subprocess

# Load environment variables
load_dotenv()

# Check for GOOGLE_API_KEY
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY is not set. Please set it in your environment variables.")

# Configure the explicit Gemini object (as requested) for documentation and for optional direct usage.
# CrewAI agent llm is set by model name string, based on this configuration.
chat_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# LLM name used by CrewAI
llm_name = "gemini-1.5-flash"

# Define Agents
architect = Agent(
    role="Low-Level Systems Architect",
    goal="Design ultra-efficient backend systems focusing on performance and compression.",
    backstory="Expert in Rust, Go, Memory optimization, Semantic compression.",
    llm=llm_name,
    verbose=True
)

auditor = Agent(
    role="Security Auditor (Memory Safety Specialist)",
    goal="Critically analyze system design and identify security flaws.",
    backstory="Expert in Memory safety, Race conditions, Vulnerability detection. Highly critical, skeptical, detail-oriented.",
    llm=llm_name,
    verbose=True
)

# Define Tasks
design_task = Task(
    description="Design a detailed backend architecture for a high-performance system that handles large-scale data processing with emphasis on memory efficiency and semantic compression.",
    agent=architect,
    expected_output="Detailed backend architecture design including technology choices, data flow, and optimization strategies."
)

audit_task = Task(
    description="Perform a deep security audit on the provided system design, identifying potential vulnerabilities, race conditions, and memory safety issues.",
    agent=auditor,
    expected_output="Deep audit report with identified vulnerabilities, risk assessments, and mitigation recommendations."
)

# Create Crew
crew = Crew(
    agents=[architect, auditor],
    tasks=[design_task, audit_task],
    verbose=True
)

# Run the crew
result = crew.kickoff()

# Print final result
print("=== FINAL RESULT ===")
print(result)

# Auto Git Automation
def run_git():
    try:
        print("Running git add .")
        subprocess.run(["git", "add", "."], check=True)
        print("Running git commit")
        subprocess.run(["git", "commit", "-m", "Auto update from CrewAI execution"], check=True)
        print("Running git push")
        subprocess.run(["git", "push"], check=True)
        print("Git operations completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")

run_git()