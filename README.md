# ant-walk

Simulate Langton's ant from a blank square grid and render the result in the terminal. The ant turns left on a black square, right on a white square, flips the square, and moves forward.

## Use

Requires Python 3.8+; no packages to install.

```sh
python ant_walk.py
python ant_walk.py --steps 5000
```

The run is deterministic and starts at `(0, 0)` facing north. The step count is limited to 100,000. If the final grid exceeds 250,000 cells, the summary is printed without the grid; use fewer steps for a smaller rendering. `.` is white, `#` is black, and `^`, `>`, `v`, `<` show the ant's direction.

## License

MIT
