# note: comments here are used for understanding code and how it works.
# brackets are explaining where the information about specific code is obtainted and learned from.

# importing the required packages and specified things in them
import os # to interact with the operating system
import io
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from dotenv import load_dotenv
from google import genai
from PIL import Image #(pypi python imaging library) includes image processing capabilities 

load_dotenv() #(pypi python-dotenv) reads the environment variables from the .env file and sets them in an os.environ

app = FastAPI()

client = genai.Client() # intialize the gemini ai and reads the api key

@app.post("/analyze-item") #(gemini ai) tells the application that when a POST request is sent to the web address, to run the function below 

def process_scan(selected_category: str = Form(...), file: UploadFile = File(...)):
    '''
    process_scan takes an image (already uploaded) and asks the AI model used to match what 
    we ask it to do in the prompt and return that text to be called to the frontend.

    selected_category 		- obtained from the frontend and converted into a string,
				(Household items btn or Electronics).
    file			- the image file that the function scans and returns an 
   				output for, which matches the prompt given.

    Examples:
    process_scan(selected_category: str = Form(Electronics), file: UploadFile = File(batteries.png))
    --> "category" : Electronics, "item details" : <what the AI says to do with that item>
    '''
    try:
        image_bytes = file.file.read() #(gemini ai) takes the image (file.) we process and looks through its contents (file.read) 
        uploaded_image = Image.open(io.BytesIO(image_bytes)) # gets and reads the image file obtained from the frontend

	# mimics the function: Process_scan in psedocode
	prompt = (
    	    f"The user selected the recycling category: '{selected_category}'. "
            "Analyze this image and identify the item name, the material its made of, wheather it's recyclable,"
    	    "and provide 3 (max) clear preperation steps (like rinsing or emptying) numbered."
            "Format your response clearly so the frontend can display it."
        )

	response = client.models.generate_content(
    	    model="gemini-2.5-flash",
            contents=[prompt,uploaded_image]
        )

        return {
	    "category": selected_category,
	    "item_details": response.text
	}

    except Exception as e:
	raise HTTPException(status_code=500,detail=str(e))

