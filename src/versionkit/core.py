import re

_PATTERN = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def parse(version: str) -> tuple[int, int, int]:
    if not isinstance(version, str) or not _PATTERN.fullmatch(version):
        raise ValueError(f"invalid version: {version!r}")
    return tuple(map(int, version.split(".")))


def is_valid(version: str) -> bool:
    try:
        parse(version)
    except ValueError:
        return False
    return True


def compare(left: str, right: str) -> int:
    a, b = parse(left), parse(right)
    return (a > b) - (a < b)


def bump(version: str, part: str) -> str:
    major, minor, patch = parse(version)
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    if part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError("part must be major, minor, or patch")
