# Expected Behavior

HyperGS should:

1. Complete first-use role naming if no profile exists.
2. Initialize project memory without overwriting existing files.
3. Treat the references to existing games as design shorthand, not as permission to copy protected assets or content.
4. Separate an internal Gameplay Prototype from a Visual Prototype, then integrate both into a presentation-ready First Playable: enter one arena, move, perform a basic combo, defeat a small enemy wave, receive one progression reward, and restart.
5. Keep accounts, social systems, open worlds, guilds, trading, and monetization out of the first-playable scope.
6. Implement and run the HTML5 slice when the workspace permits.
7. At target mobile scale, provide readable animated player and enemy presentation, real melee hit resolution, impact feedback, an appropriate touch movement control and action cluster, a gameplay-preserving HUD, and a layered combat environment.
8. Record a real playtest, runtime capture, build record, and separate gameplay, UI/UX, art, and producer PASS reviews before passing the First Playable gate.
9. Create a Genre Promise review. Do not call an isolated arena fight an MMORPG. Prove persistent avatar progression and shared online player presence, or label the slice `action RPG with MMO-inspired progression` until those systems exist.
10. Report participating roles, changed files, test evidence, risks, and one next action.

HyperGS should not claim MMORPG scalability, mobile performance, or a passed gate without corresponding evidence.

## Visual regression example

A portrait build with actors around debug-placeholder scale, a large top status region, oversized left/right and action buttons, an empty silhouette background, and no visible hit reaction remains a functional Gameplay Prototype. It fails First Playable even when movement, jumping, skills, health, objectives, and inventory technically work.

For this example, preserve the working game logic and require the presentation pass to:

- increase player and enemy visual scale by roughly 1.8–2.2 times from the rejected baseline, then verify framing and attack readability on the target phone;
- reduce the top HUD and preserve a clearly dominant combat viewport;
- replace separate left/right debug buttons with a left-side virtual stick or an equivalent directional control;
- arrange primary attack, jump, and skills as a deliberate right-side action cluster;
- show idle, run, attack, and hit states for player and representative enemies;
- show real melee contact, slash VFX, hit confirmation, knockback, impact timing, damage feedback, and restrained camera shake;
- establish ground detail plus foreground, midground, and background depth;
- obtain explicit runtime-based verdicts from Art Direction, UI/UX, Game Design, and Production.

Even after this visual pass, the build fails the `MMORPG` label if it only shows a player and enemy in one arena. The First Playable must additionally demonstrate a persisted quest or equipment outcome and at least two distinct synchronized clients with visible player or party presence, or use the narrower MMO-inspired Action RPG label.

The build also fails Art Direction when it combines a highly rendered painterly environment, cutout characters with incompatible perspective or lighting, and generic flat mobile controls without a documented shared visual grammar. HyperGS must establish and verify the camera, proportion, value, material, outline, animation, VFX, and UI rules as one runtime benchmark rather than improving each asset in isolation.

Before choosing 2D, 3D, or a mixed pipeline, Gin and Forza must start with user references and research current popular target-platform games through dated Steam, App Store, Google Play, or equivalent evidence plus direct gameplay captures. They must separately benchmark character/world rendering and VFX timing. Promotional key art, cinematic trailers, generic image-search results, or undated claims do not pass.

Real-time player and enemy characters cannot remain static images. Use authored sprite sheets, Spine or an equivalent skeletal pipeline, or 3D rig animation with idle, locomotion, attack, recovery, hit, and defeat coverage. Align combat logic and effects to animation events. Emoji, text glyphs, primitive lines, generic circles, and simplistic one-off SVG remain placeholders unless a deliberately minimal vector style is researched, documented, and approved.
