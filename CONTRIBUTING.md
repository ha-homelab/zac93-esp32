# Contributing

Use issues for reproducible problems and pull requests for changes. Include the exact board/module and versions, the first failing diagnostic layer and redacted evidence. Do not present an untested pin map or firmware build as hardware-verified.

Before committing, install Gitleaks and enable the local hooks with `git config core.hooksPath .githooks`. See [SECURITY.md](SECURITY.md). The hooks inspect staged content and history; they intentionally fail if Gitleaks is unavailable.

Run these checks from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
python3 scripts/render_diagrams.py
git diff --exit-code -- assets/diagrams
```

Validate both board configurations with the pinned ESPHome release. `scripts/validate_configs.py` uses disposable dummy credentials in a temporary directory and never overwrites your real secrets. Add `--compile` to compile both variants; it does not flash hardware.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/validate_configs.py
python3 scripts/validate_configs.py --compile
```

Pin-map changes need the relevant board schematic or a clearly identified physical test. Keep the English wiring/setup pages, Russian guide, YAML and diagram generator consistent. Add new photographs only if you have permission to publish them; cite external reference material and explain differences. Recheck links and commands when updating software versions.


Every major functionality change must include automated tests and relevant
negative cases. Firmware/configuration changes require successful full builds
of both supported boards with disposable credentials; this proves compilation,
not physical commissioning. Python changes must pass Ruff E4/E7/E9/F checks.
The maintainer reviews test evidence and substantive findings before a normal
pull-request merge. Do not disable checks to obtain a green result.


## Project participation

Use public GitHub issues and pull requests for questions, proposals and reproducible non-sensitive bugs. English is the shared discussion language. Read [governance](GOVERNANCE.md), [Code of Conduct](CODE_OF_CONDUCT.md) and the [roadmap](ROADMAP.md). All major functionality changes require automated regression coverage, including relevant negative cases, and updated interface documentation. Resolve review findings and required CI failures before normal merge. Original contributions are accepted under the repository MIT license; preserve third-party licensing and attribution.
