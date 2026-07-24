# 🚀 CareerPilot AI Agent

CareerPilot AI Agent is an AI-powered career guidance system that helps students and job seekers identify the right career path based on their education, current skills, and target role.

The application uses **LangGraph** to orchestrate multiple AI workflow nodes and **Google Gemini** through **LangChain** to perform intelligent role matching and generate personalized career recommendations.

---

## ✨ Features

- 🎯 Intelligent career role matching using Google Gemini
- 📊 Skill gap analysis
- 🛣 Personalized learning roadmap generation
- 💡 Project recommendations based on career goals
- 📄 AI-generated career report
- ⚡ Modular LangGraph workflow
- 📚 CSV-based career knowledge base

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- LangGraph
- LangChain
- Google Gemini API
- Pandas

### Frontend
- React
- Vite
- JavaScript
- Axios

### Database
- CSV Files (Career & Project Knowledge Base)

---

## 🏗 Project Structure

```
careerpilot-ai/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── nodes.py
│   │   ├── prompts.py
│   │   ├── state.py
│   │   ├── utils.py
│   │   └── graph.py
│   │
│   ├── data/
│   │   ├── career_data
