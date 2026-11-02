#!/usr/bin/env bash
# Auto-generated test harness — run after cloning to verify the build.
set -uo pipefail
FAIL=0

echo "-- syntax/build check --"
if python3 swift-stash.py --help; then echo "  ok"; else echo "  FAIL"; FAIL=1; fi

echo "-- functional check --"
OUT="$(echo '{"b":1,"a":[1,2]}' | ./swift-stash.py --indent 2 2>&1)"
if echo "$OUT" | grep -qF -- '"b": 1'; then
  echo "  ok   - contains: "b": 1"
else
  echo "  FAIL - expected to contain: "b": 1"
  echo "  got: $OUT"
  FAIL=1
fi

if [ "$FAIL" = "1" ]; then echo; echo "FAILED"; exit 1; fi
echo; echo "All tests passed."
