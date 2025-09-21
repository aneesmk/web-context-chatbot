import streamlit as st
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv(override= True)
# Configure the Gemini API key
# Make sure to set up your API key securely in your environment
gemini_api_key = os.environ.get("GEMINI_API_KEY")
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)
else:
    st.error(
        "Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")


def get_website_content(url):
    """Fetches and extracts text content from a given URL and all its internal links."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get all links from the page
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print("links", links)
        # Make links absolute
        absolute_links = [urljoin(url, link) for link in links]
        
        # Filter for links that are on the same domain
        base_domain = urlparse(url).netloc
        internal_links = [link for link in absolute_links if urlparse(link).netloc == base_domain]
        
        # Add the base url to the list of links to scrape
        all_links_to_scrape = list(set([url] + internal_links))
        print("all_links_to_scrape", all_links_to_scrape)
        all_text_content = ""
        scraped_links = []

        for link in all_links_to_scrape[:3]:
            try:
                print("scrapping from the link", link)
                page_response = requests.get(link)
                page_response.raise_for_status()
                page_soup = BeautifulSoup(page_response.content, 'html.parser')
                text_content = page_soup.body.get_text(separator=' ', strip=True)
                all_text_content += text_content + "\n\n"
                scraped_links.append(link)

            except requests.exceptions.RequestException as e:
                st.warning(f"Could not fetch content from {link}: {e}")

        return all_text_content, scraped_links
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching URL: {e}")
        return None, []


def get_gemini_response(prompt, context):
    """Generates a response from the Gemini model based on a prompt and context."""
    print("context", context)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    # Combine context and prompt for the model
    full_prompt = f"Context: {context}\n\nQuestion: {prompt}\n\nAnswer:"
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response from Gemini: {e}")
        return "Sorry, I couldn't generate a response."


def main():
    """Main function to run the Streamlit chatbot application."""
    st.set_page_config(page_title="Contextual Chatbot", page_icon="🤖")
    st.title("Chatbot with Website Context")

    # Initialize session state for conversation history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Sidebar for URL input
    with st.sidebar:
        st.header("Configuration")
        website_url = st.text_input("Enter a URL to scrape for context:")

        if st.button("Fetch and Set Context"):
            if website_url:
                with st.spinner("Scraping website..."):
                    content, scraped_links = get_website_content(website_url)
                    if content:
                        st.session_state.context = content
                        st.session_state.scraped_links = scraped_links
                        st.success("Context has been set from the URL.")
                    else:
                        st.error("Failed to retrieve content from the URL.")
            else:
                st.warning("Please enter a URL.")

    # Display context if available
    if 'context' in st.session_state:
        st.info("Context is set. You can now ask questions.")
        if 'scraped_links' in st.session_state:
            st.write("Scraped links:")
            for link in st.session_state.scraped_links:
                st.write(link)

    # Chat input from the user
    user_prompt = st.chat_input(
        "Ask a question based on the website's content:")

    if user_prompt:
        if 'context' in st.session_state:
            # Add user message to chat history
            st.session_state.chat_history.append(
                {"role": "user", "content": user_prompt})

            # Generate and display the bot's response
            with st.spinner("Generating response..."):
                bot_response = get_gemini_response(
                    user_prompt, st.session_state.context)
                st.session_state.chat_history.append(
                    {"role": "bot", "content": bot_response})
        else:
            st.warning(
                "Please set a context from a URL before asking questions.")

    # Display the conversation
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


if __name__ == "__main__":
    main()
