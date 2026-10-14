#!/usr/bin/env python3
"""Small, dependency-free repository validator."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path.relative_to(ROOT)}: {exc}")


plugin = validate_json(ROOT / "plugin.json")
mcp = validate_json(ROOT / "mcp.json")

if plugin.get("name") != "esignatures":
    fail("plugin.json must use the plugin name 'esignatures'")

server = mcp.get("mcpServers", {}).get("esignatures", {})
if server.get("type") != "streamable-http":
    fail("mcp.json must declare a streamable-http server")
if server.get("url") != "https://esignatures.com/mcp":
    fail("mcp.json must use the official hosted MCP endpoint")

skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
if len(skill_files) != 2:
    fail("expected exactly two packaged skills")

for path in skill_files:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or text.count("---\n") < 2:
        fail(f"{path.relative_to(ROOT)} is missing YAML frontmatter")
    frontmatter = text.split("---\n", 2)[1]
    if not re.search(r"^name: [a-z0-9-]+$", frontmatter, re.MULTILINE):
        fail(f"{path.relative_to(ROOT)} has an invalid or missing name")
    if not re.search(r"^description: .+$", frontmatter, re.MULTILINE):
        fail(f"{path.relative_to(ROOT)} is missing a description")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"ESIGNATURES_SECRET_TOKEN\s*[:=]\s*['\"]?(?!\$\{)[A-Za-z0-9_-]{12,}", text):
        fail(f"possible literal eSignatures token in {path.relative_to(ROOT)}")

print("OK: plugin metadata, MCP endpoint, skills, and secret checks passed")
