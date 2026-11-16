#!/usr/bin/env python3
"""
Build script for the GTA 6 Answers static site hub.
Generates the landing page and all answer pages into a staging directory.

Usage:
    python build.py              # Build into default staging dir
    python build.py --dir /path  # Build into custom directory
    python build.py --verify     # Check output only, no build
"""

import argparse
import csv
import json
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
ANSWERS_SRC = REPO_ROOT / "answers"
QUESTIONS_CSV = REPO_ROOT / "questions.csv"
STAGING_DEFAULT = REPO_ROOT / "staging"

# Page metadata for GEO extraction
PAGE_META = {
    "gta-6-money-guide-landing.html": {
        "title": "GTA 6 Money Guide — Complete Hub for Making Money in Grand Theft Auto VI",
        "description": "The complete GTA 6 money guide hub. Fastest money methods, best heists, passive income, business investments, early game tips, story mode earning, and online predictions.",
        "type": "CollectionPage",
    },
    "how-to-make-money-fast-gta-6.html": {
        "title": "How to Make Money Fast in GTA 6 — Complete Guide (2026)",
        "description": "Fastest money-making methods in GTA 6 including heists, robberies, businesses, and passive income. Ranked by $/hour with verified payout estimates.",
        "type": "Article",
    },
    "best-money-making-methods-gta-6.html": {
        "title": "Best Money Making Methods in GTA 6 — Ranked",
        "description": "Every GTA 6 money method ranked. Heists, businesses, robberies, street racing and passive income with verified payout data.",
        "type": "Article",
    },
    "how-to-get-rich-gta-6.html": {
        "title": "How to Get Rich in GTA 6 — The Complete Path to Millions",
        "description": "The definitive path to becoming a millionaire in GTA 6. Early grinding, heist strategies, business investments, and endgame wealth.",
        "type": "Article",
    },
    "gta-6-best-heist-for-money.html": {
        "title": "GTA 6 Best Heist for Money — All Heists Ranked by Payout",
        "description": "Every GTA 6 heist ranked by payout, difficulty, and crew requirements. Find the best heist for money whether you play solo or with a team.",
        "type": "Article",
    },
    "how-to-make-money-gta-6-story-mode.html": {
        "title": "How to Make Money in GTA 6 Story Mode — Complete Guide",
        "description": "Complete guide to making money in GTA 6 story mode. Heists, stock market, robberies, street racing, and passive businesses for Jason and Lucia.",
        "type": "Article",
    },
    "gta-6-early-money-making-guide.html": {
        "title": "GTA 6 Early Money Making Guide — First 5 Hours",
        "description": "GTA 6 early money guide covering the first 5 hours. Best starter methods, what to buy first, and how to avoid common beginner money traps.",
        "type": "Article",
    },
    "what-businesses-to-buy-first-gta-6.html": {
        "title": "What Businesses to Buy First in GTA 6 — Investment Guide 2026",
        "description": "GTA 6 business investment guide ranked by ROI. Auto shop, nightclub, laundromat, nail salon — which to buy first and in what order.",
        "type": "Article",
    },
    "best-passive-income-gta-6.html": {
        "title": "Best Passive Income in GTA 6 — Make Money While Offline",
        "description": "Complete guide to passive income in GTA 6. Nightclubs, laundromats, nail salons, and auto shops — set up income that runs while you play or while offline.",
        "type": "Article",
    },
    "how-to-make-money-gta-6-online.html": {
        "title": "How to Make Money in GTA 6 Online — What We Know So Far",
        "description": "GTA 6 Online money making guide — what's confirmed and what to expect from the online economy when it launches in Q1 2027.",
        "type": "Article",
    },
}

PAGE_ORDER = [
    "gta-6-money-guide-landing.html",
    "how-to-make-money-fast-gta-6.html",
    "best-money-making-methods-gta-6.html",
    "how-to-get-rich-gta-6.html",
    "gta-6-best-heist-for-money.html",
    "how-to-make-money-gta-6-story-mode.html",
    "gta-6-early-money-making-guide.html",
    "what-businesses-to-buy-first-gta-6.html",
    "best-passive-income-gta-6.html",
    "how-to-make-money-gta-6-online.html",
]


def count_questions(csv_path: Path) -> int:
    """Count rows in questions.csv (excluding header)."""
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        return sum(1 for _ in reader) - 1  # subtract header


def load_questions_for_sitemap(csv_path: Path) -> list[dict]:
    """Load question data from CSV."""
    questions = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row)
    return questions


def build_landing_page(staging_dir: Path):
    """Build a sitemap and confirm landing page was copied."""
    landing_src = ANSWERS_SRC / "gta-6-money-guide-landing.html"
    landing_dst = staging_dir / "index.html"
    shutil.copy2(landing_src, landing_dst)
    return landing_dst


def create_llms_txt(staging_dir: Path, base_url: str = "https://gta6-moneyguide.com"):
    """Create llms.txt for AI agent discovery."""
    lines = [
        "# GTA 6 Money Guide",
        "",
        "> Complete guide hub for making money in Grand Theft Auto VI. Covers all earning methods,",
        "> heists, businesses, passive income, and investment strategies.",
        "",
        "## About",
        "- Type: Fan game guide resource",
        "- Topic: GTA 6 in-game economy and money-making strategies",
        "- Status: Active (pre-launch preparation, launch Nov 19, 2026)",
        "- Contact: Not applicable (independent fan site)",
        "",
        "## Key Pages",
    ]
    for page_file in PAGE_ORDER:
        meta = PAGE_META[page_file]
        slug = page_file.replace(".html", "")
        if slug == "gta-6-money-guide-landing":
            path = ""
        else:
            path = slug + "/"
        lines.append(f"- [{meta['title']}]({base_url}/{path}) — {meta['description']}")
    lines.append(f"")
    lines.append(f"## Optional")
    lines.append(f"- {base_url}/sitemap.xml")
    lines.append(f"- {base_url}/llms.txt")
    lines.extend([
        "",
        "## Content Summary",
        "This site provides detailed guides on every money-making method in GTA 6:",
        "- Heists: payout comparisons, crew leveling, approach strategies",
        "- Businesses: investment order, ROI analysis, passive income stacking",
        "- Early game: optimal first-5-hours progression path",
        "- Story mode: character-specific earning strategies",
        "- Online predictions: expected economy features for online launch",
        "",
        "## Structured Data",
        "All answer pages include FAQPage JSON-LD schema for direct answer extraction.",
        "Landing page uses CollectionPage schema.",
    ])
    output_path = staging_dir / "llms.txt"
    output_path.write_text("\n".join(lines) + "\n")
    return output_path


def build_all(staging_dir: Path):
    """Copy all answer pages into the staging directory with clean URLs."""
    staging_dir.mkdir(parents=True, exist_ok=True)

    # Copy landing page as index.html
    build_landing_page(staging_dir)

    # Copy each answer page into its own slug directory for clean URLs
    for page_file in PAGE_ORDER:
        src = ANSWERS_SRC / page_file
        if not src.exists():
            print(f"WARNING: {src} not found, skipping")
            continue

        slug = page_file.replace(".html", "")
        if slug == "gta-6-money-guide-landing":
            continue  # Already copied as index.html

        page_dir = staging_dir / slug
        page_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, page_dir / "index.html")

    # Create llms.txt for AI discovery
    create_llms_txt(staging_dir)

    # Create sitemap.xml
    create_sitemap(staging_dir)

    # Copy questions.csv for reference
    shutil.copy2(QUESTIONS_CSV, staging_dir / "questions.csv")

    return staging_dir


def create_sitemap(staging_dir: Path, base_url: str = "https://gta6-moneyguide.com"):
    """Generate a basic sitemap.xml."""
    urls = [
        {"loc": base_url, "priority": "1.0"},
    ]
    for page_file in PAGE_ORDER[1:]:  # Skip landing (it's index)
        meta = PAGE_META.get(page_file, {})
        slug = page_file.replace(".html", "")
        prio = "0.9" if page_file in (
            "how-to-make-money-fast-gta-6.html",
            "best-money-making-methods-gta-6.html",
            "how-to-get-rich-gta-6.html",
        ) else "0.8"
        urls.append({"loc": f"{base_url}/{slug}/", "priority": prio})

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        lines.append(f"  <url><loc>{u['loc']}</loc><priority>{u['priority']}</priority></url>")
    lines.append("</urlset>")

    (staging_dir / "sitemap.xml").write_text("\n".join(lines) + "\n")


def verify_output(staging_dir: Path, csv_path: Path):
    """Verify build output exists and is valid."""
    issues = []

    # Check staging dir exists
    if not staging_dir.exists():
        return {"status": "FAIL", "issues": ["Staging directory does not exist"]}

    # Check landing page
    index = staging_dir / "index.html"
    if not index.exists():
        issues.append("Missing: index.html")
    else:
        content = index.read_text()
        if "FAQPage" in content and len(content) < 500:
            issues.append("index.html too short or incomplete")

    # Check all answer pages
    for page_file in PAGE_ORDER:
        if page_file == "gta-6-money-guide-landing.html":
            continue
        slug = page_file.replace(".html", "")
        page_path = staging_dir / slug / "index.html"
        if not page_path.exists():
            issues.append(f"Missing: {slug}/index.html")
        else:
            content = page_path.read_text()
            if "FAQPage" not in content:
                issues.append(f"{slug}/index.html missing FAQPage JSON-LD")
            if len(content) < 1000:
                issues.append(f"{slug}/index.html too short ({len(content)} chars)")

    # Check llms.txt
    llms_file = staging_dir / "llms.txt"
    if not llms_file.exists():
        issues.append("Missing: llms.txt")
    else:
        content = llms_file.read_text()
        if "GTA 6 Money Guide" not in content:
            issues.append("llms.txt seems incomplete")

    # Check sitemap
    sitemap = staging_dir / "sitemap.xml"
    if not sitemap.exists():
        issues.append("Missing: sitemap.xml")

    # Check questions.csv
    q_csv = staging_dir / "questions.csv"
    if not q_csv.exists():
        issues.append("Missing: questions.csv (reference copy)")

    # Count questions
    q_count = count_questions(csv_path)
    if q_count < 50:
        issues.append(f"Only {q_count} questions in CSV (expected 50+)")

    status = "PASS" if not issues else "FAIL"
    return {"status": status, "issues": issues, "question_count": q_count}


def main():
    parser = argparse.ArgumentParser(description="Build GTA 6 Answers static site")
    parser.add_argument("--dir", default=str(STAGING_DEFAULT), help="Output staging directory")
    parser.add_argument("--verify", action="store_true", help="Verify output only, no build")
    args = parser.parse_args()

    staging_dir = Path(args.dir)
    csv_path = QUESTIONS_CSV

    if not csv_path.exists():
        print(f"ERROR: questions.csv not found at {csv_path}")
        sys.exit(1)

    if args.verify:
        result = verify_output(staging_dir, csv_path)
        print(f"Verification: {result['status']}")
        if result["issues"]:
            for issue in result["issues"]:
                print(f"  - {issue}")
        print(f"Questions in CSV: {result['question_count']}")
        sys.exit(0 if result["status"] == "PASS" else 1)

    # Build
    print(f"Building GTA 6 Answers site into: {staging_dir}")
    print(f"Questions in CSV: {count_questions(csv_path)}")
    print(f"Answer pages: {len(PAGE_ORDER) - 1} (plus landing)")

    build_all(staging_dir)

    # Verify
    result = verify_output(staging_dir, csv_path)
    print(f"\nBuild verification: {result['status']}")
    if result["issues"]:
        for issue in result["issues"]:
            print(f"  - {issue}")

    # Summary
    total_size = sum(
        f.stat().st_size for f in staging_dir.rglob("*") if f.is_file()
    )
    files_built = list(staging_dir.rglob("*"))
    html_files = [f for f in files_built if f.suffix in (".html", ".xml", ".txt")]
    
    print(f"\nStaging directory: {staging_dir}")
    print(f"Files built: {len(html_files)}")
    print(f"Total size: {total_size:,} bytes")
    print(f"\nPages:")
    for f in sorted(html_files):
        print(f"  {f.relative_to(staging_dir)}")

    if result["status"] == "PASS":
        print("\n✅ Build complete. Site ready for review.")
    else:
        print("\n⚠ Build complete with issues to resolve.")
        sys.exit(1)


if __name__ == "__main__":
    main()