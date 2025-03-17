from pydantic import BaseModel, Field

from mcp.server.fastmcp import FastMCP

from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName
from pydantic_ai.usage import Usage


mcp = FastMCP(
    "LLM Bridge",
    instructions="A simple MCP (Message Control Protocol) server that provides a unified interface to various LLM providers (OpenAI, Anthropic, Google, DeepSeek) using Pydantic AI.",
)


class LLMResponse(BaseModel):
    """Response from an LLM."""

    content: str
    model_name: str
    usage: Usage
    temperature: float


@mcp.tool()
async def run_llm(
    prompt: str,
    model_name: KnownModelName = Field(
        default="openai:gpt-4o-mini",
        description=f"Specific model name. Available models: {', '.join(KnownModelName.__args__)}",
    ),
    temperature: float = Field(
        default=0.7,
        description="Controls randomness (0.0 to 1.0)",
    ),
    max_tokens: int = Field(
        default=8192,
        description="Maximum number of tokens to generate",
    ),
    system_prompt: str = Field(
        default="",
        description="Optional system prompt to guide the model's behavior",
    ),
) -> str:
    """Run a prompt through an LLM and return the response."""
    agent = Agent(
        model=model_name,
        system_prompt=system_prompt,
    )
    response = await agent.run(
        prompt,
        model_settings={
            "temperature": temperature,
            "max_tokens": max_tokens,
        },
    )
    res = LLMResponse(
        content="안녕하세요",
        model_name=model_name,
        usage=response.usage(),
        temperature=temperature,
    )
    return res.model_dump_json()


def main():
    print("Starting LLM Bridge MCP server...")
    mcp.run(transport="stdio")
