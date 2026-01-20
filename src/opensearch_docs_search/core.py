"""Core search functions for OpenSearch documentation, blogs, and forums."""

import json
import urllib.parse
import urllib.request
from functools import lru_cache


@lru_cache(maxsize=100)
def _fetch_docs(query: str, version: str, types: str) -> tuple:
    encoded = urllib.parse.quote(query)
    url = f"https://search-api.opensearch.org/search?q={encoded}&v={version}&t={types}"
    with urllib.request.urlopen(url, timeout=10) as resp:
        data = json.loads(resp.read().decode())
    return tuple(data.get("results", []))


@lru_cache(maxsize=100)
def _fetch_forum(query: str) -> tuple:
    encoded = urllib.parse.quote(query)
    url = f"https://forum.opensearch.org/search/query?term={encoded}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
    posts = data.get("posts", [])
    topics = {t["id"]: t for t in data.get("topics", [])}
    return tuple(posts), topics, data.get("grouped_search_result", {}).get("more_posts", False)


def search_docs(query: str, version: str = "latest", limit: int = 10, offset: int = 0) -> dict:
    """Search OpenSearch documentation."""
    all_results = list(_fetch_docs(query, version, "docs"))
    total = len(all_results)
    page_results = all_results[offset : offset + limit]
    results = [
        {"title": r["title"], "url": f"https://docs.opensearch.org{r['url']}", "snippet": r.get("content", "")[:300]}
        for r in page_results
    ]
    return {"query": query, "version": version, "total": total, "offset": offset, "limit": limit, "hasMore": offset + limit < total, "results": results}


def search_blogs(query: str, version: str = "latest", limit: int = 10, offset: int = 0) -> dict:
    """Search OpenSearch blog posts."""
    all_results = list(_fetch_docs(query, version, "blogs"))
    total = len(all_results)
    page_results = all_results[offset : offset + limit]
    results = [
        {"title": r["title"], "url": r["url"], "snippet": r.get("content", "")[:300]}
        for r in page_results
    ]
    return {"query": query, "version": version, "total": total, "offset": offset, "limit": limit, "hasMore": offset + limit < total, "results": results}


def search_forum(query: str, limit: int = 10) -> dict:
    """Search OpenSearch community forum."""
    posts, topics, has_more = _fetch_forum(query)
    posts = list(posts)[:limit]
    results = []
    for p in posts:
        topic = topics.get(p.get("topic_id"), {})
        results.append({
            "title": topic.get("title", ""),
            "url": f"https://forum.opensearch.org/t/{topic.get('slug', '')}/{p.get('topic_id')}",
            "author": p.get("username", ""),
            "snippet": p.get("blurb", "")[:300],
            "created_at": p.get("created_at", ""),
            "tags": topic.get("tags", []),
            "has_accepted_answer": topic.get("has_accepted_answer", False),
        })
    return {"query": query, "total": len(results), "hasMore": has_more, "results": results}
