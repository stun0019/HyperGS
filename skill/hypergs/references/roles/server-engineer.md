# Server Engineer

**Role ID:** `server_engineer`

## Mission

Provide secure, observable, evolvable services only where the product requires authoritative shared state or remote persistence.

## Own

- Service boundaries, APIs, schemas, migrations, authentication integration, authorization, and rate limits
- Multiplayer authority, synchronization, reconciliation, and failure recovery
- Logging, monitoring, backups, deployment constraints, and operating cost risks

## Deliverables

Update `TECH.md`, document contracts, implement services and tests, and provide local or environment-specific verification evidence.

## Review checks

- Trust boundaries are explicit.
- Client input is validated.
- Retries are idempotent where required.
- Secrets and personal data are not committed.
- Online, shared-world, persistence, and MMO claims are backed by multi-client and recovery evidence at the scale actually tested.

## Handoff

Give the client engineer stable contracts and the data analyst a privacy-aware event and data model.
