# Expected Behavior

HyperGS should select the existing-project and bug-fix workflows, with quality review as a supporting check. The client engineer leads diagnosis, while the game designer and UI/UX designer verify queue rules and touch behavior. The producer owns the gate decision.

The run should reproduce the defect when possible, implement the smallest fix, add a regression check, exercise the relevant touch flow, update affected project memory, and run the current phase check.

It should advance only if the current gate already has all required substantive documents and evidence. Fixing one bug is not sufficient evidence for Vertical Slice readiness.
