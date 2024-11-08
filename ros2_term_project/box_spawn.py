import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity
from tf_transformations import quaternion_from_euler
import os
from ament_index_python.packages import get_package_share_directory


class BoxSpawn(Node):
    def __init__(self):
        super().__init__('spawn_entity')
        self.client = self.create_client(SpawnEntity, '/spawn_entity')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = SpawnEntity.Request()
        self.future = None


    def send_request(self):
        self.req.name = "my_box"

        #model_file = os.path.join(
        #    get_package_share_directory('ros2_term_project'),
        #    'models', 'cube', 'moving_cube.sdf'
        #)
        model_file = '/home/ros2/Downloads/ros2_term_project/models/cube/moving_cube.sdf'

        try:
            with open(model_file, 'r') as f:
                model_xml = f.read()
        except FileNotFoundError:
            self.get_logger().error(f"Model file not found: {model_file}")
            return

        self.req.xml = model_xml

        self.req.initial_pose.position.x = 0.0
        self.req.initial_pose.position.y = 0.0
        self.req.initial_pose.position.z = 0.0


        self.future = self.client.call_async(self.req)
        self.get_logger().info('Spawn request sent.')
        
def main(args=None):
    rclpy.init(args=args)
    client = BoxSpawn()
    client.send_request()

    while rclpy.ok():
        rclpy.spin(client)

        if client.future and client.future.done():
            try:
                response = client.future.result()
                print('Response status:', response.status_message)
            except Exception as e:
                client.get_logger().info('Service call failed: %s' % e)
            break

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

