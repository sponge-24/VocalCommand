# Voice-Controlled Media Player

## Overview

This project allows you to control media playback and system volume using voice commands. It leverages Azure Cognitive Services for speech recognition and provides functionalities like play/pause, mute/unmute, volume adjustment, and more. Notifications are displayed to inform the user of ongoing actions.

## Features

- **Voice Commands:** Control media playback, volume, and other functions using voice commands.
- **Notifications:** Inform the user about listening status and actions taken.
- **Keyboard Shortcuts:** Use keyboard shortcuts to interact with media and system volume.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sponge-24/VocalCommand
   cd VocalCommand
   ```

2. **Install Dependencies:**

   ```bash
   pip install azure-cognitiveservices-speech python-dotenv pyautogui keyboard pycaw
   ```

3. **Setup Environment Variables:**

   Create a `.env` file in the root directory with the following content:

   ```env
   SPEECH_KEY="your api key"
   SPEECH_REGION="your end point"
   ```

## Usage

1. **Run the Application:**

   Execute the script to start listening for voice commands:

   ```bash
   python voice_media_control.py
   ```

2. **Voice Commands:**

   - **Play/Pause:** Say "play" or "pause".
   - **Mute/Unmute:** Say "mute" or "unmute".
   - **Volume:** Say "volume X" where X is a percentage (e.g., "volume 50").
   - **Next/Previous:** Say "next" or "previous".
   - **Fullscreen/Normal:** Say "full" or "normal".
   - **Close Window:** Say "close".
   - **Forward/Rewind:** Say "forward" or "rewind". Press "n" to stop forwarding or rewinding.

## Code Structure

- `voice_media_control.py`: Main script that handles voice recognition, command execution, and notifications.
- `volume.py`: Contains functions for setting and extracting volume levels.
- `display.py`: Contains functions for displaying notifications.

## Troubleshooting

- Ensure you have the correct API key and endpoint in the `.env` file.
- Make sure your microphone is set up correctly and accessible.
- Check if required libraries are installed and updated.
