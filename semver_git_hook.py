from pick import pick
import os
from termcolor import colored

def main():
    path = f'{os.environ.get("SEMVER_HOOK_PATH_PREFIX", "")}.version'
    title = 'Is this commit change bugfix, minor or major ?'
    options = ['no-change', 'bugfix', 'minor', 'major']
    option, index = pick(options, title)
    if os.path.isfile(path):
        with open('.version') as f:
            major, minor, bugfix = map(int, f.read().strip().split('.'))
    else:
        major, minor, bugfix = 0, 0, 1
    version = f'{major}.{minor}.{bugfix}'
    print(f'Current version is {colored(version, "cyan")}')
    if option == 'major':
        major += 1
    if option == 'minor':
        minor += 1
    if option == 'bugfix':
        bugfix += 1
    version = f'{major}.{minor}.{bugfix}'
    print(f'New {colored(option, "green")} version is now {colored(version, "cyan")}')
    with open(path, 'w') as f:
        f.write(version)