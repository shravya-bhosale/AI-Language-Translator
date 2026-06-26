import streamlit as st
from deep_translator import GoogleTranslator
import speech_recognition as sr

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

.title {
    text-align:center;
    color:#4CAF50;
    font-size:45px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:white;
    margin-bottom:20px;
}

.stButton>button {
    width:100%;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.result-box {
    background-color:#1e293b;
    padding:15px;
    border-radius:10px;
    color:white;
    font-size:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<p class="title">🌍 AI Language Translator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Translate text instantly into multiple languages</p>', unsafe_allow_html=True)

# ---------- VOICE INPUT ----------
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except:
        return ""

# ---------- LANGUAGES ----------
source_languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr"
}

target_languages = {
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Telugu": "te"
}

# ---------- TEXT INPUT ----------
text = st.text_area(
    "📝 Enter Text",
    height=150,
    placeholder="Type something here..."
)

# ---------- VOICE BUTTON ----------
if st.button("🎤 Voice Input"):
    voice_text = speech_to_text()

    if voice_text:
        text = voice_text
        st.success(f"Recognized: {voice_text}")

# ---------- LANGUAGE SELECTION ----------
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        source_languages.keys()
    )

with col2:
    target = st.selectbox(
        "Target Language",
        target_languages.keys()
    )

# ---------- CHARACTER COUNT ----------
st.caption(f"Characters: {len(text)}")

# ---------- TRANSLATE ----------
if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("Please enter text.")
    else:

        translated = GoogleTranslator(
            source=source_languages[source],
            target=target_languages[target]
        ).translate(text)

        st.success("Translation Completed!")

        st.markdown(
            f"""
            <div class="result-box">
                {translated}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.text_area(
            "Copy Translation",
            translated,
            height=120
        )