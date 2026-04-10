## Supported Versions

- Only the latest content on `master` receives fixes. Exercises should be synced before reporting issues.
- Archived kata or historical snapshots are considered out of scope for security servicing.

## Ecosystem & Compatibility

| Track / Component    | Version(s) / Tooling               | Notes                                                                           |
| -------------------- | ---------------------------------- | ------------------------------------------------------------------------------- |
| OS baseline          | WSL (Ubuntu 25.10)                 | Shared environment across tracks.                                               |
| Ruby exercises       | Ruby 4.0.2 (`.ruby-version`)       | Bundler-managed gems per kata; default relies on stdlib.                        |
| Python exercises     | CPython 3.14.4 (`.python-version`) | Requirements are declared per exercise; base templates use stdlib only.         |
| JavaScript exercises | Node v25.9.0 (`.node-version`)     | Use the Node toolchain plus any dependencies listed inside each `package.json`. |

## Backward Compatibility

- Katas aim to remain stable within a runtime line (Ruby 4.0.x, Python 3.14.x, Node 25.x). When an exercise requires a breaking change, the README for that kata will call it out explicitly.
- Older interpreter majors are not tested and will not receive security backports. Please upgrade your toolchain before filing security reports.

## Reporting a Vulnerability

Please report issues privately via **GitHub Security Advisory** (preferred) — open through the repository’s **Security → Report a vulnerability** workflow.

Acknowledgement occurs and status updates follow as soon as possible.  
After remediation we publish guidance alongside required dependency updates.
