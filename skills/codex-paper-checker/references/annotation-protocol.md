# Readable PDF Annotation Protocol

Use this protocol when the user requests annotations or when a visual review copy is the clearest deliverable.

## Layout

- Preserve the original PDF and create a separate annotated copy.
- Favor a landscape review sheet with the original page enlarged on the left and a readable comment column on the right when ordinary PDF sticky notes would be hard to read.
- Put a strong translucent highlight around the exact text, symbol, equation region, caption, figure element, or bibliography entry.
- Place the comment number directly beside the highlighted material. Repeat the same number on the corresponding comment.
- Add a `LOCATE` line naming the section and equation/figure/table/reference number plus a short searchable anchor.
- When one finding applies at multiple locations, mark every location with the same number.
- Use a short leader or gutter cue where it improves mapping without drawing lines through manuscript text.

Do not rely on page-edge dots or approximate vertical positions alone. If text extraction cannot locate the target, inspect the rendered page and use a manually verified bounding box. Never present an approximate marker as exact.

## Categories

Use consistent, color-accessible categories such as:

- red: mathematical, factual, or compliance error;
- amber: missing definition, unresolved evidence, or internal inconsistency;
- blue: definite grammar, typo, or formatting defect.

Retain text labels in addition to color so the document remains usable without color perception.

## Comment content

Each comment should state:

1. what is wrong;
2. why it matters;
3. the exact correction, or what the authors must decide or verify.

Exclude weak stylistic suggestions unless the user explicitly requests optional polish.

## QA

Use the PDF skill's required creation/edit workflow. Render every output page to PNG and inspect at least one contact sheet plus every dense or equation-heavy page at full size. Confirm:

- no comment is clipped or overlapping;
- all badges and highlights are legible;
- every comment maps to the intended source location;
- equations and references remain readable;
- headers, footers, and page numbering are correct;
- the output reopens successfully and preserves all source pages.
