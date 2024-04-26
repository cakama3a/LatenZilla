LatenZilla  

LatenZilla is a Windows executable that measures the latency of a gamepad using a high-speed camera. It provides a precise way to analyze the responsiveness of gamepad inputs by capturing the time difference between the physical button press or joystick movement and the corresponding action on the screen.

Features  
Supports multiple gamepads connected to the system  
Measures the latency of button presses and joystick movements  
Provides real-time feedback on the latency in milliseconds  
Utilizes high-speed camera footage to accurately determine the latency  

Requirements  
To use LatenZilla effectively, you need the following:  

A high-speed camera capable of recording at least 240 frames per second (FPS)  
A monitor with a high refresh rate for accurate latency measurement  
Windows operating system  

Getting Started  
Download the latest release of LatenZilla.exe from the Releases page.  
Connect your gamepad(s) to your computer.  
Set up your high-speed camera to capture the monitor screen and the gamepad simultaneously.  
Ensure that the camera is recording at a minimum of 240 FPS.  
Run the LatenZilla.exe executable.  
Follow the on-screen instructions to select the desired gamepad.  
Press buttons or move the joystick on the gamepad to measure the latency.  
Analyze the latency results displayed on the console.  

How It Works 
LatenZilla utilizes the Pygame library to detect and interact with connected gamepads. It continuously polls the gamepad for button presses and joystick movements. When an input event is detected, LatenZilla records the timestamp of the event.
Simultaneously, the high-speed camera captures the physical action on the gamepad and the corresponding visual feedback on the monitor screen. By analyzing the video footage frame by frame, you can determine the time difference between the physical input and the on-screen response.
LatenZilla provides real-time feedback on the console, displaying the latency in milliseconds for each button press or joystick movement. This allows you to assess the responsiveness of your gamepad and identify any potential latency issues.

Limitations  
The accuracy of the latency measurement depends on the quality and setup of the high-speed camera.  
The program assumes that the camera is properly synchronized with the gamepad and monitor.  
LatenZilla does not provide automated video analysis; manual frame-by-frame analysis is required.  

Contributing  
As LatenZilla is provided as an executable file, the source code is not available for direct contributions. However, if you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

License  
LatenZilla is released under the MIT License.

Acknowledgements  
LatenZilla was inspired by the need for accurate gamepad latency measurement in the gaming community. Special thanks to the Pygame community for their excellent library and support.

Feel free to customize this README file based on your specific project details and add any additional sections or information that you think would be helpful for users of your program.
