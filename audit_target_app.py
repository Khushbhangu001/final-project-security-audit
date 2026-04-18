"""
Intentionally insecure demo code for COMP-3021 Final Project: Code Security Audit.

Each section is labeled with OWASP Top 10:2021 categories for mapping in your audit report.
Do NOT run in production. Do NOT deploy publicly.
"""

import os
import pickle
import sqlite3
import subprocess
from urllib.request import urlopen

# -----------------------------------------------------------------------------
# A02:2021 Cryptographic Failures — hard-coded secret in source
# -----------------------------------------------------------------------------
ADMIN_API_TOKEN = "hardcoded-secret-token-DO-NOT-COMMIT-IN-REAL-APPS"


# -----------------------------------------------------------------------------
# A05:2021 Security Misconfiguration — "debug" / permissive defaults
# -----------------------------------------------------------------------------
DEBUG_MODE = True  # verbose errors can leak internals in real web frameworks


# -----------------------------------------------------------------------------
# A07:2021 Identification and Authentication Failures — weak credential check
# -----------------------------------------------------------------------------
def login_demo(username: str, password: str) -> bool:
    # Weak: compares plaintext; no hashing, no rate limiting (demo only)
    return username == "admin" and password == "admin123"


# -----------------------------------------------------------------------------
# A01:2021 Broken Access Control — path traversal / arbitrary file read
# -----------------------------------------------------------------------------
def read_user_file_demo(user_supplied_path: str) -> str:
    with open(user_supplied_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


# -----------------------------------------------------------------------------
# A03:2021 Injection — OS command injection (shell=True)
# -----------------------------------------------------------------------------
def run_shell_demo(user_value: str) -> None:
    subprocess.run(f"echo {user_value}", shell=True, check=False)


def legacy_os_system_demo(cmd: str) -> int:
    return os.system(cmd)


# -----------------------------------------------------------------------------
# A03:2021 Injection — SQL injection (string-built query)
# -----------------------------------------------------------------------------
def sql_demo(username: str, password: str) -> None:
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cur.execute(query)
    conn.commit()
    conn.close()


# -----------------------------------------------------------------------------
# A02:2021 Cryptographic Failures — cleartext HTTP (no TLS)
# -----------------------------------------------------------------------------
def fetch_over_http_demo() -> str:
    return urlopen("http://example.com").read().decode("utf-8", errors="ignore")


# -----------------------------------------------------------------------------
# A10:2021 Server-Side Request Forgery (SSRF) — fetch user-controlled URL
# -----------------------------------------------------------------------------
def fetch_url_demo(url: str) -> str:
    # Dangerous if `url` can point to internal services (file://, metadata IPs, etc.)
    return urlopen(url).read().decode("utf-8", errors="ignore")


# -----------------------------------------------------------------------------
# A08:2021 Software and Data Integrity Failures — unsafe deserialization
# -----------------------------------------------------------------------------
def unsafe_deserialize_demo(blob: bytes) -> object:
    return pickle.loads(blob)


# -----------------------------------------------------------------------------
# A04:2021 Insecure Design — business logic flaw (authorization by client input)
# -----------------------------------------------------------------------------
def is_admin_demo(client_claims_admin: bool) -> bool:
    # Insecure design: trusting client-supplied flag instead of server-side session
    return client_claims_admin


# -----------------------------------------------------------------------------
# A06:2021 Vulnerable and Outdated Components — (flag for audit; Bandit may note imports)
# Use dependency scanners (pip-audit, Dependabot) on requirements.txt in real projects.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# A09:2021 Security Logging and Monitoring Failures — silent failure / no audit trail
# -----------------------------------------------------------------------------
def sensitive_operation_demo(user_id: str) -> None:
    # No security event logged; failures could hide abuse
    _ = user_id
    pass


if __name__ == "__main__":
    print("owasp_top10_demo_audit.py loaded (intentionally vulnerable demo)")
