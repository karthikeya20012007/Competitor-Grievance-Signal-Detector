# ChatGPT Usage Log

AI assistance was used for:

- architecture planning
- debugging
- implementation guidance
- scoring logic refinement
- serverless integration troubleshooting
- README drafting

All code was reviewed, modified, tested, and understood before inclusion in the final submission.

---

# Project Planning

- Discussed modular signal detector architecture
- Planned separation of:
  - fetcher
  - detector
  - scorer
  - parser
- Chose heuristic scoring instead of ML models

---

# Data Ingestion

- Discussed Reddit public JSON ingestion
- Designed hybrid ingestion:
  - live Reddit fetching
  - seeded deterministic examples
- Discussed handling noisy public recruiting discussions

---

# Signal Detection Logic

- Implemented competitor keyword detection
- Implemented negative sentiment detection
- Added pain point categorization:
  - cost
  - speed
  - fairness
  - reliability
  - candidate experience

---

# Ambiguity Handling

- Discussed contextual proximity matching
- Added word-window based contextual detection
- Added low-confidence filtering to reduce false positives

---

# Scoring Logic

- Designed heuristic confidence scoring system
- Added weighted contextual scoring
- Added ambiguity penalties
- Added differentiated confidence levels

---

# Serverless Integration

- Converted CLI runner into Serverless Framework endpoint
- Configured serverless-offline
- Debugged timeout and routing issues
- Tested endpoint using Postman

---

# Testing & Cleanup

- Tested JSON signal output
- Verified multiple scoring outcomes
- Refined structured signal records
- Improved README explanations

---

# Example AI Interaction Excerpts

## Prompt

How can I reduce ambiguity where negative phrases may not actually refer to the competitor platform?

## AI Guidance Summary

Suggested contextual proximity matching using word windows around competitor mentions instead of global keyword matching.

---

## Prompt

How should confidence scores be assigned without using ML models?

## AI Guidance Summary

Suggested heuristic scoring using:
- competitor detection
- contextual negative phrases
- category count
- ambiguity penalties

---

## Prompt

How can I make the system compatible with Serverless Framework locally?

## AI Guidance Summary

Suggested converting the CLI runner into a lightweight serverless-offline endpoint using handler.py and serverless.yml.