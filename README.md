# Bad Habit Breaker 🚫👍

An AI-powered desktop utility designed to help you break body-focused repetitive behaviors (like thumb-biting, nail-biting, or face-touching) while working at your computer. 

Using **OpenCV** and **MediaPipe**, this lightweight Python script monitors your webcam feed in real-time. If your hand gets too close to your mouth, it instantly triggers an audio alert to subconsciously remind you to drop your hand.

## ✨ Features
* **Real-time Detection:** Uses Google's MediaPipe Face Mesh and Hands tracking for rapid response.
* **CPU & RAM Optimized:** Employs frame-skipping, reduced capture resolutions, and downscaled display rendering to run efficiently in the background without lagging your PC.
* **Smart Cooldowns:** Audio alerts use a cooldown timer to prevent annoying, overlapping audio loops.
* **Privacy Focused:** All computer vision processing happens locally on your machine. No video data is saved or sent over the internet.

## 🛠️ Prerequisites & Installation

1. **Python 3.12:** Make sure you have Python installed (Python 3.12 is highly recommended for compatibility with older MediaPipe architectures).

2. **Clone the Repository:**
   ```bash
   git clone [https://github.com/bolanxu/bad-habit-breaker.git](https://github.com/bolaxu/bad-habit-breaker.git)
   cd bad-habit-breaker
   ```
3. **Install Dependencies:** Run the following command to install the precise, stable versions of the required libraries:
   ```bash
   pip install opencv-python pygame mediapipe==0.10.14
   ```

## 🚀 How to Use
1. Add your audio file: Drop a short notification sound (e.g., a beep or alarm) into the root folder of the project and name it
   ```warning.mp3```.

3. Run the script:
   ```bash
   python habit_breaker.py
   ```

4. **Calibrate (Optional)**: If the alarm triggers too early or too late, open habit_breaker.py and adjust the ```TRIGGER_DISTANCE``` variable:
   * Increase it (e.g., ```0.12```) if it's missing your hand.
   * Decrease it (e.g., ```0.07```) if it's too sensitive.

4. **Exit:** Click on the camera window and press q to close the program.

## ⚙️ Performance Customization
If you want the application to use virtually 0% display resources, you can comment out or delete the ```cv2.imshow``` lines at the bottom of the script. The code will run completely hidden in the background while you study or work, only making a sound when your hand approaches your face.

## 📜 License
This project is open-source and available under the MIT License.
