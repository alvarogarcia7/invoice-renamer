# File Renamer

## Purpose
Note: I use this script to rename invoices, to a very particular format:

## Resulting format

```
$DATE - $PROVIDER - other.pdf
```

Where:
  * `$DATE` is like '2020-03-09' (ISO)
  * `$PROVIDER` is like 'Google SL' (Company name)

## Technical notes

### Uses the 'delayed execution' method

The script itself generates a `mv` command that can be reviewed or edited before executing (dry-run)

The script is just a transformer of strings, has no direct side effect on the system.


  