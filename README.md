# ai-hotel-assistant
Multilingual AI assistant for hotel customer service, built with Python and Streamlit
🤖 Soraya - AI Assistant for Hotel El Norcy
Soraya is a multilingual AI agent built with Python and Streamlit, designed to help hotel guests ask questions in English, Spanish, or French.

🧠 Powered by OpenAI (GPT-3.5)
🛎️ Use case: Customer Service Assistant for Hotel
📦 Deployed using Streamlit

Created by Stanley Norcius – Junior AI Developer

✨ Key Features
Multilingual Support: Automatically detects the user's language (English, Spanish, or French) and responds in that same language, ensuring a seamless experience for international guests.

Basic Conversational Memory: Maintains context throughout the interaction for more natural and coherent dialogues.

24/7 Availability: Provides immediate and continuous assistance to hotel guests, regardless of time zones.

Comprehensive Information: Answers questions related to hotel services, amenities, room details, facilities, schedules, and general hospitality inquiries.

🚀 How to Use
To interact with Soraya, simply:

Type your question in the input field.

Press Enter (or click outside the input field after typing).

Soraya will process your query, identify the language, and provide a relevant response based on Hotel El Norcy's information.

🛠️ Technical Details
This project leverages the following technologies:

Streamlit: For creating the interactive web user interface.

OpenAI API: Utilizes gpt-3.5-turbo for natural language understanding (NLU) and intelligent response generation.

Langdetect: For robust and automatic language detection of user inputs.

API Configuration
Your OpenAI API Key (OPENAI_API_KEY) is securely managed as a Secret within the Hugging Face Space settings. It is not exposed in the public codebase.

Deployment
This AI assistant is deployed on Hugging Face Spaces using the Streamlit SDK. All necessary dependencies are specified in the requirements.txt file.

📄 License
This project is licensed under the MIT License. For more details, please refer to the LICENSE file (if applicable).
