

TOOLS = [
    {
        "type":"function",
        "function": {
            "name": "search_cve",
            "description":"Search the NIST NVD database for CVEs when the user asks about vulnerabilities, security flaws, or exploits for a specific product or keyword",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "keyword": {
                        "type": "string",
                        "description": "Product name or technology to search CVEs for e.g. Apache, OpenSSL, log4j"
                    },
                    "severity": {
                        "type": "string",
                        "description": "Filter by severity level",
                        "enum": ["low", "medium", "high", "critical"]
                    },
                    "days_back": {
                        "type": "integer",
                        "description": "How many days back to search, default is 30"
                    },
                    "cve_id": {
                        "type": "string",
                        "description": "Specific CVE ID to look up e.g. CVE-2024-1234"
                    }
                }
            },
            "required": []

        }

    },

    {
        "type":"function",
        "function": {
            "name" : "search_papers",
            "description":"Search the arXiv for research papers when user ask about any kind of research paper on topics such vulnerabilities, security flaws, or exploits for a specific product or keyword",
            "parameters" : {
               "type" : "object",
                "properties" : {
                    "keyword": {
                        "type": "string",
                        "description": "Product name or technology to search research papers on for e.g. LLM, fuzzing, Cloud, Web Application"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Number of papers to return, default is 5"
                    }

                } 
            },
            "required": []

        }

    },

{
    "type": "function",
    "function": {
        "name": "fetch_security_news",
        "description": "Fetch latest cybersecurity and AppSec news from RSS feeds when the user asks about recent news, latest threats, or current events in security",
        "parameters": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "News source to fetch from",
                    "enum": ["hackernews", "bleepingcomputer", "krebs", "reddit_netsec", "reddit_appsec", "tldr_sec", "all"]
                },
                "max_items": {
                    "type": "integer",
                    "description": "Number of news items to return, default is 5"
                },
                "since_hours": {
                    "type": "integer",
                    "description": "Fetch news from the last N days, default is 5"
                }
            },
            "required": []
        }
    }
},
{
    "type": "function",
    "function": {
        "name": "summarize_url",
        "description": "Fetch and summarize the content of a URL when the user shares a link or asks to read a specific article, blog post, or security advisory",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The full URL to fetch and summarize e.g. https://example.com/article"
                }
            },
            "required": ["url"]
        }
    }
},

{
    "type": "function",
    "function": {
        "name": "echo_tool",
        "description": "Echo back whatever arguments are passed to it",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "Message to echo back"
                }
            },
            "required": ["message"]
        }
    }
}


]