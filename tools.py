from crewai_tools import YoutubeChannelSearchTool

#Initialize tool to search for youtube channels
def tool_yt(channel):
    return YoutubeChannelSearchTool(youtube_channel_handle=channel)