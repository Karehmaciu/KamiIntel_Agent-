
from datetime import datetime
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

VECTOR_DB_PATH = "chat_data/vector_store"

def generate_course_outline(prompt, category="general"):
    """
    Hybrid course generator:
    - Uses FAISS vector store if matches are strong
    - Falls back to Oxford-style prompt if no relevant material found
    """
    try:
        use_vector = False
        matched_docs = []
        if os.path.exists(VECTOR_DB_PATH):
            db = FAISS.load_local(
                folder_path=VECTOR_DB_PATH,
                embeddings=OpenAIEmbeddings(),
                allow_dangerous_deserialization=True
            )

            results = db.similarity_search_with_score(prompt, k=5)
            matched_docs = [doc for doc, score in results if score > 0.6]
            use_vector = bool(matched_docs)

        llm = ChatOpenAI(model_name="gpt-4", temperature=0.3)

        if use_vector:
            print(f"📄 Using {len(matched_docs)} matched documents for course generation.")
            content = "\n\n".join([doc.page_content for doc in matched_docs])
            course_prompt = f"""
You are an expert course designer. Based on the material below, generate a detailed training course outline. Include:
1. Course Title
2. Introduction
3. Learning Objectives (3–5)
4. Key Topics
5. Activities or Exercises
6. Assessment Methods

=== Source Material ===
{content}
=== End of Material ===
"""
        else:
            print("⚠️ No strong matches found. Using Oxford-level standalone prompt.")
            course_prompt = f"""
You are a top-tier academic course designer at Oxford University.
Design a full university course on the following topic: "{prompt}"

Structure the course as follows:
1. Course Title
2. Course Description
3. Learning Outcomes (5–6 measurable outcomes)
4. Weekly Modules (8–12 weeks, with a title and 2–3 bullet points each)
5. Teaching Methodology
6. Required Reading Materials (books, articles, etc.)
7. Assignments and Evaluation (quizzes, essays, presentations)
8. Target Audience and Prerequisites
9. Capstone Project (if applicable)

Ensure the tone is academic, polished, and professional.
"""

        try:
            response = llm.invoke(course_prompt)
            output_text = response.content if hasattr(response, "content") else str(response)
        except Exception as e:
            print(f"⚠️ Fallback to legacy model due to error: {e}")
            output_text = llm.call_as_llm(course_prompt)

        output_text = output_text.strip()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_category = category.replace(" ", "_").lower()
        folder_path = os.path.join("chat_data", "generated_courses", safe_category)
        os.makedirs(folder_path, exist_ok=True)

        filename = f"course_outline_{timestamp}.txt"
        filepath = os.path.join(folder_path, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(output_text)

        return {
            "content": output_text,
            "filename": filename,
            "category": category
        }

    except Exception as e:
        import traceback
        print(f"Course generation error: {traceback.format_exc()}")
        return f"❌ Error generating course outline: {e}"
