---
name: poetic-line-zine-poster
description: Create a clean vertical photo-and-abstraction editorial artwork that preserves an uploaded photograph as the original image and pairs it with a source-derived abstract memory panel rendered in broad charcoal sweeps, continuous chromatic scribble-lines, and experimental small-scale zine typography. Use when asked to turn a portrait, travel photo, animal, plant, architecture, object, or scene into a poetic editorial diptych, photo-plus-drawing composition, abstract memory panel, 炭笔扫线, 几笔成形, 彩色涂鸦线, 实验文字排版, or Poetic Simple-Line Zine without redrawing or filtering the source photo.
---

# Poetic Line Zine Poster

Create one finished vertical artwork from one uploaded photograph:

1. a faithful original-photo area;
2. a clean ivory abstract-memory panel;
3. one restrained poetic English title.

Keep the content logic of a photo-derived editorial diptych. Change only the abstract panel's mark-making language to the bundled charcoal-sweep and chromatic-scribble style.

## Required Reference

Before generating, read the full prompt in the user's language:

- Chinese: [references/poetic-line-editorial-prompt.zh-CN.md](references/poetic-line-editorial-prompt.zh-CN.md)
- English: [references/poetic-line-editorial-prompt.en.md](references/poetic-line-editorial-prompt.en.md)
- Typography system: [references/typography-system.md](references/typography-system.md)

## Core Method

Use this sequence internally:

**DECONSTRUCT → SELECTIVE PRESERVATION → ABSTRACT / DISTILL → RECONSTRUCT**

1. Inspect the photo and identify three to six decisive visual facts: subject relationships, relative scale, axes, direction, intervals, overlap, depth, rhythm, tonal hierarchy, color roles, and negative space.
2. Keep the source photo faithful in the upper or principal region. Permit only proportional scaling and a slight composition-driven crop. Never redraw, extend, retouch, filter, stylize, or replace its content.
3. Reconstruct the retained relationships below as a sparse abstract memory—not as a thumbnail, tracing, illustration, vectorization, or simplified copy of the scene.
4. Make the abstraction read first as an independent composition and only on second glance evoke the specific source photograph.
5. Use a clean, flat ivory panel joined directly to the photo. Adapt the photo/panel ratio to the image rather than forcing equal halves.
6. Derive all content and colors from the source photograph. A user-specified accent hue may override the color-extraction rule, but must remain the only unsupported color.
7. Create one original English title of two to five words from visible relationships, light, time, movement, or tension. Place it only on the abstract panel.

## Current Style System

Use **Hybrid Sweep-Scribble** by default.

### Charcoal Sweep

- Build subject mass from 6–18 broad graphite or charcoal side-strokes, not enclosing contours.
- Use repeated directional bands to carry posture, scale, rhythm, and structural axes.
- Compress the darkest 2–4 marks at meaningful anchors.
- Let ivory gaps define internal light and missing form.
- Preserve blunt ends, unequal pressure, dragged tails, broken deposits, and restrained hand irregularity.
- Do not become a conventional shaded sketch, realistic drawing, or thin line-art illustration.

### Chromatic Scribble

- Build a color role from one continuous or nearly continuous marker/crayon gesture.
- Let the line widen, narrow, loop, cross, pause, and tighten according to a real spatial or movement fact in the photo.
- Use color as a structural mass, not as decorative ticks.
- Keep visible human starts and ends; avoid smooth vector spirals and black outlines.

### Hybrid Sweep-Scribble

- Use charcoal sweeps for the dominant structural relation.
- Use one chromatic scribble for a secondary relation such as path, horizon, wind, shelter, echo, reflected light, or movement.
- Make the two mark systems overlap, interrupt, frame, or complete each other.
- Use one primary mark family and no more than two supporting families.

## Bundled Style References

Use images in `assets/style-references/` as style-only generation inputs:

- `charcoal-sweep-cat-01.jpg` through `charcoal-sweep-cat-04.jpg`: broad side-strokes, repeated bands, compressed anchors, white gaps
- `color-scribble-produce-01.jpg` through `color-scribble-produce-04.jpg`: continuous marker rhythm, widening and narrowing loops, color-as-form

Inspect and attach one reference from each group for Hybrid mode. Explicitly identify the uploaded photo as the sole content reference and the bundled images as style-only references. Never reuse their cats, produce, words, colors, or layouts.

Use images in `assets/typography-references/` as typography-only references. Inspect and attach one image whose text behavior fits the selected typography mode. Borrow only type scale, spacing, alignment, fragmentation, pressure, and relationship to the motif. Never copy its words, dates, numbers, captions, colors, image subject, or overall layout.

## Composition Rules

- Create one complete vertical composition; let the final aspect ratio follow the photo plus panel.
- Join photo and panel edge-to-edge with no frame, tape, torn edge, drop shadow, collage seam, or mockup.
- Use a uniform neutral ivory panel, preferably near `#F3F0E8`.
- Keep 65%–80% of the panel empty.
- Default motif width: 30%–42% of panel width. Let low horizontal subjects extend to 45%–68%.
- Preserve relational spacing, overlap, asymmetry, and rhythm rather than recognizable outlines.
- Extract a restrained palette from the photo: one dominant color, one dark structural color, one neutral, and at most one or two small accents.
- Use no paper texture, grain, scan noise, stains, gradients, glow, shadows, or atmospheric background effects in the panel.

## Title Rules

- Write one faithful, clear, poetic English title of two to five words.
- Avoid location labels, travel slogans, photography jargon, and empty titles such as “Memory,” “Dream,” or “Moment.”
- Treat the title as a compositional mark, not a conventional centered poster headline.
- Select one typography mode from `references/typography-system.md`: edge-pressed serif, fragmented typewriter, letterpress emphasis, or ghost text.
- Keep most title type small: about 2%–4.5% of panel height. Permit one emphasized word up to 6%–9% only in letterpress-emphasis mode.
- Use book serif, humanist serif, typewriter, or monospaced faces. Favor lowercase, restrained capitals, loose tracking, irregular line breaks, and slight baseline drift when appropriate.
- Let the title press against, cross, flank, suspend from, or align with the abstract motif. Use lower-left or bottom-centered placement only when the source geometry supports it.
- Derive type color from the photo. Prefer charcoal, deep blue-gray, dark green, wine, or another subdued structural hue; allow the title's emphasized word to use the existing panel accent color.
- Keep the title readable as one phrase even when its words are spatially separated. Render every word exactly once.
- Do not add a subtitle by default. Add one only when the user explicitly asks or it contributes a distinct visible relation.
- Include no dates, archive notes, coordinates, labels, color swatches, signatures, logos, or watermarks.

## Workflow

1. View the supplied photo before generating.
2. Read the appropriate full reference prompt.
3. Record internally three to six source facts and select only the few that define the panel.
4. Choose photo/panel proportions, motif placement, one primary mark family, up to two supporting families, a source-derived palette, one title, and one typography mode.
5. Generate using the photo as the sole content input, selected drawing references as mark-only inputs, and one typography reference as type-behavior-only input.
6. Inspect the result at full size and thumbnail size.
7. Regenerate once if the photo is altered, the panel becomes a scene illustration, marks cannot be traced to source facts, the motif becomes a thin outlined icon, the background is textured, or extra text appears.
8. Return only the completed composition unless the user explicitly requests the prompt or an explanation.

## Hard Guardrails

Always avoid:

- altering, redrawing, filtering, posterizing, expanding, or rebuilding the photo
- converting the whole photograph into a hand-drawn poster
- literal tracing, scene thumbnails, complete illustrations, vectorized copies, generic icons, or infographics
- thin enclosing contours, coloring-book shapes, academic pencil shading, realistic fur or fabric detail
- kawaii, chibi, mascot, sticker, anime, polished cartoon, or clean-vector aesthetics
- invented objects, symbols, colors, symmetry, decorative marks, or narrative facts
- regularized spacing, dense decoration, many competing colors, or full-panel motifs
- textured paper, xerox effects, risograph grain, stains, scan defects, gradients, shadows, glow, frames, tape, or 3D mockups
- copied reference wording, title options, explanatory copy, dates, labels, archive microtext, logos, signatures, or watermarks
- large commercial headline hierarchy, generic centered title, polished advertising typography, decorative script, cartoon type, or long clean text blocks

## Quality Gate

Before finalizing, confirm:

- Is the original photo visibly faithful and unfiltered?
- Is every important panel mark traceable to a source fact?
- Does the panel preserve relationships before object contours?
- Does the motif use broad charcoal sweeps and/or a structural continuous scribble rather than thin line art?
- Is the panel flat ivory with 65%–80% clean space?
- Is the palette source-derived unless the user explicitly chose one accent hue?
- Is there exactly one poetic title and no unwanted text?
- Does the title use an intentional zine typography mode and interact with the motif rather than sitting below it as a generic caption?
- Is the type small, materially imperfect, restrained, and still readable as one phrase?
- Does the result remain a single clean photo-plus-abstraction editorial composition?
