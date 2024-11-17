import rclpy
from nav_msgs.msg import Odometry
from rclpy.node import Node
from geometry_msgs.msg import Twist


class cube_mover(Node):
    def __init__(self):
        super().__init__('cube_publisher')

        self.cube_dir = -1.0
        self.cube_targets = ((35, -64.0), (35, -77.0))

        self.publisher_ = self.create_publisher(Twist, '/CUBE/cmd_demo', 10)
        self.subscription = self.create_subscription(Odometry, '/CUBE/odom', self.get_cube_position, 10)

        self.timer1 = self.create_timer(0.1, self.set_cube_movement)

    def set_cube_movement(self):
        msg = Twist()
        msg.linear.y = self.cube_dir * 2.0
        self.publisher_.publish(msg)

    def get_cube_position(self, msg):
        current_position = (msg.pose.pose.position.x, msg.pose.pose.position.y)

        if self.cube_dir < 0.0:
            dist = self.cube_targets[1][1] - current_position[1]
        else:
            dist = self.cube_targets[0][1] - current_position[1]

        if abs(dist) <= 0.1:
            self.cube_dir *= -1


def main(args=None):
    rclpy.init(args=args)
    cube_publisher = cube_mover()
    try:
        rclpy.spin(cube_publisher)
    except KeyboardInterrupt:
        cube_publisher.stop()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
