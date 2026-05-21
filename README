# Amnay

Amnay is a CI/CD validation engine for modern pipelines.

It helps teams validate:

- security
- reliability
- best practices

across CI providers like:

- GitHub Actions
- GitLab CI

---

# Features

- GitHub Actions validation
- Policy-based rules
- Security checks
- Reliability checks
- Multi-provider architecture
- Simple CLI

---

# Example Rules

- Missing timeout
- Dangerous commands
- Unpinned GitHub Actions
- Missing concurrency
- Overly permissive permissions

---

# Installation

```bash id="y5m2q8"
pip install amnay
```

---

# Usage

Validate a GitHub Actions workflow:

```bash id="x1v7m4"
amnay validate github \
.github/workflows/build.yml
```

---

# Example Output

```text id="q8m3v1"
HIGH timeout:
build: missing timeout

CRITICAL pinned-actions:
deploy: action not pinned to immutable SHA
```

---

# Policies

Rules can be configured with YAML policies.

Example:

```yaml id="n4x9m2"
rules:
  timeout:
    enabled: true
    max_timeout: 30

  concurrency:
    enabled: true

  pinned_actions:
    enabled: true
```

---

# Architecture

```text id="m7v2q5"
Provider
    ->
Normalized Workflow
    ->
Rules Engine
    ->
Issues
```

---

# Project Goals

Amnay focuses on:

- CI/CD governance
- workflow quality
- security validation
- deployment reliability

It is NOT:

- a CI runner
- an orchestrator
- a workflow engine

---

# Roadmap

- GitLab CI support
- SARIF output
- JSON output
- Auto-fix mode
- Organization-wide auditing

---

# License

MIT License.
