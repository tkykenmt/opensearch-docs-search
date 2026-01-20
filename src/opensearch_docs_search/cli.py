"""CLI for OpenSearch documentation search (SKILL mode)."""

import argparse
import json
import sys
from .core import search_docs, search_blogs, search_forum


def main():
    parser = argparse.ArgumentParser(description="Search OpenSearch documentation, blogs, and forums")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # docs
    p_docs = subparsers.add_parser("docs", help="Search documentation")
    p_docs.add_argument("query", help="Search query")
    p_docs.add_argument("-v", "--version", default="latest", help="OpenSearch version")
    p_docs.add_argument("-l", "--limit", type=int, default=10, help="Max results")
    p_docs.add_argument("-o", "--offset", type=int, default=0, help="Skip N results")

    # blogs
    p_blogs = subparsers.add_parser("blogs", help="Search blog posts")
    p_blogs.add_argument("query", help="Search query")
    p_blogs.add_argument("-v", "--version", default="latest", help="OpenSearch version")
    p_blogs.add_argument("-l", "--limit", type=int, default=10, help="Max results")
    p_blogs.add_argument("-o", "--offset", type=int, default=0, help="Skip N results")

    # forum
    p_forum = subparsers.add_parser("forum", help="Search community forum")
    p_forum.add_argument("query", help="Search query")
    p_forum.add_argument("-l", "--limit", type=int, default=10, help="Max results")

    args = parser.parse_args()

    if args.command == "docs":
        result = search_docs(args.query, args.version, args.limit, args.offset)
    elif args.command == "blogs":
        result = search_blogs(args.query, args.version, args.limit, args.offset)
    elif args.command == "forum":
        result = search_forum(args.query, args.limit)

    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
