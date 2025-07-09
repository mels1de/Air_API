FROM ubuntu:latest
LABEL authors="Artemem"

ENTRYPOINT ["top", "-b"]