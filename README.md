Dependencies
* Install python 3.12
* brew install python@3.12

Install UV Package Manager
curl -LsSf https://astral.sh/uv/install.sh | sh

Create a new folder “mcpserver”
* Open a terminal window and navigate to mcpserver folder
* uv init .

Install MCP Libraries
* uv add “mcp[cli]”
  
Create main.py file with mcp tools, resources and prompts

Install the mcp server in claude desktop with following command
* uv run mcp install main.py
* Open CLaude Desktop -> Developer Settings and Check if mcp server has been added
