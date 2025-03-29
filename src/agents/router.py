from dataclasses import dataclass

from pydantic_ai import Agent, RunContext

from config import openai_model

ROUTER_AGENT_PROMPT = """Just be a good agent."""


@dataclass
class Deps: ...


# Main agent (named "router" because it routes queries to tools or other agents)
router_agent = Agent(
    openai_model,
    system_prompt=ROUTER_AGENT_PROMPT,
)


@router_agent.tool
async def my_tool(ctx: RunContext[Deps]): ...
