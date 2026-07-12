# Contributing to LifeOfPy

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution.

## Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [I Have a Question](#i-have-a-question)
3. [I Want To Contribute](#i-want-to-contribute)
    * [Reporting Bugs](#reporting-bugs)
    * [Suggesting Enhancements](#suggesting-enhancements)
    * [Contributing to Components](#contributing-to-components)
    * [Contributing to the Engine](#contributing-to-the-engine)
4. [Development Setup](#development-setup)
5. [Pull Request Process](#pull-request-process)
6. [Coding Conventions](#coding-conventions)

## Code of Conduct
This project and everyone participating in it is governed by the [LifeOfPy Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## I Have a Question
If you have a question, please first search our [Issue Tracker](https://github.com/lifeofpy/lifeofpy/issues) to see if it has already been answered. If not, feel free to open a new issue using the **Question** template.

## I Want To Contribute

### Reporting Bugs
Bugs are tracked as GitHub issues. When creating an issue, please use the **Bug Report** template and provide as much detail as possible, including:
- Operating System and Python version
- Steps to reproduce
- Expected behavior vs actual behavior

### Suggesting Enhancements
Enhancement suggestions are tracked as GitHub issues. Use the **Feature Request** template to propose new features or improvements.

### Contributing to Components
LifeOfPy is built on a vibrant ecosystem of components. To submit a new component:
1. Create an issue using the **Component Request** template to discuss your idea.
2. Ensure your component follows our design guidelines (accessible, zero-dependency if possible, well-documented).
3. Submit a Pull Request targeting the `registry/v1` directory.

### Contributing to the Engine
The core Engine (CLI, Downloader, Installer) is written in modern Python (3.12+).
- We use `uv` for dependency management.
- We use `Pydantic v2` for strict type validation.
- We require 100% test coverage for new Engine features.

## Development Setup
1. Fork and clone the repository.
2. Install `uv`: `pip install uv`
3. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip sync requirements.txt
   ```
4. Run the test suite:
   ```bash
   pytest packages/engine/tests
   ```

## Pull Request Process
1. Ensure your branch is named appropriately (e.g., `feat/add-new-button`, `fix/downloader-timeout`).
2. Update the README or documentation if you are changing user-facing features.
3. Fill out the Pull Request template completely.
4. Ensure all CI checks (linting, tests) pass.
5. Wait for a core maintainer to review and approve your PR.

## Coding Conventions
- **Formatting**: We use `ruff` to format our Python code. Run `ruff format` before committing.
- **Typing**: Strict type hints are required everywhere.
- **Commit Messages**: We follow conventional commits (e.g., `feat(cli): add list command`, `fix(engine): resolve cycle detection bug`).
