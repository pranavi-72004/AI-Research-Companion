import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_paper(text, feature):

    print("=" * 50)
    print("FEATURE RECEIVED IN GEMINI:", feature)
    print("=" * 50)

    formatting_rule = """
    IMPORTANT:

    Return the response in CLEAN HTML format.

    Use:
    <h2> for headings
    <h3> for subheadings
    <p> for paragraphs
    <ul><li> for lists

    DO NOT use:
    *
    **
    #
    ##
    ---
    Markdown tables

    Make the response professional and easy to read.
    """

    prompts = {

        "summary": f"""
        {formatting_rule}

        Summarize this research paper.

        Include:

        Overview
        Key Findings
        Conclusion

        Paper:
        {text[:15000]}
        """,

        "ideas": f"""
        {formatting_rule}

        You are an AI innovation expert.

        Generate 5 UNIQUE project ideas.

        For each project include:

        Project Name
        Problem Solved
        Key Features
        Tech Stack
        Difficulty Level

        Paper:
        {text[:15000]}
        """,

        "roadmap": f"""
        {formatting_rule}

        Create a complete implementation roadmap.

        Include:

        Project Goal
        Dataset Required
        Libraries Required
        Development Steps
        Testing Phase
        Deployment Phase

        Paper:
        {text[:15000]}
        """,

        "gap": f"""
        {formatting_rule}

        Act as a research professor.

        Analyze this paper and provide:

        Research Gaps
        Existing Limitations
        Future Scope
        Suggested Improvements

        Paper:
        {text[:15000]}
        """,

        "chat": f"""
        {formatting_rule}

        Explain this paper like I am a final year engineering student.

        Include:

        What problem is being solved
        How the solution works
        Why it is important
        Real-world applications

        Paper:
        {text[:15000]}
        """,

        "review": f"""
        {formatting_rule}

        Generate a professional literature review.

        Include:

        Objective
        Methodology
        Results
        Strengths
        Weaknesses
        Conclusion

        Paper:
        {text[:15000]}
        """,

        "citation": f"""
        {formatting_rule}

        Generate citations in:

        IEEE Format
        APA Format
        MLA Format

        Paper:
        {text[:15000]}
        """
    }

    response = model.generate_content(
        prompts.get(feature, prompts["summary"])
    )

    return response.text