# PyQt5 Stopwatch

A custom stopwatch built using **PyQt5** with a sleek digital look.  
Features a frameless transparent window, draggable design, and animated borders.  

---

## Features

- Start, Stop, and Reset buttons  
- High-precision timing (updates every 10 milliseconds)  
- Custom digital font for the time display (`DS-DIGII.TTF`)  
- Frameless and transparent window  
- Draggable window  
- Animated dashed border  

---

## How to Run

1. Make sure Python 3.x is installed.  
2. Install PyQt5 if you haven't already:

```bash
pip install PyQt5
Make sure your font file (DS-DIGII.TTF) is in the correct path or update the path in the code.

Run the script:

bash
Copy code
python stopwatch.py
Usage
Start button: Begin the stopwatch

Stop button: Pause the stopwatch

Reset button: Reset time to 00:00:00:00

Drag the window: Click anywhere and drag to move the stopwatch

Code Highlights
Uses QTime to track time

Updates display every 10 ms with QTimer

Custom paintEvent for animated dashed borders

Transparent window with Qt.WA_TranslucentBackground

Draggable window implemented with mousePressEvent, mouseMoveEvent, and mouseReleaseEvent

Customization
Change the font by replacing DS-DIGII.TTF and updating the path

Adjust the border color or dash speed in paintEvent and animate_border()

Modify button and label styles in setStyleSheet

Made by Suminda Lakshan
