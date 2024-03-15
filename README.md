# A.R.M---Autonomous-Robotic-Machine
In this repository, we will design and develop Project ARM - a Raspberry Pi-based autonomous vehicle; integrating ultrasonic sensor, a USB webcam, and MJPG streamer for obstacle detection and live streaming capabilities.

## Introduction

Introducing Project ARM—an ambitious endeavor at the forefront of autonomous robotics. 
ARM, short for Autonomous Robotic Mobility, represents a groundbreaking fusion of cutting-edge technology and compassionate design principles. This visionary prototype transcends conventional limitations, aiming to redefine the landscape of mobility. 
With a primary focus on enhancing lives, ARM encompasses a diverse range of applications, from empowering individuals with disabilities through wheelchair integration to revolutionizing logistics through seamless transportation of goods. 
Through innovative features like obstacle detection, live streaming capabilities, and adaptive navigation, ARM embodies a future where technology fosters inclusivity and efficiency. Join us on this journey as we explore the intersection of humanity, innovation, and technology, shaping a future where mobility knows no bounds.

## Acknowledgement

I extend my sincere appreciation to the Integral University Robotics Lab(https://www.robotics.iul.ac.in/) for their invaluable support throughout the development of the ARM project. 
Their generous provision of funds, tools, and a conducive environment for research and innovation has been instrumental in bringing this project to fruition. I am deeply grateful for their guidance and expertise, which have played a pivotal role in the successful design and implementation of this autonomous vehicle using Raspberry Pi. This project would not have been possible without their unwavering support and mentorship.

## Objectives

The primary objectives of the ARM project include:

1. Develop an autonomous robotic platform that enhances mobility for individuals with disabilities, including wheelchair integration, to provide newfound freedom and independence.

2. Revolutionize logistics by creating a versatile and adaptable autonomous vehicle capable of seamlessly transporting luggage and goods.

3. Transform existing vehicles into smart transport systems by integrating autonomy features such as lane assist, automatic steering, automatic braking, and adaptive cruise control.

4. Prioritize safety and convenience in mobility solutions through the implementation of advanced features that ensure safe navigation and a smooth driving experience.

5. Explore the intersection of technology, humanity, and innovation to shape a future where ARM signifies progress, inclusivity, and efficiency in mobility solutions.

## Hardware Requirements

To assemble the ARM robot, you will need the following hardware components:

- Raspberry Pi (with power supply and microSD card)
- Ultrasonic and IR sensors
- USB webcam
- Motor drivers
- DC motors and wheels
- LEDs (optional)
- Breadboard and jumper wires

## Software Requirements

The software setup for the ARM project includes:

- Raspbian operating system flashed onto the microSD card
- Required libraries and dependencies, such as OpenCV for image processing and MJPG streamer for live streaming

## Installation and Setup

Follow these steps for the installation of Raspberry Pi OS and the required libraries for the ARM project:

### 1. Raspberry Pi OS Installation:

1. Download the Raspberry Pi OS image from the official website (https://www.raspberrypi.com).
2. Flash the Raspberry Pi OS image onto the microSD card using a tool like Etcher (https://etcher.balena.io/).
3. Insert the microSD card into the Raspberry Pi and power it up.
4. Follow the on-screen setup instructions to configure the Raspberry Pi OS.
5. Assign a static IP address during the setup process for network connectivity.

### 2. Installing Required Libraries:


#### MJPG Streamer Installation:

bash
sudo apt-get install libjpeg62-turbo-dev imagemagick libv4l-dev
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install


#### GPIO Library Installation:

bash
sudo apt-get install python3-gpiozero


#### Other Dependencies:

Ensure to install any other dependencies required for your specific application, such as additional Python libraries or packages for sensor interfacing.

Once these steps are completed, the Raspberry Pi OS and required libraries will be installed and configured for the ARM project. You can proceed with further setup and implementation of the project.

## Project Implementation

Follow these steps for the implementation of the ARM project, covering hardware setup, software setup, and running the code:

### Hardware Setup:

1. Connect Ultrasonic:
   - Wire the ultrasonic to the GPIO pins on the Raspberry Pi according to the specifications of your sensors. Ensure proper connections and secure them in place.

2. Attach USB Webcam:
   - Connect the USB webcam to any available USB port on the Raspberry Pi. Position the webcam appropriately for capturing the desired field of view.

3. Wire Motor Drivers:
   - Connect the motor drivers to control the DC motors responsible for the robot's movement. Follow the manufacturer's instructions for wiring the motor drivers to the GPIO pins on the Raspberry Pi.

4. Optional: Connect LEDs:
   - If desired, wire LEDs for status indication. Connect them to the GPIO pins on the Raspberry Pi and position them accordingly.

5. Secure Components:
   - Ensure all components are securely connected and properly mounted on the chassis or frame of the robot. Check for any loose connections or potential hazards.

### Software Setup:

1. Install Raspberry Pi OS:
   - Follow the steps outlined in the "Raspberry Pi OS Installation" section above to install the Raspberry Pi OS on the microSD card and configure the operating system.

2. Install Required Libraries:
   - Use the commands provided in the "Installing Required Libraries" section above to install MJPG Streamer, GPIO library, and any other dependencies required for the ARM project.

3. Download ARM Project Code:
   - Obtain the Python code for the ARM project from the appropriate source, such as a GitHub repository or local files.

4. Modify Code (if necessary):
   - Depending on your specific hardware configuration and project requirements, you may need to modify the Python code to ensure compatibility and functionality.

5. Configure Webcam and Sensors:
   - Configure the webcam and sensors parameters in the code as per their specifications and desired operation settings.

### Running the Code:

1. Navigate to Project Directory:
   - Open a terminal window on the Raspberry Pi and navigate to the directory where the ARM project code is located.

2. Execute Python Script:
   - Run the Python script by executing the following command:
     bash
     python3 arm_project.py
     
   - Replace arm_project.py with the actual filename of your Python script if it's different.

3. Monitor Output:
   - Monitor the terminal output for any error messages or status updates generated by the ARM project code.

4. Observe Robot Behavior:
   - Observe the behavior of the robot as it performs obstacle detection and live streaming functionalities based on the code implementation.

5. Interact (if applicable):
   - If the code includes remote operation capabilities, interact with the robot through the user interface or commands provided in the code.

By following these steps, you can successfully implement the ARM project, configure the hardware and software components, and run the Python code to enable obstacle detection and live streaming functionalities on the autonomous robot.

## Conclusion

The ARM project presents an innovative solution for autonomous robotics with obstacle detection and live streaming capabilities. By following the provided guidelines and steps, you can contribute to advancements in robotics technology and explore various applications of autonomous robots in real-world scenarios.
