# Sim2real
We created a bridge node called `ros_to_tcp_bridge` given the Websockets from Unity gives raw messages not JSON (hence why we couldn't use [rosbridgetcp](https://docs.ros.org/en/lunar/api/rosbridge_server/html/namespacerosbridge__tcp.html)).  

# Why TCP and not use DDS for unity-ros2 communication? 
