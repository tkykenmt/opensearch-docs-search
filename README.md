# opensearch-docs-search

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Search OpenSearch documentation, blogs, and community forums. Available as MCP server and CLI.

> **Note**: This is an unofficial community tool and is not affiliated with or endorsed by the OpenSearch Project.

## Features

- 🔍 **Documentation Search** - Search official OpenSearch docs
- 📝 **Blog Search** - Search OpenSearch blog posts
- 💬 **Forum Search** - Search community forum posts and discussions
- 🚀 **Fast** - LRU cache for repeated queries (MCP mode only)
- 📦 **Dual Mode** - Use as MCP server or CLI (SKILL)
- 🎯 **Version Support** - Search docs for specific OpenSearch versions

## Installation

```bash
uv tool install git+https://github.com/tkykenmt/opensearch-docs-search
```

Or for development:

```bash
git clone https://github.com/tkykenmt/opensearch-docs-search.git
cd opensearch-docs-search
uv sync
```

## Usage

### CLI (SKILL mode)

```bash
opensearch-doc-search docs "k-NN"
opensearch-doc-search docs "neural search" --version 2.12 --limit 5
opensearch-doc-search blogs "performance"
opensearch-doc-search forum "cluster health"
```

### MCP Server

#### Claude Desktop / Cursor

```json
{
  "mcpServers": {
    "opensearch-docs-search": {
      "command": "opensearch-docs-search"
    }
  }
}
```

### Kiro SKILL

Add `skill/SKILL.md` path to Kiro's skill configuration.

## Tools / Commands

### search_docs / `docs`

Search OpenSearch documentation.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | (required) | Search query |
| `version` | string | "latest" | OpenSearch version |
| `limit` | integer | 10 | Max results |
| `offset` | integer | 0 | Skip N results |

### search_blogs / `blogs`

Search OpenSearch blog posts. Same parameters as `search_docs`.

### search_forum / `forum`

Search OpenSearch community forum.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | (required) | Search query |
| `limit` | integer | 10 | Max results |

## Output Example

```json
{
  "query": "k-NN",
  "version": "latest",
  "total": 12,
  "hasMore": true,
  "results": [
    {
      "title": "k-NN",
      "url": "https://docs.opensearch.org/latest/query-dsl/specialized/k-nn/index/",
      "snippet": "Use the knn query for running nearest neighbor searches..."
    }
  ]
}
```

## Development

```bash
uv run mcp dev src/opensearch_docs_search/server.py
uv run pytest tests/ -v
```

## License

MIT

## Disclaimer

This project uses the "OpenSearch" name to indicate compatibility with OpenSearch software. OpenSearch is a trademark of the OpenSearch Project. This tool is not affiliated with, endorsed by, or sponsored by the OpenSearch Project or its contributors.
