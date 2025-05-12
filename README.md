# mcp-toy
Toy project to explore the MCP capability
* Following [the example here](https://modelcontextprotocol.io/quickstart/server#why-claude-for-desktop-and-not-claude-ai).

## MCP Servers
MCP servers can provide 3 main types of capabilities:
* `Resources` - File-like data that can be read by clients
* `Tools` - Functions that can be called by LLM
* `Prompts` - Pre-written templates that can help users accomplish specific tasks

Run `mcp install server.py` to load the MCP server to `Claude`, the corresponding config in `~/Library/Application\ Support/Claude/claude_desktop_config.json` will be updated. Here is an example:
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/xiangshiyin/Documents/Coding/mcp-toy/server.py"
      ]
    }
  }
}
```

## References
* Official intro [[link](https://modelcontextprotocol.io/introduction)]
  * Test MCP server on `Claude` [[link](https://modelcontextprotocol.io/quickstart/server#testing-your-server-with-claude-for-desktop)]
  * National weather service (NWS) API [[doc](https://www.weather.gov/documentation/services-web-api)]
* MCP python SDK [[link](https://github.com/modelcontextprotocol/python-sdk)]
* Stepwise tutorials
  * [[1](https://medium.com/@syed_hasan/step-by-step-guide-building-an-mcp-server-using-python-sdk-alphavantage-claude-ai-7a2bfb0c3096)]
* `uv`
  * About `pyproject.toml` [[link](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)]
  * Official doc [[link](https://docs.astral.sh/uv/getting-started/)]