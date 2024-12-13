from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator
from dotenv import load_dotenv
import openai
import os

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key 
# Change environment variable name from "OPENAI_API_KEY" to the name given in 
# your .env file.
api_key = os.environ['OPENAI_API_KEY']

def main():
    # Get embedding for a word.
    print(f"APIKey: {api_key}")

if __name__ == "__main__":
    main()
