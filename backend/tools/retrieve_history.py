from langchain_core.tools import tool

@tool
def retrieve_history(hcp_name: str) -> dict:
    """
    Fetch previous interactions with the same doctor.
    Use this tool when the user asks for the history of a specific doctor or HCP.
    """
    return {
        "action": "retrieve_history",
        "data": {
            "hcp_name": hcp_name
        }
    }
