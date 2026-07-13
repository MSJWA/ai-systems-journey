# My AI Systems Journey — Devlog

##  13th July 2026 — Day 1: Environment setup + first file I/O script

**What I did:**
- Set up venv on a separate drive (E:) since C: was almost full
- Ran into VS Code install breaking due to disk space — cleaned up ~10GB
  (npm/pip caches, old Adobe update files, old node_modules)
- Fixed PowerShell execution policy to activate the venv
- Linked VS Code to the venv via "Select Interpreter"
- Wrote my first real try/except script — reads a file, handles it
  missing, handles it being empty

**What confused me / what I didn't know before today:**
- Had never used open() or try/except before — learned both from scratch
- Didn't realize a string on its own line doesn't print unless you
  wrap it in print() — small bug, good lesson
- Didn't know VS Code needs to be manually pointed at a venv's
  interpreter, or it just uses global Python silently

**What's next:**
- requests library — call a real API, handle a failed request