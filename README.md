# opensearch-docs-search

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Search OpenSearch documentation, blogs, and community forums.

> **Note**: This is an unofficial community tool and is not affiliated with or endorsed by the OpenSearch Project.

## Installation

### Agent Skill (Recommended)

Works with Claude Code, Cursor, Kiro CLI, and [35+ agents](https://www.npmjs.com/package/skills#supported-agents).

```bash
npx skills add tkykenmt/opensearch-docs-search
```

### MCP Server

```bash
uv tool install git+https://github.com/tkykenmt/opensearch-docs-search[mcp]
```

Add to your MCP config:

```json
{
  "mcpServers": {
    "opensearch-docs-search": {
      "command": "opensearch-docs-search"
    }
  }
}
```

### Standalone CLI

```bash
uv tool install git+https://github.com/tkykenmt/opensearch-docs-search
```

## Usage

### Skill

After installation, the agent can use `scripts/search.py`:

```bash
python scripts/search.py docs "k-NN"
python scripts/search.py blogs "performance" --limit 5
python scripts/search.py forum "cluster health"
```

### CLI

```bash
opensearch-doc-search docs "k-NN"
opensearch-doc-search blogs "neural search" --version 2.12 --limit 5
opensearch-doc-search forum "cluster health"
```

### Options

| Option | Commands | Description |
|--------|----------|-------------|
| `-v, --version` | docs, blogs | OpenSearch version (default: latest) |
| `-l, --limit` | all | Max results (default: 10) |
| `-o, --offset` | docs, blogs | Skip N results for pagination |

## Output

```json
{
  "query": "k-NN",
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

## License

MIT
