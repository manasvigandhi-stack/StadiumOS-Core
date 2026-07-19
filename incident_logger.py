#!/usr/bin/env python3
# Part of the StadiumOS-Core project for PromptWars
import argparse
import datetime
import json
import os
import sys
import uuid

ALLOWED_CATEGORIES = {'Medical', 'Safety', 'Missing Child', 'Crowd', 'Accessibility'}
ALLOWED_URGENCY_LEVELS = {'Low', 'Medium', 'High'}

def log_incident(location, category, description, reporter_id, urgency_level, output=None):
    # 1. Validation
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(f"Category '{category}' is not allowed. Must be one of: {', '.join(ALLOWED_CATEGORIES)}")
        
    if urgency_level not in ALLOWED_URGENCY_LEVELS:
        raise ValueError(f"Urgency level '{urgency_level}' is not allowed. Must be one of: {', '.join(ALLOWED_URGENCY_LEVELS)}")

    # 2. Field derivation
    incident_id = uuid.uuid4().hex[:8].upper()
    timestamp = datetime.datetime.now().astimezone().isoformat()
    needs_immediate_review = urgency_level == 'High'

    # Prepare entry
    entry = {
        "incident_id": incident_id,
        "timestamp": timestamp,
        "location": location,
        "category": category,
        "description": description,
        "reporter_id": reporter_id,
        "urgency_level": urgency_level,
        "status": "open",
        "needs_immediate_review": needs_immediate_review
    }

    # Determine file path
    output_path = output
    if not output_path:
        # Default to volunteer/incidents.json relative to the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Go up two levels to volunteer/ from volunteer/skills/incident_logger/
        output_path = os.path.abspath(os.path.join(script_dir, "..", "..", "incidents.json"))

    # Ensure parent directory exists
    parent_dir = os.path.dirname(output_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    # Read existing database
    incidents = []
    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                incidents = json.load(f)
                if not isinstance(incidents, list):
                    print(f"Warning: Output file '{output_path}' was not a list. Resetting to a new list.", file=sys.stderr)
                    incidents = []
                else:
                    # Guard: If any entry is missing keys, assign 'N/A' to those keys
                    schema_keys = [
                        'incident_id', 'timestamp', 'location', 'category', 
                        'description', 'reporter_id', 'urgency_level', 
                        'status', 'needs_immediate_review'
                    ]
                    for incident in incidents:
                        if isinstance(incident, dict):
                            for key in schema_keys:
                                if key not in incident:
                                    incident[key] = 'N/A'
        except json.JSONDecodeError as e:
            print(f"Warning: Output file '{output_path}' contained invalid JSON ({e}). Resetting to a new list.", file=sys.stderr)
            incidents = []
        except Exception as e:
            print(f"Error: Could not read output file '{output_path}': {e}", file=sys.stderr)
            raise e

    # Append entry
    incidents.append(entry)

    # Write safely using a temporary file and atomic replace
    temp_path = output_path + ".tmp"
    try:
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(incidents, f, indent=2)
        # Atomic replace
        os.replace(temp_path, output_path)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"Error: Failed to write to '{output_path}': {e}", file=sys.stderr)
        raise e

    return entry

def main():
    parser = argparse.ArgumentParser(description="StadiumOS-Core Incident Logger CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    log_parser = subparsers.add_parser("log", help="Log a new volunteer incident")
    log_parser.add_argument("--location", required=True, help="Stadium zone/sector")
    log_parser.add_argument("--category", required=True, help=f"Category of incident: {', '.join(ALLOWED_CATEGORIES)}")
    log_parser.add_argument("--description", required=True, help="Brief summary of the event")
    log_parser.add_argument("--reporter-id", required=True, help="Volunteer ID")
    log_parser.add_argument("--urgency-level", required=True, help=f"Urgency level: {', '.join(ALLOWED_URGENCY_LEVELS)}")
    log_parser.add_argument("--output", help="Custom output JSON file path")

    args = parser.parse_args()

    if args.command == "log":
        try:
            entry = log_incident(
                location=args.location,
                category=args.category,
                description=args.description,
                reporter_id=args.reporter_id,
                urgency_level=args.urgency_level,
                output=args.output
            )
            print(f"Success! Incident logged successfully.")
            print(json.dumps(entry, indent=2))
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: Unexpected failure: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
