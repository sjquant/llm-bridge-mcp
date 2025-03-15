# LLM Bridge MCP

LLM Bridge MCP allows AI agents to interact with multiple large language models through a standardized interface. It leverages the Message Control Protocol (MCP) to provide seamless access to different LLM providers, making it easy to switch between models or use multiple models in the same application.

## Features

- Unified interface to multiple LLM providers:
  - OpenAI (GPT models)
  - Anthropic (Claude models)
  - Google (Gemini models)
  - DeepSeek
  - ...
- Built with Pydantic AI for type safety and validation
- Supports customizable parameters like temperature and max tokens
- Provides usage tracking and metrics

## Tools

The server implements the following tool:

```
run_llm(
    prompt: str,
    model_name: KnownModelName = "openai:gpt-4o-mini",
    temperature: float = 0.7,
    max_tokens: int = 8192,
    system_prompt: str = "",
) -> LLMResponse
```

- `prompt`: The text prompt to send to the LLM
- `model_name`: Specific model to use (default: "openai:gpt-4o-mini")
- `temperature`: Controls randomness (0.0 to 1.0)
- `max_tokens`: Maximum number of tokens to generate
- `system_prompt`: Optional system prompt to guide the model's behavior

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/llm-bridge-mcp.git
cd llm-bridge-mcp
```

2. Install [uv](https://github.com/astral-sh/uv) (if not already installed):

```bash
# On macOS
brew install uv

# On Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Configuration

Create a `.env` file in the root directory with your API keys:

```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
```

## Usage

### Using with Claude Desktop or Cursor

Add a server entry to your Claude Desktop configuration file or `.cursor/mcp.json`:

```json
"mcpServers": {
  "llm-bridge": {
    "command": "uvx",
    "args": [
      "llm-bridge-mcp"
    ],
    "env": {
      "OPENAI_API_KEY": "your_openai_api_key",
      "ANTHROPIC_API_KEY": "your_anthropic_api_key",
      "GOOGLE_API_KEY": "your_google_api_key",
      "DEEPSEEK_API_KEY": "your_deepseek_api_key"
    }
  }
}
```

### Troubleshooting

#### Common Issues

##### 1. "spawn uvx ENOENT" Error

This error occurs when the system cannot find the `uvx` executable in your PATH. To resolve this:

**Solution: Use the full path to uvx**

Find the full path to your uvx executable:

```bash
# On macOS/Linux
which uvx

# On Windows
where.exe uvx
```

Then update your MCP server configuration to use the full path:

```json
"mcpServers": {
  "llm-bridge": {
    "command": "/full/path/to/uvx",  // Replace with your actual path
    "args": [
      "llm-bridge-mcp"
    ],
    "env": {
      // ... your environment variables
    }
  }
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
