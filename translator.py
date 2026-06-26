import streamlit as st
from deep_translator import GoogleTranslator

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#4F8BF9;
}

.sub-title{
    text-align:center;
    color:#888888;
    font-size:18px;
    margin-bottom:30px;
}

.result-box{
    background-color:#1E293B;
    padding:18px;
    border-radius:12px;
    color:white;
    font-size:20px;
    border-left:5px solid #4F8BF9;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    background-color:#4F8BF9;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background-color:#2563EB;
}

footer{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------

st.markdown("<p class='main-title'>🌍 AI Language Translator</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Translate text into multiple languages instantly</p>", unsafe_allow_html=True)

# ------------------ LANGUAGES ------------------

source_languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr"
}

target_languages = {
    "Hindi": "hi",
    "Marathi": "mr",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml"
}

# ------------------ TEXT INPUT ------------------

text = st.text_area(
    "📝 Enter Text",
    height=180,
    placeholder="Type your text here..."
)

# Character Count

st.caption(f"Characters : {len(text)}")

# ------------------ LANGUAGE DROPDOWNS ------------------

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(source_languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(target_languages.keys())
    )

# ------------------ TRANSLATE ------------------

if st.button("🌐 Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        translated = GoogleTranslator(
            source=source_languages[source],
            target=target_languages[target]
        ).translate(text)

        st.success("Translation Successful!")

        st.markdown(
            f"<div class='result-box'>{translated}</div>",
            unsafe_allow_html=True
        )

        st.text_area(
            "📋 Copy Translated Text",
            translated,
            height=120
        )

# ------------------ FOOTER ------------------

st.markdown("---")
st.caption("Developed using Python • Streamlit • Deep Translator")