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

    prompts = {

        "summary": f"""
        Summarize this research paper.

        Provide:
        1. Overview
        2. Key Findings
        3. Conclusion

        Paper:
        {text[:15000]}
        """,

        "ideas": f"""
        You are an AI innovation expert.

        Based on this research paper, generate 5 UNIQUE project ideas.

        For each project provide:

        Project Name:
        Problem Solved:
        Features:
        Tech Stack:
        Difficulty:

        Paper:
        {text[:15000]}
        """,

        "roadmap": f"""
        Create a COMPLETE implementation roadmap.

        Include:

        1. Project Goal
        2. Dataset Required
        3. Libraries Required
        4. Development Steps
        5. Testing Phase
        6. Deployment Phase

        Paper:
        {text[:15000]}
        """,

        "gap": f"""
        Act as a research professor.

        Analyze this paper and provide:

        1. Research Gaps
        2. Existing Limitations
        3. Future Scope
        4. Suggested Improvements

        Paper:
        {text[:15000]}
        """,

        "chat": f"""
        Explain this paper like I am a final year engineering student.

        Include:

        - What problem is being solved?
        - How does the solution work?
        - Why is it important?
        - Real-world applications

        Paper:
        {text[:15000]}
        """,

        "review": f"""
        Generate a proper literature review.

        Include:

        - Objective
        - Methodology
        - Results
        - Strengths
        - Weaknesses
        - Conclusion

        Paper:
        {text[:15000]}
        """,

        "citation": f"""
        Generate citations in:

        IEEE Format

        APA Format

        MLA Format

        Based on the paper content below:

        Paper:
        {text[:15000]}
        """
    }

    response = model.generate_content(
        prompts.get(feature, prompts["summary"])
    )

    return response.text