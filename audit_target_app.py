import os
import pickle
import sqlite3
import subprocess
from urllib.request import urlopen

# Intentionally insecure demo code for a security audit course project.
# Do NOT use this pattern in real applications.

API_KEY = "DEMO-API-KEY-DO-NOT-USE-IN-PRODUCTION" 


def run_shell_demo(user_value: str) -> None:
    # Command injection risk (shell=True + user-controlled input)
    subprocess.run(f"echo {user_value}", shell=True, check=False)


def read_file_demo(path: str) -> str:
    # Path traversal risk if caller can pass "../../../Windows/win.ini" etc.
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def fetch_over_http_demo() -> str:
    # Cleartext transport (no TLS verification concerns because it's HTTP)
    return urlopen("http://example.com").read().decode("utf-8", errors="ignore")


def sql_demo(username: str, password: str) -> None:
    # SQL injection risk (string-built SQL)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cur.execute(query)
    conn.commit()
    conn.close()


def unsafe_deserialize_demo(blob: bytes) -> object:
    # Insecure deserialization (pickle can execute arbitrary code)
    return pickle.loads(blob)


def legacy_os_system_demo(cmd: str) -> int:
    # Another command injection pattern (shell command built from input)
    return os.system(cmd)


if __name__ == "__main__":
    print("audit_target_app.py loaded (demo insecure project)")