# graph-theory-in-python

This is a Python implementation of Dijkstra's algorithm for finding shortest paths in a graph. It allows to read graphs from .gra-files and calculate the shortest distances from a target node to all other nodes using backward differences or find the shortest path of a source node to a target node either with unmodified or modified edge weights for better performance.

The project was an assignment in the course "Operations Research" at Berliner Hochschule für Technik (BHT) in Department II, lectured by Prof. Martin Oellrich. To read and handle graphs, a [generic graph class](https://github.com/saschkoh/oellrich-graph-in-python) in Python based on the C++ implementation of Prof. Oellrich is being used.

The future plan is to expand the package with further graph exploration methods and add visualization methods.

## Installation
Git is needed to install the requirements.
```bash
pip install -r requirements.txt
```

## Usage
```bash
python dijkstra <input_file_path>.gra -t <target_name>  # backward distances
python dijkstra <input_file_path>.gra -s <source_name> -t <target_name>  # unmodified
```

### Options
Only if both source and target node are given:
- `-m, --modified` Use modified edge weights for better runtime.
- `-i, --iter` Print iterations needed to console.
- `-pr, --predecessors` Print predecessors list to console.
- `-pa, --path` Print shortest path to console.
  
### Run Unit Tests
```bash
cd graph-theory-in-python
python -m unittest test.test_dijkstra
```