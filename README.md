<div align="center">
  <a href="https://github.com/your-username/your-repository">
    <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fchatbot_13574333&psig=AOvVaw20-f-g-g-g-g-g-g-g-g-g-g&ust=1678886400000000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJj-g-g-g-g-g-g-g-g-g-g" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Website Content-Aware Chatbot</h3>

  <p align="center">
    A Streamlit web application that scrapes website content to create a contextual chatbot.
    <br />
    <a href="https://github.com/your-username/your-repository"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/your-username/your-repository/issues">Report Bug</a>
    ·
    <a href="https://github.com/your-username/your-repository/issues">Request Feature</a>
  </p>
</div>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-orange?style=for-the-badge&logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-green?style=for-the-badge&logo=google)
![GitHub contributors](https://img.shields.io/github/contributors/your-username/your-repository?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/your-username/your-repository?style=for-the-badge)

## About The Project

This project is a Streamlit web application that acts as a contextual chatbot. It scrapes a given website's content and uses it as a knowledge base to answer user questions. The chatbot leverages the Google Gemini API for its generative responses.

### Key Features

*   **Web Scraping:** Scrapes a website and its internal links to gather context.
*   **Contextual Chat:** Uses the scraped content as a knowledge base for the chatbot.
*   **Generative AI:** Integrates with Google's Gemini API to generate human-like responses.
*   **Streamlit Interface:** A simple and user-friendly web interface built with Streamlit.
*   **Conversation History:** Keeps track of the conversation between the user and the bot.

## How It Works

The application follows a simple workflow:

1.  **URL Input:** The user provides a website URL through the Streamlit interface.
2.  **Web Scraping:** The application scrapes the content of the provided URL and its internal links.
3.  **Context Building:** The scraped text is combined to form a context.
4.  **Chat Interaction:** The user asks questions, and the chatbot uses the context and the Google Gemini API to provide relevant answers.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

*   Python 3.8+
*   An API key for Google Gemini.

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/your-username/your-repository.git
    ```
2.  Install PIP packages
    ```sh
    pip install -r requirements.txt
    ```
3.  Create a `.env` file and add your API key
    ```
    GEMINI_API_KEY="your_gemini_api_key"
    ```

## Usage

1.  Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```
2.  Open the application in your browser (usually at `http://localhost:8501`).
3.  Enter a website URL in the sidebar and click "Fetch and Set Context".
4.  Wait for the application to scrape the website and set the context.
5.  Once the context is set, you can ask questions in the chat input box.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.