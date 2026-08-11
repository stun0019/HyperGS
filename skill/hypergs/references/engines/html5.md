# HTML5 Adapter

## Detect

Look for `index.html`, `package.json`, Vite or similar configuration, Canvas, WebGL, Phaser, PixiJS, or DOM-based game code.

## Prototype defaults

- Use a zero-install static build when dependencies are unnecessary.
- Prefer a small module structure with game state separated from rendering and input.
- Support keyboard and pointer; add touch controls for mobile targets.
- Use deterministic update steps where gameplay correctness matters.
- Keep save data versioned and resilient to malformed local storage.

## Verify

Run available tests and the documented dev or static server. Inspect the browser console, initial load, resize behavior, input, the full core loop, restart, and mobile viewport when targeted.

Do not claim mobile readiness from a desktop viewport alone.
