import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
	load_dotenv()
	
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)

	if len(sys.argv) <= 1:
		print("Please provide a prompt in the form $ python3 main.py 'prompt'")
		sys.exit(1)
	elif len(sys.argv[1]) == 0:
		print("No prompt provided")
		sys.exit(1)
	else:
		user_prompt = sys.argv[1]
		messages = [
		types.Content(role="user", parts=[types.Part(text=user_prompt)]),
		]		
		response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
	
	if "--verbose" in sys.argv:
		print(f"User prompt: {user_prompt}")
		print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
		print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

	print(f"Response: \n{response.text}")
	
	

if __name__ == "__main__":
	main()