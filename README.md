**[DOCS][] | [STRUCTURE][] | [GETTING STARTED][] | [BUILD][] | [RUN][] | [CI/CD][] | [TEST][] | [RELEASE][] | [CHANGE CONTROL][] | [CONTRIBUTING][] | [LICENSING][]**

# ngeht-arrayperformance-sims
[r]: #repo

This repository is hosted at https://github.com/Smithsonian/ngeht-arrayperformance-sims

It contains the simulations that predict the performance of VLBI array configurations. They are
primarily as part of the ngEHT program's design stage to understand how well specific array
configurations meet the array system requirements specified in [NG0140].

This software is developed in conformance with [ngEHT Software Guidelines v0.1.0](https://github.com/Smithsonian/ngeht-sw-guidelines/releases/tag/v0.1.0).

# Documentation
[docs]: #documentation "Documentation"



## Reference documents  
| Document | Subject | Version and/or date | Issued by |
|:---:|---|:---:|:---:|
| NG0140 | L1 Array System Requirements Specification | R2 | SAO |

# Repository structure
[structure]: #repository-structure "Repository structure"

The repository contains multiple simulations that characterize various aspects of performance of
a specified VLBI array configuration. Each simulation is a self-contained Python script or set of
scripts, and includes a README that describes how to install the necessary dependencies and run the
simulation.

|Path|Description|Version-controlled|
|--|--|:--:|
| ~~docs/~~     | (TODO) Documentation | Yes |
| **sims/**     | Simulations, one per subdirectory  | Yes |
| ~~tests/~~    | (TODO) Tests for the simulations | Yes |
| ~~tools/~~    | (TODO) Scripts and things to aid development, not part of end software | Yes |
| **.github/**  | GitHub Actions, etc. | Yes |
| [**.gitignore**](.gitignore)  | Lists what *not* to version control at the application level | Yes |
| [**README.md**](README.md) | This file | Yes |

# Getting Started
[getting started]: #getting-started "Getting Started"

These instructions will get a copy of the repository up and running on your local machine for
development and testing purposes. See [deployment][] for notes on how to deploy the project on a
live system.

## Prerequisites

This section describes the things you need to build, test, and deploy the software and how to install and configure them.

*Describe the requierments on the build, test, and deployment environments here. Or, reference a document that describes them.*

## Setting up the environment

Here is a step by step guide to getting a development & execution environment up and running.
They are provided assuming a UNIX environment; some adaptation may be required if you are running
on another platform.

1. Create a Python virtual environment in a directory named `.venv` and activate it  
    _While you could do this without a virtual environment, it is not recommended_

    ```
    $ python -m venv .venv
    $ source .venv/bin/activate
    (.venv) $ python -m pip install --upgrade pip
    ```

You are now ready to develop and execute simulations. See the README for each simulation for any
further instrunctions on setting up the environment or executing the simulation.

# CI/CD summary
[ci/cd]: #cicd-summary "CI/CD summary"

GitHub Actions are used to automate testing the software. See the files under [`.github/workflows`](.github/workflows) for details.

# Testing the software
[test]: #testing-the-software "Testing the software"

*Describe how to test the software. Use all pertinent sections below.*

## Manual tests

*Describe manual tests (e.g., unit tests, smoke tests). Link to relevant documentation elsewhere in this repo if available rather than extending the length of this file.*

## Automated tests
The table below shows the automated tests carried out with GiHub Actions.

| Workflow | Description | Status |
|---|---|:---:|
| [Lint](.github/workflows/lint.yml) | Lints the source code with Flake8 | [![Lint status](https://github.com/Smithsonian/ngeht-arrayperformance-sims/actions/workflows/lint.yml/badge.svg)](https://github.com/Smithsonian/ngeht-arrayperformance-sims/actions) |

# Releasing the software
[release]: #releasing-the-software "Releasing the software"

* ## Versioning scheme

    Versions of software are recorded through the use of Git tags. Tags are in the form of
    `vX.Y.Z` where

    * `X` is the major version number
    * `Y` is the minor version number
    * `Z` is the patch version number

    The major, minor, and patch numbers are used as defined in
    [Semantic Versioning](https://semver.org).

    The version number is obtained from the most recent Git tag matching the regex `^v\d+\.\d+\.\d+$`.

* ## Release procedure

    This repository is not intended to be a deployable Python package (i.e., not available on PyPI
    or installable with `pip install`). Therefore, releases involve simply tagging the `main`
    branch with the appropriate version string when a new release is desired.

# Deployment / Installation
[deployment]: #deployment--installation "Deployment / Installation"

Because the simulations are not intended to be deployable Python packages (i.e., available on
PyPI or installable with `pip install`), there is no defined deployment method. Users can "install"
the simulations by cloning this Git repository.

# Change control
[change control]: #change-control "Change control"

The branches shown in the table below are associated with development milestones or otherwise have
a policy requiring the branch content remain stable and therefore be kept under a level of change
control. GitHub's branch protection rules are used to enforce change control for these branches.

| Branch | Description |
|:---:|---|
| main | The default branch; expected to always contain stable, feature-complete versions of the software |

See the [Branch protection rules](https://github.com/Smithsonian/ngeht-arrayperformance-sims/settings/branches) for details on the protection configuration for all branches. The typical configuration will require pull requests to be used to merge changes into a protected branch; no direct commits will be permitted. This allows an independent member of the team to review the changes and explain what requires attention. This workflow encourages a more regular code review process than might otherwise happen. The set of approvers is specified in the pull request.

# Contributing
[contributing]: #contributing "Contributing"

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on the developer workflow for contributing changes to the software.

# Licensing
[licensing]: #licensing "Licensing"

See the [LICENSE](LICENSE) file for details on the licensing of this software.
