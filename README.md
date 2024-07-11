# Multiagent YouTube Video to Blog Creator

This project uses CrewAI to create a multiagent system that generates blog content from YouTube videos. It focuses on AI, Data Science, Machine Learning, and Gen AI topics from the Veritasium YouTube channel.

## Features

- Utilizes two AI agents: a Blog Researcher and a Blog Writer
- Searches YouTube videos using the Veritasium channel
- Generates detailed blog posts based on video content
- Uses Ollama with the Llama 2 model for language processing

## Prerequisites

- Python 3.x
- Ollama running locally
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/1666sApple/Multiagent-YT-video-to-blog-creator.git
cd Multiagent-YT-video-to-blog-creator
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Ensure Ollama is running locally on `http://localhost:11434`

## Usage

1. Run the main script:

```bash
python crew.py
```

2. The script will generate a blog post about "The Terrifying Real Science Of Avalanches" based on a Veritasium video.

3. The output will be saved in a Markdown file named `blog_post_The Terrifying Real Science Of Avalanches.md`.

* Note: The script will take a few minutes to run. *

* Note: If you want, you can modify the script to use a different topic. Simply go to `crew.py` and change the `topic` parameter in the `crew.kickoff()` method. *

## Structure

- `agents.py`: Defines the Blog Researcher and Blog Writer agents
- `tasks.py`: Defines the research and writing tasks
- `tools.py`: Contains the YouTube channel search tool
- `crew.py`: Crew script to run the CrewAI process

## Customization

- To change the topic, modify the `topic` parameter in the `crew.kickoff()` method in `crew.py`
- To use a different YouTube channel, update the `channel` parameter in the `tool_yt()` function calls

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
