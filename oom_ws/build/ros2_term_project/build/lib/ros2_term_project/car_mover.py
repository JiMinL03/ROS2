import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from custom_interface.msg import StartCar

class CarMover(Node):
    def __init__(self):
        super().__init__('car_mover')
        
        self.publisher_ = None
        self.car_name = None
        
        self.create_subscription(StartCar, 'start_car', self.start_car_callback, 10)

        self.timer1 = self.create_timer(0.1, self.set_cube_movement)

    def start_car_callback(self, msg):
        self.car_name = msg.car
        if self.car_name:
            self.publisher_ = self.create_publisher(Twist, f'/{self.car_name}/cmd_demo', 10)

    def set_cube_movement(self):
        if self.car_name and self.publisher_:
            msg = Twist()
            msg.linear.x = 6.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    car_publisher = CarMover()
    try:
        rclpy.spin(car_publisher)
    except KeyboardInterrupt:
        car_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

