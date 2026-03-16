from langchain_core.tools import tool

@tool
def edit_interaction(
    interaction_id: int = None,
    hcp_name: str = None,
    topics_discussed: str = None,
    sentiment: str = None,
    follow_up: str = None,
    **kwargs
) -> dict:
    """
    Modify an existing interaction.
    Use this tool if the user wants to update or change details of an interaction.
    """
    return {
        "action": "edit_interaction",
        "data": {
            "interaction_id": interaction_id,
            "updates": {k: v for k, v in locals().items() if v is not None and k not in ["interaction_id", "kwargs"]}
        }
    }
