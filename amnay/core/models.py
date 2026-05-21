from dataclasses import dataclass


@dataclass
class Job:
    name: str
    timeout: int | None
    commands: list[str]
    actions: list[str]
    permissions: dict | None = None
    image: str | None = None


@dataclass
class Workflow:
    name: str
    provider: str
    jobs: list[Job]
    raw: dict


@dataclass
class ValidationIssue:
    rule_id: str
    severity: str
    message: str
