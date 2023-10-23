# **ROS_Obstacle_Avoidance_Robot**

## <ins>**What is ROS?**</ins>
 ROS is an abbreviation of Robot Operating System which is like a bridge to hardware and 
software, like a middleware software. Although the name is robot operating system it is not an 
actual operating system like Windows or Linux it is more like a framework that we are using 
in these operating systems which we can perform operations for hardware with the help of 
software. As you can see from Figure 3.1 without touching to hardware, we can create 
programs for robots.

![image](https://github.com/yavuzCodiin/ROS_Obstacle_Avoidance_Robot/assets/82445309/0a5d0c77-1c86-4337-ad89-46a346b27ff1)

## <ins>**What is ROS Node?**</ins>

Node is an executable, a process that is for performing computation. Graph is where they 
are combined, there is a topic concept in which nodes can publish something or subscribe to 
topics so we can say that they are communicating over topics, ROS client library, RPC services 
protocol, or parameter server. Let me also talk about other things in the graph concept. Nodes 
communicate with each other with messages over topics, a message can have different types. 
Master is helping nodes to find their way, to find each other. rosout is for nodes to subscribe 
log and republish messages. There is one more concept which is important nodes to 
communicate which is called roscore. It is a combination of rosout, parameter server, and 
Master. If we didn’t start roscore ROS master, parameter server and rosout logging node won’t 
work either so it is important to run roscore as a first thing when we are working with ROS.
 Our nodes sometimes could be written in a different language so in order them to 
communicate with each other we need something which is called a client library. It allows our 
nodes to communicate with each other in different languages. For instance, we have rospy and 
roscpp, they are client libraries for python and c++.

![image](https://github.com/yavuzCodiin/ROS_Obstacle_Avoidance_Robot/assets/82445309/8d58a604-f546-4732-9b39-31d7dd4a7a0b)

## <ins>**Service and Client**</ins>

![image](https://github.com/yavuzCodiin/ROS_Obstacle_Avoidance_Robot/assets/82445309/ec5c543a-a4f6-449f-b3c3-4ca5091bac6b)

## <ins>**The Project**</ins>

>* Simulation: Gazebo(test environment), Rviz(visualizing sensors)
>* IDE: Vs Code
>* Language: ROS, Python

1. **Linear Speed Control:**
The program initializes the robot's movement with a consistent linear speed. This foundational control ensures the robot's
continuous and predictable motion, allowing it to cover distances effectively and maintain a stable pace during its operation.

3. **Laser Data Processing and Obstacle Detection:**
Upon subscribing to the "laser" topic, the program receives raw data from laser sensors. The received data array is processed
to identify the index corresponding to the obstacle directly in front of the robot. By parsing the laser data, the program
determines the precise location of obstacles, enabling the robot to navigate around them intelligently.

5. **Dynamic Velocity Adjustment:**
When the distance between the robot and an obstacle falls below a predefined threshold, typically 1.0 meter, the program
dynamically adjusts the robot's velocity. In such scenarios, the robot's velocity is instantaneously reduced to 0.0,
causing the robot to stop. This safety feature prevents collisions and ensures the robot halts when encountering obstacles
within close proximity.

7. **Camera Topic Subscription and Image Capture:**
Following obstacle detection and velocity adjustment, the robot subscribes to a different topic, specifically the "camera"
topic. Upon subscribing, the robot's camera captures an image of the area directly in front of it. This captured image is
then processed and saved to the local storage of the computer. This step allows the robot to visually record its surroundings,
facilitating various applications such as mapping or object recognition.

In summary, the program orchestrates the robot's movement, obstacle detection, velocity adjustments, and image capturing 
operations seamlessly. Through its integration with laser and camera topics, the robot exhibits an intelligent and adaptive 
behavior, making it capable of navigating complex environments and capturing visual data for further analysis or 
decision-making processes.

![image](https://github.com/yavuzCodiin/ROS_Obstacle_Avoidance_Robot/assets/82445309/b15a8019-40b3-40b4-8dd1-1c580efe51ae)

