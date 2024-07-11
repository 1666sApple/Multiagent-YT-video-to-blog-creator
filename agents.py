from crewai import Agent

# blog researcher

blog_researcher = Agent(
    role = 'Blog researcher from Youtube Videos',
    goal = 'get the relevant video content for the topic{topic} from youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science, Machine Learning, Gen AI and providing suggestions to the blog content creators."
    ),
    tool = [],
    allow_delegation = True,
    delegation_cost = 0.2,
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
    tool = [],
    allow_delegation = False,
    name = 'blog_writer',
    description = 'A blog content writer',
/
)