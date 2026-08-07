# Two-Stage Production Pipeline

Use this pipeline for strict photo fidelity, exact aspect ratios, and dependable typography.

## Stage 1: generate the panel

Generate only the abstract panel. Do not include the source photograph, title, border, seam, mockup, or surrounding page.

Set the requested panel aspect ratio from the final canvas size and selected photo share:

```text
panel width = final width
panel height = final height × (1 - photo share)
```

Use the uploaded photo as the sole content reference. Use bundled drawing images as style-only inputs. Demand a flat `#F3F0E8` background and keep all corners empty.

## Stage 2: compose and typeset

Compose the untouched source photo and generated panel:

```powershell
python scripts/compose_poster.py source.jpg panel.png composed.png --size 1080x1920 --photo-share 0.55
```

Render the selected title mode:

```powershell
python scripts/render_typography.py composed.png final.png `
  --title "a small arrival" `
  --mode letterpress `
  --emphasis-word arrival `
  --panel-start 0.55
```

Validate the final artifact:

```powershell
python scripts/validate_output.py final.png `
  --ratio 9:16 `
  --source source.jpg `
  --photo-share 0.55
```

Use `--focus-x` and `--focus-y` in both composition and validation when a centered crop would cut the subject. Keep their values between 0 and 1.

## Fallback

Use a one-pass generated composition only when the environment cannot run Pillow or cannot access the generated panel as a local file. Inspect photo fidelity, spelling, ratio, and unwanted text before returning it.
