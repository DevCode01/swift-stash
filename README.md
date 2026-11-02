# Swift Stash

**Python** · **v0.1.0**

_JSON validator, formatter and minifier for the command line_

---

## Features

- Validates JSON from a file or stdin
- Pretty-prints with configurable indentation
- Minify mode for compact output

## Installation

```bash
git clone https://github.com/DevCode01/swift-stash.git
cd swift-stash
```

## Usage

```bash
cat data.json | ./swift-stash.py --indent 2
```

## How it works

Parses JSON from a file or stdin, validates it, and re-emits it pretty-printed with configurable indentation. `--minify` produces compact output for transfer, and any parse error is reported with the exact location.

## Options

- `file` - path to the JSON file (reads stdin if omitted)
- `-i, --indent N` - indentation width in spaces (default 2)
- `-m, --minify` - output compact single-line JSON
- `-h, --help` - show usage

## Example

```bash
$ echo '{"b":1,"a":[1,2]}' | ./swift-stash.py --indent 2
{
  "b": 1,
  "a": [
    1,
    2
  ]
}
```

## Testing

```bash
bash tests/run.sh
```

Includes a functional check against real captured output, plus the build/syntax check.

## License

MIT
