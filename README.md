# Zsearch

Perform zenodo searches with python.

## Installation

```bash
pip install zsearch
```

## Dependencies

- requests

## Usage

```python
import zsearch

search_string = 'resource_type.type:other AND creators.name:("Probst, Matthias")'
records = zsearch.search(search_string)
```

More examples can be found in the [examples](examples/example.ipynb) folder.
