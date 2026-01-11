#!/usr/bin/env python3
"""
Setup a complete MkDocs site for a DSA & LeetCode preparation hub
using the Material for MkDocs theme, ready to publish on GitHub Pages.

What this script does:
- Creates the required docs/ folder structure and Markdown files
- Populates roadmap files with a 45-day SDE plan (checkboxes + LeetCode links)
- Adds empty notes files per topic with placeholder sections
- Creates solved/ topic folders with an index and a solution TEMPLATE
- Generates mkdocs.yml with Material theme and GitHub Pages settings
- Prints instructions to preview locally and deploy to GitHub Pages

Usage:
- Run from your project root:
    python3 setup_mkdocs_site.py

Prereqs:
- Install MkDocs and Material theme:
    pip install mkdocs mkdocs-material

Preview:
- mkdocs serve

Publish to GitHub Pages:
- mkdocs gh-deploy
"""

import os
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"

# Topics required by the user
TOPICS_ORDERED = [
    "arrays",
    "strings",
    "linkedlists",
    "stack_queue",
    "trees",
    "graphs",
    "heap",
    "dp",
    "backtracking",
]

# Roadmap also includes a misc.md
ROADMAP_TOPICS = TOPICS_ORDERED + ["misc"]

# 45-day plan across topics with direct LeetCode links.
# Each entry: (title, url)
PROBLEMS = {
    "arrays": [
        ("Two Sum", "https://leetcode.com/problems/two-sum/"),
        ("Best Time to Buy and Sell Stock", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"),
        ("Contains Duplicate", "https://leetcode.com/problems/contains-duplicate/"),
        ("Product of Array Except Self", "https://leetcode.com/problems/product-of-array-except-self/"),
        ("Maximum Subarray", "https://leetcode.com/problems/maximum-subarray/"),
        ("3Sum", "https://leetcode.com/problems/3sum/"),
        ("Container With Most Water", "https://leetcode.com/problems/container-with-most-water/"),
        ("Merge Intervals", "https://leetcode.com/problems/merge-intervals/"),
        ("Set Matrix Zeroes", "https://leetcode.com/problems/set-matrix-zeroes/"),
    ],
    "strings": [
        ("Valid Palindrome", "https://leetcode.com/problems/valid-palindrome/"),
        ("Longest Substring Without Repeating Characters", "https://leetcode.com/problems/longest-substring-without-repeating-characters/"),
        ("Longest Repeating Character Replacement", "https://leetcode.com/problems/longest-repeating-character-replacement/"),
        ("Valid Anagram", "https://leetcode.com/problems/valid-anagram/"),
        ("Group Anagrams", "https://leetcode.com/problems/group-anagrams/"),
        ("Longest Palindromic Substring", "https://leetcode.com/problems/longest-palindromic-substring/"),
        ("Palindromic Substrings", "https://leetcode.com/problems/palindromic-substrings/"),
    ],
    "linkedlists": [
        ("Reverse Linked List", "https://leetcode.com/problems/reverse-linked-list/"),
        ("Merge Two Sorted Lists", "https://leetcode.com/problems/merge-two-sorted-lists/"),
        ("Reorder List", "https://leetcode.com/problems/reorder-list/"),
        ("Remove Nth Node From End of List", "https://leetcode.com/problems/remove-nth-node-from-end-of-list/"),
        ("Linked List Cycle", "https://leetcode.com/problems/linked-list-cycle/"),
        ("Add Two Numbers", "https://leetcode.com/problems/add-two-numbers/"),
    ],
    "stack_queue": [
        ("Valid Parentheses", "https://leetcode.com/problems/valid-parentheses/"),
        ("Min Stack", "https://leetcode.com/problems/min-stack/"),
        ("Daily Temperatures", "https://leetcode.com/problems/daily-temperatures/"),
        ("Implement Queue using Stacks", "https://leetcode.com/problems/implement-queue-using-stacks/"),
    ],
    "trees": [
        ("Maximum Depth of Binary Tree", "https://leetcode.com/problems/maximum-depth-of-binary-tree/"),
        ("Same Tree", "https://leetcode.com/problems/same-tree/"),
        ("Invert Binary Tree", "https://leetcode.com/problems/invert-binary-tree/"),
        ("Binary Tree Level Order Traversal", "https://leetcode.com/problems/binary-tree-level-order-traversal/"),
        ("Subtree of Another Tree", "https://leetcode.com/problems/subtree-of-another-tree/"),
        ("Balanced Binary Tree", "https://leetcode.com/problems/balanced-binary-tree/"),
    ],
    "graphs": [
        ("Number of Islands", "https://leetcode.com/problems/number-of-islands/"),
        ("Clone Graph", "https://leetcode.com/problems/clone-graph/"),
        ("Course Schedule", "https://leetcode.com/problems/course-schedule/"),
        ("Rotting Oranges", "https://leetcode.com/problems/rotting-oranges/"),
    ],
    "heap": [
        ("Kth Largest Element in an Array", "https://leetcode.com/problems/kth-largest-element-in-an-array/"),
        ("Top K Frequent Elements", "https://leetcode.com/problems/top-k-frequent-elements/"),
        ("Merge k Sorted Lists", "https://leetcode.com/problems/merge-k-sorted-lists/"),
    ],
    "dp": [
        ("Climbing Stairs", "https://leetcode.com/problems/climbing-stairs/"),
        ("House Robber", "https://leetcode.com/problems/house-robber/"),
        ("Coin Change", "https://leetcode.com/problems/coin-change/"),
    ],
    "backtracking": [
        ("Subsets", "https://leetcode.com/problems/subsets/"),
        ("Combination Sum", "https://leetcode.com/problems/combination-sum/"),
        ("Permutations", "https://leetcode.com/problems/permutations/"),
    ],
}

MISC_ITEMS = [
    "Bit Manipulation essentials",
    "Math tricks & modulo patterns",
    "Sliding Window patterns roundup",
    "Two Pointers patterns roundup",
    "Greedy technique highlights",
]

NOTES_TEMPLATE = dedent(
    """
    # {Title}

    ## Overview
    Briefly describe the topic, common patterns, and core concepts.

    ## Key Techniques
    - Technique 1
    - Technique 2
    - Technique 3

    ## Common Pitfalls
    - Pitfall A
    - Pitfall B

    ## Practice Notes
    Add notes, insights, and personal takeaways from problems.
    """
)

SOLVED_INDEX_TEMPLATE = dedent(
    """
    # {Title} — Solved Problems

    Use the `TEMPLATE.md` in this folder to add solutions.

    Recommended filename format: `{{slug}}.md` where slug is the problem name.

    ## How to add a solution
    1. Copy `TEMPLATE.md` to a new file, e.g., `two-sum.md`
    2. Fill in title, link, statement summary, approach, and code
    3. Add time/space complexity and notes
    """
)

SOLVED_TEMPLATE = dedent(
    """
    # Problem: TITLE_HERE

    - Link: https://leetcode.com/problems/your-problem-here/

    ## Problem Statement
    Brief summary or notes (do not paste full statement).

    ## Approach
    Outline the algorithm, key ideas, and edge cases.

    ## Code (Python)
    ```python
    # TODO: add solution
    def solve():
        pass
    ```

    ## Code (Java)
    ```java
    // TODO: add solution
    class Solution {}
    ```

    ## Code (C++)
    ```cpp
    // TODO: add solution
    class Solution {};
    ```

    ## Complexity
    - Time: O(...)
    - Space: O(...)

    ## Notes / Variants
    Additional notes, variants, or alternative approaches.
    """
)

INDEX_MD = dedent(
    """
    # DSA & LeetCode Preparation Hub

    Welcome! This hub organizes a focused 45-day SDE prep plan,
    topic notes, and a place to track solved LeetCode problems.

    ## Quick Links
    - Roadmap: see topic plans under [Roadmap](roadmap/arrays.md)
    - Notes: start with [Arrays Notes](notes/arrays.md)
    - Solved Problems: browse [Solved LeetCode](solved/arrays/index.md)

    ## How to Use
    - Follow the 45-day plan across topics with daily checkboxes
    - Add notes as you learn patterns and techniques
    - Log solved problems with approach and code in `solved/*`

    Happy coding and consistent practice!
    """
)

MKDOCS_YML = dedent(
    """
    site_name: DSA & LeetCode Prep Hub
    site_description: Structured 45-day plan, notes, and solutions for DSA & LeetCode
    site_url: https://your-username.github.io/your-repo
    repo_url: https://github.com/your-username/your-repo

    theme:
      name: material
      palette:
        - scheme: default
          primary: blue
          accent: indigo

    nav:
      - Home: index.md
      - Roadmap:
          - Arrays: roadmap/arrays.md
          - Strings: roadmap/strings.md
          - Linked Lists: roadmap/linkedlists.md
          - Stack & Queue: roadmap/stack_queue.md
          - Trees: roadmap/trees.md
          - Graphs: roadmap/graphs.md
          - Heap: roadmap/heap.md
          - Dynamic Programming: roadmap/dp.md
          - Backtracking: roadmap/backtracking.md
          - Misc: roadmap/misc.md
      - Notes:
          - Arrays: notes/arrays.md
          - Strings: notes/strings.md
          - Linked Lists: notes/linkedlists.md
          - Stack & Queue: notes/stack_queue.md
          - Trees: notes/trees.md
          - Graphs: notes/graphs.md
          - Heap: notes/heap.md
          - Dynamic Programming: notes/dp.md
          - Backtracking: notes/backtracking.md
          - Mathematics: notes/maths.md
      - Solved LeetCode:
          - Arrays: solved/arrays/index.md
          - Strings: solved/strings/index.md
          - Linked Lists: solved/linkedlists/index.md
          - Stack & Queue: solved/stack_queue/index.md
          - Trees: solved/trees/index.md
          - Graphs: solved/graphs/index.md
          - Heap: solved/heap/index.md
          - Dynamic Programming: solved/dp/index.md
          - Backtracking: solved/backtracking/index.md

    markdown_extensions:
      - admonition
      - codehilite
      - toc
      - tables
      - pymdownx.superfences
      - pymdownx.details
      - pymdownx.tabbed

    plugins:
      - search

    # GitHub Pages: deploy with `mkdocs gh-deploy`
    # Optionally set branch/name via CLI flags if needed.
    """
)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_structure():
    # Base structure
    (DOCS / "roadmap").mkdir(parents=True, exist_ok=True)
    (DOCS / "notes").mkdir(parents=True, exist_ok=True)
    solved_dir = DOCS / "solved"
    solved_dir.mkdir(parents=True, exist_ok=True)

    # Create solved subfolders
    for t in TOPICS_ORDERED:
        (solved_dir / t).mkdir(parents=True, exist_ok=True)

    # Index page
    write_file(DOCS / "index.md", INDEX_MD)

    # Notes pages
    for t in TOPICS_ORDERED:
        title = t.replace("_", " ").title()
        write_file(DOCS / "notes" / f"{t}.md", NOTES_TEMPLATE.format(Title=title))

    # Solved index + template in each topic
    for t in TOPICS_ORDERED:
        title = t.replace("_", " ").title()
        write_file(DOCS / "solved" / t / "index.md", SOLVED_INDEX_TEMPLATE.format(Title=title))
        write_file(DOCS / "solved" / t / "TEMPLATE.md", SOLVED_TEMPLATE)

    # Roadmap pages with 45-day distribution across topics
    day_counter = 1
    for t in TOPICS_ORDERED:
        problems = PROBLEMS.get(t, [])
        start_day = day_counter
        lines = [
            f"# {t.replace('_', ' ').title()} — 45-Day Plan",
            "",
        ]
        # Add checkbox list items with Day numbers and direct links
        for title, url in problems:
            lines.append(f"- [ ] Day {day_counter}: [{title}]({url})")
            day_counter += 1
        end_day = day_counter - 1
        lines.insert(1, f"_Days {start_day}–{end_day}_")
        write_file(DOCS / "roadmap" / f"{t}.md", "\n".join(lines) + "\n")

    # Misc roadmap page (non-day-specific placeholders)
    misc_lines = [
        "# Misc — 45-Day Plan (Supplementary)",
        "",
        "Use these as supplementary study items alongside daily tasks:",
        "",
    ]
    for item in MISC_ITEMS:
        misc_lines.append(f"- [ ] {item}")
    write_file(DOCS / "roadmap" / "misc.md", "\n".join(misc_lines) + "\n")

    # mkdocs.yml
    write_file(ROOT / "mkdocs.yml", MKDOCS_YML)


if __name__ == "__main__":
    make_structure()
    print("\nMkDocs DSA & LeetCode site scaffolded successfully!\n")
    print("Created:")
    print(f"- {DOCS}/index.md")
    print(f"- {DOCS}/roadmap/*.md")
    print(f"- {DOCS}/notes/*.md")
    print(f"- {DOCS}/solved/* (with index.md + TEMPLATE.md)")
    print(f"- {ROOT}/mkdocs.yml")
    print("\nNext steps:")
    print("1) Install MkDocs + Material: \n   pip install mkdocs mkdocs-material")
    print("2) Preview locally: \n   mkdocs serve")
    print("3) Publish to GitHub Pages: \n   mkdocs gh-deploy")
