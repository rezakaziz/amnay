from amnay.rules.base import Rule


class LeastPrivilegeRule(Rule):

    id = "least-privilege"

    name = "Least Privilege"

    severity = "high"

    def validate(self, workflow):

        if workflow.provider != "github":
            return []

        issues = []

        permissions = workflow.raw.get("permissions")

        if permissions is None:

            issues.append(self.issue("workflow: missing " "permissions block"))

        elif permissions == "write-all":

            issues.append(self.issue("workflow: overly permissive " "GITHUB_TOKEN"))

        return issues
