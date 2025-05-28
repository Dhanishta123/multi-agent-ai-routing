# Multi-Agent AI Document Routing System

This project implements a multi-agent artificial intelligence (AI) system designed to classify, extract, and route input documents in PDF, JSON, or Email (text) format. Each input is processed by a Classifier Agent and then passed to the appropriate specialized agent (Email Agent or JSON Agent). All agents interact with a shared memory module for traceability and chaining.

## Features
- Classifies document type and intent from input (PDF/JSON/Email).

- Routes to specialized agents:

  - Email Agent: Extracts sender, urgency, summary.

  - JSON Agent: Validates schema, normalizes invoice structure, flags missing fields.

- Maintains shared context using memory (Redis or in-memory fallback).

- Saves processed outputs as structured JSON logs in an /outputs directory.

- Modular and extensible design using Python classes.

## Agents
### Classifier Agent
- Input: Raw file path or JSON content.

- Output: Format and intent.

- Action: Routes to correct agent and logs in shared memory.

### Email Agent
- Input: Raw email text.

- Extracts: Sender, urgency, short summary.

- Output: Saves to outputs/{source_id}_email.json.

### JSON Agent
- Input: Structured JSON (e.g., invoice).

- Validates required fields: invoice_number, date, amount.

- Flags anomalies or missing fields.

- Output: Saves to outputs/{source_id}_json.json.

## Shared Memory
- Stores format, intent, timestamps, and extracted fields.

- Supports chaining and context tracking across documents.

- Powered by Redis (or fallback options like in-memory/SQLite).

## Sample Inputs
- sample_email.txt: Email with header (e.g., "From: john@example.com").

- sample_invoice.json: Structured invoice with fields like amount, invoice_number, etc.

## Sample Output Logs
- outputs/email1_email.json

- outputs/json1_json.json

Each file contains structured output fields extracted and normalized by agents.

## Tech Stack
- Python 3.10+

- Redis (optional, for shared memory)

- Regular Expressions (Email parsing)

- JSON handling
