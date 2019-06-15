from setuptools import setup
from os import path

cd = path.abspath(path.dirname(__file__))
with open(path.join(cd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
with open(path.join(cd, ".version"), encoding="utf-8") as f:
    version = f.read().strip()

setup(
    name="semver-git-hook",
    version=version,
    py_files=["semver_git_hook.py"],
    description="Enforce semver management in git repositories",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Eric Régnier",
    author_email="utopman@gmail.com",
    license="MIT",
    install_requires=["pick", "termcolor"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: Jython",
        "Intended Audience :: Developers",
    ],
    keywords=["utility", "productivity", "tool", "versionning", "git", "semver"],
    url="http://github.com/eregnier/semver-git-hook",
    entry_points={"console_scripts": ["semver-git-hook=semver_git_hook:main"]},
)
