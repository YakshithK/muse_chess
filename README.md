# Muse Chess

## Overview
Muse Chess is an experimental project that combines Brain-Computer Interface (BCI) technology with the classic game of chess. It allows players to control chess pieces on a virtual board using brainwave signals captured by the Muse headband.

## Table of Contents
- **Introduction**
- **Dependencies**
- **Setup**
- **Usage**
- **Pyautogui coordination (MUST READ)**
- **Contributing**

## Introduction
Brain-Computer Interface (BCI) technology enables direct communication between the brain and an external device, bypassing traditional pathways such as muscles or nerves. Muse Chess leverages this technology to provide an innovative way of interacting with a chess game.

The project utilizes the Muse headband, a consumer-grade EEG device developed by Interaxon. The Muse headband measures brainwave activity and transmits the data wirelessly to a computer. The data is then processed using the MuseLSL and BlueMuse libraries to interpret the user's intent.

## Dependencies
- **MuseLSL**: A Python library for streaming data from the Muse headband using Lab Streaming Layer (LSL) protocol (see github repo [here](https://github.com/alexandrebarachant/muse-lsl)).
- **BlueMuse**: A cross-platform Java application for connecting to and streaming data from the Muse headband (see github repo [here](https://github.com/kowalej/BlueMuse)).
- **Python**: The programming language used for developing the chess game and integrating with MuseLSL.
- **PyQt5**: Python bindings for the Qt application framework, used for creating the graphical user interface.
- **NumPy**: A library for numerical computations, used for processing data arrays.
- **Matplotlib**: A plotting library used for visualizing EEG data.

## Setup

Install Python on your computer if you haven't already.

**Install the required Python dependencies using pip:**

*Copy code*

pip install muselsl PyQt5 numpy matplotlib

Clone the MuseLSL and BlueMuse repositories and follow their setup instructions.

## PyAutoGUI Coordinates

Some parts of the application may be specific to the user's screen orientation, such as the PyAutoGUI coordinates used for mouse interactions. Adjustments may be needed based on your screen resolution and layout to ensure accurate gameplay. Wherever you see the following functions, you may need to change them either directly or in the *chess_utils.py* file.

- **closeCmd()**
- **pyautogui.click()**
- **The lists of file and rank coordinates declared at the beginning**
- **This isn't PyAutoGUI but even the UI window sizes, font sizes and event button sized *may* need to be adjusted.** 

## Usage
Launch BlueMuse and connect your Muse headband.

Clone this repo or download this repo to your computer

**Run the *main.py* file**

Switch to a window with chess.com already logged into a game and enjoy!

## Contributing
Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request.
