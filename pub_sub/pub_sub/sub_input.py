import rclpy
from rclpy.node import Node
import math

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('Subscriber')
        self.subscription = self.create_subscription(
            String,
            'distance',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('"%s".' % msg.data)
        val=msg.data.split(",")
        x1=int(val[0])
        x2=int(val[1]) 
        y1=int(val[2]) 
        y2=int(val[3])  
            

        dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
        self.get_logger().info('x1: "%s".' %x1)
        self.get_logger().info('x2: "%s".' %x2)
        self.get_logger().info('y1: "%s".' %y1)
        self.get_logger().info('y2: "%s".' %y2)
        self.get_logger().info('Distance is: "%s".' %dist)

        
        

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
