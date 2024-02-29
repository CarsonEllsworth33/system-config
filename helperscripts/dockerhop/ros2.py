# /home/dunderscore/workspace/git-repos/system-config/helperscripts/dockerhop/bin python
import click
from typing import Optional, Union
import subprocess


@click.command()
@click.option("--container-name", default="ros2", help="Name of container")
@click.option("--image-name", default="dunder_ros:devel", help="Image name")
@click.option("--command", default="bash", help="Command to run on container start")
@click.option("--mount-dir", default="ros2", help="Name of container")
@click.option(
    "--mount-location",
    default=":/opt/ros_ws/src",
    help="Location in contianer to mount mount_dirs",
)
def ros2(
    container_name: str,
    image_name: str,
    command: str,
    mount_dir: Optional[str],
    mount_location: Optional[str],
) -> None:
    """Run a ros2 container"""
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
    if isinstance(mount_dir, str) and mount_dir and isinstance(mount_location, str):
        print("mount_dir: ", mount_dir)
        docker_launch_command.insert(MOUNT_INSERT_POINT, "-v")
        docker_launch_command.insert(MOUNT_INSERT_POINT + 1, mount_dir + mount_location)
    print(docker_launch_command)
    subprocess.run(docker_launch_command)


if __name__ == "__main__":
    ros2()
