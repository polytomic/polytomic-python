<!-- Begin Title -->
# Polytomic Python Library

The Polytomic Python Library provides convenient access to the Polytomic API from applications written in Python.
<!-- End Title  -->

<!-- Begin Installation -->
# Installation

```sh
pip install --upgrade polytomic
```
<!-- End Installation -->

<!-- Begin Usage -->
# Usage

```python
from polytomic.client import Polytomic

client = Polytomic(
    token="YOUR_TOKEN",
)
```
<!-- End Usage -->

<!-- Begin Async Usage -->
# Async Client

```python
from polytomic.client import AsyncPolytomic

client = AsyncPolytomic(
    token="YOUR_TOKEN",
)
```
<!-- End Async Usage -->

<!-- Begin Contributing -->
# Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. 
Additions made directly to this library would have to be moved over to our generation code, 
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
 a proof of concept, but know that we will not be able to merge it as-is. We suggest opening 
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
<!-- End Contributing  -->

