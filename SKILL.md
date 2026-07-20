---
name: youtube-ai-content-to-chinese-social-v2
description: Turn English YouTube AI videos, transcripts, or AI learning topics into Chinese learning notes first, then route them into either normal WeChat publishing, enterprise AI implementation content for demand generation, Xiaohongshu notes, or short video scripts. Use when the user wants learning-first Chinese content from YouTube AI material, wants to judge whether a video is publishable, wants enterprise AI landing/advisory articles for decision makers, or wants each article to include practical judgment, objections, risks, ROI, and a lead-capture action.
---

# YouTube AI Content to Chinese Social 2.0

## Core Idea

Use this skill to process English YouTube AI content into Chinese learning assets first, then decide whether it should become public content.

Do not force every YouTube learning item into an article. The learning note is the stable base. Publishing is conditional.

## Default Workflow

Follow this sequence unless the user explicitly narrows the task:

1. Run source ops if the user only gives a URL, channel name, or search topic.
2. Extract or accept the English source material.
3. Produce Chinese learning notes, a method summary, and an actionable checklist.
4. Run the route decision.
5. If publishable, choose one or more output routes.
6. Apply the personal voice profile before writing.
7. Add platform-specific versions only after the route is clear.

## Source Ops

Read `references/source_ops.md` when the task starts from a YouTube URL, channel, keyword, or any source that still needs discovery, subtitle extraction, transcription, or transcript cleaning.

Source ops should handle:
- English YouTube search
- multi-pass search
- metadata fetching
- subtitle extraction
- transcript fallback
- Whisper fallback
- SRT cleaning
- failure handling

If the user already provides a clean transcript or a learning note, skip source ops unless they ask for verification or recovery.

## Required Routes

There are three possible outcomes:

### Learning Only

Use when the content has learning value but is too narrow, fragmented, technical, source-dependent, or weakly structured for public publishing.

Output:
- Chinese learning notes
- Chinese method summary
- Chinese actionable checklist
- Optional migration ideas
- Reason not to publish

### Route 1: Normal WeChat Content

Use when the content can become a useful Chinese article but does not naturally map to a concrete enterprise AI implementation problem.

Output:
- Chinese learning notes
- Normal WeChat article
- Optional Xiaohongshu note
- Optional short video script

### Route 2: Enterprise AI Implementation Content

Use only when the content can connect to a real enterprise problem and a clear target decision maker.

Required inputs or inferred fields:
- enterprise_problem
- target_decision_maker
- business_scenario
- practical_result_or_validation_path

Output:
- Chinese learning notes
- Enterprise opportunity brief
- Enterprise WeChat article
- Platform variants
- One lead-capture action

## Route Decision

Read `references/route_decision.md` before deciding routes.

Always answer:

- Is it worth learning?
- Is it suitable for public publishing?
- Is it suitable for enterprise AI implementation content?
- What route is recommended?
- What evidence supports the route?
- What should not be generated?

Do not generate normal or enterprise articles when the route decision says not to.

## Learning Base

Read `references/learning_note_template.md` when producing the learning base.

Learning notes must include:
- What the source is really about
- Core conclusion
- 3-7 valuable points
- Method or workflow extracted
- What can be tried today
- What is still uncertain
- Whether the material is worth publishing

## Source Ops Details

Read these files when the task involves acquisition or cleaning:
- `references/source_ops.md`
- `references/youtube_search_strategy.md`
- `references/transcript_extraction_fallbacks.md`
- `references/transcript_cleaning_rules.md`
- `references/test_cases.md`

Use the `scripts/clean_subtitles.py` helper when the input is an SRT subtitle file with repeated lines.

## Normal Publishing Route

Read `references/normal_wechat_article.md` for Route 1.

Normal WeChat content should:
- Be based on Chinese learning notes, not raw subtitles
- Preserve learning-first value
- Include the author's judgment
- Avoid translation tone
- Avoid enterprise framing when it is not naturally supported

## Enterprise AI Route

Read these files for Route 2:
- `references/enterprise_opportunity_brief.md`
- `references/enterprise_wechat_article.md`
- `references/lead_capture_actions.md`

Enterprise AI content must include:
- Business scenario
- Target decision maker
- Applicable conditions
- Non-applicable conditions
- Investment and return
- Implementation risks
- Practical result or validation path
- The author's judgment
- A counterargument or objection
- One lead-capture action

Never write enterprise AI implementation content by only summarizing or translating YouTube material.

## Personal Voice

Read `references/personal_voice_profile.md` before producing publishable outputs.

The article voice should come from:
- Practical testing
- Clear judgment
- Conservative implementation advice
- Willingness to say "not suitable"
- Business-context thinking

Do not simulate personality with catchphrases. Express the author's personality through judgment density, tradeoffs, objections, and grounded examples.

## Platform Variants

Read `references/platform_variants.md` when the user asks for multiple platforms or when the route recommends them.

Default platform mapping:
- Normal WeChat: long-form learning article
- Enterprise WeChat: demand-generation article for decision makers
- Xiaohongshu: compressed key insight, checklist, or warning note
- Short video: spoken explanation with a clear hook and one action

Do not reuse one article unchanged across platforms.

## Output Discipline

Always avoid:
- Direct translation from subtitles
- Pure summary of the YouTube video
- Hype-first AI writing
- Generic "AI era" openings
- Enterprise advice without business scenario, conditions, risks, and ROI
- Lead-capture actions that do not match the article

Prefer:
- Learning first
- Route clarity
- Practical judgment
- Explicit objections
- Narrow business scenarios
- One clear next action

## Minimal Invocation Examples

User: "Process this YouTube AI Agent video and tell me whether it is worth publishing."

Output:
- Learning notes
- Route decision
- Publish / no-publish reason

User: "Turn this learning note into a normal WeChat article."

Output:
- Route 1 check
- Normal WeChat article
- Optional Xiaohongshu version

User: "Use this video to write an enterprise AI implementation article for operations managers."

Output:
- Route 2 check
- Enterprise opportunity brief
- Enterprise WeChat article
- One lead-capture action
