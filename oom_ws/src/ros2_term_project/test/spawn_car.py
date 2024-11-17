import os
import rclpy
from rclpy.node import Node
from custom_interface.msg import StartCar

class StartCarPublisher(Node):
    def __init__(self):
        super().__init__('start_car_publisher')
        self.publisher = self.create_publisher(StartCar, '/start_car', 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        
        # 차량 모델 배치
        self.spawn_car_models()

    def spawn_car_models(self):
        # Gazebo에 차량 모델 배치
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models/prius_hybrid.sdf')
        os.system(f"ros2 run gazebo_ros spawn_entity.py -file {model_path} -entity PR001 -x 93 -y -11.7 -Y -1.57")
        os.system(f"ros2 run gazebo_ros spawn_entity.py -file {model_path} -entity PR002 -x 93 -y -15.9 -Y -1.57")
        self.get_logger().info("차량 PR001, PR002 모델을 Gazebo에 배치하였습니다.")

    def publish_message(self):
        msg = StartCar()
        msg.car = 'PR001'  # 발행할 차량 이름
        self.publisher.publish(msg)
        self.get_logger().info('발행된 차량: %s' % msg.car)

def main():
    rclpy.init()
    node = StartCarPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()

