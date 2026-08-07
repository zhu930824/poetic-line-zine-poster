# Evaluation Rubric

Use this rubric on a fixed test set after changing prompts, references, scripts, or routing rules.

## Test set

Keep 12–20 source photos. Include people, animals, architecture, nature, paths, and one cluttered scene. Reuse the same photos and user prompts for each release candidate.

## Scoring

Rate each dimension from 0 to 10.

| Dimension | Weight | A score of 8–10 means |
|---|---:|---|
| source fidelity | 25 | the photo region matches the supplied image after crop and resize |
| abstraction | 20 | the panel reads as an independent composition before it evokes the source |
| traceability | 20 | each major mark maps to a recorded source fact |
| composition | 15 | the motif, photo split, and empty space form one balanced page |
| typography | 10 | one correct title remains readable and interacts with the motif |
| color restraint | 10 | the palette follows the source and uses at most one unsupported accent |

Run `scripts/score_output.py` with the six ratings. Accept a candidate at 75 or above. Reject any candidate that breaks a hard guardrail even if its weighted score passes.

## Automatic checks

Run `scripts/validate_output.py` after composition and typography. Require:

- exact requested aspect ratio within the configured tolerance;
- source-photo pixel fidelity after the same crop and resize;
- clean ivory samples in the panel corners.

## Comparison protocol

Generate one baseline and one candidate for each test photo. Review them at full size and thumbnail size. Record the score, rejected guardrails, route, abstraction level, typography mode, and title. Change one system variable per comparison.
