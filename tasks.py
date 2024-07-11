from crewai import Task
from tools import tool_yt
from agents import blog_researcher, blog_writer

# Research task
research_task = Task(
    description=(
       "Identify the video{topic}."
       "Get detailed information about the video from the channel" 
    ),
    expected_output=(
        "Get multiple detailed descriptive paragraphs based on the video{topic}."
    ),
    tools = [tool_yt(channel='@veritasium')],
    agent=blog_researcher,
    name='research_task',
)

# Write task
write_task = Task(
    description=(
       "Get info from the given youtube channel on the video {topic} and write a blog post about the video{topic}."
    ),
    expected_output=(
        "Write a blog post about the video{topic} based on the summarization of the video{topic}."
    ),
    tools = [tool_yt(channel='@veritasium')],
    agent=blog_writer,
    async_execution=False,
    output_file = 'blog_post_{topic}.md',
    name='write_task',
) 