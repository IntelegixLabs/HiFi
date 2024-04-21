import os
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def pan_card_extractor(image_path):
    genai.configure(api_key=GEMINI_API_KEY)
    img = PIL.Image.open(image_path)

    model = genai.GenerativeModel(model_name='gemini-pro-vision')
    prompt = """
            From the given Indian Pan card image, detect pan card number, name of the person, father's name, date of birth 
            give response in the json format 
            {
            'pan_number': {pan card number},
            'name': {name},
            'father_name': {father's name},
            'dob': {date of birth}
        }
        Do not explain what you are doing
            """
    response = model.generate_content([prompt, img])
    try:
        resp = response.text

        # # Replace "\n\n" with actual newline characters
        formatted_text = resp.replace("\\n\\n", "\n")

        start_index, end_index = 0, -1

        for i in range(0, len(formatted_text)):
            if formatted_text[i:i + 7] == "```json":
                start_index = i + 7
                break

        for i in range(len(formatted_text), -1, -1):
            if formatted_text[i:i + 3] == "```":
                end_index += i
                break

        formatted_text = formatted_text[start_index:end_index]
        return formatted_text
    except:
        return None
