import os
import rclpy
from rclpy.node import Node
from custom_interface.msg import StartCar
from std_msgs.msg import String

class SpawnCar(Node):
    def __init__(self):
        super().__init__('spawn_car')
        
        self.publisher = self.create_publisher(StartCar, 'start_car', 10)
        self.spawn_cars()
        
    def spawn_cars(self):
        model1_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models/prius_hybrid1.sdf')
        os.system(f"ros2 run gazebo_ros spawn_entity.py -file {model1_path} -entity PR001 -x 93 -y -11.7 -Y -1.57")
        
        model2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models/prius_hybrid2.sdf')
        os.system(f"ros2 run gazebo_ros spawn_entity.py -file {model2_path} -entity PR002 -x 93 -y -15.9 -Y -1.57")
        
        # Publish message to start PR001
        self.publish_start_car_message('PR001')
        
        
    def publish_start_car_message(self, car_name):
        # Create and populate the StartCar message
        msg = StartCar()
        msg.car = car_name
        
        # Publish the message
        self.publisher.publish(msg)
        self.get_logger().info(f'Published start command for car: {car_name}')


def main(args=None):
    rclpy.init(args=args)
    car_spawner = SpawnCar()
    
    rclpy.spin(car_spawner)

    car_spawner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

