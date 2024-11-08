import sys
import rclpy
from gazebo_msgs.srv import SpawnEntity
from rclpy.node import Node


class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('spawn_entity')  # 노드 이름을 'spawn_entity'로 설정
        self.client = self.create_client(SpawnEntity, '/spawn_entity')  # 서비스 이름 수정
        # 서비스가 준비될 때까지 기다림
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        self.req = SpawnEntity.Request()

    def send_request(self):
        # sys.argv로부터 입력받은 값 사용
        self.req.name = str(sys.argv[1])  # 첫 번째 인자: 엔티티 이름
        self.req.model_xml = str(sys.argv[2])  # 두 번째 인자: 모델 XML 데이터
        self.future = self.client.call_async(self.req)  # 서비스 비동기 호출


def main(args=None):
    rclpy.init(args=args)  # ROS 2 초기화
    minimal_client_async = MinimalClientAsync()  # 클래스 이름을 수정
    minimal_client_async.send_request()  # 요청 전송

    # 노드가 종료되지 않도록 계속 실행
    while rclpy.ok():
        rclpy.spin(minimal_client_async)  # 노드 이벤트 처리
        if minimal_client_async.future.done():  # 요청 완료 여부 확인
            try:
                response = minimal_client_async.future.result()  # 서비스 응답 처리
                minimal_client_async.get_logger().info('Status message: %s' % response.status_message)
            except Exception as e:
                minimal_client_async.get_logger().info('Service call failed %r' % (e,))
            else:
                minimal_client_async.get_logger().info('Entity name: {}'.format(minimal_client_async.req.name))
            break  # 응답을 받으면 종료

    minimal_client_async.destroy_node()  # 노드 파괴
    rclpy.shutdown()  # ROS 2 종료


if __name__ == '__main__':
    main()
