# Missing Ranges

Given a **sorted list** of integers and an inclusive `[lower, upper]` range, list the numbers and ranges that are missing from the list.

```python
get_missing_range([0, 1, 3, 50, 75], lower=0, upper=99)
# ['2', '4->49', '51->74', '76->99']
```

- A single missing number is returned as `"n"`.
- A run of missing numbers is returned as `"start->end"`.
- Runs in O(n) with one pass over the list.

## Run

```bash
python3 assignment.py
```
