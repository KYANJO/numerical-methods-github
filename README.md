# GitHub for numerical methods

**Instructor: Dr. Brian Kyanjo**

A small numerical experiment for learning GitHub. The instructor will introduce this repository in class.

## Get your copy after account creation

1. Sign in and verify your GitHub email.
2. Choose **Fork > Create fork** under your own username.
3. Check that the address is `github.com/YOUR-USERNAME/numerical-methods-github`.
4. Work in **your fork**. The entire core exercise works in your browser.
5. To work locally, follow [SSH_SETUP.md](SSH_SETUP.md), then clone your fork:

```bash
git clone git@github.com:YOUR-USERNAME/numerical-methods-github.git
cd numerical-methods-github
```

A **fork** is your copy on GitHub. A **clone** is a working copy on your computer. Cloning this instructor repository alone does not give you permission to push here. Fork first to publish your own changes.

## The numerical experiment

Estimate the integral of **f(x) = x² on [0,1]** with the composite trapezoidal rule.

- Exact integral: **1/3**.
- `n` is the number of equal intervals.
- `h = 1/n` is the sample spacing.
- Absolute error: **|estimate - 1/3|**.

| File | Purpose |
| --- | --- |
| `trapezoid.py` | Optional Python 3 calculation, no extra packages |
| `results.csv` | Supplied results for n = 4,8,16 |
| `STUDENT_GUIDE.md` | Browser and local exercise steps |
| `SSH_SETUP.md` | SSH keys, connection test, and cloning |

Optional reproduction: `python3 trapezoid.py` or, on Windows, `py trapezoid.py`.

## Conclusion

The large the n, the closer you get to the exact answer

## Your exercise

The Conclusion is deliberately flawed.

1. In **your fork**, create `explain-convergence` from `main`.
2. Use `results.csv` to replace only the Conclusion with a supported claim. Identify the function, interval, n values, error ratios, and a limitation.
3. Commit with `Explain trapezoidal error reduction`.
4. Open a pull request **within your own fork**. Select your repository as both base and head repository, base branch `main`, compare branch `explain-convergence`.
5. Review the diff with a partner, merge, and inspect README on **your fork’s main**.

GitHub may initially suggest KYANJO as the base repository. Change it to **YOUR-USERNAME/numerical-methods-github**. Everyone works independently and the instructor starter stays unchanged.

Show your merged pull request, commit message, updated conclusion, and numerical explanation. See [STUDENT_GUIDE.md](STUDENT_GUIDE.md) for details.
