# MEMORY.md

This file is the working memory for the AI assistant.

The assistant MUST update this file after every completed task.

The purpose is to avoid re-reading the entire project during future sessions.

---

# Current Project State

## Goal

Build a deterministic ML/MLOps batch processing application for the internship assessment.

---

# Architecture

(To be updated as development progresses.)

---

# Completed Tasks

- [ ] CLI
- [ ] YAML parsing
- [ ] Config validation
- [ ] CSV loading
- [ ] CSV validation
- [ ] Rolling mean
- [ ] Signal generation
- [ ] Metrics
- [ ] Logging
- [ ] Error handling
- [ ] Docker
- [ ] README

---

# Decisions

Document important implementation decisions here.

Example:

- Rolling mean uses pandas rolling().
- First `window - 1` rows produce NaN.
- NaN rows are excluded from signal-rate calculation.

Only record decisions that affect implementation.

---

# Files

## run.py

Purpose:

Status:

Notes:

---

## config.yaml

Purpose:

Status:

Notes:

---

## Dockerfile

Purpose:

Status:

Notes:

---

## README.md

Purpose:

Status:

Notes:

---

# Known Issues

Record unresolved bugs or TODO items.

---

# Session Log

Each completed development session should append a short summary.

Example:

## Session 1

Completed:

- CLI parsing
- YAML parsing

Next:

- CSV validation

---

## Instructions for AI Assistant

Before writing code:

1. Read this file first.
2. Continue from the latest completed task.
3. Update this file after finishing work.
4. Do NOT rewrite previous sections unnecessarily.
5. Keep entries concise and factual.