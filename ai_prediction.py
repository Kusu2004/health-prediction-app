import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def predict_health(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Patient Data:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Predict a possible health risk in one sentence.
    """

    response = model.generate_content(prompt)

    return response.text
