# Your first GitHub contribution

**Dr. Brian Kyanjo**

## Start in class

The instructor will introduce https://github.com/KYANJO/numerical-methods-github. After creating and verifying your account, choose Fork > Create fork under your username. Check github.com/YOUR-USERNAME/numerical-methods-github.

**Browser route:** work in your fork online. No Git installation or SSH required.

**Computer route:** fork, follow SSH_SETUP.md, then clone your own fork. Choose one editing route for this exercise.

## 1. Inspect the experiment

Read README.md and results.csv. The exact integral of x² on [0,1] is 1/3. Here n=4,8,16 and h=1/n. The Conclusion in README is deliberately flawed. Replace it using evidence.

## 2. Create a branch

Browser: open the main dropdown, type explain-convergence, create the branch from main, and check its name.

Local, after cloning your fork:

```bash
git switch -c explain-convergence
```

## 3. Edit README.md

Browser: open README.md and choose the pencil. Local: use your text editor. Replace only the Conclusion section. Identify the function, interval, n values, absolute error, error ratios, and a limitation. What happens when n doubles? What order p fits an error ratio about 2^p?

## 4. Commit

Browser: Commit changes, message Explain trapezoidal error reduction, save to explain-convergence.

Local:

```bash
git diff
git add README.md
git commit -m "Explain trapezoidal error reduction"
git push -u origin explain-convergence
```

## 5. Open a pull request inside your own fork

Open your fork > Pull requests > New pull request. If needed, choose compare across forks to expose repository selectors.

- Base repository: YOUR-USERNAME/numerical-methods-github
- Base branch: main
- Head repository: YOUR-USERNAME/numerical-methods-github
- Compare branch: explain-convergence

GitHub may initially suggest KYANJO as the base. Change it to your own fork. Do not send the practice PR to the instructor repository.

Title: Document trapezoidal convergence. Explain what changed and which numerical evidence supports it. Read Files changed before creating the PR.

## 6. Review and merge

Ask a partner to inspect your screen. Does the claim match the data? Does the diff contain only intended edits? A verbal review is enough. Choose Merge pull request, then Confirm merge. Open your fork’s main and verify the conclusion.

After merging, local users update their copy:

```bash
git switch main
git pull --ff-only origin main
```

## Completion

Show the merged PR, new README on main, commit message, and an explanation of the numerical evidence.

## If you get stuck

- Signup or SSH blocked: pair in the browser using a signed-in partner’s account. Never share credentials.
- No comparison changes: check the branch and commit.
- Base says KYANJO: choose your own fork.
- Edited main by mistake: ask the instructor. Practice a fresh branch with another meaningful improvement without deleting history.
- Conflict or rejected push: ask for help. Avoid force-pushing or discarding work blindly.

## Optional calculation

Run python3 trapezoid.py, or py trapezoid.py on Windows. Add n=32 and n=64 in a new branch and document the error ratios. For x², compare with T_n=1/3+1/(6n²). Explain why this example does not prove the same behavior for all functions or all floating-point step sizes.
