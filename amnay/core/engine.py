from amnay.core.registry import (
    RULE_REGISTRY,
)

SEVERITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "info": 4,
}


class ValidationEngine:

    def __init__(self, policy):

        self.rules = []

        self.load_rules(policy)

        self.sort_rules()

    def load_rules(self, policy):

        for rule_name, config in policy["rules"].items():

            if not config.get("enabled"):
                continue

            rule_class = RULE_REGISTRY[rule_name]

            kwargs = {k: v for k, v in config.items() if k != "enabled"}

            self.rules.append(rule_class(**kwargs))

    def sort_rules(self):

        self.rules.sort(
            key=lambda rule: SEVERITY_ORDER.get(
                rule.severity,
                999,
            )
        )

    def validate(self, workflow):

        issues = []

        for rule in self.rules:

            issues.extend(rule.validate(workflow))

        return issues
