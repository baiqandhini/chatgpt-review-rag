import streamlit as st
from rag import answer_question

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="ChatGPT Review Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1100px;
}

h1{
    color:#202123;
}

.metric-card{
    background:white;
    border-radius:16px;
    padding:20px;
    text-align:center;
    box-shadow:0 2px 12px rgba(0,0,0,.08);
}

.answer-box{
    background:#ffffff;
    padding:22px;
    border-radius:15px;
    border-left:6px solid #10a37f;
    box-shadow:0 2px 12px rgba(0,0,0,.08);
}

.reference-box{
    background:#ffffff;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 10px rgba(0,0,0,.06);
    margin-bottom:10px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.title("🤖 ChatGPT Review Assistant")

st.markdown(
"""
### AI-powered Retrieval-Augmented Generation (RAG)

This application retrieves the most relevant **ChatGPT user reviews**
using semantic similarity and generates answers using **Google Gemini**.

The generated responses are based **only on the retrieved reviews**.
"""
)

st.divider()

# ==========================================================
# STATISTICS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
    """
    <div class="metric-card">
        <h2>100,000+</h2>
        <p>Reviews</p>
    </div>
    """,
    unsafe_allow_html=True
    )

with col2:

    st.markdown(
    """
    <div class="metric-card">
        <h2>384</h2>
        <p>Embedding Dimension</p>
    </div>
    """,
    unsafe_allow_html=True
    )

with col3:

    st.markdown(
    """
    <div class="metric-card">
        <h2>Top-5</h2>
        <p>Retrieved Reviews</p>
    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")
st.divider()

# ==========================================================
# QUESTION INPUT
# ==========================================================

st.subheader("Ask a Question")

question = st.text_area(
    "",
    height=90,
    placeholder="Example: Why do users like ChatGPT?"
)

generate = st.button(
    "🚀 Generate Answer",
    use_container_width=True
)

# ==========================================================
# GENERATE ANSWER
# ==========================================================

if generate:

    if question.strip() == "":

        st.warning("Please enter a question first.")

    else:

        with st.spinner("Searching relevant reviews and generating answer..."):

            answer, references = answer_question(question)

        st.write("")
        st.subheader("Generated Answer")

        st.markdown(
            f"""
            <div class="answer-box">
            {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")
        st.subheader("Retrieved Reviews")

        for i, (_, row) in enumerate(references.iterrows(), start=1):

            with st.expander(
                f"Review {i} • Similarity {row['Similarity']:.4f}"
            ):

                c1, c2 = st.columns(2)

                with c1:
                    st.metric("Rating", f"{row['Rating']} ⭐")

                with c2:
                    st.metric("Sentiment", row["Sentiment"])

                st.markdown("**Comment**")

                st.info(row["Comment"])

        st.write("")
        st.divider()

        st.caption(
            "Answers are generated using Google Gemini based only on the retrieved reviews."
        )