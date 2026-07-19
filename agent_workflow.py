#!/usr/bin/env python3
# Part of the StadiumOS-Core project for PromptWars
import os
import sys

# Add incident_logger directory to path for clean import
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, 'skills', 'incident_logger'))

try:
    from incident_logger import log_incident, ALLOWED_CATEGORIES, ALLOWED_URGENCY_LEVELS
except ImportError as e:
    print(f"Error importing incident_logger: {e}", file=sys.stderr)
    sys.exit(1)

# ANSI escape codes for rich terminal styling
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Simple rule-based heuristics for parsing natural language incident reports
CATEGORY_KEYWORDS = {
    'Medical': ['medical', 'injured', 'injury', 'sick', 'pain', 'heart', 'doctor', 'bleed', 'unconscious', 'hurt', 'slip', 'concussion'],
    'Safety': ['safety', 'hazard', 'wet', 'floor', 'spill', 'broken', 'fire', 'smoke', 'danger', 'theft', 'fight', 'leak'],
    'Missing Child': ['lost child', 'lost kid', 'missing child', 'missing kid', 'separated', 'found child', 'child'],
    'Crowd': ['crowd', 'congestion', 'block', 'overflow', 'line', 'queue', 'gate', 'capacity', 'stampede'],
    'Accessibility': ['wheelchair', 'ramp', 'elevator', 'disabled', 'accessibility', 'deaf', 'blind', 'sensory']
}

URGENCY_KEYWORDS = {
    'High': ['immediate', 'emergency', 'urgent', 'critical', 'severe', 'unconscious', 'high', 'danger', 'bleeding'],
    'Medium': ['warning', 'caution', 'moderate', 'medium', 'congestion', 'blocked'],
    'Low': ['minor', 'low', 'info', 'slight', 'question', 'check']
}

def analyze_input(text):
    text_lower = text.lower()
    
    # 1. Determine if this is an incident report
    # If the text has keywords matching any category or urgency level, we classify it as an incident.
    is_incident = False
    detected_category = 'Safety' # Default fallback
    detected_urgency = 'Low'     # Default fallback
    
    # Check categories
    category_scores = {cat: 0 for cat in CATEGORY_KEYWORDS}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                category_scores[cat] += 1
                is_incident = True
                
    if is_incident:
        detected_category = max(category_scores, key=category_scores.get)
        
    # Check urgency
    urgency_scores = {urg: 0 for urg in URGENCY_KEYWORDS}
    for urg, keywords in URGENCY_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                urgency_scores[urg] += 1
                is_incident = True
                
    if is_incident:
        # If High urgency keywords are present, default to High
        if urgency_scores['High'] > 0:
            detected_urgency = 'High'
        elif urgency_scores['Medium'] > 0:
            detected_urgency = 'Medium'
            
    # Simple location extraction (e.g. "at Sector A", "in Row 12", "near Gate 4")
    location = "Unknown Zone"
    for phrase in ["at ", "in ", "near ", "zone ", "sector "]:
        if phrase in text_lower:
            idx = text_lower.find(phrase) + len(phrase)
            words = text[idx:].split()
            if words:
                location = words[0].strip(".,?!")
                if len(words) > 1 and words[1][0].isupper():
                    location += " " + words[1].strip(".,?!")
                break
                
    return is_incident, detected_category, detected_urgency, location

def main():
    # Setup initial mock context
    print(f"\n{BOLD}{CYAN}=================================================={RESET}")
    print(f"{BOLD}{CYAN}             STADIUMOS-CORE ONLINE                {RESET}")
    print(f"{BOLD}{CYAN}=================================================={RESET}")
    print(f"{CYAN}Initializing session context...{RESET}")
    
    reporter_id = input(f"{BOLD}Enter Volunteer ID (e.g., VOL-1049): {RESET}").strip()
    if not reporter_id:
        reporter_id = "VOL-9999"
        print(f"No ID entered. Defaulting to: {reporter_id}")
        
    default_location = input(f"{BOLD}Enter Current Sector/Location (e.g., Sector A): {RESET}").strip()
    if not default_location:
        default_location = "Sector A"
        print(f"No location entered. Defaulting to: {default_location}")
        
    print(f"\n{GREEN}StadiumOS-Core active. Ready to monitor natural language reports.{RESET}")
    print(f"Type 'exit' or 'quit' to terminate session.\n")
    
    while True:
        try:
            user_input = input(f"{BOLD}StadiumOS-Core>{RESET} ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ['exit', 'quit']:
                print(f"\n{CYAN}Terminating StadiumOS-Core session. Stay safe!{RESET}")
                break
                
            print(f"\n{BOLD}{BLUE}[OBSERVE]{RESET} Intake report: \"{user_input}\"")
            
            is_incident, category, urgency, location = analyze_input(user_input)
            
            if location == "Unknown Zone":
                location = default_location
                
            print(f"{BOLD}{YELLOW}[THINK]{RESET} Analyzing against FIFA Volunteer Operational Handbook...")
            print(f"  - Detected Category: {BOLD}{category}{RESET}")
            print(f"  - Calculated Urgency: {BOLD}{urgency}{RESET}")
            print(f"  - Resolved Location: {BOLD}{location}{RESET}")
            
            if is_incident:
                print(f"{BOLD}{GREEN}[ACT]{RESET} Match confirmed. Activating incident_logger tool...")
                try:
                    entry = log_incident(
                        location=location,
                        category=category,
                        description=user_input,
                        reporter_id=reporter_id,
                        urgency_level=urgency
                    )
                    print(f"{BOLD}{GREEN}[ACT] Incident logged successfully!{RESET} ID: {entry.get('incident_id', 'N/A')}")
                    if entry.get('needs_immediate_review') is True:
                        print(f"{BOLD}{RED}[ALERT] High urgency detected. Supervisor escalation queued.{RESET}")
                except Exception as e:
                    print(f"{BOLD}{RED}[ERROR] Action failed: {e}{RESET}")
            else:
                print(f"{BOLD}{GREEN}[ACT]{RESET} Informational query. No incident logging required.")
                print(f"Response: \"Received. Let me know if you need assistance at {location}.\"")
                
            print(f"\n{CYAN}--------------------------------------------------{RESET}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{CYAN}Session interrupted. Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()
