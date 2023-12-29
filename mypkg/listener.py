import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_publisher(Int16, "countup", self.cb, 10)
    
    def cb(self, msg):
        self.get_logger().info("Listen:%d"%msg.data)

rclpy.init()
node = listener
rclpy.spin(node)
