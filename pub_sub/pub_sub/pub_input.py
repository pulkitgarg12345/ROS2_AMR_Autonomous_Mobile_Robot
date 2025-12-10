import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('Publisher')
        self.publisher_ = self.create_publisher(String, 'distance', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.val = 0

    def timer_callback(self):
        x1=input("Enter x1: ")
        x2=input("Enter x2: ")
        y1=input("Enter y1: ")
        y2=input("Enter y2: ")
    	
        msg = String()
        msg.data = (f"{x1},{x2},{y1},{y2}")
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: ' + str(msg.data))
        

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
