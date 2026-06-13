# from src.tools.cve import SearchCVETool
# from src.tools.papers import SearchPapersTool
# from src.tools.news import FetchSecurityNewsTool
# from src.tools.scraper import SummarizeURLTool
from src.tools.base import Tool

# TOOL_REGISTRY = {
#     "search_cve" : SearchCVETool,
#     "search_papers" : SearchPapersTool,
#     "fetch_security_news" : SearchNewsTool,
#     "summarize_url" : SummarizeURLTool

# }


class EchoTool(Tool):
    def execute(self, **kwargs) -> dict:
        return {"echo": kwargs}

TOOL_REGISTRY = {

    "echo_tool": EchoTool
}

def dispatch(tool_name, args) -> dict:

    if (tool_name not in TOOL_REGISTRY):
        return {"error": "Tool not found"}
        
    try:
        tool = TOOL_REGISTRY[tool_name]()
        return tool.execute(**args)
    except Exception as e:
        return {"error": str(e)}



