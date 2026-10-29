# QA Report

## Unit tests written

The project includes five automated tests that cover the main grade-calculation behaviors:

- average calculation for regular integer values
- average calculation for decimal values
- empty input validation
- passing threshold evaluation
- letter-grade mapping across score ranges

These checks help confirm that the grade logic behaves correctly across common student scenarios.

## Linter findings

The repository uses flake8 for style and consistency checks. During early validation, issues such as line length and missing blank lines were identified and corrected. After configuration updates, the codebase passes lint checks without errors.

## Code review summary

The project follows a simple peer-review workflow through GitHub pull requests. Review steps included verifying logic accuracy, checking readability, and confirming test coverage before merging changes. The review process encouraged clearer naming, simpler code, and better documentation of intent.

## Overall QA outcome

The combination of automated tests, linting, and pull-request review improves confidence in the code and makes it easier for students to collaborate responsibly.
