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

*Describe or link to where the reader can find documentation for the project. List any reference documents in the table below.*

| Document | Subject | Version and/or date | Issued by |
|:---:|---|:---:|:---:|
| NG0140 | L1 Array System Requirements Specification | R2 | SAO |

# Repository structure
[structure]: #repository-structure "Repository structure"

The repository contains multiple simulations that characterize various aspects of performance of
a specified VLBI array configuration. Each simulation is a self-contained Python package.

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

These instructions will get a copy of the repository up and running on your local machine for development and testing purposes. See [deployment][] for notes on how to deploy the project on a live system.

## Prerequisites

This section describes the things you need to build, test, and deploy the software and how to install and configure them.

*Describe the requierments on the build, test, and deployment environments here. Or, reference a document that describes them.*

## Setting up the development environment

*If not referencing another document, consider capturing installation and configuration steps in a separate file in this repository. Otherwise, use the template below.*

A step by step guide to getting a development environment up and running.

1. Say what the step will be

    ```
    Give the example
    ```

2. And repeat

    ```
    until finished
    ```

End with an example of running the system.


# Building the software
[build]: #building-the-software "Building the software"

*Describe how to build the software. Note that your software may not have a "build" step (i.e., it is a Python application)!*

# Running the software
[run]: #running-the-software "Running the software"

*Describe how to run the software.*

# CI/CD summary
[ci/cd]: #cicd-summary "CI/CD summary"

*Summarize the CI/CD approach used. Don't provide detail that is best captured as comments in CI/CD configuration files (e.g., GitHub Action YAML files). Use the text below as an example.*

GitHub Actions are used to automate building, testing, and deploying the software. See the files under [`.github/workflows`](.github/workflows) for details.

# Testing the software
[test]: #testing-the-software "Testing the software"

*Describe how to test the software. Use all pertinent sections below.*

* ## Manual tests

    *Describe manual tests (e.g., unit tests, smoke tests). Link to relevant documentation elsewhere in this repo if available rather than extending the length of this file.*

* ## Automated tests

    *Describe any automated tests (e.g., unit tests, static analysis, integration tests) present in this repository. Link to relevant documentation in the tests themselves if available rather than extending the length of this file.*

# Releasing the software
[release]: #releasing-the-software "Releasing the software"

* ## Versioning scheme

    *Describe the versioning scheme used for this repo and how it relates to the use of Git tags. For example, "tags should be of the format `major.minor.patch`.*

    *All projects should normally use the Git commit hash they were built from as a build identifier (this should be incorporated automatically with an appropriate build script) but you may also want a major and minor version number if there are many releases planned.*

    *[Semantic Versioning](https://semver.org) is recommended for use as a release numbering convention, where the Git commit hash can be part of the version metadata field (field that follows the `+` character).*

* ## Release procedure

    *Describe the release procedure for the software.*

    *It is recommended to create a new branch for releases, even on simple projects. Almost no extra effort is required and CI will by default run against all branches with no extra setup.*

    *Create tags from a branch dedicated for the release in question.*

    *Git does not support modifying the files under source control to include revision strings or commit hashes. Instead, the revision should always be determined and injected at build/runtime, typically using `git describe` to determine tag/branch names and to check for uncommitted changes.*

    *If credentials are required to perform a release or deployment whcih is triggered by CI, manage them as GitHub Secrets.*

    *An example release procedure is shown below. Tailor to your project's needs.*

1. Tag the branch from which the release is to be made with the version number for the release
1. Wait for the CI pipeline to complete successfully
1. Commit the build artifacts to permanent storage
1. Write a Software Release Note
1. Carry out the necessary level of testing and document the results
1. Update the Software Release Register with the details for the new release
1. Issue the release along with the corresponing Software Release Note

# Deployment / Installation
[deployment]: #deployment--installation "Deployment / Installation"

*Describe how releases are deployed and installed.*

# Change control
[change control]: #change-control "Change control"

*Describe how change control is enacted and enforced. Include details such as configuration policies for branch protection or pull requests.*

*Example text is provided below. Adapt to your project's needs.*

The branches shown in the table below are associated with development milestones or otherwise have a policy requiring the branch content remain stable and therefore be kept under a level of change control. GitHub's branch protection rules are used to enforce change control for these branches.

| Branch | Description |
|:---:|---|
| main | The default branch; expected to always contain stable, feature-complete versions of the software |

See the [Branch protection rules](https://github.com/Smithsonian/RepositoryName/settings/branches) for details on the protection configuration for all branches. The typical configuration will require pull requests to be used to merge changes into a protected branch; no direct commits will be permitted. This allows an independent member of the team to review the changes and explain what requires attention. This workflow encourages a more regular code review process than might otherwise happen. The set of approvers is specified in the pull request.

# Contributing
[contributing]: #contributing "Contributing"

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on the developer workflow for contributing changes to the software.

# Licensing
[licensing]: #licensing "Licensing"

See the [LICENSE](LICENSE) file for details on the licensing of this software.
