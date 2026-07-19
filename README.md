# StadiumOS-Core: Agentic Incident Management System

An agentic, offline-first incident reporting and triaging system designed for **FIFA 2026 World Cup** decentralized stadium operations. StadiumOS-Core operates directly at the stadium "last mile", assisting volunteers and supervisors in logging critical events under heavy load or poor network conditions.

---

## Key Core Architectures

### 1. Local-First Data Architecture
To counter unreliable stadium Wi-Fi and high network congestion, StadiumOS-Core features a **local-first design**:
- **Zero Remote Dependencies**: Stores all logged incidents inside a structured, append-only, localized file (`incidents.json`).
- **Atomic File-Update Safety**: Updates are performed via write-to-temporary-file and rename/replace operations, preventing file corruption in case of unexpected script termination.
- **Node & Python Parallel Implementations**: Features identical CLI/programmatic implementations in both Python and Node.js for environment portability.

### 2. Observe-Think-Act Agent Loop
The system implements a structured **Observe-Think-Act** loop in `agent_workflow.py`:
- **Observe**: Capture volunteer natural language reports and resolve metadata (like reporter ID and location keywords).
- **Think**: Analyze context against pre-set heuristics to classify category (Medical, Safety, Missing Child, Crowd, Accessibility) and estimate urgency.
- **Act**: Automatically call the incident logger tool to record incidents and trigger immediate supervisor alert notifications.

### 3. Automated Urgency Tagging & Accessibility
- **Urgency Tagging**: Automatically detects urgency levels based on keywords (e.g., "emergency", "urgent", "critical") and escalates high-urgency incidents with a `needs_immediate_review: true` flag.
- **Accessibility-First Design**: The UI is optimized for readability with high-contrast elements and screen-reader-friendly widget labeling, ensuring all volunteers can report incidents regardless of their environment or physical requirements.

---

## Quick Start & Verification

### Live Dashboard
Access the deployed interactive interface here: **[https://stadiumos-core-xicr5s8rzmege7725nde6j.streamlit.app/](https://stadiumos-core-xicr5s8rzmege7725nde6j.streamlit.app/)**

### Running the Agent Loop
Ensure your Python interpreter is configured, then run:
```bash
python volunteer/agent_workflow.py
