from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

# Load environment variables
load_dotenv()


def main():

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

    # Groq LLM
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
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