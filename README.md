# `l-track`

Track your projects in the terminal using [ledger-cli](https://ledger-cli.org/) file format.

## Usage

### [ledger-cli](https://ledger-cli.org/)

Start by [installing `ledger-cli`](https://ledger-cli.org/download.html), if not done already.

To use this program, declare a new environmental variable `LEDGER_TIME_FILE` pointing to a file that will store your
project's different tasks.

Each project can have multiple entries that reflect a project's task. Here's the example of an entry saved to the
`LEDGER_TIME_FILE`:

```ledger
2025-05-02 Refactored the code base
    Projects:Company 1:2025-05-01 Ledger project tracker        0.35h
    Time
```

You can then use ledger to see how much time you've worked for a company, or a particular project:

```bash
ledger -f "$LEDGER_TIME_FILE" balance "Projects:Company 1"
#               2.36h  Projects:Company 1:2025-05-01 Ledger project tracker
```

## Installation

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/), if not done already.

2. Install the dependencies (uv creates the virtual environment in `.venv` automatically):
    ```bash
    uv sync
    ```

3. Run the app:
   ```bash
   uv run l-track.py
   ```

4. (Optional) Add an alias to run it from anywhere:
    - Bash (Linux):
      ```bash
      # run this from this project root
      echo "alias l-track=\"uv run --project $(pwd) $(pwd)/l-track.py\"" >> ~/.bashrc
      ```
    - Zsh (macOS):
      ```bash
      # run this from this project root
      echo "alias l-track=\"uv run --project $(pwd) $(pwd)/l-track.py\"" >> ~/.zshrc
      ```

   Open a new terminal and run `l-track`.
