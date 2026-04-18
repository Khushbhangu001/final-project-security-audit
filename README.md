# final-project-security-audit
Course: COMP-3021 Secure Coding and Testing
auther : khushdeep kaur 
This repository contains a small intentionally insecure Python demo (audit_target_app.py) used only for learning and for a security audit in this course.

Whats included
Python code with patterns that illustrate common issues (e.g. hard-coded secrets, weak authentication demo, command injection, SQL injection, cleartext HTTP, unsafe URL fetch / SSRF-style pattern, unsafe deserialization).
GitHub Actions: Bandit workflow (.github/workflows/bandit.yml) runs on every push and pull request.
Local scanning: Bandit is run from the project folder to generate findings (terminal output and/or HTML report for the audit PDF).
Important
This code is not production-ready and must not be deployed as a real application. The goal is to find and document issues and mitigations for the final audit report.

License
MIT License LICENSE.

