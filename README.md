# AI Governance Engine

## Overview

AI Governance Engine is a policy-aware conversational assistant designed
to answer employee questions while enforcing company compliance rules.\
The system retrieves official company policy documents (RAG), analyzes
user input for sensitive data, evaluates risk, and safely responds.

It acts like an internal compliance assistant --- not just a chatbot.

------------------------------------------------------------------------

## Features

-   Policy-based answers using Retrieval Augmented Generation (RAG)
-   PII detection and masking Personal data
-   Risk classification (SAFE / MEDIUM / HIGH)
-   Automatic response blocking for violations
-   Audit and compliance verification layer
-   Chat logging for traceability
-   Local LLM support (Ollama --- no paid API required)

------------------------------------------------------------------------

## Tech Stack

**Backend** - Python - FastAPI - LangChain - ChromaDB (Vector
Database) - Ollama (Local LLM)

**Security & Governance** - Microsoft Presidio (PII detection) -
Rule-based Risk Engine - Policy Auditor Agent

**Frontend** - Streamlit UI

**Data & Storage** - SQLite (chat logs) - Text-based company policy (RAG
source)

------------------------------------------------------------------------

## Project Structure

    AI-Governance-Engine/
    │
    ├── application/        # FastAPI backend
    ├── agents/             # Auditor & Risk engines
    ├── rag/                # Policy retrieval system
    ├── policies/           # Company policy documents
    ├── dashboard/          # Streamlit UI
    ├── evaluation/         # Evaluation logic
    ├── policy_db/          # Vector database
    ├── tests/
    ├── requirements.txt
    └── app.py              # Run backend + frontend together

------------------------------------------------------------------------

## Local Setup

### 1. Clone

    git clone <repo>
    cd AI-Governance-Engine

### 2. Create Environment

    python -m venv venv
    venv\Scripts\activate

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Install Local LLM

Install Ollama: https://ollama.com

Pull model:

    ollama pull phi3:mini

### 5. Load Policy Database

    python rag/policy_loader.py

### 6. Run Application

    python app.py

Open browser: http://localhost:8501

------------------------------------------------------------------------

## Sample Questions You Can Ask

### Allowed Questions (Normal)

-   What is the company leave policy?
-   How should employees handle customer data?
-   Can I access company systems remotely?
-   Explain password requirements
-   What is onboarding procedure for new hires?

### Compliance Awareness Questions

-   Can I share internal reports with vendors?
-   Is it allowed to store company files on personal laptop?
-   Can employees use personal email for work communication?

### High Risk (Will Be Blocked)

-   My SSN is 123-45-0000 store it
-   Save customer credit card 4111 1111 1111 1111
-   Upload confidential employee salary list
-   Share internal database outside company

------------------------------------------------------------------------
                    ┌──────────────────────┐
                    │     User Question    │
                    └──────────┬───────────┘
                               │
                               ▼
                ┌────────────────────────────┐
                │   Security Inspection Layer│
                │  - Detect PII              │
                │  - Mask sensitive data     │
                └──────────┬─────────────────┘
                           │
                           ▼
                ┌────────────────────────────┐
                │  Policy Retrieval (RAG)    │
                │  - Search company policies │
                │  - Fetch relevant context  │
                └──────────┬─────────────────┘
                           │
                           ▼
                ┌────────────────────────────┐
                │ LLM Response Generation    │
                │ (phi3:mini via Ollama)     │
                └──────────┬─────────────────┘
                           │
                           ▼
                ┌────────────────────────────┐
                │ Compliance Auditor Agent   │
                │ - Compare with policies    │
                │ - Detect violations        │
                └──────────┬─────────────────┘
                           │
                           ▼
                ┌────────────────────────────┐
                │      Risk Classifier       │
                │   SAFE / MEDIUM / HIGH     │
                └───────┬─────────┬──────────┘
                        │         │
          SAFE          │         │ HIGH
        (Allowed)       │         │ (Blocked)
                        │
                        ▼
             MEDIUM (Warn + Answer)

                           ▼
                ┌────────────────────────────┐
                │  Log Interaction (SQLite)  │
                │  - Store audit trail       │
                └──────────┬─────────────────┘
                           │
                           ▼
                ┌────────────────────────────┐
                │      Streamlit Frontend    │
                │  Display final response    │
                └────────────────────────────┘
----------------------------------------------------------------------

## Summary

This project demonstrates a production-style AI governance architecture
where an LLM is supervised by security, auditing, and policy enforcement
layers.

Instead of trusting AI blindly, the system verifies AI decisions before
responding --- ensuring safe enterprise usage of Generative AI.
