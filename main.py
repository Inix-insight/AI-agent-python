import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("no API key found")

client = genai.Client(api_key = api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument(
    "user_prompt", 
    type = str, 
    help = "User prompt"
    )
parser.add_argument(
    "--verbose", 
    action = "store_true", 
    help = "Enable verbose output"
    )
args = parser.parse_args()

messages = [
    types.Content(role = "user", 
    parts = [types.Part(text = args.user_prompt)])
    ]

response = client.models.generate_content(
    model = 'gemini-2.5-flash', 
    contents = messages,
    config = types.GenerateContentConfig(
        tools = [available_functions], 
        system_instruction = system_prompt
        )
    )


if response.usage_metadata is None:
    raise RuntimeError("failed API request")
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print("Response:")
function_results = []
if response.function_calls is not None:
    for function_call in response.function_calls:
        function_call_result = call_function(function_call)
        if function_call_result.parts is None:
            raise Exception("Content is None")
        if function_call_result.parts[0].function_response.response is None:
            raise Exception("No result returned.")
        function_results.append(function_call_result.parts[0])
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
else:
    print(response.text)