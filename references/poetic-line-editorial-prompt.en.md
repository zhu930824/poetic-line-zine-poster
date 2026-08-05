# Poetic Sweep-Scribble Photo Editorial — Full Prompt Specification

## 1. Finished structure

Treat the uploaded photograph as the sole content source. Create one complete vertical editorial artwork composed of:

**a faithful original-photo area + a source-derived abstract memory panel + one poetic English title.**

Keep the photograph unchanged. Reconstruct only its observed spatial, rhythmic, tonal, and color relationships in the lower panel using broad charcoal sweeps and continuous chromatic scribble-lines. This is not full-image line-art conversion, filtering, vectorization, or style transfer.

## 2. Two roles of the input photograph

1. **Original photograph:** present it faithfully in the upper or principal region. Permit only proportional scaling and a slight crop needed for the join. Do not redraw, extend, retouch, color-grade, filter, embellish, replace, or alter its content.
2. **Information source:** inspect subject relationships, relative scale, left/right and upper/lower positions, axes, directions, curves, spacing, repetition, occlusion, depth, tonal hierarchy, color roles, and negative space.

Do not introduce unsupported objects, scenes, symbols, or colors. The sole exception is one accent hue explicitly requested by the user. Bundled images are style references only, never content references.

## 3. Internal method

Use this sequence without printing the analysis:

**DECONSTRUCT → SELECTIVE PRESERVATION → ABSTRACT / DISTILL → RECONSTRUCT**

Identify three to six decisive visual facts. Separate subject mass from relational information. Remove surface detail, perspective noise, background clutter, and low-information ornament. Reorganize the retained relationships with the fewest marks possible. The panel should read first as an independent abstraction and only on second glance recall the specific photograph.

Never produce a scene thumbnail, tracing, full illustration, vector copy, or generic icon.

## 4. Recognition level

Prioritize relationships and retain only minimum necessary recognition cues:

- People: head direction, shoulder slope, torso axis, limb rhythm, spacing, and occlusion; no realistic faces, fingers, or clothing detail.
- Animals: head/body mass, spine curve, limb rhythm, ear/tail direction, and one marking.
- Plants: canopy mass, trunk direction, and gathering or dispersing rhythm; no individual leaves.
- Architecture: one to three identity cues such as eave lines, arches, tapering tower mass, spires, or layered rhythm; no windows or ornament.
- Crowds: one to three irregular charcoal marks per person; no separate circular heads or limbs.
- Roads, shores, railings, and horizons: one or two horizontal sweep groups with source-faithful interruptions.
- Small objects: two or three planar or linear marks, recognized through scale and position.

## 5. Mark-making language

Use **Hybrid Sweep-Scribble** by default.

### Charcoal Sweep

- Build the dominant mass from about 6–18 broad graphite or charcoal side-strokes rather than enclosing contours.
- Align the stroke direction with observed spines, shoulders, architectural layers, horizons, wind, movement, or repeated rhythm.
- Compress the darkest values at two to four meaningful anchors.
- Let clean ivory gaps cut through the mass to create internal light and missing form.
- Preserve pressure variation, blunt starts, dragged tails, and broken deposits without becoming conventional tonal shading.

### Chromatic Scribble

- Use one continuous or nearly continuous thick marker/crayon gesture for the secondary color relation.
- Let it widen, narrow, loop, cross, pause, tilt, or tighten according to a real source fact.
- Use it for a path, horizon, wind, reflection, canopy, light cluster, crowd rhythm, or movement echo.
- Keep visible human starts and ends. Avoid perfect spirals, digital smoothing, gradients, and black outlines.

### Hybrid relation

Use charcoal for the primary structural relation and one chromatic scribble for the secondary movement or color relation. Make them overlap, interrupt, frame, extend, or complete each other. Use one primary mark family and at most two supporting families.

## 6. Color system

Extract and reduce colors from the source photograph:

- one dominant color role;
- one dark structural role;
- one light or neutral role;
- at most one or two small accent roles.

Reduce saturation and color count. If the user explicitly requests cobalt, tomato red, or another hue, use it as the only unsupported accent; keep every other color source-derived.

## 7. Adaptive join

Do not force equal halves:

- Landscape or strongly horizontal photo: photo area about 38%–52% of total height.
- Vertical person, architecture, or tall subject: photo area about 55%–68%.
- Near-square or balanced photo: photo area about 48%–58%.
- Shift these values by about 8% when composition requires it.

Join photo and panel directly with no frame, tape, torn edge, shadow, collage seam, dimensional card, or mockup.

## 8. Panel layout

- Use a perfectly even neutral ivory background near `#F3F0E8`.
- Default motif width: 30%–42% of panel width.
- Default motif height: no more than 28%–34% of panel height.
- Low horizontal subjects may extend to 45%–68% of panel width while staying shallow.
- Keep 65%–80% clean empty space.
- Place the motif lower-middle, near center, or asymmetrically when supported by source relationships.
- Preserve irregular spacing, overlap, scale differences, center of gravity, and asymmetry.

## 9. CLEAN mode

The panel background must contain no gradient, lighting variation, shadow, glow, vignette, paper texture, grain, noise, fiber, watercolor wash, fog, stain, fading, scan mark, pasted texture, compression artifact, or banding.

Marks may have restrained charcoal tooth and hand irregularity, but the background remains clean. Create atmosphere through whitespace, distance, pause, asymmetry, scale contrast, limited marks, and restrained color.

## 10. Title

Create one original English title from real subject relationships, time, light, direction, movement, or pause.

- Prefer two to five words.
- Keep it faithful, natural, and resonant.
- Avoid travel slogans, place labels, photographic jargon, and empty “Memory,” “Dream,” or “Moment” titles.
- Use one title only; do not add a subtitle by default.
- Read `references/typography-system.md` and select edge-pressed serif, fragmented typewriter, letterpress emphasis, or ghost text.
- Treat the title as a physical compositional mark. Let it press against an edge, bridge a gap, flank an anchor, suspend below a sweep, follow a short axis, or replace a small missing mark segment.
- Keep most type around 2%–4.5% of panel height. Only letterpress-emphasis mode may enlarge one existing title word to 6%–9%.
- Use book serif, humanist serif, typewriter, or monospaced faces with restrained capitals or lowercase, loose tracking, irregular line breaks, and slight baseline drift when appropriate.
- Derive type color from a dark muted source role. An emphasized word may use the panel's existing accent hue but may not introduce another color.
- Keep a clear reading path when words are spatially separated, and render every word exactly once.
- Never default to a large centered title beneath the motif, commercial headline hierarchy, or a logo lockup.

Include no other text, dates, numbers, locations, archive notes, coordinates, legends, color swatches, signatures, logos, or watermarks.

## 11. Style references

For Hybrid mode, inspect and attach one image from each group in `assets/style-references/`. Also attach one image from `assets/typography-references/` whose type behavior fits the selected typography mode. State explicitly that the user photograph is the sole content reference; drawing images are mark-only; the typography image is type-behavior-only. Never copy their cats, produce, objects, words, dates, numbers, colors, or layouts.

## 12. Output and rejection criteria

Return only the completed composition unless the user explicitly requests the prompt or explanation.

Reject and regenerate once if the photograph is altered; the panel becomes a scene illustration or thumbnail; the subject is enclosed by thin contour lines; the color scribble is decorative rather than structural; the panel background becomes textured; the motif fills the panel; the title becomes a generic large caption below the motif; title fragments lose their reading order; reference wording is copied; or unwanted text appears.
