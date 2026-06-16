# 🚀 30-Day Roadmap: Generative AI → Agentic AI → AG-UI

**For:** A Data Science graduate starting these three topics from scratch and aiming for strong, job-ready, project-backed competence.
**Built:** June 2026. All YouTube/video links below were **checked and confirmed live on 15 June 2026.**

---

## 📌 Read this first (honest expectations)

You **can** go from zero to genuinely capable in 30 focused days. You will *not* "master" three deep, fast-moving fields in a month — nobody does, and anyone selling that is exaggerating. What this plan realistically delivers:

- A correct **mental model** of how LLMs actually work (not hand-waving).
- The ability to **build and ship** real apps: a RAG system, a multi-tool agent, and a full-stack agent with a live UI.
- **3 portfolio projects** you can put on GitHub and talk about in interviews.
- A foundation solid enough that you keep improving *fast* after day 30.

**Time budget:** Plan for **3–5 focused hours/day**. Less is fine — just stretch the calendar. The *order* matters more than the speed.

**Assumed starting point:** comfortable with Python; able to read basic JavaScript/React (you'll need light React only in Week 4 — I point you to a crash course there). You do **not** need heavy math; the resources teach what's needed.

### How to use this document
Each day has four parts:
- 🎯 **Goal** — what you should understand by end of day
- 📺 **Learn** — videos / reading (with verified links)
- 🛠️ **Do** — hands-on task
- ✅ **Checkpoint** — questions to test yourself + when a mini-project lands

Don't skip the checkpoints. If you can't answer them, re-watch before moving on. **Active recall beats passive watching.**

### Link legend
| Symbol | Meaning |
|---|---|
| ✅ | Video link personally verified live (15 Jun 2026) |
| 📄 | Official documentation (free) |
| 🎓 | Free structured course |
| 📝 | Article / reading |

---

# 🗓️ WEEK 0 — Setup (Day 0, ~2 hours)

Before Day 1, get your environment ready so you never lose momentum later.

🛠️ **Do:**
1. Install **Python 3.11+**, **VS Code**, **Git**, and **Node.js 20+** (Node is for Week 4).
2. Create a free **GitHub** account → make one repo: `genai-30-days`. Commit every project here.
3. Create accounts (all have free tiers): **Hugging Face**, **Google AI Studio** (free Gemini API key), and **OpenRouter** or **Groq** (free/cheap LLM API access so you're not blocked by cost).
4. Learn the basics of `venv` and `pip install` if rusty.
5. Optional but recommended: set up **Google Colab** (free GPU) for any training/notebook work.

✅ **Checkpoint:** You can run `python --version`, `node --version`, and push an empty README to GitHub.

---

# 🗓️ WEEK 1 — Generative AI & LLM Foundations (Days 1–7)

**Theme:** Understand *what* an LLM is and *how* it works, all the way down to building a tiny one yourself.

---

### Day 1 — The big picture: what is Generative AI & an LLM?
🎯 **Goal:** Form an accurate intuition for tokens, prediction, and why LLMs feel "smart."

📺 **Learn:**
- ✅ 3Blue1Brown — *Large Language Models explained briefly* (7 min): https://www.youtube.com/watch?v=LPZh9BOjkQs
- ✅ Andrej Karpathy — *Intro to Large Language Models* (1 hr, the single best beginner talk): https://www.youtube.com/watch?v=zjkBMFhNj_g

🛠️ **Do:** Open ChatGPT / Claude / Gemini and write down 5 prompts. For each, predict what it will do *before* hitting enter. Note where your prediction was wrong.

✅ **Checkpoint:**
1. In one sentence, what does an LLM literally predict?
2. What is a "token"? Why don't models see whole words?
3. What's the difference between *pretraining* and *post-training*?

---

### Day 2 — How LLMs are actually built (the full pipeline)
🎯 **Goal:** Understand pretraining, fine-tuning, and RLHF without needing the math yet.

📺 **Learn:**
- ✅ Andrej Karpathy — *Deep Dive into LLMs like ChatGPT* (3.5 hrs — watch in 2 sittings; this is the crown jewel): https://www.youtube.com/watch?v=7xTGNNLPyMI

🛠️ **Do:** Take notes as a diagram: raw internet text → base model → instruction tuning → RLHF → assistant. Label what each stage adds.

✅ **Checkpoint:**
1. Why does a *base* model behave differently from ChatGPT?
2. What is a "hallucination," mechanically, and why do they happen?
3. What does RLHF optimize for?

---

### Day 3 — Practical LLM usage & prompt foundations
🎯 **Goal:** Use LLMs effectively as a power user before you build with them.

📺 **Learn:**
- ✅ Andrej Karpathy — *How I Use LLMs* (practical, real workflows): https://www.youtube.com/watch?v=EWvNQjAaOHw
- 🎓 DeepLearning.AI free short course — *ChatGPT Prompt Engineering for Developers* (find it free in the catalog): https://www.deeplearning.ai/short-courses/

🛠️ **Do:** Take one boring real task (summarize an article, draft an email, extract data from text) and solve it 3 ways: zero-shot, few-shot, and with a system role. Compare quality.

✅ **Checkpoint:**
1. What is the difference between *zero-shot* and *few-shot* prompting?
2. What is a "system prompt" and why does it matter?
3. Give one example where adding examples to the prompt clearly improved output.

---

### Day 4 — Transformers & attention (the engine)
🎯 **Goal:** Understand the attention mechanism conceptually.

📺 **Learn:**
- 🎓 Hugging Face *LLM Course* — Chapter 1 (Transformers, how they work): https://huggingface.co/learn/llm-course/chapter1/1
- ✅ (Visual deep-dive) 3Blue1Brown — *Neural Networks* series, the chapters on Transformers & Attention, on his channel: https://www.youtube.com/@3blue1brown

🛠️ **Do:** Write a one-page plain-English explanation of "attention" as if teaching a friend. If you can't explain it simply, re-watch.

✅ **Checkpoint:**
1. What problem does *attention* solve that older models (RNNs) struggled with?
2. What do "query, key, value" roughly represent?
3. Why are transformers easy to run in parallel?

---

### Day 5–6 — Build a tiny GPT from scratch (the "aha" moment)
🎯 **Goal:** Demystify LLMs completely by coding one. This is what separates people who *use* AI from people who *understand* it.

📺 **Learn / Code along (pick ONE track):**
- ✅ **Track A (recommended, code-along):** Andrej Karpathy — *Let's build GPT: from scratch, in code, spelled out* (~2 hrs): https://www.youtube.com/watch?v=kCc8FmEb1nY
  - Repo + notebooks: 📄 https://github.com/karpathy/nn-zero-to-hero
- ✅ **Track B (longer, gentler, no math assumed):** freeCodeCamp — *Create a Large Language Model from Scratch with Python* (~6 hrs): https://www.youtube.com/watch?v=UU1WVnMk4E8

🛠️ **Do:** Actually type the code yourself (don't copy-paste). Train the tiny model on a text file you like (song lyrics you own, your own notes, a public-domain book). Watch the loss go down and generate text.

✅ **Checkpoint (Mini-Project #1 lands here):**
- ✅ Push your working tiny-GPT notebook to GitHub with a README explaining each part in your own words.
1. What is "loss" and what does it mean when it drops?
2. What is an embedding table?
3. Where exactly does "attention" appear in your code?

---

### Day 7 — Consolidation + the state of the field
🎯 **Goal:** Zoom back out, connect the dots, and rest your brain a little.

📺 **Learn:**
- ✅ Andrej Karpathy — *YC AI Startup School 2025* talk ("Software is changing" / Software 3.0 — the best framing of where this is all going): https://www.youtube.com/watch?v=LCEmiRjPEtQ

🛠️ **Do (Week 1 review):** Re-answer all checkpoint questions from Days 1–6 from memory. Fill gaps by re-watching specific sections.

✅ **Week 1 Milestone:**
- [ ] You can explain how an LLM works end-to-end to a non-technical person.
- [ ] You built and trained a tiny GPT.
- [ ] Mini-Project #1 is on GitHub.

---

# 🗓️ WEEK 2 — Applied Gen AI: Embeddings, RAG & Building Apps (Days 8–14)

**Theme:** Stop just *understanding* LLMs and start *building products* with them.

---

### Day 8 — Calling LLMs with code (APIs)
🎯 **Goal:** Programmatically call an LLM and handle the response.

📄 **Learn:**
- Read the quickstart for whichever API you set up (Google AI Studio / Gemini, Groq, or OpenRouter). All have free tiers and Python SDKs.
- 🎓 DeepLearning.AI free short course — *Building Systems with the ChatGPT API* (catalog): https://www.deeplearning.ai/short-courses/

🛠️ **Do:** Write a Python script that takes a user question from the terminal, sends it to an LLM API, and prints the answer. Add a system prompt that gives it a persona.

✅ **Checkpoint:**
1. What are `temperature` and `max_tokens` and what do they control?
2. What's the difference between the `system`, `user`, and `assistant` roles?
3. How would you keep a multi-turn conversation (hint: message history)?

---

### Day 9 — Embeddings & vector search
🎯 **Goal:** Understand how text becomes searchable "meaning."

📄 **Learn:**
- 🎓 Hugging Face LLM Course — sections on embeddings & semantic search: https://huggingface.co/learn/llm-course
- 📝 Concept to grasp: cosine similarity, vector databases (Chroma, FAISS, Pinecone).

🛠️ **Do:** Use a free embedding model (e.g., via Hugging Face `sentence-transformers`) to embed 20 sentences, then write a function that finds the most similar sentence to a query.

✅ **Checkpoint:**
1. What is an embedding, in one sentence?
2. Why is semantic search better than keyword search for Q&A?
3. What does a vector database store and why?

---

### Day 10–12 — Retrieval-Augmented Generation (RAG) — the most in-demand skill
🎯 **Goal:** Build a system that answers questions about *your own* documents.

📄 **Learn:**
- 🎓 DeepLearning.AI free short courses (find by name in catalog): *LangChain: Chat with Your Data* and *Building and Evaluating Advanced RAG*: https://www.deeplearning.ai/short-courses/
- 📄 LangChain docs (RAG tutorial): https://python.langchain.com/docs/tutorials/rag/

🛠️ **Do:** Build a RAG pipeline:
1. Load 3–5 PDFs (e.g., research papers or a product manual).
2. Chunk the text → embed → store in Chroma/FAISS.
3. On a question: retrieve top chunks → stuff into the prompt → answer with citations.
4. Wrap it in a simple **Streamlit** or **Gradio** UI.

✅ **Checkpoint (Mini-Project #2 lands here):**
- ✅ Push a working "Chat with your PDFs" app to GitHub with a demo screenshot/GIF.
1. Why does RAG reduce hallucinations?
2. What is "chunking" and why does chunk size matter?
3. What happens if retrieval returns irrelevant chunks — and how would you fix it?

---

### Day 13 — Fine-tuning vs RAG vs prompting (when to use what)
🎯 **Goal:** Know which tool fits which problem — a question you *will* get asked in interviews.

📄 **Learn:**
- 🎓 Hugging Face LLM Course — fine-tuning chapters: https://huggingface.co/learn/llm-course
- 📝 Concepts: full fine-tuning vs **LoRA/PEFT**, when fine-tuning is overkill.

🛠️ **Do:** Write a one-page decision guide: "Given problem X, do I prompt, RAG, or fine-tune?" with 5 example scenarios.

✅ **Checkpoint:**
1. Give one scenario where RAG is right and fine-tuning is wrong.
2. What does LoRA let you avoid?
3. Why is prompting usually the first thing to try?

---

### Day 14 — Week 2 consolidation
🛠️ **Do:** Improve Mini-Project #2 — add conversation memory, better chunking, or source highlighting. Polish the README.

✅ **Week 2 Milestone:**
- [ ] You can call LLM APIs confidently in code.
- [ ] You understand embeddings & vector search.
- [ ] You shipped a working RAG app (Mini-Project #2).
- [ ] You can explain prompt vs RAG vs fine-tune.

---

# 🗓️ WEEK 3 — Agentic AI (Days 15–22)

**Theme:** Go from "LLM that answers" to "AI that *acts*" — uses tools, plans, remembers, and works in loops.

---

### Day 15 — What is an "agent," really?
🎯 **Goal:** Understand the core agent loop and stop the buzzword confusion.

🎓 **Learn:**
- Hugging Face **AI Agents Course** — Unit 0 & Unit 1 (free, certified): https://huggingface.co/learn/agents-course
- 📝 Reading: Anthropic — *Building Effective Agents* (the clearest practical breakdown of patterns): https://www.anthropic.com/engineering/building-effective-agents

🛠️ **Do:** Draw the **Thought → Action → Observation** loop on paper. Map a real task ("book me a flight") onto it.

✅ **Checkpoint:**
1. What makes an "agent" different from a normal LLM call?
2. What are "tools" in agent terms?
3. What's the difference between a *workflow* and an *agent* (per Anthropic's framing)?

---

### Day 16 — The ReAct pattern & tool use (build one by hand)
🎯 **Goal:** Build a minimal agent *without* a framework so you understand the magic.

🎓 **Learn:**
- Hugging Face AI Agents Course — Unit 1 (building a basic agent from scratch): https://huggingface.co/learn/agents-course

🛠️ **Do:** Build a tiny agent in pure Python: give the LLM 2 tools (a calculator and a web search or a fake "weather" function). Let it decide when to call them by parsing its output. Loop until it produces a final answer.

✅ **Checkpoint:**
1. How does the LLM "decide" to use a tool?
2. What is the "observation" that gets fed back into the loop?
3. What happens if the agent loops forever — how do you guard against it?

---

### Day 17–18 — Agent frameworks: LangGraph
🎯 **Goal:** Learn the most widely used production agent framework (graph-based, controllable).

🎓 **Learn:**
- 🎓 DeepLearning.AI free short course — *AI Agents in LangGraph* (catalog): https://www.deeplearning.ai/short-courses/
- 📄 LangGraph docs & tutorials: https://langchain-ai.github.io/langgraph/

🛠️ **Do:** Rebuild yesterday's agent in LangGraph. Add: a tool node, a conditional edge, and persistent state. Add a second tool.

✅ **Checkpoint:**
1. Why represent an agent as a *graph* of nodes and edges?
2. What is "state" in LangGraph and why does it matter?
3. What does a conditional edge let you do?

---

### Day 19 — Multi-agent systems: CrewAI & smolagents
🎯 **Goal:** Make multiple specialized agents collaborate.

🎓 **Learn:**
- 🎓 DeepLearning.AI free short course — *Multi AI Agent Systems with crewAI* (catalog): https://www.deeplearning.ai/short-courses/
- 📄 CrewAI docs: https://docs.crewai.com
- 📄 Hugging Face `smolagents` (lightweight, code-first agents): https://github.com/huggingface/smolagents

🛠️ **Do:** Build a 2–3 agent "crew" (e.g., a *Researcher* agent + a *Writer* agent) that together produce a short report on a topic.

✅ **Checkpoint:**
1. When is multi-agent worth the extra complexity vs one good agent?
2. How do agents pass information to each other?
3. What's a risk of multi-agent systems (hint: cost, loops, error propagation)?

---

### Day 20 — MCP (Model Context Protocol): how agents connect to the world
🎯 **Goal:** Understand the open standard for giving agents tools/data — increasingly essential.

🎓 **Learn:**
- 🎓 Hugging Face **MCP Course** (free): https://huggingface.co/learn/mcp-course
- 📄 Official MCP site & docs: https://modelcontextprotocol.io

🛠️ **Do:** Connect an existing MCP server (e.g., filesystem or a public one) to a client, or read through a simple MCP server's code and explain what it exposes.

✅ **Checkpoint:**
1. What problem does MCP solve (why not just hardcode tools)?
2. What's the relationship between an MCP *client* and *server*?
3. How does MCP differ from AG-UI (preview of Week 4)?

---

### Day 21–22 — Agentic build + consolidation
🎯 **Goal:** Ship a real agent.

🛠️ **Do (Mini-Project #3):** Build a **useful** agent of your choice in LangGraph or CrewAI. Ideas:
- A "research assistant" that searches the web, reads results, and writes a cited summary.
- A "data analyst" agent that takes a CSV, writes/runs Python, and reports findings.
- A "personal task" agent that uses 2–3 real tools.

✅ **Week 3 Milestone (Mini-Project #3 on GitHub):**
- [ ] You built an agent by hand *and* in a framework.
- [ ] You understand multi-agent collaboration and MCP.
- [ ] Your agent does something genuinely useful and it's on GitHub with a demo.

---

# 🗓️ WEEK 4 — AG-UI: Building Full-Stack Agentic Apps Users Can See & Touch (Days 23–30)

**Theme:** Most agents talk in plain text. **AG-UI** (the *Agent–User Interaction Protocol*) lets your agent render real UI — charts, forms, live state — and collaborate with the user in your app. This is the cutting edge and a strong differentiator.

> **What AG-UI is:** an open, lightweight, event-based protocol (over SSE/WebSockets) that standardizes how an agent backend and a user-facing frontend stay in sync — streaming, tool calls, shared state, and human-in-the-loop. It was created by the **CopilotKit** team and has first-party integrations with LangGraph, CrewAI, Pydantic AI, Mastra, AWS, Google, and Microsoft. It sits *alongside* MCP (tools/context) and A2A (agent-to-agent) — different layers, same stack.

---

### Day 23 — React crash course (only what you need)
🎯 **Goal:** Get just enough frontend to wire an agent to a UI. (Skip/skim if you already know React.)

📄 **Learn:**
- Official React docs "Quick Start": https://react.dev/learn
- Focus only on: components, props, `useState`, and `fetch`. Don't go deep.

🛠️ **Do:** Build a one-page React app with an input box and a button that calls your Week-2 LLM API and displays the answer.

✅ **Checkpoint:**
1. What is a component and what is `useState`?
2. How do you call an API and update the UI with the result?

---

### Day 24 — Understand the AG-UI protocol
🎯 **Goal:** Understand the events and architecture before coding.

📄 **Learn:**
- AG-UI official docs — Introduction & core concepts: https://docs.ag-ui.com/introduction
- CopilotKit's AG-UI overview: https://www.copilotkit.ai/ag-ui
- AG-UI GitHub (read the README + browse the **Dojo** examples, each 50–200 lines): https://github.com/ag-ui-protocol/ag-ui

🛠️ **Do:** List the main AG-UI event types and write one sentence on what each does (e.g., text streaming, tool calls, state deltas, human-in-the-loop).

✅ **Checkpoint:**
1. What does AG-UI standardize that you'd otherwise hand-wire?
2. How is AG-UI different from MCP and from A2A?
3. What is "shared state" between an agent and a UI?

---

### Day 25–28 — Build a full-stack agent with generative UI (the capstone)
🎯 **Goal:** Connect an agent backend to a React frontend via AG-UI, with the agent rendering real UI components.

🎓 **Learn (your main guide — free to audit):**
- DeepLearning.AI — **Build Interactive Agents with Generative UI**, taught by Atai Barkai (co-founder of CopilotKit, the team behind AG-UI): https://www.deeplearning.ai/courses/build-interactive-agents-with-generative-ui
- CopilotKit docs (your implementation reference): https://docs.copilotkit.ai

🛠️ **Do (Capstone Project):** Build a full-stack agentic app where:
1. **Backend:** a LangGraph (or CrewAI/Pydantic AI) agent exposes an AG-UI endpoint.
2. **Frontend:** a React app using CopilotKit connects to it.
3. The agent **renders UI on demand** — e.g., a chart, a form, or cards — not just text.
4. Add **human-in-the-loop** (the agent asks for approval before an action).
5. Add **shared state** (agent and user edit the same data — e.g., a canvas, a to-do list, or a dashboard).

Suggested capstone ideas:
- A **travel planner** that renders an itinerary card + map and asks you to confirm bookings.
- A **finance dashboard** agent that renders charts from data and lets you tweak filters.
- A **document co-editor** where the agent and you edit shared text/canvas together.

✅ **Checkpoint:**
1. How does the agent tell the frontend to render a specific component?
2. How does a user action in the UI flow *back* into the agent?
3. Where would you add a human approval step, and why?

---

### Day 29 — Polish, deploy & document
🎯 **Goal:** Make the capstone presentable and shareable.

🛠️ **Do:**
- Deploy: frontend on **Vercel** (free), backend on **Render**/**Railway**/**Fly.io** (free tiers).
- Record a 60–90 second demo video/GIF.
- Write a strong README: problem, architecture diagram, stack, what AG-UI/agent patterns you used, and a "what I'd improve next" section.

✅ **Checkpoint:** Can a stranger clone your repo and understand it in 5 minutes?

---

### Day 30 — Review, reflect & plan the next 30 days
🎯 **Goal:** Lock in learning and set direction.

🛠️ **Do:**
- Re-answer every weekly milestone checklist from memory.
- Write a short blog post / LinkedIn post on "What I learned building agents in 30 days" — teaching is the best test of mastery and great for visibility.
- Pick your **specialization** for the next month (see below).

✅ **FINAL Milestone — your portfolio now has:**
- [ ] Project 1: Tiny GPT from scratch
- [ ] Project 2: RAG "Chat with your documents" app
- [ ] Project 3: Useful autonomous agent (LangGraph/CrewAI)
- [ ] Project 4 (Capstone): Full-stack agent with AG-UI generative UI
- [ ] A written reflection / blog post

---

# 🏆 The 4 Portfolio Projects (summary)

| # | Project | Skills shown | Lands on |
|---|---|---|---|
| 1 | Tiny GPT from scratch | Transformers, training, fundamentals | Day 5–6 |
| 2 | RAG "Chat with your PDFs" | Embeddings, vector DB, LLM apps, UI | Day 10–12 |
| 3 | Autonomous tool-using agent | Agent loops, LangGraph/CrewAI, tools | Day 21–22 |
| 4 | Full-stack agent + AG-UI | Generative UI, full-stack, HITL, shared state | Day 25–28 |

These four, well-documented, are a *genuinely strong* junior-to-mid AI engineer portfolio.

---

# 📚 Master Resource Library (all links, grouped)

### Foundations & Gen AI (videos verified ✅ 15 Jun 2026)
- 3Blue1Brown — LLMs explained briefly: https://www.youtube.com/watch?v=LPZh9BOjkQs
- 3Blue1Brown channel (Neural Networks / Transformers series): https://www.youtube.com/@3blue1brown
- Karpathy — Intro to LLMs: https://www.youtube.com/watch?v=zjkBMFhNj_g
- Karpathy — Deep Dive into LLMs like ChatGPT: https://www.youtube.com/watch?v=7xTGNNLPyMI
- Karpathy — How I Use LLMs: https://www.youtube.com/watch?v=EWvNQjAaOHw
- Karpathy — Let's build GPT: https://www.youtube.com/watch?v=kCc8FmEb1nY
- Karpathy — Neural Networks: Zero to Hero (playlist): https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- Karpathy — nn-zero-to-hero (code): https://github.com/karpathy/nn-zero-to-hero
- Karpathy — YC AI Startup School 2025 (Software 3.0): https://www.youtube.com/watch?v=LCEmiRjPEtQ
- freeCodeCamp — Create an LLM from Scratch (Elliot Arledge): https://www.youtube.com/watch?v=UU1WVnMk4E8

### Structured free courses
- Hugging Face — LLM Course: https://huggingface.co/learn/llm-course
- Hugging Face — AI Agents Course (certified): https://huggingface.co/learn/agents-course
- Hugging Face — MCP Course: https://huggingface.co/learn/mcp-course
- DeepLearning.AI — Free short courses catalog: https://www.deeplearning.ai/short-courses/
- DeepLearning.AI — Build Interactive Agents with Generative UI (AG-UI): https://www.deeplearning.ai/courses/build-interactive-agents-with-generative-ui
- Google Cloud Skills Boost — search "Introduction to Generative AI" (free learning path): https://www.cloudskillsboost.google

### Agentic AI docs
- Anthropic — Building Effective Agents: https://www.anthropic.com/engineering/building-effective-agents
- LangGraph: https://langchain-ai.github.io/langgraph/
- LangChain (RAG & tools): https://python.langchain.com
- CrewAI: https://docs.crewai.com
- smolagents: https://github.com/huggingface/smolagents
- Model Context Protocol (MCP): https://modelcontextprotocol.io

### AG-UI & full-stack
- AG-UI docs: https://docs.ag-ui.com/introduction
- AG-UI GitHub + Dojo examples: https://github.com/ag-ui-protocol/ag-ui
- CopilotKit: https://www.copilotkit.ai and docs https://docs.copilotkit.ai
- React: https://react.dev/learn

---

# 🧭 After Day 30 — how to actually reach "pro"

30 days makes you *capable*. The next 2–3 months make you *strong*. Pick a direction:

- **AI Engineer (apps):** go deeper on RAG evaluation, agent reliability, observability (LangSmith), and deployment.
- **Generative AI / ML depth:** finish Karpathy's full *Zero to Hero* playlist, learn fine-tuning with LoRA on a real dataset, study evals.
- **Full-stack agentic products:** master AG-UI + CopilotKit deeply, ship a real product, contribute to the open-source AG-UI repo.

**Habits that compound:**
- Build in public (post weekly).
- Read one good paper/blog a week and summarize it in your own words.
- Re-implement, don't just watch.
- Keep one "real" project alive and keep improving it.

---

# ✅ Link verification note

Every YouTube link marked ✅ was checked and confirmed live on **15 June 2026**, including pulling the exact Karpathy video IDs from his own site (karpathy.ai) to avoid dead links. Course and documentation pages (Hugging Face, DeepLearning.AI, AG-UI, CopilotKit, LangGraph, CrewAI, MCP) were confirmed to exist as of the same date. Web content moves — if any single link ever 404s, search the exact title; these are all well-known, stable resources.

**One caution:** for DeepLearning.AI short courses I point you to the *catalog* and the course *name* rather than guessing deep URLs, because their course URLs change. Just search the course title on https://www.deeplearning.ai/short-courses/ — all the named courses are real and free to audit.

Good luck. Build every single day, and ship in public. 🚀
