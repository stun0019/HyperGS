# New Project Workflow

## Trigger

Use for a game idea, an empty workspace, or a request to start a game from scratch.

## Lead and support

Lead: Producer. Support: Game Designer and Market Analyst; add technical or art roles only for material constraints.

## Procedure

1. Preserve the user's original pitch and identify platform, engine, audience, and constraints from available context.
2. If engine or platform is unspecified, recommend one reversible prototype default and record the assumption.
3. Initialize `.hypergs` with `init_project.py` after authorization to modify the workspace.
4. Fill only the sections required for Discovery or Concept.
5. Define the smallest playable hypothesis, non-goals, acceptance criteria, and top risks.
6. Implement only if the user requested creation or building, then run the adapter-specific smoke test.

## Completion

Return a bounded product brief, initialized project memory, current phase, evidence produced, and the next cheapest uncertainty to resolve.
