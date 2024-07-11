from crewai import Agent
from tools import tool_yt
from langchain_community.llms import Ollama
import os
os.environ['OPENAI_API_KEY'] = 'NA'

llm = Ollama(
    model = "llama2",
    base_url = "http://localhost:11434")

# blog researcher

blog_researcher = Agent(
    role = 'Blog researcher from Youtube Videos',
    goal = 'get the relevant video content for the topic{topic} from youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science, Machine Learning, Gen AI and providing suggestions to the blog content creators."
    ),
    tool = [tool_yt(channel='@veritasium')],
    allow_delegation = True,
    delegation_cost = 0.2,
    llm = llm,
    name = 'blog_researcher',
    description = 'A blog content researcher from the youtube videos',
)
 
    
    
# Blog writer

blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate the compelling points of the video{topic} to the blog content creator',
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying the complex topics, you craft engaging blog content that captivate and educate, bringing in the new discoveries to light in an accessible manner."
    ),
    tool = [tool_yt(channel='@veritasium')],
    allow_delegation = False,
    llm = llm,
    name = 'blog_writer',
    description = 'A blog content writer',
)