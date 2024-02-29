# /home/dunderscore/workspace/git-repos/system-config/helperscripts/dockerhop/bin python
import click
from typing import Optional, Union
import subprocess


@click.command()
@click.option(
    "--docker-file", default="./Dockerfiles/ros2.Dockerfile", help="Dockerfile to use"
)
@click.option("--name", default="dunder_ros", help="Name of ros2 image")
@click.option("--tag", default="devel", help="Name of ros2 image tag")
@click.option("--build-env", default=".", help="Context for docker build to build from")
def build(
    docker_file: str,
    name: str,
    tag: str,
    build_env: str,
) -> None:
    """Build a docker image from the specific options"""
    subprocess.run(
        ["docker", "build", "-t", name + ":" + tag, "-f", docker_file, build_env]
    )


if __name__ == "__main__":
    build()
