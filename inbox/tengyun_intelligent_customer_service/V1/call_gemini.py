import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel(model_name="gemini-1.5-pro")
response = model.generate_content("Write a story about a AI and magic")
print(response.text)
