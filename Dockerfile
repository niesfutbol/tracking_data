FROM ultralytics/ultralytics:latest-python
COPY . .
RUN apt update && apt install --yes make
RUN pip install --upgrade pip && pip install \
    black \
    flake8 \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov
