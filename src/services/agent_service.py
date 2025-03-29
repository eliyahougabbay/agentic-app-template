from pydantic_ai.usage import Usage, UsageLimits

from agents.router import router_agent

DEFAULT_USAGE_LIMITS = UsageLimits(request_limit=5)


async def run_router_agent(query: str) -> dict:
    """Run the router agent with usage limits and return the result."""
    usage = Usage()
    result = await router_agent.run(query, usage=usage, usage_limits=DEFAULT_USAGE_LIMITS)
    return result.data
