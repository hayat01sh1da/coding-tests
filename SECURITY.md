# Security Policy

## Supported Versions

- Only the latest content on `master` receives fixes. Exercises should be synced before reporting issues.
- Archived kata or historical snapshots are considered out of scope for security servicing.

## Ecosystem & Compatibility

| Track / Component      | Version(s) / Tooling          | Notes |
| ---------------------- | ----------------------------- | ----- |
| OS baseline            | WSL (Ubuntu 24.4.3 LTS)       | Shared development environment across languages. |
| Ruby exercises         | Ruby 4.0.1 (`.ruby-version`)  | Bundler-managed gems per kata; default relies on stdlib. |
| Python exercises       | CPython 3.14.3 (`.python-version`) | Requirements are declared per exercise; base templates use stdlib only. |
| JavaScript exercises   | Node v25.3.0 (`.node-version`) | Use the Node toolchain plus any dependencies listed inside each `package.json`. |

## Backward Compatibility

- Katas aim to remain stable within a runtime line (Ruby 4.0.x, Python 3.14.x, Node 25.x). When an exercise requires a breaking change, the README for that kata will call it out explicitly.
- Older interpreter majors are not tested and will not receive security backports. Please upgrade your toolchain before filing security reports.

## Reporting a Vulnerability

Please disclose security issues privately:

1. Use GitHub’s **Security → Report a vulnerability** flow to open a private  advisory (preferred).
2. If GitHub is unavailable, contact the maintainers using the email address or contact method listed in the repository or organization profile, including reproduction steps, affected tracks, and expected/actual behavior.

We respond within **3 business days** and keep you updated at least every **7 business days**.  
After remediation we will coordinate disclosure and offer credit if desired.
