# Shutdown_timer_macOS

This is a simple Python GUI application that allows you to schedule a shutdown on your macOS machine after a specified number of minutes. The app also allows you to abort a scheduled shutdown if needed.

## Features

- Set a timer (in minutes) to automatically shut down your Mac.
- Abort a scheduled shutdown at any time.
- Simple graphical user interface (GUI) using Tkinter.
- Prompts for the `sudo` password when necessary.

## Requirements

1. **Python 3.x**
2. **Tkinter** (This is usually included with Python installations on macOS)
3. **sudo access** (required to execute the shutdown command)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/mac-shutdown-timer.git
   cd mac-shutdown-timer
