from abc import ABC, abstractmethod

from amnay.core.models import (
    ValidationIssue,
)


class Rule(ABC):

    id = "base-rule"

    name = "Base Rule"

    severity = "medium"

    @abstractmethod
    def validate(self, workflow):
        pass

    def issue(self, message):

        return ValidationIssue(
            rule_id=self.id,
            severity=self.severity,
            message=message,
        )
