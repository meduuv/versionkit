# VersionKit

Small, dependency-free Python helpers for parsing, comparing, and bumping semantic versions.

## Features

- Parse `MAJOR.MINOR.PATCH` versions
- Compare versions
- Bump major, minor, and patch releases
- Validate simple semantic versions
- JSON-friendly results

## Usage

```python
from versionkit import bump, compare, parse

assert parse("1.2.3") == (1, 2, 3)
assert bump("1.2.3", "minor") == "1.3.0"
assert compare("1.2.0", "1.1.9") == 1
```

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

Built by meduuv. Find more projects at https://guns.lol/meduu
