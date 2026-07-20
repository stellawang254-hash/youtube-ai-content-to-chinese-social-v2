# Route Decision

Use this file before writing any public-facing output.

## Inputs

Accept any of:
- English YouTube URL
- English transcript
- Existing Chinese learning note
- AI topic plus source notes

Optional but important:
- enterprise_problem
- target_decision_maker
- content_goal
- platform_goal
- practical_result

## Step 1: Learning Value

Score the source:
- S: Strong method, workflow, demo, reusable pattern, and implementation value
- A: Clear method or structure with useful learning value
- B: Useful perspective but weak implementation depth
- C: Interesting but shallow, newsy, or fragmented
- D: Not worth processing

If learning value is C or D, do not generate public content unless the user explicitly asks.

## Step 2: Public Publishing Fit

A source is suitable for normal WeChat only if it can become a self-contained Chinese article.

Positive signals:
- Has a clear reader problem
- Has a method, workflow, or judgment
- Can be reorganized beyond the video order
- Can stand alone without watching the video
- Supports a useful title and argument

Negative signals:
- Only valuable as personal notes
- Too dependent on code or screen details
- Too fragmented
- Mostly news, hype, or tool list
- Cannot produce a clear Chinese reader benefit

## Step 3: Enterprise AI Fit

A source is suitable for enterprise AI implementation content only if it can answer:

- What enterprise problem does this map to?
- Who is the target decision maker?
- What business scenario is concrete enough?
- What conditions must be true before implementation?
- What investment is required?
- What return is plausible?
- What risks could block adoption?
- What practical result or validation path can the author provide?
- What objection should be included?
- What lead-capture action naturally follows?

If any of the first four answers are vague, do not use the enterprise route.

## Recommended Output Format

```yaml
learning_value: S/A/B/C/D
learning_reason: ""
keep_learning_note: true/false

normal_wechat_fit:
  fit: yes/no
  reason: ""

enterprise_ai_fit:
  fit: yes/no
  enterprise_problem: ""
  target_decision_maker: ""
  reason: ""

recommended_route: learning_only / normal_wechat / enterprise_ai / normal_and_enterprise
do_not_generate:
  - ""
next_required_inputs:
  - ""
```

## Route Rules

- If learning is strong but publishing fit is weak, choose learning_only.
- If normal WeChat fits but enterprise fields are vague, choose normal_wechat.
- If enterprise route fits, still preserve the learning note first.
- If both routes fit, generate separate versions. Do not blend them into one article.

