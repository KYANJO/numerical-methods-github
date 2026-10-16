# Git and SSH setup

SSH authenticates Git from your computer. Browser-only work does not require SSH.

## 1. Check your tools and identity

Use Terminal on macOS/Linux, or **Git Bash from Git for Windows** on Windows. The commands below assume that shell.

```bash
git --version
ssh -V
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR VERIFIED GITHUB EMAIL OR EXACT NO-REPLY ADDRESS"
```

Install missing Git tools from https://git-scm.com/downloads with instructor support, or use the browser route today. Find your exact no-reply email in GitHub Settings > Emails. Git author settings identify commits but do not authenticate you. On a shared lab device, ask about account isolation and use repository-local identity after cloning rather than global settings.

## 2. Check for an existing key

```bash
ls -al ~/.ssh
```

A missing folder is normal on a new setup. An existing key pair such as id_ed25519 and id_ed25519.pub may already work. Never overwrite an existing key.

## 3. Generate a key only if needed

```bash
ssh-keygen -t ed25519 -C "YOUR GITHUB EMAIL"
```

Accept the default file location only if unused. Set a passphrase. If prompted to overwrite a key, answer no and ask for help. If using another filename, substitute it consistently below and ask about SSH configuration.

## 4. Load your key

Terminal on macOS/Linux or Git Bash on Windows:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Enter the passphrase if prompted. macOS Keychain integration is optional; see the official guide. Windows PowerShell uses different agent instructions. Use Git Bash for this tutorial.

## 5. Register the public key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the whole line beginning ssh-ed25519. On GitHub, choose profile picture > Settings > SSH and GPG keys > New SSH key. Give it a device label, choose Authentication Key, paste the public key, and save. Complete any account verification yourself.

- **Public:** id_ed25519.pub goes to GitHub.
- **Private:** id_ed25519 stays on your computer. Never upload it, share it, or commit key files.

## 6. Test authentication

```bash
ssh -T git@github.com
```

On the first connection, compare the host-key fingerprint against GitHub’s official fingerprint page before accepting it:
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints

Success says: Hi USERNAME! You have successfully authenticated, but GitHub does not provide shell access. Check that USERNAME is your account. A successful GitHub SSH test may exit with code 1 because no shell is available.

Permission denied (publickey): check loaded keys with `ssh-add -l`, confirm the matching public key belongs to your GitHub account, and check the SSH clone URL. A fingerprint mismatch needs instructor help. If campus networking blocks SSH, use the browser route for the exercise.

## 7. Fork, then clone your fork

In the browser, fork https://github.com/KYANJO/numerical-methods-github to your username. In your fork, choose Code > Local > SSH and copy its URL. Replace YOUR-USERNAME below:

```bash
git clone git@github.com:YOUR-USERNAME/numerical-methods-github.git
cd numerical-methods-github
git remote -v
```

Origin should point to your fork. Cloning the instructor repository does not give you permission to push there. Continue with STUDENT_GUIDE.md.

## Official references

- Keys and agents: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- Register a public key: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
- Test SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection
- Forking: https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo
