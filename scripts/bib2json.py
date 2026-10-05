#!/usr/bin/env python3
"""Convert journal.bib and preprint.bib into _data/publications.json.

Run from the repo root after editing either bib file:

    python3 scripts/bib2json.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = {"journal.bib": "journal", "preprint.bib": "preprint"}
OUT = ROOT / "_data" / "publications.json"

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], start=1)}


def parse_bib(text):
    """Yield (key, fields) for each @entry, handling nested braces."""
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", text):
        i, depth = m.end(), 1
        start = i
        while depth and i < len(text):
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        body = text[start:i - 1]
        fields = {}
        for f in re.finditer(r"(\w+)\s*=\s*", body):
            j = f.end()
            if body[j] == "{":
                d, k = 1, j + 1
                while d:
                    d += {"{": 1, "}": -1}.get(body[k], 0)
                    k += 1
                value = body[j + 1:k - 1]
            else:
                value = re.match(r"[^,\n]*", body[j:]).group(0)
            fields.setdefault(f.group(1).lower(), value.strip())
        yield m.group(1), fields


def clean(s):
    s = s.replace("\\&", "&").replace("--", "–")
    s = re.sub(r"\s+", " ", s)
    return s.replace("{", "").replace("}", "").strip()


def format_author(name):
    student = "$^\\dagger$" in name
    name = clean(name.replace("$^\\dagger$", ""))
    if "," in name:
        last, first = [p.strip() for p in name.split(",", 1)]
        # add periods to bare initials: "Leo L" -> "Leo L."
        first = re.sub(r"\b([A-Z])(?=\s|$)", r"\1.", first)
        name = f"{first} {last}"
    return {"name": name, "me": "Duan" in name, "student": student}


def build_entry(key, f, kind):
    authors = [format_author(a) for a in re.split(r"\s+and\s+", f["author"])]
    journal = clean(f.get("journal", ""))
    entry = {
        "key": key,
        "type": kind,
        "title": clean(f["title"]),
        "authors": authors,
        "year": int(f["year"]),
        "month": MONTHS.get(f.get("month", "").lower(), 0),
    }
    arxiv = re.search(r"arXiv:(\d{4}\.\d{4,5})", journal)
    if arxiv:
        entry["arxiv"] = f"https://arxiv.org/abs/{arxiv.group(1)}"
        # arXiv ids are YYMM.NNNNN: date of the first version
        entry["year"] = 2000 + int(arxiv.group(1)[:2])
        entry["month"] = int(arxiv.group(1)[2:4])
        status = journal.split(",", 1)[1].strip() if "," in journal else ""
        entry["venue"] = status[:1].upper() + status[1:]
    else:
        venue = journal
        vol, num, pages = (clean(f.get(x, "")) for x in ("volume", "number", "pages"))
        if vol:
            venue += f", {vol}" + (f"({num})" if num else "")
        if pages:
            venue += ": " + re.sub(r"(?<=\w)-(?=\w)", "–", pages)
        entry["venue"] = venue
    if f.get("doi"):
        entry["link"] = "https://doi.org/" + f["doi"]
    elif f.get("url"):
        entry["link"] = f["url"]
    elif "arxiv" in entry:
        entry["link"] = entry["arxiv"]
    return entry


def main():
    pubs = []
    for fname, kind in SOURCES.items():
        for key, fields in parse_bib((ROOT / fname).read_text()):
            if "Duan" not in fields.get("author", ""):
                print(f"skip {fname}:{key} (no Duan in authors)")
                continue
            pubs.append(build_entry(key, fields, kind))
    pubs.sort(key=lambda p: (p["year"], p["month"]), reverse=True)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(pubs, indent=2, ensure_ascii=False) + "\n")
    n_pre = sum(p["type"] == "preprint" for p in pubs)
    print(f"wrote {OUT.relative_to(ROOT)}: {n_pre} preprints, {len(pubs) - n_pre} journal")


if __name__ == "__main__":
    main()
