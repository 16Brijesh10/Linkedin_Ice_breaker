import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain.agents import(
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

from tools.tools import get_profile_url_tavily

load_dotenv()

def lookup(name: str) -> str:
    llm =  ChatGoogleGenerativeAI(
        temperature=0,
        model="gemini-1.5-pro",
    )
    template= """give the full name {name_of_the_person} i want you to get it me link to their Linkedin profile page.
    Your answer should contain only a URL"""
    
    prompt_template=PromptTemplate(
        
        template=template,input_variables=['name_of_the_person']
    )
    
    tools_for_agent=[
        Tool(
        name="crawl google 4 Linkedin profile Page",
        func=get_profile_url_tavily,
        description="useful for when you need get the Linkedin Page URL"
        )
    ]
    react_promt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_promt)
    
    agent_executor=AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)
    
    result = agent_executor.invoke( 
           
            input={"input": prompt_template.format_prompt(name_of_the_person=name)}
    
    )
    linkedin_profile_url=result["output"]
    
    return linkedin_profile_url

if __name__ == "__main__":
    
    linkedin_url = lookup(name="BRIJESH A")

    