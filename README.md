# YouTube AI Content to Chinese Social 2.0

This is a learning-first Codex/Hermes skill for turning English YouTube AI content into Chinese learning notes, then routing the material into the right publishing path.

## What 2.0 Adds

- Keep Chinese learning notes as the base output.
- Keep the source-ops layer for search, subtitles, transcription, and cleaning.
- Decide whether the source is suitable for public publishing.
- Split publishing into normal WeChat content and enterprise AI implementation content.
- Require enterprise content to include business scenario, applicable conditions, investment and return, implementation risks, practical judgment, objections, and one lead-capture action.
- Block fabricated enterprise context, ROI numbers, client cases, and personal test claims.
- Preserve the author's personal voice through practical testing, clear judgment, and conservative implementation advice.

## Main Workflow

```text
English YouTube AI material
  -> Chinese learning notes
  -> route decision
  -> learning only / normal WeChat / enterprise AI WeChat / platform variants
```

## Key Files

- `SKILL.md`: main workflow and routing instructions
- `references/route_decision.md`: publishability and enterprise-fit router
- `references/source_ops.md`: search / subtitle / transcription / cleaning layer
- `references/transcript_extraction_fallbacks.md`: fallback paths for transcript capture
- `references/transcript_cleaning_rules.md`: what cleaning may and may not do
- `references/learning_note_template.md`: required learning-note base
- `references/normal_wechat_article.md`: normal public WeChat route
- `references/enterprise_opportunity_brief.md`: enterprise AI opportunity brief
- `references/enterprise_wechat_article.md`: enterprise AI demand-generation article
- `references/personal_voice_profile.md`: author voice constraints
- `references/lead_capture_actions.md`: lead-capture actions
- `references/platform_variants.md`: WeChat, Xiaohongshu, and short-video variants
- `scripts/clean_subtitles.py`: SRT cleanup helper

## Usage Examples

```text
Use this skill to process this English YouTube AI Agent video. First write Chinese learning notes, then decide whether it should become a normal WeChat article or enterprise AI implementation article.
```

```text
Use this skill on this learning note. Target decision maker: operations manager. Enterprise problem: repetitive manual data collection and reporting.
```
