---
name: opensearch-docs-search
description: Search OpenSearch documentation, blogs, and community forums. Use when the user asks about OpenSearch features, configuration, APIs, or troubleshooting.
---

# OpenSearch Documentation Search

## Setup

```bash
uv tool install git+https://github.com/tkykenmt/opensearch-docs-search
```

## Commands

```bash
opensearch-doc-search docs "k-NN"
opensearch-doc-search docs "neural search" --version 2.12 --limit 5
opensearch-doc-search blogs "performance"
opensearch-doc-search forum "cluster health"
```

## Output Example

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
