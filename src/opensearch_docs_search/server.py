"""OpenSearch Documentation MCP Server."""

from mcp.server.fastmcp import FastMCP
from .core import search_docs as _search_docs, search_blogs as _search_blogs, search_forum as _search_forum

mcp = FastMCP("opensearch-docs-search")


@mcp.tool()
def search_docs(query: str, version: str = "latest", limit: int = 10, offset: int = 0) -> dict:
    """Search OpenSearch documentation.

    Args:
        query: Search query
        version: OpenSearch version (default: latest)
        limit: Max results per page (default: 10)
        offset: Skip first N results for pagination (default: 0)
    """
    return _search_docs(query, version, limit, offset)


@mcp.tool()
def search_blogs(query: str, version: str = "latest", limit: int = 10, offset: int = 0) -> dict:
    """Search OpenSearch blog posts.

    Args:
        query: Search query
        version: OpenSearch version (default: latest)
        limit: Max results per page (default: 10)
        offset: Skip first N results for pagination (default: 0)
    """
    return _search_blogs(query, version, limit, offset)


@mcp.tool()
def search_forum(query: str, limit: int = 10) -> dict:
    """Search OpenSearch community forum.

    Args:
        query: Search query
        limit: Max results (default: 10)
    """
    return _search_forum(query, limit)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
