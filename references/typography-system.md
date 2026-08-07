# Zine Typography System

Use this reference for every generation. Derive the type behavior from the public `gc-minimal-zine-poster` visual system while keeping this skill's clean photo-plus-panel content rules.

Source inspiration: `https://github.com/LiamGvchi/gc-minimal-zine-poster`

## Core Principle

Treat words as physical marks that participate in the abstraction. Do not place a large polished title under the motif as a generic caption. Preserve one short title, but let scale, spacing, alignment, interruption, and pressure express the photo's relationship.

The title must remain semantically readable and every word must appear exactly once. Never copy wording, dates, coordinates, archive notes, captions, or letter arrangements from the reference images.

Generate and verify the title as text before rendering. Use `scripts/render_typography.py` for the final lettering so the source photo remains untouched and every word appears once. Map the modes below to CLI values `edge`, `fragmented`, `letterpress`, and `ghost`.

## Mode A — Edge-Pressed Serif

Use when the motif has a strong side, opening, vertical edge, shelter, doorway, tree trunk, tower, or paired panels.

- Set the title in a small book serif or humanist serif.
- Break the phrase into two to five short lines when useful.
- Press the text close to one motif edge, place it across a narrow gap, or let one line lightly overlap the mark boundary.
- Use a restrained size around 2.5%–4.5% of panel height.
- Permit narrow leading, slight baseline drift, and modest tracking.
- Keep color charcoal, deep blue-gray, dark green, wine, or another source-derived structural hue.
- Avoid centered literary-cover styling and oversized elegance.

## Mode B — Fragmented Typewriter

Use when the source is about distance, drift, pause, repetition, steps, scattered people, separate objects, or interrupted horizons.

- Use a small typewriter or monospaced face.
- Separate the title into word fragments while preserving a clear reading path.
- Place fragments around, beside, or between motif parts; align them to real axes in the photo.
- Use loose tracking, uneven line lengths, deliberate pauses, and slight baseline mismatch.
- A word may run vertically one letter per line only when the source contains a strong vertical axis.
- Keep all fragments within one compact typographic field; do not scatter them across the whole panel.
- Do not add decorative letters, random numbers, or pseudo-technical labels.

## Mode C — Letterpress Emphasis

Use when one word carries the source relationship: `PAUSE`, `UNDER`, `TIDE`, `RETURN`, `DISTANCE`, or another concrete action/condition.

- Set the supporting words in small serif, typewriter, or monospaced type.
- Set exactly one existing title word larger in a condensed serif, slab serif, or rough letterpress face.
- Let the emphasized word occupy about 6%–9% of panel height; keep the rest around 2%–3.5%.
- Use the panel's existing accent color or a dark structural color for the emphasized word. Do not introduce another hue.
- Allow slight ink spread, imperfect fill, misregistration, or rough edges only inside the letters; keep the panel background clean.
- Avoid commercial campaign hierarchy, bold sans-serif advertising, and full-width headlines.

## Mode D — Ghost Text

Use when the source is quiet, distant, misty, reflective, empty, or memory-like.

- Use a fine serif, typewriter, or monospaced face at low-to-medium contrast.
- Keep the phrase small and place it near a negative-space boundary, beneath a horizon, or partly across a pale mark.
- Permit one softened, slightly incomplete, or misregistered printing pass, but keep the wording legible.
- Do not duplicate the title, blur it into illegibility, or create a long block of prose.

## Spatial Behaviors

Choose one behavior supported by the source geometry:

- **press:** title touches or nearly touches a motif edge;
- **bridge:** phrase crosses a gap between two marks;
- **flank:** words sit on opposite sides of one vertical anchor;
- **suspend:** title hangs beneath a horizontal sweep with visible air;
- **thread:** phrase follows one short straight or gently curved axis;
- **interrupt:** one word replaces a small missing segment of a mark;
- **echo:** type alignment repeats the spacing or rhythm of source-derived marks.

Do not curve every letter along a path, wrap text around a silhouette, or build a logo lockup.

## Scale and Hierarchy

- Default title size: 2%–4.5% of panel height.
- Default title field: no more than 18%–32% of panel width unless words are fragmented along a source axis.
- Emphasized word in Mode C: 6%–9% of panel height.
- Use one type family by default; two families only in Mode C.
- Prefer lowercase or restrained capitals. Use all caps only for a short emphasized word.
- Keep typography subordinate to the photograph and in active dialogue with the abstract motif.

## Clean-Panel Compatibility

Borrow material imperfection only inside glyphs: light ink bleed, uneven pressure, rough letterpress fill, photocopy softness, or slight misregistration. Do not import aged paper, stains, fibers, scan noise, shadows, or mottling into the ivory panel background.

## Reference Routing

Attach one typography-only reference during image generation:

- `night-door.jpeg`: edge-pressed serif and text attached to a vertical anchor;
- `pause-map.jpeg`: letterpress emphasis with small supporting type;
- `yellow-step.jpeg`: fragmented typewriter words aligned to spatial axes;
- `moon-tide.jpeg`: ghost text and a quiet phrase bridging paired fields.

Explicitly state that the image is typography-only. Borrow only scale, spacing, alignment, fragmentation, and print behavior. Forbid copying all words, numbers, dates, captions, colors, objects, and layout.

## Reject and Regenerate

Regenerate once if:

- the title becomes a large centered commercial headline;
- it sits beneath the motif as an unrelated caption;
- extra pseudo-archive text, dates, numbers, or labels appear;
- fragments cannot be read as one title;
- decorative script, cartoon type, polished ad typography, or logo styling appears;
- the model copies visible words from the typography reference;
- background texture from the typography reference leaks into the clean ivory panel.
