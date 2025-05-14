from course_generator import generate_course_outline

test_prompt = "Introduction to Solar Energy Systems"

result = generate_course_outline(test_prompt)

if isinstance(result, dict):
    print("✅ Course generated successfully!\n")
    print("📂 Saved File:", result["filename"])
    print("📁 Category:", result["category"])
    print("\n📘 Course Content:\n")
    print(result["content"][:1500])  # preview first 1500 chars
else:
    print("❌ Error or fallback message:")
    print(result)
