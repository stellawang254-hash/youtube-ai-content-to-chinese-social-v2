# YouTube Search Strategy

Use this when the task starts from a topic, channel, or broad AI learning direction.

## Search Goal

Search for English YouTube content that is worth learning and possibly worth turning into Chinese content.

Learning value comes before popularity.

## Freshness Modes

### classic

Use when the user wants stable concepts, methods, or evergreen workflows.

Search examples:
- `AI agent from scratch tutorial`
- `LangGraph workflow tutorial`
- `tool calling AI agent implementation`
- `LLM workflow automation step by step`

### recent

Use when the user wants recent developments.

Search examples:
- `latest AI agent workflow 2026`
- `AI agent tutorial this month`
- `recent LangGraph best practices`
- `new AI coding agent workflow`

### hybrid

Use by default when the user does not specify freshness.

Process:
1. Search recent candidates first.
2. Add a small classic pass.
3. Keep recent candidates and classic supplements separate.

## Multi-Pass Search

Do not rely on one query.

Suggested passes:

1. Core topic:
   - `AI agent workflow`
   - `LLM automation`
   - `tool calling`

2. Practical build:
   - `from scratch`
   - `tutorial`
   - `step by step`
   - `implementation`

3. Method and reliability:
   - `best practices`
   - `production`
   - `evaluation`
   - `memory`
   - `orchestration`

4. Recent:
   - `latest`
   - `recent`
   - `this month`
   - `2026`

## Downrank

Downrank videos that are:

- pure news
- pure hype
- tool list without method
- demo without explanation
- too short to provide learning value
- not English-first
- enterprise-sounding but without implementation detail

## Candidate Output

For each candidate, capture:

- title
- channel
- URL
- publish date if available
- duration
- likely topic
- why it might be worth learning
- why it might not be worth publishing

