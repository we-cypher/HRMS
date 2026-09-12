# Contributing Guidelines for WePeople HRMS

Thank you for considering contributing to WePeople HRMS! We welcome your input and appreciate the community effort to make this project even better.

## Branches

- **`dev/v2.0`** — the active integration branch. Always clone this and always open PRs against this — never against `2.0` directly.
- **`2.0`** — the repository's default branch: a periodic public snapshot for running/deploying, not where day-to-day development happens.

## How to Contribute

1. **Fork the Repository**
   - Fork [we-cypher/HRMS](https://github.com/we-cypher/HRMS) on GitHub.

2. **Clone the Repository**

     ```bash
     git clone -b dev/v2.0 https://github.com/YOUR_USERNAME/HRMS.git
     cd HRMS
     git remote add upstream https://github.com/we-cypher/HRMS.git
     ```

3. **Create a Branch**

     ```bash
     git checkout -b feature-or-bugfix-branch
     ```

4. **Set Up Locally**

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     pip install pre-commit
     pre-commit install
     # Optional Docker stack:
     make dev
     ```

5. **Make Changes**
   - Follow coding conventions (extend `HorillaModel`, use decorators, HTMX patterns).
   - Run formatters via pre-commit (Black + isort).

6. **Commit Changes**

     ```bash
     git commit -m "[ADD] APP: clear description of why"
     ```

     Allowed tags: `[ADD]`, `[FIX]`, `[UPDT]`, `[REMOVE]` (and existing `[FEAT]` where used).

7. **Push and Open a Pull Request**
   - Target branch: **`dev/v2.0`**
   - Provide a clear title/description and link related issues
   - CI should stay green: **Docker CI** + **Quality**

## Code Style and Guidelines

- Follow [PEP 8](https://pep8.org/); format with Black; sort imports with isort (`--profile black`).
- Keep changes focused; prefer small PRs for reviewability.
- Never commit secrets: `.env`, API keys, TLS keys, database dumps, or local SQLite files.
- Use `.env.dist` as the public template (`cp .env.dist .env`); keep real `.env` files local only.

### Line endings

`.gitattributes` normalises text files to LF in the repository. Git checks
them out with your platform's native endings, so this needs no change to how
you edit — it only fixes what gets stored.

## CI Expectations

| Workflow | What it checks |
|----------|----------------|
| `Docker CI` | Image build, migrate, collectstatic, `/health/`, `/ready/` |
| `Quality` | `ruff check .` over the whole repo, Black/isort, `manage.py check`, production settings gate |

## Issues

- Bugs and features: open a public GitHub issue with reproduction steps.
- **Security vulnerabilities:** do **not** open a public issue — use [GitHub Private Vulnerability Reporting](https://github.com/we-cypher/HRMS/security/advisories/new). See [SECURITY.md](SECURITY.md) for full details.

## Community Guidelines

- Be respectful and considerate of others.
- Provide constructive feedback.
- Encourage a positive and inclusive community.

Thank you for your contributions to WePeople HRMS!
