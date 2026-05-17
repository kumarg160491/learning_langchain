from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

# Load environment variables
load_dotenv()


def main():

    # Check API key
    print(os.getenv("OPENAI_API_KEY"))

    information = """
    Elon Musk is a businessman known for Tesla, SpaceX, X (Twitter),
    Neuralink, and xAI. He is one of the richest people in the world.
    """

    summary_template = """
    Given the information {information} about a person, I want you to create:

    1. A short summary
    2. Two interesting facts about them
    """

    # Prompt Template
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # OpenAI LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    # Chain
    chain = summary_prompt_template | llm

    # Invoke chain
    response = chain.invoke({"information": information})

    # Print response
    print("\nResponse:\n")
    print(response.content)


if __name__ == "__main__":
    main()