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
The system implements a structured **Observe-Think-Act** loop in [agent_workflow.py](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/agent_workflow.py):
- **Observe**: Capture volunteer natural language reports and resolve metadata (like reporter ID and location keywords).
- **Think**: Analyze context against pre-set heuristics to classify category (Medical, Safety, Missing Child, Crowd, Accessibility) and estimate urgency.
- **Act**: Automatically call the incident logger tool to record incidents and trigger immediate supervisor alert notifications.

### 3. Automated Urgency Tagging
- Automatically detects urgency levels based on keywords (e.g., "emergency", "urgent", "critical").
- High-urgency incidents are automatically tagged with a `needs_immediate_review: true` escalation flag to guarantee swift supervisory dispatch.

---

## Directory Structure
- [agent_workflow.py](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/agent_workflow.py): The interactive StadiumOS-Core CLI loop implementing the agent workflow.
- [volunteer_handbook.md](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/volunteer_handbook.md): Central handbook defining volunteer protocols (e.g., Missing Child guidelines).
- [incidents.json](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/incidents.json): The local-first JSON array database holding logged incidents.
- **`skills/incident_logger/`**
  - [SKILL.md](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/skills/incident_logger/SKILL.md): Agent skill documentation detailing parameters and CLI execution.
  - [incident_logger.py](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/skills/incident_logger/incident_logger.py): The Python implementation of the logging skill.
  - [incident_logger.js](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/skills/incident_logger/incident_logger.js): The Node.js fallback companion script.

---

## Quick Start & Verification

### Running the Agent Loop

Ensure your Python interpreter is configured, then run:
```bash
python volunteer/agent_workflow.py
```

### Logging an Incident Manually (CLI Direct)

**Using Python:**
```bash
python volunteer/skills/incident_logger/incident_logger.py log \
  --location "Sector A, Row 12" \
  --category "Medical" \
  --description "Spectator slipped on staircase. Medical team dispatched." \
  --reporter-id "VOL-1049" \
  --urgency-level "High"
```

**Using Node.js (Fallback):**
```bash
node volunteer/skills/incident_logger/incident_logger.js log \
  --location "Sector A, Row 12" \
  --category "Medical" \
  --description "Spectator slipped on staircase. Medical team dispatched." \
  --reporter-id "VOL-1049" \
  --urgency-level "High"
```

*Outputs will append to [incidents.json](file:///c:/Users/Manasvi%20Gandhi/agy-cli-projects/volunteer/incidents.json) atomically.*
