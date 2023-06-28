# graph-theory-in-python

This is a Python implementation of Dijkstra's algorithm for finding shortest paths in a graph. It allows to read graphs from .gra-files and calculate the shortest distances from a target node to all other nodes using backward differences or find the shortest path of a source node to a target node either with unmodified or modified edge weights for better performance.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python dijkstra <input_file_path>.gra -s <source_name> -t <target_name> # print shortest path and iterations
python dijkstra <input_file_path>.gra -s <source_name> -t <target_name> -pr # also print predecessors
```

### Run Unit Tests
```bash
cd graph-theory-in-python
python -m unittest test.test_dijkstra
```