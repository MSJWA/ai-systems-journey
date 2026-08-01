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

## 27th July 2026 — Day 5: First real LLM API call

**What I did:**
- Signed up for Groq (avoided OpenAI, avoided the Anthropic free-credit
  hunt since it wasn't showing up on my account)
- Learned the real difference between Groq (single provider, open-weight
  models) and OpenRouter (a gateway routing to many providers through
  one API) - kept OpenRouter in mind for later cost/model-routing work
- Set up a .env file properly, confirmed .gitignore covers it before
  ever putting a real key in
- Wrote llm_call.py: loads the API key safely, authenticates a client,
  sends a structured request to an actual LLM, gets a real response back
- Got my first genuine AI-generated reply from my own code - not
  hardcoded, not a chat interface, my own script talking to a real model

**What confused me / what I didn't know before today:**
- Didn't know model names are exact, provider-defined strings you have
  to get right (like "llama-3.3-70b-versatile") - not arbitrary labels
- Learned max_tokens isn't just a formatting limit - it's directly tied
  to real cost/usage, first hands-on touch of token economics
- Realized this whole exercise used the *exact same pattern* as every
  other API call I've made this week (GitHub, my own FastAPI endpoints)
  - the "AI" part didn't need new mechanics, it just slotted into
  request -> response -> extract data, same as always
- Also learned about Hugging Face (model hosting hub, not an API
  provider like Groq) and the real difference between fine-tuning /
  distillation vs training a model from scratch - distillation is
  roughly why cheaper models like DeepSeek can still be capable

**What's next:**
- Build a hand-built agent loop: a while loop where the LLM decides to
  call one of my own functions based on its response, and the result
  gets fed back in - the exercise that's supposed to make LangGraph
  make sense later instead of being a black box

## 27th July 2026 — Day 6: Hand-built agent — LLM tool calling

**What I did:**
- Built the actual "hand-built agent loop" exercise from Phase 0 of my
  roadmap - the one flagged as the most important exercise in the whole
  plan
- Described a real Python function (add_numbers) to the LLM using a
  structured "tools" format (name, description, parameters)
- Learned the LLM never actually executes anything itself - it only
  decides which tool to use and fills out a structured "request form"
  with the right inputs; my own code is what actually runs the function
- Tested two cases: a question needing the tool (correctly calculated
  47+89=136), and one that didn't need it (answered normally in text)

**What confused me / what I didn't know before today:**
- Initially couldn't see the point if my code does the actual execution
  - realized the LLM's real value isn't calculation, it's translating
  messy natural language into a precise, structured function call
  (which tool, which inputs) - something my code has no way to do on
  its own
- Understood real agents have many tools available at once, not just
  one, and the LLM picks whichever is relevant based on the question
- Connected this directly to MCP - what I built by hand (the tools
  list format) is essentially a small custom version of what MCP
  standardizes across every provider

**What's next:**
- Try a more "real" tool - maybe looking someone up in my SQL database
  instead of simple addition, to see this pattern do something my code
  genuinely couldn't do alone
- Eventually: LangGraph, once this mechanism is second nature

## 27th July 2026 — Day 6.5: Agent tool calling with a real database lookup

**What I did:**
- Rebuilt the tool-calling pattern from the add_numbers exercise, but
  with a real, useful tool this time: find_user(name), looking someone
  up in my actual SQLite users table from Day 4
- Tested with a name that exists (Ali) - got real data back
- Tested with a name that doesn't exist (Ahmed) - got a clean, handled
  error instead of a crash, same defensive pattern as always

**What confused me / what I didn't know before today:**
- Forgot to include imports/client setup when starting the new file -
  good reminder that each new file needs its own full setup, not just
  the new logic being demonstrated
- This version made the LLM's real value obvious in a way the addition
  example didn't - my code genuinely couldn't have known "Ali" was the
  name to look up from a casual sentence like "can you find Ali's info"

**What's next:**
- LangGraph - now that the underlying tool-calling mechanism is
  actually understood, not a black box

## 28th July 2026 — Day 7: RAG — from word-matching to real embeddings

**What I did:**
- Built RAG's core pattern by hand: retrieve relevant info, inject it
  into the prompt, then let the LLM answer using it
- Started with crude word-overlap matching (set intersection) to
  understand the store -> retrieve -> inject -> ask shape without new
  dependencies
- Corrected a misunderstanding: it's my own code doing the matching,
  never the LLM - same "who does what" split as tool-calling
- Tested what happens when retrieval picks the WRONG document on
  purpose - watched the LLM correctly say "no information in context"
  instead of making something up - real, working hallucination control
- Upgraded to real embeddings using sentence-transformers
  (all-MiniLM-L6-v2, from Hugging Face) - converts sentences into
  meaning-vectors, not just words
- Tested with a reworded question sharing zero exact words with the
  correct document, and it still found the right match - proved this
  is genuinely meaning-based, not just fancier word-matching

**What confused me / what I didn't know before today:**
- Initially thought the LLM does the matching in RAG - it doesn't, my
  own code always does the retrieval, the LLM only ever generates the
  final answer using what it's handed
- Learned embeddings are produced by a separate, smaller, specialized
  model - not the same LLM I've been chatting with
- Ran a real local model (sentence-transformers) for the first time -
  no API call, no cost, runs entirely on my own machine

**What's next:**
- LangGraph - now that both core LLM patterns (tool-calling and RAG)
  are built and understood from scratch

## 29th July 2026 — Day 8: LangGraph — multi-tool agent with real debugging

**What I did:**
- Built a working LangGraph agent, mapped every new concept back to my
  hand-built version: @tool decorator = auto-generating the tool
  description I used to write by hand, StateGraph/nodes/edges = the
  same decide-execute-loop pattern as a formal graph structure
- Added a second tool (add_numbers) alongside find_user, giving the
  agent a real choice between tools for the first time
- Hit a genuine bug: the LLM incorrectly tried to call find_user for a
  "capital of Japan" question and malformed the tool-call syntax,
  crashing the program
- Diagnosed it correctly: not a code bug, a model reasoning failure -
  smaller/faster models are less reliable at tool selection than
  larger ones, a real tradeoff in the cost/capability discussion
- Fixed it two ways: added try/except so it never crashes ugly again,
  and made the tool's docstring more specific about when to use it,
  which resolved the actual confusion
- Reran all three test questions - correct tool routing across all of
  them this time

**What confused me / what I didn't know before today:**
- Didn't know LangChain and LangGraph were different things (LangGraph
  is built by the LangChain team, specifically for looping/branching
  flows) - also learned about Langflow (visual builder) and Langfuse/
  LangSmith (observability tools) as the wider ecosystem
- Learned firsthand that tool-calling reliability varies by model size
  - not something a tutorial would show, only showed up from testing
  a real edge case myself
- Realized clearer, more specific tool descriptions are a real fix for
  agent confusion, not just a nice-to-have

**What's next:**
- Consider this the end of the core "understand the mechanism" phase -
  tool-calling, RAG, and LangGraph are all built and genuinely
  understood from scratch now, not through blind framework use
- Ahead: MCP, then Tier 4 (the unglamorous production-hardening list -
  testing, observability, auth, rate limiting)

## 29th July 2026 — Day 9: asyncio fundamentals

**What I did:**
- Learned why asyncio matters with a concrete before/after: 3 sequential
  2-second waits = 6 seconds, done concurrently = ~2 seconds
- Initially mismapped this to Linux's wait()/zombie process concept -
  corrected: asyncio is single-thread cooperative multitasking (like
  one waiter juggling multiple tables during idle wait time), not
  multiple processes/threads running in true parallel
- Ran async_intro.py and confirmed the real behavior: all 3 tasks start
  immediately, all finish around the same time, total time ~2s not 6s

**What confused me / what I didn't know before today:**
- Wrongly assumed asyncio was about process-level concepts I already
  knew from OS/Linux - it's actually a different mechanism entirely,
  scoped to a single thread
- Learned asyncio only helps when tasks are WAITING on something
  external (network, timers) - it wouldn't help with heavy computation,
  that needs real threading/multiprocessing instead, a different tool

**What's next:**
- Docker basics - closes out the last Tier 1 gap
- Then MCP, then a real vector database (pgvector)

## 31st July 2026 — Day 10: Docker — containerizing FastAPI, real infra crash recovery

**What I did:**
- Learned Docker's core concept: isolates the whole environment (OS,
  Python version, dependencies), not just packages like a venv does
- Wrote a Dockerfile for fastapi_app.py, built an image, ran it as a
  container, and confirmed /docs loads identically to running it
  directly - the "works on my machine" problem, actually solved
- Hit a serious real infrastructure crash: my main requirements.txt
  included sentence-transformers (pulls in PyTorch, multiple GB), which
  ate almost all my remaining disk space mid-build and crashed the
  Docker daemon itself (bus error, core dumped)
- Diagnosed the actual cause: Docker's docker_data.vhdx virtual disk
  had ballooned to 6.8GB from the interrupted install
- Recovered safely: shut down WSL, deleted the corrupted virtual disk,
  let Docker recreate a fresh one, confirmed space was back
- Fixed the real root cause (not just retried blindly): created a
  separate, minimal docker-requirements.txt with only what
  fastapi_app.py actually needs, instead of my whole venv's packages
- Rebuilt successfully, ran the container, confirmed all 3 endpoints
  working correctly through the browser

**What confused me / what I didn't know before today:**
- Didn't know a Docker image should only include what that specific
  service needs - bundling my whole dev environment's dependencies is
  a real, common mistake, not just wasteful
- Learned virtualization needs to be enabled at the BIOS level for
  Docker/WSL to work at all - a genuine hardware-adjacent setup step
- Got real experience diagnosing and recovering from an actual
  infrastructure failure, not just a code bug - different, valuable
  kind of debugging

**What's next:**
- Tier 1 is now fully closed (async + Docker both done)
- MCP next, then a real vector database (pgvector)

## 31st July 2026 — Day 11: MCP — server, client, and a real multi-layered debugging session

**What I did:**
- Learned MCP standardizes the exact tool-description mechanism I'd
  already built by hand 3 times - not a new concept, a standard
  packaging of one I already understood
- Built mcp_server.py, wrapping find_user as a real MCP tool
- Hit a genuine, serious debugging chain: broken import path (SDK's
  internal structure changed in a recent version), VS Code debugger
  using a different Python interpreter than my terminal, a client
  subprocess launching the wrong Python entirely (command="python"
  resolving to global Python, not my venv)
- Fixed the final root cause using sys.executable instead of the
  string "python", to guarantee the subprocess uses the exact same
  environment as the parent script
- Got a genuine, correct end-to-end result: client discovers the
  server's tools, calls find_user, gets real database data back,
  through the actual MCP protocol

**What confused me / what I didn't know before today:**
- Learned running an MCP server alone (with no client) is supposed to
  look like "nothing happening" - same as uvicorn, just not obvious
  until seeing it explained
- Learned the VS Code debugger and terminal can use different Python
  interpreters even in the "same" project - a real, non-obvious gotcha
- Learned sys.executable is the reliable way to guarantee a subprocess
  uses the same Python environment as its parent, instead of trusting
  PATH to resolve "python" correctly

**What's next:**
- A real vector database (pgvector via Postgres) - closes Tier 2 fully
- Then Tier 4 - the production hardening list

## 01st August 2026 — Day 12: pgvector — real vector database, closing Tier 2

**What I did:**
- Installed PostgreSQL locally, then pivoted to a Docker-based pgvector
  image (pgvector/pgvector:pg18-trixie) after hitting Windows-specific
  extension installation friction - reused Docker skills from Day 10
- Enabled the vector extension, created a documents table with a
  vector(384) column matching my embedding model's exact output size
- Learned precisely what an embedding is: a whole sentence (not words,
  not letters) compressed into one coordinate in 384-dimensional
  "meaning space" - distance between points = difference in meaning
- Hit a genuine, hard-to-diagnose password authentication bug -
  systematically ruled out wrong password, hidden whitespace, wrong
  auth method, eventually traced to localhost resolving to IPv6 (::1)
  vs needing explicit 127.0.0.1 for IPv4
- Inserted real documents with real embeddings into persistent storage
- Ran a real similarity search using pgvector's <-> operator - the
  exact same job as my earlier np.dot() code, now done inside the
  database itself, at real scale
- Confirmed correct meaning-based retrieval, zero word overlap between
  question and matched document, same proof as the original RAG
  exercise but now backed by real, scalable, persistent infrastructure

**What confused me / what I didn't know before today:**
- Learned localhost and 127.0.0.1 aren't always interchangeable -
  localhost can resolve to IPv6 (::1), which can behave differently
  than explicit IPv4, a genuinely subtle networking gotcha
- Learned docker exec bypasses network authentication (trusted
  internal access), which is why an early "it works!" test was
  misleading - had to specifically test with -h localhost -W to force
  real network-style authentication for a valid comparison

**What's next:**
- Tier 2 fully closed
- Formal agent evals (Tier 3's last piece), then Tier 4 seriously