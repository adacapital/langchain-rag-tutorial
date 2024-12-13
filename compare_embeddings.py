from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.evaluation.loading import load_evaluator
from dotenv import load_dotenv
import os

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()

def main():
    # Set OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    # Get embedding for a word
    embedding_function = OpenAIEmbeddings(
        model="text-embedding-ada-002",  # Specify the embedding model
        openai_api_key=api_key
    )
    vector = embedding_function.embed_query("apple")
    print(f"Vector for 'apple': {vector}")
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words
    evaluator = load_evaluator("pairwise_embedding_distance")
    words = ("apple", "iphone")
    x = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    print(f"Comparing ({words[0]}, {words[1]}): {x}")

if __name__ == "__main__":
    main()
