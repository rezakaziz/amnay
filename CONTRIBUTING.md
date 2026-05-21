# Contributing to Amnay

Thank you for contributing to Amnay.

Amnay is a provider-agnostic CI/CD validation tool focused on:

- workflow security
- reliability
- CI/CD governance
- pipeline best practices

The project is designed to stay:

- simple
- extensible
- provider-agnostic

---

# Project Architecture

Amnay follows a simple architecture:

```text id="x3m7q1"
Provider
    ->
Normalized Workflow
    ->
Validation Engine
    ->
Rules
    ->
Issues
```

Providers are responsible for parsing CI/CD configuration files and converting them into a normalized workflow model.

Rules validate the normalized workflow model independently from the CI provider.

---

# Running the Project

Clone the repository:

```bash id="m8v2q5"
git clone https://github.com/rezak430/amnay.git

cd amnay
```

Create a virtual environment:

```bash id="n4x7m1"
python -m venv .venv
```

Activate the environment:

```bash id="u1m5q8"
source .venv/bin/activate
```

Install the project:

```bash id="p7v3m9"
pip install -r requirements.txt
pip install -e .
```

Run the CLI:

```bash id="q2m8x4"
amnay --help
```

---

# Adding a New Rule

Rules are located in:

```text id="r5v1m7"
amnay/rules/
```

Rules should:

- validate normalized workflow models
- remain provider-agnostic whenever possible
- stay simple and focused

Example rule:

```python id="j8m4q2"
from amnay.rules.base import Rule


class ExampleRule(Rule):

    id = "example"

    severity = "medium"

    def validate(self, workflow):

        issues = []

        return issues
```

Rules should return validation issues using:

```python id="k1v7m5"
self.issue("message")
```

---

# Registering a Rule

Rules must be registered in:

```text id="p9m2x6"
amnay/core/registry.py
```

Example:

```python id="u4m8q1"
RULE_REGISTRY = {
    "timeout": TimeoutRule,
    "pinned_actions": PinnedActionsRule,
}
```

---

# Enabling Rules Through Policies

Rules are enabled using YAML policy files.

Policies are located in:

```text id="m6v3q9"
amnay/policies/
```

Example:

```yaml id="x2m7q4"
rules:
  timeout:
    enabled: true
    max_timeout: 30

  pinned_actions:
    enabled: true
```

---

# Adding a New Provider

Providers are located in:

```text id="q7m1v5"
amnay/providers/
```

Each provider is responsible for:

- loading CI/CD configuration files
- parsing provider-specific syntax
- producing normalized workflow models

Example structure:

```text id="u5m8q2"
providers/
└── github/
    └── provider.py
```

Example provider:

```python id="n3v7m4"
class ExampleProvider:

    def load(self, path):
        pass
```

Providers should normalize concepts such as:

- jobs
- commands
- actions
- timeouts

so rules can remain reusable across providers.

---

# Design Principles

Amnay follows a few important principles:

- rules should not parse YAML directly
- rules should not depend on provider syntax
- providers normalize CI/CD workflows
- rules validate normalized workflows
- the engine orchestrates validation

The project intentionally avoids unnecessary complexity and heavy abstractions.

---

# Future Areas

Contributions are welcome for:

- new validation rules
- GitLab CI support
- output formats
- SARIF support
- JSON reporting
- auto-fix capabilities
- documentation improvements

---

# License

By contributing to Amnay, you agree that your contributions will be licensed under the MIT License.
