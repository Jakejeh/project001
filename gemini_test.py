import os
import google.generativeai as genai

# ตรวจสอบว่า API Key ถูกตั้งค่าใน Environment Variable หรือไม่
# หากคุณได้ตั้งค่าด้วย 'set GEMINI_API_KEY="YOUR_API_KEY"' ไปแล้ว
# โค้ดนี้จะดึงค่ามาใช้โดยอัตโนมัติ
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable is not set.")
    print("Please set it using: set GEMINI_API_KEY=\"YOUR_API_KEY\"")
    print("Replace YOUR_API_KEY with your actual Gemini API Key.")
    exit()

genai.configure(api_key=API_KEY)

# ทดลองเรียกดูโมเดล
print("Available Gemini Models:")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(f"- {m.name}")

# ทดลองสร้างข้อความ
try:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("เขียนประโยคสั้นๆ เกี่ยวกับ AI")
    print("\nGenerated Content:")
    print(response.text)
except Exception as e:
    print(f"\nError generating content: {e}")
    print("Please ensure you have access to 'gemini-pro' model and your API Key is valid.")