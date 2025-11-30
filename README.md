# agent-sofia
| Creating agents for better health care understanding.

By: 
- [Susan Kraemer, PhD]
- Cameron Guthrie
- Patrick Cavins, PhD

## Background 

An agentic application can have multiple users and each user may have multiple sessions with the application. To manage these sessions and events, ADK offers a Session Manager and Runner.

**SessionService: The storage layer**

Manages creation, storage, and retrieval of session data
Different implementations for different needs (memory, database, cloud)

**Runner: The orchestration layer**

Manages the flow of information between user and agent
Automatically maintains conversation history
Handles the Context Engineering behind the scenes

## Current structure
- `b4-soup-edit` - python file for parsing a full text html publication 
- `capstone-project-notebook.ipynb` - jupyter notebook that 2 different agent deployments. 
- `query-script` - python script that creates and runs the agents end - to - end
- `query-pub-med` - pythong script that query the pubmed database
-  `pubmed-univ-of-alabama.ipynb` - demo notebook created by UofAla


## Reserarch

**PUBMED MCP**
- [GITHUB](https://github.com/grll/pubmedmcp)
- [REDDIT](https://www.reddit.com/r/modelcontextprotocol/comments/1kuc03k/cyanheadspubmedmcpserver_an_mcp_server_enabling/)

**PUMBED CLIENT**
- [GITHUB](https://github.com/grll/pubmedclient)


### PUBMED API CLIENT IN PYTHON
- [University of Alabama, Library](https://ua-libraries-research-data-services.github.io/UALIB_ScholarlyAPI_Cookbook/src/python/pubmed.html)

#### Searching Based on Publication Types

We can sort by publication type by adding `AND` into the search:

```
term=<searchQuery>+AND+filter[filterType]
```

`[pt]` specifies that the filter type is publication type. More filters can be found at <a href="https://pubmed.ncbi.nlm.nih.gov/help/" target="_blank">PubMed Help</a>.