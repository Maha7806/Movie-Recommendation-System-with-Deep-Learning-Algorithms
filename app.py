import streamlit as st
from main import recommend

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Movie Recommender", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
    color: #cccccc;
}

.card {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
    background-color: rgba(255, 255, 255, 0.2);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🎬 Movie Recommender</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find movies similar to your taste 🍿</div>', unsafe_allow_html=True)

# ---------- INPUT ----------
movie_name = st.text_input("🔍 Enter a movie name")

# ---------- BUTTON ----------
if st.button("✨ Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name")
    else:
        results = recommend(movie_name)

        st.markdown("### 🎯 Top Picks For You")

        # ---------- DISPLAY AS CARDS ----------
        for movie in results:
            st.markdown(f'<div class="card">👉 {movie}</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built with ❤️ using TF-IDF & Cosine Similarity")