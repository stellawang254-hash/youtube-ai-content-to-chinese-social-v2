# Source Ops

Use this layer when the user gives only a YouTube URL, channel, search topic, or raw video list.

## Purpose

Recover a usable English source before any learning or publishing route.

## Operating Order

1. Search English YouTube candidates.
2. Apply topic and learning-value filters.
3. Fetch metadata.
4. Try manual subtitles first.
5. Try auto subtitles or transcript.
6. Fall back to audio transcription.
7. Clean the transcript.
8. Only then move into learning notes and route decision.

## Search Strategy

Use multiple passes when needed:

- broad topic pass
- topic + tutorial / build / workflow pass
- recent / latest / this month pass
- classic / evergreen pass

Do not trust one search pass when the topic is broad.

## Metadata

If available, capture:

- title
- channel
- publish date
- duration
- view count
- like count
- comment count
- description
- subtitle availability
- language hint

## Subtitle Priority

1. Manual English subtitles
2. Auto English subtitles
3. Transcript
4. Audio transcription

## Fallback Rules

If subtitles are missing or weak:

- retry with a looser language setting
- try the platform transcript path
- try audio transcription
- if still weak, mark the source as insufficient and stop before publishing

## Cleaning Rules

Clean the text without turning it into prose:

- remove numbering and timestamps
- remove obvious repeated subtitle lines
- remove filler noise
- normalize obvious technical terms
- keep uncertainty if terms are unclear

## Failure Handling

Return a clear failure note when:

- there is no English source material
- subtitle extraction fails
- transcription quality is too poor
- terminology is too noisy
- the video is not really English-first

