# Transcript Extraction Fallbacks

Use this file when subtitle extraction is not enough.

## Preferred Path

1. Manual English subtitles
2. Auto English subtitles
3. Transcript
4. Audio transcription

## When to Retry

Retry extraction when:

- the first subtitle source is incomplete
- the transcript is clearly noisy
- the language detection is inconsistent
- technical terms are badly distorted

## Whisper Fallback

If no usable subtitles exist, download the audio and transcribe locally.

Use this only as a fallback, not the default.

## Stop Conditions

Stop and report failure when:

- the video has no usable English audio path
- the transcription is too broken to clean
- the result would be misleading to a downstream learning note

