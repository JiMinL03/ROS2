import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from .line_tracker import LineTracker
from custom_interface.msg import StartCar
import cv_bridge


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

    def start_car_callback(self, msg: StartCar):
        self.car_name = msg.car
        if self.car_name == 'PR001':  
            self._publisher = self.create_publisher(Twist, 'PR001/cmd_demo', 10)
            self._subscription = self.create_subscription(Image, 'PR001_camera/PR001_camera/image_raw', self.image_callback, 10)
        else:  
            self._publisher = self.create_publisher(Twist, 'PR002/cmd_demo', 10)
            self._subscription = self.create_subscription(Image, 'PR002_camera/PR002_camera/image_raw', self.image_callback, 10)

    def image_callback(self, msg: Image):
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.line_tracker.process(img)

        self.twist.angular.z = (-1) * self.line_tracker.delta / 450
        self.get_logger().info('angular.z = %f' % self.twist.angular.z)

        self._publisher.publish(self.twist)

    def stop(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self._publisher.publish(self.twist)

    @property
    def publisher(self):
        return self._publisher


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

