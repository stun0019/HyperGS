# HTML5 Adapter

## Detect

Look for `index.html`, `package.json`, Vite or similar configuration, Canvas, WebGL, Phaser, PixiJS, or DOM-based game code.

## Prototype defaults

- Use a zero-install static build when dependencies are unnecessary.
- Prefer a small module structure with game state separated from rendering and input.
- Support keyboard and pointer; add touch controls for mobile targets.
- Use deterministic update steps where gameplay correctness matters.
- Keep save data versioned and resilient to malformed local storage.

## Presentation pipeline

- Use Canvas or WebGL for animation-heavy presentation; reserve DOM and CSS for accessible interface structure and lightweight transitions.
- Prefer an established renderer, timeline or tween system, audio mixer, atlas loader, particle system, and skeletal runtime when they materially reduce production risk. Do not reject dependencies merely to claim a framework-free build.
- Drive presentation from named gameplay events and data-defined beats rather than scattered timeouts.
- Preload critical atlases, audio, fonts, and effects; pool transient objects and cap simultaneous particles, filters, blend layers, and audio voices.
- Synchronize gameplay resolution to authored event markers. Keep outcome logic authoritative and make presentation safely skippable or recoverable.
- Test reduced-motion behavior, background-tab recovery, interrupted audio, resize, orientation changes, and mobile memory pressure.

## Verify

Run available tests and the documented dev or static server. Inspect the browser console, initial load, resize behavior, input, the full core loop, restart, and mobile viewport when targeted. Record video for timing-dependent presentation and inspect frame pacing, event synchronization, dropped assets, audio overlap, and recovery after interrupted sequences.

Do not claim mobile readiness from a desktop viewport alone.
