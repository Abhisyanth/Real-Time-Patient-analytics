# Patient Analytics Pro

AI-Driven ICU Performance & Clinical Insights Dashboard
Patient Analytics Pro is a real-time data application designed for healthcare administrators and clinicians. It transforms raw ICU dataset records into actionable insights by combining high-speed data processing with Llama 3.3-70B via the Groq API.

Live App: https://patientanalytics-app-abhisyanth.streamlit.app/

## Key Features

Dynamic ICU Analysis: Instantly filter through over 91,000 patient records by ICU department.

Real-Time KPIs: Live calculation of Mortality Rates, Patient Volume, and Average Wait Times (LOS).

AI Clinical Assistant: A built-in chatbot powered by Llama 3.3 that "sees" your filtered data and provides data-driven recommendations.

Intelligent Session Memory: The AI maintains conversation history, allowing for follow-up questions and deep-dive analysis.

High-Performance Backend: Powered by Groq for near-instant inference and Pandas for efficient data manipulation.

## The Tech Stack

Frontend: Streamlit (Interactive Web UI)

Intelligence: Groq Cloud (Llama-3.3-70b-versatile)

Orchestration: LangChain

Data Handling: Pandas

Environment: Python 3.x with python-dotenv for secure API management.

## Dashboard Preview

Interface Highlights:

Sidebar Controls: Switch between ICU types (Med-Surg, CCU, etc.) to update the entire dashboard.

Metric Cards: High-level clinical summaries.

AI Chat: Context-aware conversations with a "Clear History" function for focused analysis.

## Installation & Setup

1. Clone the Repository:

Bash
git clone https://github.com/Abhisyanth/Real-Time-Patient-analytics.git
cd Real-Time-Patient-analytics

2. Install Dependencies:

pip install streamlit pandas langchain-groq python-dotenv

3. Configuration:
Create a .env file in the root directory and add your API key:

Code snippet
GROQ_API_KEY=your_actual_key_here

4. Run the App:

Bash
python -m streamlit run app.py

## Security Note

This project uses .gitignore to ensure that sensitive environment variables (.env) and large datasets are never pushed to the public repository.

## 👤 Author
Abhisyanth
