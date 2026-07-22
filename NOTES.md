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

## 22nd July 2026 — Day 2: API calls with requests + error handling

**What I did:**
- Learned what an API actually is — interface for software to talk to
  software, vs GUI/IDE which is for humans (restaurant/menu analogy helped)
- Wrote a script using requests.get() to call the GitHub API
- Learned about status codes (200 = success, 404 = not found) and used
  an if/else to handle both cases instead of assuming it always works
- Added a try/except around the whole thing to catch
  requests.exceptions.ConnectionError — handles the case where there's
  no internet at all, not just a bad response
- Tested all 3 paths: valid username, invalid username, no internet

**What confused me / what I didn't know before today:**
- Didn't know the difference between a "bad but valid response" (404,
  handled with if/else) and a full connection failure (no response at
  all, handled with try/except) — different failure types need
  different tools
- Learned response.status_code and response.json() aren't magic — they
  come from the response object requests.get() returns
- Learned "response" isn't a reserved keyword, just a naming convention
  — same as "content" yesterday

**What's next:**
- SQL fundamentals + building a basic API myself with FastAPI