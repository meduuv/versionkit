# VersionKit

> Small, dependency-free Python helpers for working with semantic versions.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

VersionKit provides focused utilities for **parsing, comparing, validating and bumping** `MAJOR.MINOR.PATCH` versions.

## Features

- Parse semantic versions
- Compare versions
- Validate supported version strings
- Bump major, minor and patch releases
- JSON-friendly values
- Zero runtime dependencies

## Installation

```bash
pip install versionkit
```

## Quick Start

```python
from versionkit import bump, compare, parse

assert parse("1.2.3") == (1, 2, 3)
assert bump("1.2.3", "minor") == "1.3.0"
assert compare("1.2.0", "1.1.9") == 1
```

## Typical Uses

VersionKit can be embedded into release scripts, CI checks, project tooling and small automation workflows where bringing in a larger versioning framework would be unnecessary.

## Design Principles

```text
predictable input
      ↓
 deterministic parsing
      ↓
 explicit operations
      ↓
 easy automation
```

The library is intentionally small and does not mutate files, tags or releases by itself.

## Development

```bash
python -m pytest
```

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
