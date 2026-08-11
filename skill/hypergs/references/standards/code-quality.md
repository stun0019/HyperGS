# Code Quality

- Follow the existing repository conventions before introducing abstractions.
- Keep gameplay rules separate from rendering, input transport, persistence, and networking where practical.
- Make tunable values discoverable and validated.
- Treat save formats, network contracts, analytics events, and public interfaces as versioned contracts.
- Validate untrusted input at boundaries and never commit secrets.
- Add focused tests for deterministic rules and regression-prone behavior.
- Keep a documented reproducible launch, build, and test path.
- Profile before claiming a performance improvement.
- Avoid speculative systems that do not serve the current phase objective.
- Preserve user changes and explain migrations that affect data or assets.
