# Documentation

Documentation is built using Sphinx in a uv environment.

To build, install uv to create a virtual environment and compile:

```bash
pip install uv
uv run make html

xdg-open build/html/index.html
```