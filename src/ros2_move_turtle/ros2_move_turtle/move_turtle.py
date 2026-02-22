import rclpy
# import the Node module from ROS2 Python library
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class MoveTurtle(Node):

    def __init__(self):
        super().__init__('move_turtle')

        # Publisher
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        # Subscriber
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.stopped = False

    def pose_callback(self, msg):

        cmd = Twist()

        # Condition: if x or y > 7 stop
        if msg.x > 7.0 or msg.y > 7.0:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0

            if not self.stopped:
                self.get_logger().info("Stopping turtle at position x={msg.x:.2f}, y={msg.y:.2f}")
                self.stopped = True
        else:
            cmd.linear.x = 0.5
            cmd.angular.z = 0.0
            self.stopped = False

        self.publisher_.publish(cmd)


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    move_turtle = MoveTurtle()
    rclpy.spin(move_turtle)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    move_turtle.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main() #call the main function