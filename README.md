# shared-folder-permission-auditor

Flag risky shared-folder permissions from a CSV, worst first: Everyone with Full Control is HIGH, Everyone with Change is MEDIUM.

## How to run

```sh
python3 main.py shares.csv
```

## Example output

```
Public (Everyone Full Control): HIGH
Docs (IT Team Full Control): INFO
1 HIGH issue(s).
```

Standard library only. Run the tests with `python3 -m unittest discover`.
