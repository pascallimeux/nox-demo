rm -Rf .nox && \
rm -Rf .pytest_cache && \
rm -Rf .coverage && \
rm -Rf .mypy_cache && \
rm -Rf dist && \
rm -Rf build && \
rm -Rf docs/_build && \
find . -type d -name  "*.egg-info" -exec rm -r {} + && \
find . -type d -name  "__pycache__" -exec rm -r {} +