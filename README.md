# Chatbot with Website Context

This is a Streamlit web application that acts as a contextual chatbot. It scrapes a given website's content and uses it as a knowledge base to answer user questions. The chatbot leverages the Google Gemini API for its generative responses.

## Description

The application provides a simple and intuitive interface where a user can input a URL. The application then scrapes the content of the provided URL and its internal links to create a context. Once the context is set, the user can ask questions, and the chatbot will provide answers based on the scraped website content.

## Features

- **Web Scraping:** Scrapes a website and its internal links to gather context.
- **Contextual Chat:** Uses the scraped content as a knowledge base for the chatbot.
- **Generative AI:** Integrates with Google's Gemini API to generate human-like responses.
- **Streamlit Interface:** A simple and user-friendly web interface built with Streamlit.
- **Conversation History:** Keeps track of the conversation between the user and the bot.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your Google Gemini API key:
    ```
    GEMINI_API_KEY="your_gemini_api_key"
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

## Usage

1.  Open the application in your browser (usually at `http://localhost:8501`).
2.  Enter a website URL in the sidebar and click "Fetch and Set Context".
3.  Wait for the application to scrape the website and set the context.
4.  Once the context is set, you can ask questions in the chat input box.
5.  The chatbot will respond based on the content of the website.