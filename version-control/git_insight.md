# Git provides the following tools to manage version control

* [Git](#git): Version control system used to track changes in source code during software development
* [GitHub](#github): Web-based platform that uses Git for version control
* [GitOps](#gitops): Single source of truth for infrastructure and application deployment

---

## Git

**Git** is a distributed version control system (DVCS) designed to track changes in <u>source code</u> during software development. Every developer has a **full copy of the repository including its history**.

### Key Features

* Tracks changes to files and directories
* Allows branching, merging, and rollbacks
* Supports collaboration through remote repositories

### Core Concepts

* <u>Repository (repo)</u>: The project folder managed by Git
* <u>Remote</u>: A shared repository on a server or cloud
* <u>Branch</u>: A separate line of development (e.g., `main`, `feature-xyz`)
* <u>Commit</u>: A snapshot of changes with a unique hash
* <u>Merge</u>: Integrating changes from one branch to another
* <u>Clone</u>: Creating a copy of a repository
* <u>Pull</u>: Fetch and merge changes from the remote repository
* <u>Push</u>: Sending local changes to a remote repository
* <u>Fetch</u>: Downloading changes from a remote repository without merging
* <u>Rebase</u>: Reapplying commits on top of another base tip
* <u>Stash</u>: Temporarily saving changes that are not ready to be committed

### Git Architecture

Git operates with three main areas:

* **Working Directory**

  * Where you modify files
  * Git tracks changes here but they aren't committed yet

* **Staging Area (Index)**

  * Files added with `git add` go here
  * Preparation area before committing

* **Local Repository**

  * The `.git` folder stores all commits, branches, and configuration
  * Committing saves staged changes here

**Flow:**

```
Working Directory → git add → Staging Area → git commit → Local Repository → git push → Remote Repository
```

### Common Git Commands

* `git init` - Initialize a new Git repository
* `git clone <url>` - Clone a repository from a remote server
* `git add <file>` - Stage changes for the next commit
* `git commit -m "message"` - Commit staged changes with a message
* `git status` - Show the status of changes as untracked, modified, or staged
* `git log` - Show commit history
* `git branch` - List, create, or delete branches
* `git checkout <branch>` - Switch to a different branch
* `git merge <branch>` - Merge a branch into the current branch
* `git pull` - Fetch and merge changes from the remote repository
* `git push` - Push local changes to the remote repository

---

## GitHub

**GitHub** is a web-based platform for hosting Git repositories. It allows teams and developers to **collaborate on code, track issues, and manage projects**. Key features include:

* **Repositories** - Hosting and managing Git repositories
* **Forking** - Creating a personal copy of someone else's repository
* **Pull Requests** - Proposing changes to be merged into a repository
* **Issues** - Tracking bugs and feature requests
* **Actions** - Automating workflows with CI/CD pipelines
* **Wikis** - Documenting projects
* **Projects** - Organizing and tracking work with Kanban-style boards

### Forking

Forking is the process of creating a **personal copy of someone else's repository** under your GitHub account. This allows you to experiment without affecting the original repository.

**Key difference from clone:**

* **Fork:** Copy under your account
* **Clone:** Local copy on your machine

**Forking Flow:**

```
Original Repo → Fork → Your Fork (origin) → Clone → Local Repository → Make changes → Commit & Push → Pull Request → Merge → Original Repo
```

**Best Practices:**

* Fork only if you don’t have write access to the original repo
* Keep your fork up-to-date with `upstream`
* Always use feature branches
* Write clear commit messages
* Clean up merged branches to avoid clutter

### Pull Requests

A **Pull Request (PR)** is a request to merge changes from one branch into another (typically from a feature branch into `main` or `develop`).

**Workflow:**

1. Make changes in a branch and push
2. Open a pull request on GitHub and submit
3. Perform code review

   * Reviewer can leave comments and request changes
   * Once approved, the PR can be merged

**Merge options:**

* **Merge commit** - Keeps all commit history
* **Squash and merge** - Combines all commits into one
* **Rebase and merge** - Reapplies commits onto the base branch cleanly

**Sync Fork/Branch:**

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

**Best Practices for PRs:**

* Keep PRs small and focused
* Use descriptive titles and descriptions
* Reference issues when applicable
* Use feature branches
* Address review comments promptly
* Keep commit history clean (consider squash commits)

### Actions

**GitHub Actions** is a workflow automation platform for CI/CD.

**Uses:**

* Build, test, and deploy code automatically
* Respond to GitHub events (push, pull requests, issues)
* Automate repetitive tasks like linting or notifications

**Key Concepts:**

* **Workflow:** Defined in `.github/workflows/*.yml` triggered by events like `push`, `pull_request`, `schedule`
* **Job:** Set of steps running on a runner (VM or container)
* **Step:** Individual task in a job
* **Action:** Reusable unit of work, e.g., setup languages, run tests, deploy
* **Runner:** Environment executing the workflow (GitHub-hosted or self-hosted)

**Best Practices:**

* Keep workflows small and focused
* Use caching for dependencies
* Store sensitive information in secrets
* Use matrix builds to test multiple versions/OSes
* Monitor workflow run times and logs

---

## GitOps

**GitOps** uses Git as the **single source of truth** for both infrastructure and applications. All changes are made via Git commits, and automated systems apply those changes to the environment.

### Core Principles

* **Git as source of truth** - Infrastructure and application manifests stored in Git; Git history acts as audit log
* **Declarative infrastructure** - Use YAML, JSON, Helm charts to define desired state
* **Automated deployment** - Tools like Argo CD or Flux continuously reconcile live state
* **Pull-based model** - Agents pull changes from Git and apply them
* **Observability & self-healing** - Systems detect drift and auto-correct

### GitOps Workflow

1. Developer commits changes to Git (config, infrastructure, dependencies)
2. GitOps operator detects changes (e.g., Argo CD, Flux)
3. Automated deployment applies changes to environment
4. Continuous reconciliation ensures live state matches declared state

### GitOps vs Traditional CI/CD

| Feature            | Traditional CI/CD  | GitOps                       |
| ------------------ | ------------------ | ---------------------------- |
| Source of truth    | Pipeline configs   | Git repository               |
| Deployment trigger | Push from pipeline | Pull by operator from Git    |
| Visibility         | Pipeline logs      | Git history & cluster state  |
| Drift detection    | Manual             | Automatic                    |
| Rollback           | Manual/scripted    | Git revert → automatic apply |

### Benefits of GitOps

* Single source of truth → easier audits
* Automation & consistency → reduces human error
* Easy rollback → revert a Git commit
* Improved collaboration → changes via pull requests
* Enhanced security → no direct access needed

### Common Tools

* **Argo CD** - Kubernetes-native GitOps operator
* **Flux** - Continuous delivery for Kubernetes via Git
* **Terraform + GitOps** - Store Terraform configs in Git and automate
* **Helm + GitOps** - Helm charts in Git for declarative deployments

### Best Practices

* Store all configs declaratively in Git
* Use branches and PRs for changes and reviews
* Apply RBAC for GitOps operators
* Encrypt secrets
* Monitor for drift and errors
