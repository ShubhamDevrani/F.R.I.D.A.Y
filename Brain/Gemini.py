import google.generativeai as genai

genai.configure(api_key="AIzaSyCjCpIyfolHDaQ8Tb9XcugG6syF85vsYxM")

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

def get_gemini_response(data):
    short_prompt = "Provide a short and concise response: " + data
    response = chat.send_message(short_prompt)
    return response.text

def Gemini(data):
    try:
        gemini_response = get_gemini_response(data)
        return gemini_response[:100] 
    except Exception as e:
        print(f"An error occurred: {e}")


# while True:
#     repeat = input("Enter: ")
#     print("\n", Gemini(repeat), "\n")
