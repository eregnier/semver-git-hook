# Semver Git Hook

## Install

pip install --user  semver-git-hook

then edit the `.git/hooks/pre-commit file`

```bash
exec < /dev/tty
semver-git-hook
```

Make it executable

```bash
chmod +x .git/hooks/pre-commit
```
