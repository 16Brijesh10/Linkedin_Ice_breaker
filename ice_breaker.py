import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from third_paries import linkedin,scrape_linledin_profile
from langchain_core.output_parsers import StrOutputParser


#BASIC Template
#information = """
#Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman and U.S. special government employee, 
#best known for his key roles in Tesla, Inc., SpaceX, the Department of Government Efficiency (DOGE), and his ownership of Twitter. 
#Musk is the wealthiest individual in the world; as of February 2025, Forbes estimates his net worth to be US$397 billion.
#"""

if __name__ == '__main__':
    print("Hello, LangChain!")

    # Check if API key is set
    api_key = os.environ.get("GOOGLE_API_KEY")
    print(api_key)
    if not api_key:
        raise ValueError("API Key is missing! Set OPENAI_API_KEY as an environment variable.")

    summary_template = """
        Given the linkedin information about a person:
        {information}
        
        Please generate:
        1. A short summary.
        2. Two interesting facts about them.
        3. give him a nickename
       """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    

    # Updated method using LangChain's recommended approach
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linledin_profile(linkedin_profile_url="https://www.linkedin.com/in/amritha-srinivasan-8b8991285/")

    res = chain.invoke({"information": linkedin_data})
    
    print(res)  # Output the full response
