import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Lstener(Node):
    def __init__(self):
        super().__init__("listener")
        self.pub = node.create_publisher(Int16, "counyup", self.cb, 10)
    
    def cb(self, msg):
        self.get_logger().info("Listen:%d"%msg.data)

rclpy.init()
node = listener
rclpy.spin(node)
