import streamlit as st
from openai import OpenAI
from langdetect import detect
import os
import time # To simulate typing indicator

# --- Application Visual Configuration ---
st.set_page_config(
    page_title="Soraya - AI El Norcy Hotel Assistant",
    page_icon="🏨", # Hotel icon
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- OpenAI API Configuration ---
# Retrieving API key from Hugging Face environment secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Conversation Memory Initialization ---
# Conversation memory is stored in st.session_state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial welcome message for a better user experience
    st.session_state.messages.append({"role": "assistant", "content": "Bonjour ! Je suis Soraya, votre assistante IA multilingue de l'Hôtel El Norcy. Comment puis-je vous aider aujourd'hui ?"})

# --- Custom CSS Styles for Improved UI ---
st.markdown("""
    <style>
        /* Main container */
        .stApp {
            background-color: #f7f9fc; /* Light background color */
            font-family: 'Inter', sans-serif;
        }

        /* Titles */
        h1, h2, h3, h4, h5, h6 {
            color: #2c3e50;
            font-weight: bold;
        }

        /* Application header */
        .title {
            font-size: 38px; /* Larger */
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 5px;
            text-align: center;
        }
        .subtitle {
            font-size: 20px; /* Slightly larger */
            color: #7f8c8d;
            margin-bottom: 30px; /* More space */
            text-align: center;
        }

        /* Chat bubble styling */
        .chat-container {
            max-height: 500px; /* Fixed height for scrolling */
            overflow-y: auto; /* Enables vertical scrolling */
            padding-right: 10px; /* Space for scrollbar */
            margin-bottom: 20px;
            border: 1px solid #e0e0e0; /* Light border */
            border-radius: 12px; /* Rounded corners */
            background-color: white; /* White background for chat container */
            padding: 15px;
        }

        /* User bubbles */
        .stChatMessage.user {
            background-color: #e0f2f7; /* Light blue for user */
            border-radius: 15px 15px 5px 15px; /* Custom rounded corners */
            padding: 12px 18px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Light shadow */
            margin-left: 20%; /* Offset for alignment */
        }
        /* Assistant bubbles */
        .stChatMessage.assistant {
            background-color: #f0f0f0; /* Light gray for assistant */
            border-radius: 15px 15px 15px 5px; /* Custom rounded corners */
            padding: 12px 18px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Light shadow */
            margin-right: 20%; /* Offset for alignment */
        }
        /* The st-emotion-cache-1c7y2qn class was for trying to directly style the avatar via CSS
           when the avatar parameter was used with emojis.
           Since we are now adding the emoji directly to the st.write content,
           this CSS is no longer needed and can be removed or ignored.
           For general chat message styling, it's still useful.
        */
        .st-emotion-cache-1c7y2qn {
            font-size: 24px;
            line-height: 1;
            margin-right: 10px;
        }

        /* Input field */
        .stTextInput > div > div > input {
            border-radius: 25px; /* Very rounded corners */
            padding: 12px 20px;
            border: 1px solid #bdc3c7;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08); /* More pronounced shadow */
        }

        /* Buttons */
        .stButton button {
            background-color: #3498db; /* Primary blue color */
            color: white;
            border-radius: 25px; /* Very rounded corners */
            padding: 10px 20px;
            font-weight: bold;
            border: none;
            transition: background-color 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .stButton button:hover {
            background-color: #2980b9; /* Darker blue on hover */
        }
    </style>
""", unsafe_allow_html=True)

# --- Application Header ---
st.markdown('<div class="title">🏨 Welcome to Hotel El Norcy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">I am Soraya, your multilingual AI assistant! 🌍</div>', unsafe_allow_html=True)

# --- Conversation Display ---
# Using a container for the conversation to make it scrollable
with st.container(height=400, border=True):
    for message in st.session_state.messages:
        # Determine avatar emoji based on role
        avatar_emoji = "🧑‍💬" if message["role"] == "user" else "🤖"
        # Display chat message without using the avatar parameter for emojis
        # Instead, prefix the emoji directly to the message content
        with st.chat_message(message["role"]): # Removed avatar=avatar
            st.write(f"{avatar_emoji} {message['content']}")

# --- User Input Field ---
user_input = st.chat_input("💬 Ask your question here...", key="user_input_field")

# --- Example Question Buttons ---
st.markdown("---")
st.markdown("##### 💡 Frequently Asked Questions:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Free Wifi?"):
        # Set user_input with the button text and trigger rerun
        st.session_state.messages.append({"role": "user", "content": "Do you have free Wi-Fi?"})
        st.rerun()
with col2:
    if st.button("Breakfast time?"):
        # Set user_input with the button text and trigger rerun
        st.session_state.messages.append({"role": "user", "content": "What time is breakfast?"})
        st.rerun()
with col3:
    if st.button("Pool available?"):
        # Set user_input with the button text and trigger rerun
        st.session_state.messages.append({"role": "user", "content": "Is the pool available?"})
        st.rerun()

# --- User Message Processing Logic ---
if user_input:
    # Language detection
    try:
        language = detect(user_input)
    except:
        language = "en" # Default language if detection fails

    # Add user message to session and display it immediately
    # We already added the user message when the button was pressed or chat_input was used,
    # so we only need to handle the display for the chat_input here to avoid duplication
    # if it's not coming from a button.
    # The st.chat_input already adds the message, so we just display it.
    # This logic is slightly adjusted to handle both chat_input and button clicks
    # consistently.
    if st.session_state.messages[-1]["content"] != user_input or st.session_state.messages[-1]["role"] != "user":
        st.session_state.messages.append({"role": "user", "content": user_input})

    # Assistant typing indicator
    with st.chat_message("assistant"): # Removed avatar=avatar
        with st.spinner("Soraya is typing..."):
            # Prepare messages for OpenAI API
            # Include full session history for conversational memory
            messages_for_openai = [
                {"role": "system", "content": "You are Soraya, a helpful multilingual AI assistant for Hotel El Norcy. Answer questions about hotel services, amenities, and general hospitality inquiries in the language the user speaks. Be concise and helpful."}
            ]
            # Add existing messages (including initial welcome message and previous messages)
            messages_for_openai.extend([
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ])

            # AI Response Generation
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo", # You can adjust the model if needed
                    messages=messages_for_openai,
                    temperature=0.7, # Controls response creativity
                    max_tokens=150 # Limits response length
                )
                assistant_reply = response.choices[0].message.content
                # Simulate a small delay for the typing indicator to be visible
                time.sleep(0.5)
                # Display assistant's reply prefixed with its emoji
                st.write(f"🤖 {assistant_reply}")

            except Exception as e:
                assistant_reply = f"Sorry, an error occurred during communication. Please try again later. ({str(e)})"
                st.error("Error generating response. Check your API key and connection.")
                # Display error message in chat prefixed with assistant's emoji
                st.write(f"🤖 {assistant_reply}")

            # Add AI response to session
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

# --- Clear Conversation Button ---
st.markdown("---")
if st.button("🔄 Clear conversation"):
    st.session_state.messages = [] # Resets history
    st.session_state.messages.append({"role": "assistant", "content": "Bonjour ! Je suis Soraya, votre assistante IA multilingue de l'Hôtel El Norcy. Comment puis-je vous aider aujourd'hui ?"})
    st.experimental_rerun() # Refreshes the app to show empty history

# --- Footer ---
st.markdown("---")
st.markdown("🔐 AI agent powered by OpenAI | Created by **Stanley Norcius**, CEO of Noraxis")
st.markdown("<p style='text-align: center; color: #a0a0a0; font-size: 12px;'><i>Note: This assistant is a demo project and may not have access to real-time hotel information.</i></p>", unsafe_allow_html=True)
