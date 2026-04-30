# /inbox/for_chatgpt/

This directory holds research prompts prepared by C-7RO (Perplexity Computer / Claude Sonnet 4.6) for **ChatGPT GPT-5 Pro** (with GitHub connector + live web browsing).

## Workflow

1. C-7RO drafts a prompt and saves it here as `YYYY-MM-DD_short-name.md`
2. Martin sends it to ChatGPT Pro in a fresh chat (GitHub connector ON, GPT-5 Pro reasoning mode, no deep research unless explicitly noted)
3. ChatGPT's response is saved to `/inbox/from_chatgpt/YYYY-MM-DD_short-name_response.md`
4. C-7RO integrates the findings into papers, fixes errors, opens new lanes if needed
5. The lane register `RESEARCH_LANES.md` is updated to reflect new status

## Why this directory exists

ChatGPT Pro's three tools (GitHub connector, live web search, deep research) cannot all run in one query. So we treat each prompt as a single-tool task:

- **GitHub connector + reasoning** → for questions where prior repo context matters
- **Live web search + reasoning** → for fact-checking or recent literature
- **Deep research** → for "explore this corner of the field" tasks (15+ minute runs)

Each prompt explicitly states which tool combo to use.

## Prompt format

Every prompt should:
- State the tool combo (GitHub-connector / web-search / deep-research)
- State the section of which paper it informs
- Include enough context that the prompt is self-contained even without the GitHub connector
- Specify a structured deliverable (Sections A–F, table, etc.)
- Include a "don't water it down" / "negative results are fine" clause where appropriate

## Cadence

Two to three prompts per week, not daily. Pace beats volume. ChatGPT Pro burns time on vague prompts; sharp prompts return in 5-15 minutes with high quality.

— C-7RO
