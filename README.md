# Competitor Grievance Signal Detector

A modular Python-based signal detection system that identifies public complaints about hiring-tech competitors such as HackerRank, HireVue, Codility, Greenhouse, and Lever.

The system ingests public recruiting-related discussions, detects negative sentiment associated with competitor platforms, categorizes the underlying pain point, assigns a confidence score, and outputs structured JSON signals.

The project is designed as a lightweight, explainable signal intelligence prototype for identifying potential outreach opportunities based on competitor dissatisfaction.

---

# Features

- Detects competitor platform mentions
- Detects nearby negative sentiment phrases
- Maps complaints into categorized pain points
- Assigns contextual confidence scores
- Filters low-confidence noisy detections
- Outputs structured JSON signal records
- Modular architecture with separated ingestion, detection, scoring, and parsing layers
- Locally runnable using Serverless Framework

---

# Tech Stack

- Python 3.x
- Serverless Framework
- serverless-offline
- Requests
- JSON-based output storage

---

## Setup and Run

### 1. Clone Repository

```bash
https://github.com/karthikeya20012007/Competitor-Grievance-Signal-Detector
cd competitor-signal-detector
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Serverless Dependencies

```bash
npm install
```

---

### 5. Start Serverless Offline

```bash
npx serverless offline
```

---

### 6. Test Endpoint

Use Postman or browser:

```text
GET http://localhost:3000/dev/signals
```

The API returns structured JSON signal records.

---

## Data Ingestion Approach

The system uses a hybrid ingestion strategy combining:

1. Live Reddit ingestion
2. Curated seeded complaint examples

### Live Reddit Ingestion

The system fetches public Reddit posts from:

- r/recruiting
- r/cscareerquestions
- r/humanresources

using Reddit’s public JSON endpoints without authentication.

Reddit was chosen because recruiting-related communities frequently contain discussions about hiring workflows, recruiting tools, candidate experiences, and technical assessment platforms.

The ingestion layer was intentionally kept lightweight using public unauthenticated endpoints and the Requests library to comply with the assignment constraints.

### Seeded Complaint Dataset

A small seeded dataset was added using representative complaint examples referencing platforms such as HackerRank, HireVue, and Codility.

This was done to:

- provide deterministic demonstrations
- ensure consistent signal generation
- avoid instability caused by live external data sources
- reduce serverless timeout issues during local execution

The seeded examples simulate realistic competitor grievances gathered from public-style recruiting discussions.

### Noise Handling

Public recruiting discussions contain large amounts of unrelated noise.

To reduce false positives:

- low-confidence detections are filtered out
- contextual proximity matching is used
- negative phrases must appear near competitor mentions

This prevents unrelated recruiting complaints from being incorrectly attributed to competitor platforms.

---

## Scoring Logic

The system uses an explainable heuristic-based scoring model.

The confidence score is calculated using:

- competitor mention presence
- number of detected pain categories
- contextual negative phrase matches
- matched keyword count
- ambiguity penalties

### Scoring Components

| Signal Feature | Effect |
|---|---|
| Competitor mention detected | Increases score |
| Multiple pain categories | Increases score |
| Negative phrases near competitor mention | Strongly increases score |
| More matched keywords | Moderately increases score |
| No contextual proximity match | Decreases score |

### Contextual Matching

The detector uses a contextual word window around competitor mentions.

Negative phrases are only treated as strong signals when they appear close to the competitor name.

Example:

Strong signal:

```text
"HireVue interviews feel biased and unreliable."
```

Weaker signal:

```text
"HireVue exists but our hiring process is slow."
```

This reduces ambiguity and false positives.

### Score Interpretation

| Score Range | Interpretation |
|---|---|
| 80–100 | Strong competitor grievance signal |
| 60–79 | Moderate confidence signal |
| 40–59 | Weak but potentially relevant signal |
| Below 40 | Filtered as noise |

The scoring system prioritizes explainability over predictive machine learning accuracy.

---

## Assumptions and Limitations

### Assumptions

The system assumes that:

- nearby negative sentiment is likely associated with the detected competitor
- seeded complaint examples are representative of realistic public complaints
- public Reddit recruiting discussions contain meaningful hiring-tech signals

### Limitations

The system currently uses rule-based heuristics rather than trained NLP models.

As a result:

- sarcasm is not detected
- implicit sentiment may be missed
- complex sentence structures can still produce false positives
- competitor mentions without explicit negative keywords may not be surfaced

The live Reddit ingestion pipeline is also subject to:

- rate limiting
- noisy unrelated discussions
- inconsistent public data quality

### Future Improvements

If given more time, the following improvements would be added:

- NLP-based sentiment classification
- duplicate signal detection
- source weighting by platform credibility
- asynchronous ingestion pipelines
- SQLite-based persistence
- better phrase tokenization
- scheduled ingestion jobs
- richer competitor knowledge base

---

# Example Output

```json
[
    {
        "company": "HireVue",
        "signal_type": "competitor_grievance",
        "source_url": "https://trustpilot.com/example2",
        "matched_keywords": [
            "HireVue",
            "biased",
            "unreliable"
        ],
        "pain_categories": [
            "fairness",
            "reliability"
        ],
        "signal_score": 100,
        "detected_at": "2026-05-27T08:40:56.785732",
        "reason": "Detected complaints related to HireVue with pain points in fairness, reliability."
    }
]
```

---

# Project Structure

```text
competitor-signal-detector/
│
├── ai-tool-usage-log/
│
├── output/
│
├── signals/
│   ├── detector.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── scorer.py
│
├── utils/
│   ├── keywords.py
│
├── handler.py
├── serverless.yml
├── requirements.txt
├── package.json
├── README.md
└── .gitignore
```

---

# AI Tool Usage

AI tools including ChatGPT were used during development for:

- architecture brainstorming
- scoring logic refinement
- modularization ideas
- debugging assistance
- documentation drafting

All generated code was manually reviewed, tested, modified, and understood before inclusion in the final submission.