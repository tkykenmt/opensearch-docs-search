---
name: opensearch-docs-search
description: Search OpenSearch documentation, blogs, and community forums
---

# OpenSearch Documentation Search

Search OpenSearch documentation, blog posts, and community forum.

## Setup

```bash
cd /path/to/opensearch-docs-search
uv sync
```

## Commands

### Search Documentation

```bash
uv run opensearch-doc-search docs "k-NN"
uv run opensearch-doc-search docs "neural search" --version 2.12
uv run opensearch-doc-search docs "index settings" --limit 5
```

### Search Blog Posts

```bash
uv run opensearch-doc-search blogs "performance"
uv run opensearch-doc-search blogs "release" --limit 5
```

### Search Community Forum

```bash
uv run opensearch-doc-search forum "cluster health"
uv run opensearch-doc-search forum "snapshot" --limit 5
```

## Output

JSON format with search results including title, URL, and snippet.
