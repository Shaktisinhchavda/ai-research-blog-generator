# 🧠 AI Research & Blog Generator  
### A Multi-Agent AI Application using CrewAI & Streamlit

A production-ready **agentic AI system** that autonomously generates **in-depth research reports** and **high-quality blog posts** on any user-provided topic.  
The system is powered by **CrewAI**, orchestrated through multiple specialized agents, and exposed to end users via an interactive **Streamlit frontend**.

This project demonstrates **real-world agent orchestration**, **LLM integration**, and **frontend deployment**, going beyond toy examples into practical AI application design.

---

## 🚀 Key Features

- 🧩 **Multi-Agent Architecture**
  - Dedicated **Research Agent** for structured analysis
  - Dedicated **Blog Writer Agent** for narrative content creation

- 🤖 **Agent Orchestration with CrewAI**
  - Task dependency handling
  - Sequential execution pipeline
  - Clean separation of agent responsibilities

- 🌐 **User-Facing Frontend (Streamlit)**
  - Topic input via UI
  - Real-time agent execution
  - Rendered markdown output
  - One-click blog download

- 🔌 **LLM Abstraction via LiteLLM**
  - Compatible with Groq / OpenAI / other providers
  - Environment-based configuration

- 🛠 **Production-Aware Design**
  - `src/`-based project layout
  - YAML-based agent & task configuration
  - Safe handling of secrets
  - Clear execution boundaries

---

## 🏗 System Architecture

User (Browser)
↓
Streamlit Frontend
↓
CrewAI Orchestrator
↓
┌────────────────┬──────────────────┐
│ Research Agent │ Blog Writer Agent │
└────────────────┴──────────────────┘
↓
LLM Provider (Groq / OpenAI)


Each agent is **goal-driven**, operates independently, and contributes to a shared final output.

---

## 📂 Project Structure

research_and_blog_crew/
├── src/
│ ├── app.py # Streamlit frontend
│ ├── research_and_blog_crew/
│ │ ├── crew.py # Crew & agent definitions
│ │ ├── main.py # Programmatic entrypoint
│ │ ├── agents.yaml # Agent roles & goals
│ │ └── tasks.yaml # Task definitions & outputs
│
├── .gitignore
├── README.md
└── .env (ignored)


This structure follows **industry-standard Python `src` layout** for maintainability and scalability.

---

## 🧠 Agent Design

### 🔍 Research Agent
- Performs structured topic analysis
- Identifies key concepts, trends, and challenges
- Produces a comprehensive research summary

### ✍️ Blog Writer Agent
- Converts research into an engaging narrative
- Optimized for readability and flow
- Produces publish-ready markdown content

Agents are configured **declaratively using YAML**, making the system easy to extend.

---

##  Running the Project Locally

###  Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd research_and_blog_crew

### Create & activate a virtual environment
python -m venv .venv
.venv\Scripts\activate

### Install dependencies
python -m pip install crewai litellm streamlit python-dotenv

### Configure environment variables
GROQ_API_KEY=your_api_key_here

### Run the frontend
cd src
python -m streamlit run app.py

📥 Output

Rendered blog content displayed directly in the UI

Downloadable Markdown (.md) blog file

Programmatic access via CrewOutput.raw

🧪 Why This Project Matters

This repository showcases:

✅ Practical Agentic AI system design

✅ Real-world debugging of Python environments

✅ Multi-agent orchestration using CrewAI

✅ Frontend integration with autonomous agents

✅ Clean, scalable project structure

This is not a notebook demo — it is a working AI application prototype.

🔮 Future Enhancements

Manager–Worker (Hierarchical) agent structure

Web search and retrieval tools

Persistent agent memory

FastAPI backend for production deployment

User authentication and history

Cloud deployment (Streamlit Cloud / Docker)

📌 Notes

API keys are never committed

Virtual environments are excluded from version control

LiteLLM proxy logging warnings are optional and non-blocking
