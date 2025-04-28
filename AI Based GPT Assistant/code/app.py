
#speech based smart assistant 


'''import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import os
from apikey import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

# Text to Speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Take voice input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
    except:
        print("Sorry, I didn't catch that.")
        return "None"
    return query

# Ask Gemini and get response
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

# Main Loop
if __name__ == "__main__":
    speak("em raaa Chandu?")
    while True:
        query = take_command().lower()
        if query == "none":
            continue
        elif "bye" in query:
            speak("Goodbye!")
            break
        else:
            answer = ask_gemini(query)
            speak(answer)

models = genai.list_models()
print(models)'''



#text based voice assistant 


import streamlit as st
import google.generativeai as genai
from apikey import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

# Streamlit Page Config
st.set_page_config(page_title="Chandu's Personal Assistant", page_icon="🤖")

# Function to ask Gemini
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit Title
st.title("🧠 Chandu's AI Personal Assistant")

st.markdown("### Ask anything below:")

# Using session state to manage input clearing
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Input from user (text box)
user_input = st.text_input("You:", placeholder="Type your question here...", value=st.session_state.user_input)

# Button to submit
if st.button("Ask"):
    if user_input:
        with st.spinner('Thinking... 🤔'):
            answer = ask_gemini(user_input)
        st.success("Assistant:")
        st.write(answer)

        # Clear the input field after asking
        st.session_state.user_input = ""  # Clear the input after submission
    else:
        st.warning("Please type something to ask.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Chandu")
