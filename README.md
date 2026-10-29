# Introduce Version Control Project

This repository demonstrates a simple software development workflow that includes version control, CI automation, and QA checks. It is intentionally small so students can focus on Git, GitHub, automated testing, and style validation.

## Project Goal

The project provides a lightweight grade calculator that helps students practice:
- Git branching and commits
- Pull requests and peer review
- Automated testing in GitHub Actions
- Python linting with flake8

## Features

The application includes functions to:
- calculate an average from a list of scores
- determine whether a score is passing
- map a numeric average to a letter grade

## Git workflow example

```bash
git init
git status
git add .
git commit -m "Initial project setup"
git checkout -b feature/grade-calculator
git push origin feature/grade-calculator
git checkout main
git merge feature/grade-calculator
```

## CI pipeline

Each push and pull request triggers a GitHub Actions workflow that installs dependencies, validates formatting with flake8, and runs the automated unit tests with pytest.

## QA report

See `QA_REPORT.md` for the formal summary of the tests, lint findings, and peer review notes.

## Reflection

Working through Git, CI, and QA tools introduced several practical challenges. At first, managing commits and branches felt unfamiliar, and merge conflicts were especially intimidating because they required careful attention to keep the project working. Learning when to commit and how to write meaningful messages also took practice, as it improved traceability and made collaboration easier. The CI pipeline proved especially useful because it automated validation every time changes were pushed. Instead of manually checking for syntax issues or broken logic, the workflow quickly reported failures, which reduced debugging time and helped keep the project stable. This made the development process more efficient and less error-prone.

Version control and QA practices also improved collaboration. Branching made it possible to work on ideas independently without disrupting the main codebase, while pull requests created a clear channel for feedback and review. Linting and tests helped enforce consistency and uncover problems earlier, which raised the quality of each change. Overall, these tools made it easier to work as a team, reduce mistakes, and maintain a cleaner, more reliable project.
