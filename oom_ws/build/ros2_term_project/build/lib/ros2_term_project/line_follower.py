import time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from .line_tracker import LineTracker
from custom_interface.msg import StartCar
import cv_bridge

class LineFollower(Node):
    def __init__(self, line_tracker: LineTracker, car_name: str):
        super().__init__('line_follower')
        
        self.car_name = car_name  # 발행된 차량 이름을 구분하기 위한 변수
        self.line_tracker = line_tracker
        self.bridge = cv_bridge.CvBridge()

        # /start_car 토픽을 구독하여 차량 제어 시작
        self.start_car_subscription = self.create_subscription(StartCar, '/start_car', self.start_car_callback, 10)

        # 카메라 이미지 구독을 나중에 시작할 수 있도록 초기화
        self._subscription = None
        self._publisher = self.create_publisher(Twist, 'cmd_vel', 1)
        self.twist = Twist()
        self.twist.linear.x = 5.0
        self.img = None

    def start_car_callback(self, msg: StartCar):
        """/start_car 토픽 메시지를 받아 차량 제어를 시작"""
        if self.car_name == msg.car:
            # 차량 이름이 일치하면 카메라 구독을 시작하여 라인 주행 시작
            self._subscription = self.create_subscription(Image, 'camera/image_raw', self.image_callback, 10)
            self.get_logger().info(f'{self.car_name} 차량의 라인 주행을 시작합니다.')

    def image_callback(self, msg: Image):
        """카메라로부터 이미지를 받아서 라인 추적"""
        if not self._subscription:
            return  # 차량이 발행된 토픽을 구독하지 않으면 처리하지 않음
        
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.line_tracker.process(img)

        # 라인 추적에 따른 회전 속도 조정
        self.twist.angular.z = (-1) * self.line_tracker.delta / 450
        self.get_logger().info('angular.z = %f' % self.twist.angular.z)

        # cmd_vel 토픽으로 차량 이동 명령 발행
        self._publisher.publish(self.twist)

    def stop(self):
        """차량을 멈추는 메서드"""
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self._publisher.publish(self.twist)

    @property
    def publisher(self):
        return self._publisher

def main():
    rclpy.init()
    
    car_name = 'PR001'  # 또는 'PR002'로 차량 이름을 설정
    tracker = LineTracker()
    follower = LineFollower(tracker, car_name)
    
    try:
        rclpy.spin(follower)
    except KeyboardInterrupt:
        follower.stop()
        follower.stop()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

