import streamlit as st
from research_and_blog_crew.crew import ResearchAndBlogCrew

st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("🧠 AI Research & Blog Generator")

topic = st.text_input("Enter a topic", placeholder="F1 racing, AI agents, etc.")

if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic")
    else:
        with st.spinner("Running AI agents..."):
            crew = ResearchAndBlogCrew().crew()
            result = crew.kickoff(inputs={"topic": topic})

        # ✅ FIX: extract string output
        output_text = result.raw  

        st.success("Done!")

        st.subheader("✍️ Generated Blog")
        st.markdown(output_text)

        st.download_button(
            label="⬇️ Download Blog as Markdown",
            data=output_text,
            file_name="blog_post.md",
            mime="text/markdown"
        )
