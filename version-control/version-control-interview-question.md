# Version Control

This section covers essential **Git**, **GitHub**, and **GitOps** interview questions to help you understand and explain version control concepts effectively.

---

## 🌀 Git Questions

1. **What is Git?**  
   Git is a distributed version control system that allows developers to track changes in source code during software development. It enables multiple developers to work on the same project simultaneously without conflicts.

2. **What is a Git repository?**  
   A Git repository is a storage location where all the files and their revision history are stored. It can be local to a developer's machine or hosted on a remote server.

3. **How do you create a new Git repository?**  
   Use the command:  
   ```bash
   git init
   ```
   This initializes an empty repository in the current directory.

4. **How do you clone a repository?**  
   ```bash
   git clone <repository-url>
   ```
   This creates a local copy of the repository from a remote server.

5. **What is a commit in Git?**  
   A commit is a snapshot of changes made to the repository. It records the state of the project at a specific point in time.

6. **How do you make a commit?**  
   ```bash
   git add <file>
   git commit -m "commit message"
   ```

7. **What is branching in Git?**  
   Branching allows you to create a parallel version of the repository to work on new features or changes without affecting the main branch.

8. **How do you create a new branch?**  
   ```bash
   git branch <branch-name>
   git checkout <branch-name>
   ```

9. **What is merging in Git?**  
   Merging combines changes from one branch into another.

10. **How do you merge branches?**  
    ```bash
    git checkout main
    git merge <branch-name>
    ```

11. **What is a pull request?**  
    A pull request is a way to propose changes to a repository for review before merging.

12. **What is a conflict in Git?**  
    A conflict occurs when changes from different branches cannot be automatically merged.

13. **How do you resolve conflicts in Git?**  
    Manually edit the conflicting files, resolve differences, then commit the resolved files.

14. **What is `git stash`?**  
    Temporarily saves changes that are not ready to be committed.

15. **How do you apply stashed changes?**  
    ```bash
    git stash apply
    # or
    git stash pop
    ```

16. **What is `git pull`?**  
    Fetches changes from the remote repository and merges them into the local repository.

17. **What is `git push`?**  
    Uploads local commits to a remote repository.

18. **What is `git fetch`?**  
    Downloads changes from the remote repository without merging them.

19. **What is `git rebase`?**  
    Moves or combines commits onto a new base commit, often used to keep branches up to date.

20. **What is a detached HEAD in Git?**  
    Occurs when you check out a commit that isn’t associated with any branch.

21. **How do you delete a branch?**  
    ```bash
    git branch -d <branch-name>
    git branch -D <branch-name> # force delete
    ```

22. **What is `git diff`?**  
    Shows differences between commits or between the working directory and the repository.

23. **How do you revert a commit?**  
    ```bash
    git revert <commit-hash>
    ```

24. **What is `git log`?**  
    Displays the commit history.

25. **What is `git blame`?**  
    Shows who last modified each line in a file.

26. **What is a tag in Git?**  
    A reference to a specific commit, often marking releases.

27. **How do you create a tag?**  
    ```bash
    git tag <tag-name>
    git tag -a <tag-name> -m "message"
    ```

28. **What is `git checkout`?**  
    Used to switch branches or restore working directory files.

29. **What is a remote in Git?**  
    A reference to a repository hosted elsewhere.

30. **How do you add a remote?**  
    ```bash
    git remote add <name> <url>
    ```

---

## 🧭 GitHub Questions

(questions 31–50 as above)

---

## ⚙️ GitOps Questions

(questions 51–75 as above)

---

**Next Section:**  
[← Back to Main README](../README.md)
