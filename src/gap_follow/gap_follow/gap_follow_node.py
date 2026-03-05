#!/usr/bin/env python3

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import numpy as np
import rclpy
from ackermann_msgs.msg import AckermannDriveStamped
from rclpy.node import Node
from rclpy.publisher import Publisher
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker

if TYPE_CHECKING:
    # NDArray can be used to provide a type hint for the elements of a numpy
    # array. So NDArray[np.float32] means its elements are of type np.float32.
    from numpy.typing import NDArray


class GapFollowNode(Node):
    """Node that implements the follow the gap algorithm."""

    def __init__(self):
        super().__init__("gap_follow_node")

        # TODO: Declare parameters
        self.declare_parameter("my_param")
        ...

        # TODO: Read parameters
        self.my_param: float = self.get_parameter_value_checked("my_param", float)
        ...

        # TODO: Subscriptions and publishers
        self.my_pub: Publisher = ...
        ...

        self.get_logger().info(f"Initialized node {self.get_name()!r}")

    def get_parameter_value_checked(
        self, name: str, expected_type: type, check_none: bool = True
    ) -> Any:
        """Helper method to get the value of a parameter, check that it's not
        None, then check that its type is given.

        Args:
            name: Name of the parameter.
            expected_type: Expected type of the parameter.
            check_none: True to enable checking for None.
        Returns:
            Current parameter value.
        Raises:
            ValueError: Parameter value is None and check_none is True.
            TypeError: Incorrect type for the parameter value.
        """
        value = self.get_parameter(name).value
        if check_none and value is None:
            raise ValueError(f"No value given for parameter {name!r}")
        if not isinstance(value, expected_type):
            raise TypeError(
                f"Given value for parameter {name!r} is not of type "
                f"{expected_type.__name__!r}"
            )
        return value

    def scan_callback(self, laser_scan: LaserScan) -> None:
        """Called whenever a new laser scan message is received.

        Args:
            laser_scan: Laser scan message.
        """

        ranges: NDArray[np.float32] = np.array(laser_scan.ranges, np.float32)

        # TODO: Implement Follow-the-gap

    def extend_disparities(self, ranges: NDArray[np.float32]) -> NDArray[np.float32]:
        """Returns a new ranges array with disparity extensions.

        Args:
            ranges: Input ranges array.
        Returns:
            A new ranges array.
        """
        ranges_new = ranges.copy()
        # TODO: Implement
        return ranges_new

    def deploy_safety_bubble(self, ranges: NDArray[np.float32]) -> NDArray[np.float32]:
        """Returns a new ranges array with a safety bubble deployed on the closest point.

        Args:
            ranges: Input ranges array.
        Returns:
            A new ranges array.
        """
        ranges_new = ranges.copy()
        # TODO: Implement
        return ranges_new

    def find_best_gap(self, ranges: NDArray[np.float32]) -> tuple[int, int]:
        """Finds the best gap to follow.

        Args:
            ranges: Input ranges array.
        Returns:
            Start (inclusive) and end (exclusive) indices of the best gap.
        """
        # TODO: Implement
        return (0, 1080)  # (start, end)

    def find_best_point(self, ranges: NDArray[np.float32], start: int, end: int) -> int:
        """Finds the best point (index) to follow from the ranges between the
        given indices.

        Args:
            ranges: Input ranges array.
            start: Start index (inclusive)
            end: End index (exclusive)
        Returns:
            Index of the point to follow.

        """
        # TODO: Implement
        return 540

    def get_drive_speed(
        self,
        # TODO: Choose which values to calculate speed from!
    ) -> np.float32:
        """Calculates the drive speed based on the given parameters.

        Returns:
            Drive speed.
        """
        # TODO: Implement
        return np.float32(1.0)


def main(args=None) -> None:
    """Main entry point function."""
    rclpy.init(args=args)
    reactive_node = GapFollowNode()
    rclpy.spin(reactive_node)
    reactive_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
