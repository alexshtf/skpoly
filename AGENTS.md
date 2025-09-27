# Contribution Guidelines for skpoly

## Documentation
- Write docstrings using the scikit-learn (NumPy) style, including Parameters, Returns, and Examples when appropriate.
- Keep narrative documentation precise and action-oriented; prefer bullet lists and short sentences over lengthy prose.
- Build the documentation in ``docs/`` with ``uv run sphinx-build docs docs/_build/html``.

## Code Style
- Strive for concise, intention-revealing code—avoid "slop" such as redundant variables, overly defensive checks, and sprawling helper layers.
- Use SciPy / NumPy to the extent possible, including vectorization whenever possible.
- Use Scikit-Learn utilities, such as the classes from the `sklearn.base` package, and functions in the `sklearn.utils` package.
- Favor self-explanatory identifiers, short functions, and cohesive classes so the code documents itself.
- Only add comments when they communicate non-obvious context or rationale; do not restate what the code already expresses.
- Follow type hints consistently across the codebase and prefer explicit imports over wildcard imports.

## Testing & Tooling
- Builds and dependency installations are done using `uv`.
- Add or update tests alongside behavioral changes. Prefer focused unit tests in `tests/` and keep fixtures minimal.
- Run the relevant test suite (typically `pytest`) before submitting changes, and ensure static checks (e.g., `ruff`, `mypy`) pass when they apply to the touched areas.

## Git & PR Workflow
- Keep commits scoped and descriptive. Reference the impacted modules or features in the commit message subject.
- Update changelogs or user-facing documentation when the public API changes.
- Review the repository for nested `AGENTS.md` files; more specific instructions override the general guidance here.

## Communication
- When opening pull requests, provide a concise summary of the change, the motivation, and key verification steps. Use bullet lists for clarity.
- Highlight any follow-up work or known limitations so reviewers can plan accordingly.

Adhering to these guidelines helps maintain a clean, predictable codebase that is easy for collaborators to navigate and extend.
