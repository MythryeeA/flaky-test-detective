# Flaky Test Detective

An autonomous AI agent that identifies, investigates, and helps remediate flaky tests in CI/CD pipelines.

## Problem

Flaky tests are automated tests that fail intermittently despite no changes to the underlying code. Engineering teams waste significant time rerunning builds, manually inspecting logs, and determining whether failures represent genuine regressions or unreliable tests.

As flaky tests accumulate, developers lose trust in automated testing systems, slowing software delivery and increasing operational costs.

## Solution

Flaky Test Detective acts as an autonomous engineering assistant that continuously monitors CI/CD pipelines and investigates unstable test behavior.

The agent:

* Monitors workflow runs and test outcomes
* Detects intermittent test failures
* Computes instability scores
* Identifies probable flaky tests
* Generates evidence-backed reports
* Creates GitHub Issues automatically
* Suggests remediation actions
* Optionally prepares quarantine pull requests

## Agent Workflow

### Perceive

Collects:

* Workflow execution logs
* Test results
* Commit metadata
* Historical build outcomes

### Decide

Analyzes:

* Failure frequency
* Pass/fail inconsistencies
* Historical behavior patterns

Calculates an instability score to distinguish flaky tests from genuine regressions.

### Act

Creates:

* Investigation reports
* GitHub Issues
* Root-cause summaries
* Remediation recommendations

Optionally proposes quarantine pull requests for human review.

## MVP Scope

The initial MVP focuses on:

1. Monitoring GitHub Actions workflow runs
2. Detecting intentionally simulated flaky tests
3. Computing instability scores
4. Automatically generating investigation reports
5. Creating GitHub Issues through GitHub APIs

## Tech Stack

* Python
* GitHub Actions
* GitHub REST API
* PyGithub
* Streamlit
* SQLite

## Future Vision

The long-term vision is an autonomous CI reliability platform capable of detecting flaky tests, isolating root causes, executing git bisect workflows, and proactively maintaining engineering productivity.

## Hackathon

Kartiline AI Agent Hackathon 2026

Idea #052 — Flaky Test Detective
