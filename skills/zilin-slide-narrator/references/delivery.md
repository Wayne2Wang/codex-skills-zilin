# Player, video, homepage, and deployment

## Student-facing player

Default appearance: dark navy (#10162b), warm gold (#ffcc67), readable system fonts, restrained borders, responsive slide stage. Preserve the current design unless customized. Inspect a supplied course website before intentionally matching its styling; a similar palette alone is not evidence of matching.

Include automatic slide changes, play/pause, restart, previous/next, slide picker, local seek and overall progress, playback speeds 0.85/1/1.15/1.3/1.5, CC on by default, per-slide transcript, fullscreen, keyboard shortcuts, and downloads for MP4, SRT, and original slides. Keep interface student-facing: no voice settings, credit status, development labels, raw exceptions, filesystem instructions, or editable-source links. Useful playback help and duration are fine.

Deliver a complete player and video even if deployment is declined. State any remaining fallback narration or caption limitations clearly outside the student UI. Do not call a partial mixed-voice version complete.

## Optional static deployment

Ask during intake whether deployment is needed; respect local-only/package-only answers. For a public GitHub Pages deployment, use one course/term repository with a simple root `index.html` and lab subfolders such as `lab01/index.html`. Suggest a course-specific name; `eecs498a2se-fall2026` was the original chosen name, not a global fixed destination.

Root homepage: course title, term, available labs, a short description, runtime, caption/transcript availability, and a clear Watch link. Add new labs as real content becomes available; no fake upcoming entries. Lab player links back to All labs.

Create a clean package containing real asset files, not symlinks: HTML, player/caption data, images, playback audio, MP4 with CC, SRT/VTT, and source deck if requested. Do not publish native drafts, generation histories, production notes, source-audio backups, credentials, alignment/model caches, or private notes. Use relative links that work under a repository subpath and include `.nojekyll` for a plain GitHub Pages site. Validate all links and media in the packaged copy, not only the development directory. Check current provider file/bandwidth limits before deployment; don't assume media hosting limits remain unchanged.

No backend or ElevenLabs key is needed to serve already generated assets. Distinguish public hosting from access-restricted teaching delivery. MiVideo/Canvas is an alternative for a course video, not a deployment of this exact custom player. Follow an explicitly selected host; do not substitute Sites for GitHub Pages. When using Sites, apply available Sites skills and their current procedures.

Before publishing, resolve the destination and audience. Publish only within the user's actual authorization; a question about how to host isn't permission to publish. Follow current tool/policy confirmation requirements at the final action, without repeatedly asking about already authorized reversible preparation. Verify the final HTTPS URL and asset paths, then provide it. If no hosting access is available, deliver the upload-ready package and precise remaining step; do not claim deployment occurred.
