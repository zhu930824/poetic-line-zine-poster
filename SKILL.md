---
name: poetic-line-zine-poster
description: Create a clean vertical photo-and-abstraction editorial artwork from an uploaded portrait, travel photo, animal, plant, architecture, object, or scene. Preserve the source photo, distill its relationships into broad charcoal sweeps and one structural chromatic scribble, add restrained experimental English typography, and deliver an exact requested aspect ratio through deterministic composition and validation. Use for poetic editorial diptychs, photo-plus-drawing zines, abstract memory panels, 炭笔扫线, 几笔成形, 彩色涂鸦线, 实验文字排版, Poetic Simple-Line Zine, or requests to make the subject more abstract without turning the photograph into a sketch.
---

# Poetic Line Zine Poster

Create one finished artwork from one uploaded photograph. Preserve the photograph in one region and pair it with a source-derived abstract panel on flat ivory. Add one short English title through deterministic typesetting.

## Read before work

Read the full generation prompt in the user's language:

- Chinese: [references/poetic-line-editorial-prompt.zh-CN.md](references/poetic-line-editorial-prompt.zh-CN.md)
- English: [references/poetic-line-editorial-prompt.en.md](references/poetic-line-editorial-prompt.en.md)

Read these references for each generation:

- [references/subject-routing.md](references/subject-routing.md) for subject route and abstraction level
- [references/typography-system.md](references/typography-system.md) for title mode
- [references/two-stage-pipeline.md](references/two-stage-pipeline.md) for composition commands

Read [references/evaluation-rubric.md](references/evaluation-rubric.md) when changing or evaluating the Skill.

## Default controls

Choose explicit values before generation:

| Control | Default | Options |
|---|---|---|
| abstraction | `balanced` | `restrained`, `balanced`, `expressive` |
| subject route | inferred | `gesture`, `mass`, `rhythm`, `path`; use at most two |
| mark system | `hybrid` | charcoal primary, one chromatic scribble secondary |
| typography | inferred | `edge`, `fragmented`, `letterpress`, `ghost` |
| output | source-driven vertical | honor an explicit ratio such as `9:16` |
| accent | source-derived | accept one user-specified unsupported hue |

Map requests such as “更抽象”“再简笔一点” to `restrained`. Map requests for stronger energy or denser architectural rhythm to `expressive`.

## Core method

Use this sequence internally:

**DECONSTRUCT → SELECTIVE PRESERVATION → ABSTRACT / DISTILL → RECONSTRUCT**

1. Inspect the source photo at full size.
2. Identify three to six visual facts: scale, axis, direction, interval, overlap, depth, density, color role, and negative space.
3. Select one primary subject route and one optional secondary route.
4. Select an abstraction level.
5. Write a two-to-four-row fact-to-mark map using `source fact -> retained relation -> abstract mark`.
6. Delete surface texture, incidental background detail, and any mark without a source fact.
7. Make the panel read first as an independent composition and evoke the source on second glance.

Keep the analysis and map out of the final artwork.

## Mark system

### Charcoal sweep

- Build the dominant mass with the mark count assigned by the abstraction level.
- Use broad graphite or charcoal side-strokes with blunt ends, pressure changes, dragged tails, and broken deposits.
- Compress darkness into two to four structural anchors.
- Let ivory gaps define internal light and missing form.
- Carry posture, scale, rhythm, and structural axes through directional bands.
- Avoid enclosing contours, academic shading, realistic detail, and thin line art.

### Chromatic scribble

- Use one continuous or near-continuous crayon or marker gesture for the secondary relation.
- Map every widening, loop, crossing, pause, and tightening to a path, horizon, reflection, wind, shelter, color mass, or motion fact.
- Keep visible human starts and ends.
- Avoid decorative ticks, perfect spirals, black outlines, smooth vectors, and gradients.

### Interaction

- Make charcoal and color overlap, interrupt, frame, extend, or complete each other.
- Use one primary mark family and no more than two supporting families.
- Keep 65%–80% of the panel empty.

## Reference assets

Use the uploaded photo as the sole content reference.

Use one suitable image from each required asset group as style-only input:

- `assets/style-references/charcoal-sweep-cat-*.jpg`: side-stroke width, anchors, breaks, and white gaps
- `assets/style-references/color-scribble-produce-*.jpg`: continuous-line rhythm and color-as-form
- `assets/typography-references/`: type scale, spacing, alignment, fragmentation, and print behavior

State that local reference images supply style behavior only. Do not copy their cats, produce, words, colors, dates, objects, or layouts.

## Composition

- Generate one vertical photo-plus-panel composition.
- Keep the source photo unchanged apart from proportional resize and composition-driven crop.
- Join photo and panel edge-to-edge without a frame, tape, torn edge, shadow, seam, or mockup.
- Use a uniform panel near `#F3F0E8`.
- Adapt the photo share to source geometry: landscape `0.48`, square `0.55`, portrait `0.62`; permit a user override from `0.30` to `0.72`.
- Keep a compact motif. Let low horizontal subjects extend farther than vertical motifs.
- Derive one dominant hue, one dark structural hue, and one neutral from the photo. Add at most one user-specified unsupported accent.
- Keep the panel free of texture, grain, stains, gradients, shadows, glow, and atmospheric effects.

## Typography

Create one original English title of two to five ASCII words from a visible relation, action, light condition, direction, pause, or tension.

- Avoid location labels, travel slogans, photography jargon, and empty words such as `Memory`, `Dream`, or `Moment`.
- Generate the title before rendering and verify each word.
- Choose one mode from the typography reference.
- Keep type small and subordinate to the motif.
- Render every word once through `scripts/render_typography.py`.
- Add no subtitle, date, coordinates, archive text, labels, logo, signature, or watermark unless the user requests a subtitle.

## Production workflow

Use the two-stage pipeline by default:

1. Generate only the abstract panel. Exclude the source photograph, title, frame, seam, and mockup from this generated artifact.
2. Compose the original source photo and generated panel with `scripts/compose_poster.py`.
3. Add the verified title with `scripts/render_typography.py`.
4. Validate ratio, photo fidelity, and panel corners with `scripts/validate_output.py`.
5. Inspect the final image at full size and thumbnail size.
6. Regenerate the panel once when a visual guardrail fails. Fix composition or typography through the scripts when those checks fail.
7. Return only the completed artwork unless the user requests the prompt or analysis.

Use a one-pass generated composition only when deterministic local composition cannot run. State no implementation detail to the user; inspect the same quality gates before returning the image.

## Hard guardrails

Reject work that contains any of these faults:

- altered, redrawn, filtered, posterized, expanded, or rebuilt source photo
- complete scene illustration, photo thumbnail, tracing, vector copy, generic icon, or infographic in the panel
- thin enclosing contours, coloring-book shapes, academic pencil shading, realistic fur, or fabric detail
- kawaii, mascot, anime, sticker, polished cartoon, or clean-vector treatment
- invented objects, symbols, narrative facts, symmetry, or unsupported colors
- regular spacing, dense decoration, competing palettes, or full-panel motifs
- textured paper, xerox effects, risograph grain, stains, scan defects, gradients, shadows, glow, tape, or 3D mockups
- copied reference words, dates, numbers, captions, logos, signatures, or watermarks
- misspelled title, duplicated word, commercial headline, centered caption, decorative script, or pseudo-archive text

## Quality gate

Confirm before delivery:

- The photo region matches the source after crop and resize.
- The output ratio matches the request.
- Two to four recorded source facts explain the important panel marks.
- The selected route and abstraction level control the motif.
- Broad sweeps and one structural scribble replace object contours.
- The panel retains 65%–80% clean ivory space.
- The palette follows the source and user accent rule.
- One verified title interacts with the motif and each word appears once.
- The finished artifact reads as one clean editorial composition.
