# AURA AI

AURA AI is an AI-powered Health and Life Companion designed to provide personalized wellness guidance, fitness coaching, nutrition recommendations, health tracking, conversational assistance, and long-term user memory.

The platform combines Retrieval-Augmented Generation (RAG), specialized AI agents, memory management, and voice interaction to deliver context-aware and personalized user experiences.

---

# Overview

AURA AI acts as a unified personal assistant capable of:

- Understanding user goals and preferences
- Maintaining persistent user memory
- Providing nutrition and fitness recommendations
- Tracking health-related metrics
- Supporting voice-based interactions
- Retrieving information from a knowledge base using RAG
- Routing requests to specialized AI agents

---

# Core Capabilities

## User Memory System

The application stores and retrieves user-specific information including:

- Name
- Age
- Height
- Weight
- Fitness goals
- Dietary preferences
- Activity level

This enables personalized recommendations and continuity across conversations.

---

## Diet Intelligence Agent

Provides:

- Meal planning
- Nutrition guidance
- Protein recommendations
- Weight management strategies
- Calorie optimization

Example:

```text
Create a high-protein vegetarian diet plan.
```

---

## Fitness Coaching Agent

Provides:

- Personalized workout plans
- Strength training recommendations
- Fat-loss programs
- Exercise guidance
- Progressive fitness planning

Example:

```text
Generate a 4-day muscle-building workout plan.
```

---

## Health Advisory Agent

Provides:

- General wellness recommendations
- Symptom-based guidance
- Lifestyle improvement suggestions
- Preventive health insights

Example:

```text
I have a headache and mild fever.
```

---

## Life Coaching Agent

Provides:

- Goal-setting assistance
- Productivity recommendations
- Habit-building strategies
- Motivation and accountability support

Example:

```text
How can I improve consistency in my daily routine?
```

---

## Retrieval-Augmented Generation (RAG)

AURA AI integrates a Retrieval-Augmented Generation pipeline to improve response quality and domain-specific accuracy.

Workflow:

```text
User Query
      │
      ▼
Knowledge Retrieval
      │
      ▼
Relevant Context Extraction
      │
      ▼
Gemini Model Processing
      │
      ▼
Context-Aware Response
```

This architecture reduces hallucinations and enables responses grounded in available knowledge sources.

---

## Voice Interaction

The platform supports:

- Speech-to-Text
- Natural Language Processing
- Text-to-Speech Response Generation

This enables hands-free interaction with the assistant.

---

## Health Analytics

Built-in calculators include:

- Body Mass Index (BMI)
- Daily Protein Requirement
- Maintenance Calorie Estimation
- Fat-Loss Calorie Targets

---

## Progress Tracking

Users can record and monitor activities such as:

- Completed workouts
- Fitness milestones
- Goal progression

This allows AURA AI to provide adaptive recommendations based on historical progress.

---

# System Architecture

```text
Frontend (Next.js + TypeScript)
              │
              ▼
         FastAPI API Layer
              │
              ▼
        Query Routing Engine
              │
 ┌────────────┼────────────┐
 │            │            │
 ▼            ▼            ▼
Memory       RAG        AI Agents
System      Engine
                          │
                          ▼
                    Gemini Models
                          │
                          ▼
                   Final Response
```

---

# Technology Stack

## Frontend

- Next.js
- React
- TypeScript
- Axios
- CSS

## Backend

- FastAPI
- Python

## Artificial Intelligence

- Google Gemini
- Sentence Transformers
- Hugging Face Models

## Retrieval System

- FAISS
- Embedding-Based Search
- Retrieval-Augmented Generation (RAG)

## Voice Processing

- Browser Speech Recognition API
- Text-to-Speech Services

---

# Project Structure

```text
AURA_AI

├── frontend
│   ├── app
│   ├── components
│   ├── public
│   └── styles
│
├── backend
│   ├── api
│   ├── agents
│   ├── memory
│   ├── rag
│   ├── services
│   ├── utils
│   └── data
│
└── README.md
```

---

# Installation

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend Endpoint:

```text
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend Endpoint:

```text
http://localhost:3000
```

---

# Future Enhancements

- Multi-user authentication
- Persistent database-backed memory
- Health dashboard and analytics
- Wearable device integration
- Calendar and task integration
- Advanced agent orchestration
- Cloud deployment on Azure
- Real-time voice conversations
- Long-term contextual memory

---

# Author

Manoj J

AI & Analytics Engineer

Portfolio: https://manoj-j.netlify.app/

LinkedIn: https://linkedin.com/in/manoj0606

---

# License

This project is intended for educational, research, and portfolio purpose.