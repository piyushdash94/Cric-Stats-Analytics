CONTRIBUTION GUIDELINES
=======================

# Commit etiquette
* add flags as prefix in commits: 
  * feat: for changes which add new things, 
  * refactor: for changes which update existing implementation,
  * fix: for changes which add a fix to existing implemenation,
  * chore: chores such as clean-up, adding documentation etc

* don't club different changes in the same commit

# Development Guidelines
* Don't merge changes directly to the main branch. Work instead on development branches, and merge them when ready using Pull Requests.
* Linting: Lint python files based on PEP-8 conventions using a linter such as black
* Naming conventions in python:
  * snake_case for file- and dir-names
  * PascalCase for class-names
  * snake_case for variables, attributes and function/method names
  * SCREAMING_SNAKE_CASE for constants
* Write functions that can be tested, write tests for functions