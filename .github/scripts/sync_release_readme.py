#!/usr/bin/env python3
"""Synchronize the public README's guarded release section with published GitHub releases."""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPO = "zaizaisharpsharp/FloatShot-Releases"
START = "<!-- FLOATSHOT:RELEASE-START -->"
END = "<!-- FLOATSHOT:RELEASE-END -->"
REQUIRED = {"FloatShot-Setup.exe", "FloatShot-win-x64.zip", "floatshot-update.json"}
README = Path(__file__).resolve().parents[2] / "README.md"


def github(path: str) -> object:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required for the release README sync")
    req = Request(
        f"https://api.github.com/repos/{REPO}/{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "floatshot-release-readme-sync",
        },
    )
    with urlopen(req, timeout=30) as response:
        return json.load(response)


def valid_tag(tag: str) -> bool:
    return bool(re.fullmatch(r"v\d+\.\d+\.\d+", tag))


def release_notes(release: dict) -> str:
    tag = release["tag_name"]
    notes = (release.get("body") or "").strip()
    if not notes:
        raise ValueError(f"No published notes for {tag}")
    notes = re.sub(r"^#\s+FloatShot\s+v\d+\.\d+\.\d+\s*\n+", "", notes, count=1, flags=re.I)
    notes = re.sub(r"\s*Built and tested on Windows; updater ZIP SHA-256 verified\.\s*$", "", notes)
    return notes.strip()


def render(release: dict, releases: list[dict]) -> str:
    tag = release["tag_name"]
    if not valid_tag(tag) or release.get("draft") or release.get("prerelease"):
        raise ValueError(f"Not a stable release tag: {tag}")
    assets = {a["name"] for a in release.get("assets", [])}
    missing = REQUIRED - assets
    if missing:
        raise ValueError(f"Release {tag} missing verified assets: {sorted(missing)}")
    notes = release_notes(release)
    recent = []
    seen = set()
    for entry in releases:
        other = entry.get("tag_name", "")
        if (not valid_tag(other) or entry.get("draft") or entry.get("prerelease")
                or other in seen):
            continue
        seen.add(other)
        recent.append(f"- [{other}](https://github.com/{REPO}/releases/tag/{other})"
                      + (" (latest)" if other == tag else ""))
        if len(recent) == 5:
            break
    if tag not in seen:
        recent.insert(0, f"- [{tag}](https://github.com/{REPO}/releases/tag/{tag}) (latest)")
        recent = recent[:5]

    return "\n".join([
        START,
        f"## Latest stable release: {tag}",
        "",
        f"[**Download FloatShot for Windows (.exe)**](https://github.com/{REPO}/releases/download/{tag}/FloatShot-Setup.exe)"
        + f" · [Portable ZIP](https://github.com/{REPO}/releases/download/{tag}/FloatShot-win-x64.zip)"
        + f" · [Release details](https://github.com/{REPO}/releases/tag/{tag})"
        + f" · [All releases](https://github.com/{REPO}/releases)",
        "",
        f"### What's new in {tag}",
        "",
        notes,
        "",
        "### Recent releases",
        "",
        *recent,
        "",
        END,
    ])


def replace_block(original: str, block: str) -> str:
    if original.count(START) != 1 or original.count(END) != 1:
        raise ValueError("README must have exactly one release block marker pair")
    begin = original.index(START)
    finish = original.index(END)
    if finish <= begin:
        raise ValueError("README release block markers are out of order")
    return original[:begin] + block + original[finish + len(END):]


def main() -> None:
    # GitHub CLI can create a release before all uploaded assets appear through
    # the REST API. Retry rather than showing a partial/broken download list.
    last_error: Exception | None = None
    for attempt in range(12):
        try:
            latest = github("releases/latest")
            history = github("releases?per_page=12")
            assert isinstance(latest, dict) and isinstance(history, list)
            block = render(latest, history)
            break
        except (ValueError, HTTPError, URLError, TimeoutError, AssertionError) as ex:
            last_error = ex
            if attempt == 11:
                raise RuntimeError("Could not verify complete latest public release") from last_error
            time.sleep(10)
    original = README.read_text(encoding="utf-8")
    updated = replace_block(original, block)
    if updated == original:
        print(f"Already current: {latest['tag_name']}")
    else:
        README.write_text(updated, encoding="utf-8", newline="\n")
        print(f"README updated: {latest['tag_name']}")


if __name__ == "__main__":
    main()
