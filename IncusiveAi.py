# ✅ Install Gemini SDK
!pip install -q google-generativeai

# ✅ Configure Gemini Free API
import google.generativeai as genai
genai.configure(api_key="Your-Api-Key")  # replace with your key

# ✅ Use chat-bison-001 (free-tier friendly)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# ✅ Prepare prompt for inclusive rewriting
def rewrite_inclusive_jd(original_text):
    prompt = (
        "Rewrite this job description in a more inclusive, bias-free, and neurodivergent-friendly way:\n\n"
        f"{original_text}\n\nInclusive Version:"
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

# ✅ Input multi-line JD
print("📝 Paste your job description. Press Enter twice to finish:\n")
lines = []
while True:
    line = input()
    if not line.strip():
        break
    lines.append(line)

jd_input = "\n".join(lines)

# ✅ Generate and print inclusive rewrite
inclusive_version = rewrite_inclusive_jd(jd_input)
print("\n✅ Inclusive Job Description:\n")
print(inclusive_version)