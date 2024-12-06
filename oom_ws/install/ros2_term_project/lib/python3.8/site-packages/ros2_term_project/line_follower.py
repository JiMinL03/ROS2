import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from .line_tracker import LineTracker
from custom_interface.msg import StartCar
from sensor_msgs.msg import LaserScan
import datetime as dt
import cv_bridge
from enum import Enum


class LineFollower(Node):
    def __init__(self, line_tracker: LineTracker):
        super().__init__('line_follower')
        self.line_tracker = line_tracker
        self.bridge = cv_bridge.CvBridge()

        self.car_name = None
        self._publisher = None

        self.create_subscription(StartCar, 'start_car', self.start_car_callback, 10)

        self.twist = Twist()
        self.twist.linear.x = 5.0
        self.img = None

        self.obstacle_found = False
        self.waiting_start_time = None
        self.avoidance_move = False
        self.avoidance_start_time = None
        self.avoidance_state = LineFollower.State.WAITING
        self.avoidance_sign = 1
        self.avoidance_start_delta = 0

        self.stopped = False
        self.line_tracker.stop_callback = self.stop

    def start_car_callback(self, msg: StartCar):
        self.car_name = msg.car
        if self.car_name == 'PR001':
            self._publisher = self.create_publisher(Twist, 'PR001/cmd_demo', 10)
            self._subscription = self.create_subscription(Image, 'PR001_camera/PR001_camera/image_raw',
                                                          self.image_callback, 10)
            self.lidar_subscription = self.create_subscription(LaserScan, '/PR001_laser/scan', self.scan_callback, 10);
        else:
            self._publisher = self.create_publisher(Twist, 'PR002/cmd_demo', 10)
            self._subscription = self.create_subscription(Image, 'PR002_camera/PR002_camera/image_raw',
                                                          self.image_callback, 10)
            self.lidar_subscription = self.create_subscription(LaserScan, '/PR002_laser/scan', self.scan_callback, 10);

    def image_callback(self, msg: Image):
        if self.stopped: return
        if self.obstacle_found: return
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.line_tracker.process(img)
        if self.line_tracker.stop_checked:
            self.line_stop()
        self.twist.angular.z = (-1) * self.line_tracker.delta / 50
        self._publisher.publish(self.twist)

    def scan_callback(self, msg: LaserScan):
        min_distance = min(msg.ranges)
        self.get_logger().debug(f"Minimum distance detected: {min_distance}")

        if not self.obstacle_found and min_distance < 7.0:
            self.stop()
            self.obstacle_found = True
            if self.waiting_start_time is None:
                self.waiting_start_time = dt.datetime.now()
                self.get_logger().info(f'An obstacle found in {min_distance:.2f} m')

        if self.obstacle_found:
            if self.waiting_start_time is None: return

            if min_distance > 7.0:
                self.obstacle_found = False
                self.waiting_start_time = None
                self.get_logger().info(f'Obstacle cleared, resuming movement')
                self.go_straight()

    def stop(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self._publisher.publish(self.twist)
        self.stopped = True  # 차량 정지 상태로 변경

    def go_straight(self):
        self.twist.linear.x = 5.0
        self.twist.angular.z = (-1) * self.avoidance_sign * 0.15 if abs(self.avoidance_start_delta) > 25 else (
                                                                                                                  -1) * self.avoidance_sign * 0.3
        self._publisher.publish(self.twist)

    def resume(self):
        self.twist.linear.x = 5.0
        self._publisher.publish(self.twist)
        self.stopped = False

    def line_stop(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self._publisher.publish(self.twist)
        self.stopped = True
        self.create_timer(3.0, self.resume)

    @property
    def publisher(self):
        return self._publisher

    class State(Enum):
        WAITING = 0
        STEP_ASIDE = 1
        GO_STRAIGHT = 2
        STEP_IN = 3

def main():
    rclpy.init()
    tracker = LineTracker()
    follower = LineFollower(tracker)
    try:
        rclpy.spin(follower)
    except KeyboardInterrupt:
        follower.stop()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
