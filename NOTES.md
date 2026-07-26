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

## 22nd July 2026 — Day 2.5: Closing out Month 1-2 — context managers, JSON writing, decorators (paused)

**What I did:**
- Went back over context managers (`with` blocks) to actually understand
  *why* they exist, not just that I'd used them — they guarantee cleanup
  (like closing a file) even if something crashes in between
- Learned to write JSON, not just read it — json.dump() converts a
  Python dictionary into a real JSON file
- Tried decorators — got the basic idea (wrapping extra behavior around
  an existing function) but the syntax/mechanics felt like too much at
  once, so paused it deliberately to revisit later inside FastAPI, where
  it'll show up in real context (@app.get(...))

**What confused me / what I didn't know before today:**
- Decorators genuinely didn't click yet — noting that honestly instead
  of pretending they did. Multiple new ideas stacked together
  (functions as values, nested functions, @ syntax) all at once
- Didn't know `open()` takes a second argument for read vs write mode
  ("w") — all my file work before this defaulted to read mode without
  me realizing there was a choice being made

**What's next:**
- Month 3-4: SQL fundamentals + building my own API with FastAPI
- Revisit decorators once I hit @app.get(...) in FastAPI

## 23rd July 2026 — Day 3: FastAPI — GET, path parameters, POST + Pydantic

**What I did:**
- Installed FastAPI + uvicorn inside the venv
- Built my first working API server with a basic GET endpoint (@app.get("/"))
- Learned decorators properly this time, in real context — @app.get(...)
  wraps a function with routing logic, same mechanism as the earlier
  timer example, just doing something different
- Added a GET endpoint with a path parameter (/greet/{name}) — hit a bug
  where the placeholder name in the URL didn't match the function
  parameter name, learned they have to match exactly for FastAPI to
  connect them
- Added a POST endpoint using Pydantic (GreetRequest class) to validate
  incoming data — tested it with valid data (worked) and invalid data
  like age as text (correctly rejected before my function even ran)
- Explored /docs — FastAPI's auto-generated interactive interface for
  testing endpoints

**What confused me / what I didn't know before today:**
- Didn't understand the actual difference between GET and POST before
  today — GET reads/asks for info, POST sends data to be processed,
  not about how the user triggers it
- Realized FastAPI doesn't know or care WHO is calling it — a browser,
  a script, or later an LLM all look identical to it. This led to a
  real security question I raised myself: if an LLM could call my
  endpoints as "tools," what stops it from doing something destructive?
  Learned about permission scoping, treating LLM-read data as
  untrusted (prompt injection), and human-in-the-loop confirmation for
  risky actions — real, current, unsolved-ish problem in the field,
  not just theory

**What's next:**
- SQL fundamentals
- Then connect FastAPI to a real database, so POST requests actually
  store data instead of just echoing it back

## 26th July 2026 — Day 4: SQL fundamentals + connecting FastAPI to a database

**What I did:**
- Learned what a database actually is and why it beats plain files for
  searching/filtering large amounts of data
- Used SQLite (built into Python, no server needed) to create my first
  table (users: id, name, age)
- Learned INSERT to add rows, and the placeholder pattern (?, ?) instead
  of directly inserting variables into SQL text - this prevents SQL
  injection, a real security vulnerability, so built the safe habit in
  from day one
- Learned SELECT to read data back, and WHERE to filter (e.g. age > 20)
- Discovered that re-running an INSERT script duplicates data instead of
  overwriting it - databases only add unless told otherwise, unlike
  overwriting a file
- Connected my existing FastAPI POST /greet endpoint to the database -
  now submitted data is actually saved (persisted), not just echoed back
  and forgotten
- Verified it end-to-end: submitted data through /docs, then confirmed
  it was really there using a separate SELECT script

**What confused me / what I didn't know before today:**
- Didn't know databases don't auto-save - had to learn connection.commit()
  is required to actually save changes
- Didn't realize INSERT always adds a new row rather than overwriting -
  this caused duplicate data the first time I re-ran a script
- Learned the real distinction between "stateless" (my original FastAPI
  app - forgets everything after each request) and "persistent" (now,
  with a database behind it) - this is directly related to how agent
  memory works later on

**What's next:**
- Tier 2: raw LLM API calls, no framework
- Eventually build a RAG pipeline by hand - now understand it's a more
  advanced, meaning-based version of the same store-then-retrieve
  pattern I just used with SQL