# 🧠 AI Research & Blog Generator  
### Multi-Agent Content Generation using CrewAI & Streamlit

A **production-ready agentic AI application** that autonomously generates **structured research reports** and **high-quality blog posts** on any user-defined topic.

The system leverages **CrewAI** for multi-agent orchestration, **LiteLLM** for LLM abstraction, and a **Streamlit frontend** to make the agents accessible to end users.

This project focuses on **real-world AI system design**, not toy demos.

---

## 🚀 Features

- **Multi-Agent Architecture**
  - Research Agent for structured analysis
  - Blog Writer Agent for narrative content creation

- **CrewAI Orchestration**
  - Sequential task execution
  - Clear separation of agent responsibilities
  - YAML-driven agent & task configuration

- **Interactive Frontend (Streamlit)**
  - Topic-based input
  - Live agent execution
  - Markdown rendering
  - One-click blog download

- **LLM Provider Agnostic**
  - Powered by LiteLLM
  - Supports Groq, OpenAI, and other providers

- **Production-Oriented Codebase**
  - `src/` layout
  - Environment-safe configuration
  - Clean execution boundaries

---

## 🏗 Architecture Overview

```
User (Browser)
   ↓
Streamlit UI
   ↓
CrewAI Orchestrator
   ↓
┌────────────────┬──────────────────┐
│ Research Agent │ Blog Writer Agent │
└────────────────┴──────────────────┘
   ↓
LLM Provider (Groq / OpenAI)
```

Each agent is **goal-driven**, autonomous, and contributes to the final output.

---

## 📁 Project Structure

```
research_and_blog_crew/
├── src/
│   ├── app.py                       # Streamlit frontend
│   └── research_and_blog_crew/
│       ├── crew.py                  # Crew & agent definitions
│       ├── main.py                  # Programmatic entrypoint
│       ├── agents.yaml              # Agent roles & goals
│       └── tasks.yaml               # Task definitions
│
├── README.md
├── .gitignore
└── .env (ignored)
```

---

## 🧠 Agent Design

### 🔍 Research Agent
- Performs structured topic exploration
- Identifies key concepts, trends, and challenges
- Produces a comprehensive analytical summary

### ✍️ Blog Writer Agent
- Converts research into engaging narrative content
- Optimized for clarity, flow, and readability
- Produces publish-ready Markdown output

Agents are **configured declaratively via YAML**, making the system easy to extend or customize.

---

## ▶️ Running Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Shaktisinhchavda/ai-research-blog-generator.git
cd ai-research-blog-generator
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
python -m pip install crewai litellm streamlit python-dotenv
```

### 4️⃣ Configure environment variables
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the frontend
```bash
cd src
python -m streamlit run app.py
```

Access the app at:
```
http://localhost:8501
```

---

## 📤 Output

- Generated blog content rendered in the UI
- Downloadable **Markdown (.md)** file
- Raw output accessible via `CrewOutput.raw`

---

## 🧪 Why This Project Matters

This repository demonstrates:

- Real **agentic AI system design**
- Practical multi-agent orchestration
- Integration of LLMs with a user-facing frontend
- Debugging real Python environment issues
- Clean, scalable application structure

This is **not a notebook demo** — it’s a **working AI application prototype**.

---

## 🔮 Future Improvements

- Hierarchical (Manager–Worker) agent structure
- Web search & retrieval tools
- Persistent agent memory
- FastAPI backend for production APIs
- Authentication & user history
- Cloud deployment (Streamlit Cloud / Docker)

---

## 📌 Notes

- API keys are never committed
- Virtual environments are excluded from version control
- LiteLLM proxy logging warnings are optional and non-blocking

---

## 📜 License

MIT License — free to use, modify, and distribute.

---


