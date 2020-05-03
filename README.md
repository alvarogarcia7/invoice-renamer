# Invoice Renamer

## Purpose

Note: I use this script to rename invoices, to a my very own particular format.

## Running it

My workflow is to cumulate all the `mv` commands, then review, then execute at once.

Before and after executing, I create a temporary git repository, so I'm able to go back to the previous state. [^0]


```bash
./exec.sh invoice.pdf
```

Then, follow the wizard.

Then, you can review the commands, if needed.

To execute them:

```
bash commands_total.sh
```

[^0]: This is not handled in this script

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


  