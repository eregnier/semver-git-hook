import os
import stat
import sys
import subprocess
from pick import pick
from termcolor import colored


def main():
    if "--init" in sys.argv:
        init()
    elif "--update" in sys.argv:
        hook()
    else:
        print(
            f"""
This tool helps managing project versionning by handling semver update in git pre commit hooks

Help:
    {colored('--init', 'yellow')} Install the hook in the current .git folder
    {colored('--update', 'yellow')} run the inteactive semver file update
        """
        )


def init():
    if not os.path.isdir(".git/hooks"):
        print(f'\t{colored("✗", "red")} This is not a git folder, cannot init hook.')
        sys.exit(1)
    else:
        hook_path = ".git/hooks/pre-commit"
        commands = "\nexec < /dev/tty\nsemver-git-hook --update\n"
        mode = "a" if os.path.isfile(hook_path) else "w"
        if mode == 'a':
            with open(hook_path) as f:
                if commands in f.read():
                    print(
                        f'\t{colored("ⓘ", "cyan")} Hook already installed, nothing to do.'
                    )
                    sys.exit(0)
        with open(hook_path, mode) as f:
            f.write(commands)
        handler = os.stat(hook_path)
        os.chmod(hook_path, handler.st_mode | stat.S_IEXEC)
        print(f'\t{colored("✓", "green")} Hook installed')


def hook():
    path = f'{os.environ.get("SEMVER_HOOK_PATH_PREFIX", "")}.version'
    title = "Is this commit change patch, minor or major ?"
    options = ["no-change", "patch", "minor", "major"]
    option, index = pick(options, title)
    if os.path.isfile(path):
        with open(".version") as f:
            major, minor, patch = map(int, f.read().strip().split("."))
    else:
        major, minor, patch = 0, 0, 0
    version = f"{major}.{minor}.{patch}"
    print(f'Current version is {colored(version, "cyan")}')
    if option == "major":
        major += 1
        minor = 0
        patch = 0
    if option == "minor":
        minor += 1
        patch = 0
    if option == "patch":
        patch += 1
    version = f"{major}.{minor}.{patch}"
    print(f'New {colored(option, "green")} version is now {colored(version, "cyan")}')
    with open(path, "w") as f:
        f.write(version)
    subprocess.run(['git', 'add', path])

if __name__ == "__main__":
    main()
