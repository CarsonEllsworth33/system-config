# /home/dunderscore/workspace/git-repos/system-config/helperscripts/dockerhop/bin python
import docker
from docker.types import Mount
import typer
from typing import Optional, Union
import subprocess

dockerhop = typer.Typer()


@dockerhop.command()
def ros2(
    container_name: str = "ros2",
    image_name: str = "dunder_ros:devel",
    command: str = "bash",
    mount_dir: Optional[str] = None,
    mount_location: Optional[str] = ":/opt/ros_ws/src",
) -> None:
    MOUNT_INSERT_POINT = 4
    docker_launch_command: list[str] = [
        "docker",
        "run",
        "--rm",
        "-it",
        "--name",
        container_name,
        image_name,
        command,
    ]

    # Check if mount_dir is a string and not empty then add to list
    if isinstance(mount_dir, str) and mount_dir and isinstance(mount_location,str):
        print("mount_dir: ", mount_dir)
        docker_launch_command.insert(MOUNT_INSERT_POINT, "-v")
        docker_launch_command.insert(
            MOUNT_INSERT_POINT + 1, mount_dir + mount_location
        )
    print(docker_launch_command)
    subprocess.run(docker_launch_command)


@dockerhop.command()
def build(
    docker_file: str = "./Dockerfiles/ros2.Dockerfile",
    name: str = "dunder_ros",
    tag: str = "devel",
    build_env: str = ".",
) -> None:
    subprocess.run(
        ["docker", "build", "-t", name + ":" + tag, "-f", docker_file, build_env]
    )


if __name__ == "__main__":
    dockerhop()
