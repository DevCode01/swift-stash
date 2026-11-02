#!/usr/bin/env python3
# Validate, format and minify JSON from a file or stdin.
import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(description="JSON formatter and validator")
    parser.add_argument("file", nargs="?", help="JSON file (reads stdin if omitted)")
    parser.add_argument("-i", "--indent", type=int, default=2, help="Indent spaces (default: 2)")
    parser.add_argument("-m", "--minify", action="store_true", help="Minify instead of pretty-print")
    args = parser.parse_args()

    try:
        if args.file:
            with open(args.file, encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        return 1

    if args.minify:
        print(json.dumps(data, separators=(",", ":")))
    else:
        print(json.dumps(data, indent=args.indent, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
