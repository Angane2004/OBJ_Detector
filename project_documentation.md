# Real-Time Object Detection Project - Complete Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Project Architecture](#project-architecture)
3. [Folder Structure](#folder-structure)
4. [Technology Stack](#technology-stack)
5. [Component Details](#component-details)
6. [Setup & Installation](#setup--installation)
7. [Running the Application](#running-the-application)
8. [API Endpoints](#api-endpoints)
9. [Features](#features)
10. [Future Enhancements](#future-enhancements)

---

## 🎯 Project Overview

**Real-Time Object Detection Using Computer Vision** is a web-based application that integrates AI-powered computer vision to detect and track objects in real-time. The project combines a responsive frontend with two powerful backend detection systems:

1. **General Object Detection**: Uses YOLOv10 to detect and classify 80+ common objects
2. **PPE Safety Detection**: Specialized YOLO model for detecting Personal Protective Equipment (PPE) compliance in workplace environments

### Key Objectives
- Provide instant object identification and tracking using webcam feeds
- Enable safety monitoring through PPE detection (hardhats, masks, safety vests)
- Deliver high accuracy (98%) and fast processing (1 second)
- Support real-time video processing with low latency

### Use Cases
- Smart surveillance systems
- Industrial safety monitoring
- Autonomous vehicle object recognition
- Retail customer and inventory tracking
- Quality control in manufacturing

---

## 🏗️ Project Architecture

The project follows a client-server architecture:

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER                       │
│  ┌──────────────────────────────────────────────────┐  │
│  │  index.html (Landing Page)                       │  │
│  │  - Bootstrap 5.3.3 responsive design             │  │
│  │  - AOS animations, GLightbox, Swiper             │  │
│  │  - Navigation to detection features              │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  assets/js/main.js                               │  │
│  │  - Fetch API calls to backend                    │  │
│  │  - startDetection() → Object Detection           │  │
│  │  - Detection() → PPE Detection                   │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                         ↓ HTTP Requests
┌─────────────────────────────────────────────────────────┐
│                    BACKEND LAYER                        │
│  ┌──────────────────┐         ┌────────────────────┐   │
│  │ Flask API #1     │         │ Flask API #2       │   │
│  │ Port: 5000       │         │ Port: 8000         │   │
│  │ /start-detection │         │ /detection         │   │
│  └────────┬─────────┘         └─────────┬──────────┘   │
│           ↓                             ↓               │
│  ┌──────────────────┐         ┌────────────────────┐   │
│  │ Object_Detector/ │         │ ppe_detection/     │   │
│  │ detector.py      │         │ yolo_detector.py   │   │
│  │ YOLOv10n model   │         │ Custom PPE model   │   │
│  │ 80 classes       │         │ 10 PPE classes     │   │
│  └──────────────────┘         └────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│                   HARDWARE LAYER                        │
│              Webcam (cv2.VideoCapture)                  │
│           Real-time video stream processing             │
└─────────────────────────────────────────────────────────┘
```

### Data Flow
1. User clicks "Object Detection" or "Safety Management" in the navigation menu
2. JavaScript function triggers HTTP GET request to respective Flask endpoint
3. Flask server spawns subprocess to run YOLO detection script
4. Detection script captures webcam feed using OpenCV
5. YOLO model processes each frame and identifies objects
6. Results are displayed in real-time with bounding boxes and labels
7. User can quit detection by pressing 'q'

---

## 📁 Folder Structure

```
Frontend_Object_Detection/
│
├── index.html                    # Main landing page (482 lines)
├── README.md                     # Basic project information
├── Readme.txt                    # Template attribution
│
├── Object_Detector/              # General object detection module
│   ├── main.py                   # Flask API server (Port 5000)
│   ├── detector.py               # YOLOv10 detection script
│   ├── yolov10n.pt              # Pre-trained YOLOv10 nano model (5.8 MB)
│   └── requirements.txt          # Python dependencies
│
├── ppe_detection/                # PPE safety detection module
│   ├── detector.py               # Flask API server (Port 8000)
│   ├── yolo_detector.py          # PPE detection script (functional)
│   ├── PPE_Detection.py          # Alternative PPE script (template)
│   └── ppe.pt                    # Custom PPE YOLO model (87.6 MB)
│
├── assets/                       # Frontend resources
│   ├── css/
│   │   └── main.css              # Main stylesheet (37 KB)
│   ├── js/
│   │   └── main.js               # JavaScript logic & API calls (205 lines)
│   ├── img/                      # Image assets
│   │   ├── detection.png         # Favicon
│   │   ├── hero-bg-2.jpg         # Hero section background
│   │   ├── img1.jpg, img2.jpg    # Feature images
│   │   ├── details-1 to 4.png    # Project detail illustrations
│   │   ├── img3.avif, img4.avif  # Additional visuals
│   │   └── gallery/, team/, testimonials/
│   ├── scss/                     # SCSS source files (if needed)
│   └── vendor/                   # Third-party libraries (38 items)
│       ├── bootstrap/            # Bootstrap 5.3.3
│       ├── bootstrap-icons/      # Icon library
│       ├── aos/                  # Animate On Scroll
│       ├── glightbox/            # Lightbox for media
│       ├── swiper/               # Swiper slider
│       ├── purecounter/          # Counter animations
│       └── php-email-form/       # Form validation
│
├── forms/                        # PHP contact form handlers
│   ├── contact.php               # Contact form processor
│   ├── newsletter.php            # Newsletter subscription
│   └── Readme.txt                # Usage instructions
│
└── .git/                         # Git version control
```

### File Count Summary
- **Total Directories**: 10
- **Python Scripts**: 8
- **HTML Files**: 1
- **CSS Files**: 1 main + vendor styles
- **JavaScript Files**: 1 main + vendor scripts
- **Model Files**: 2 (.pt files)
- **Images**: 16+ in assets/img/

---

## 🛠️ Technology Stack

### Frontend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| **HTML5** | - | Semantic structure and content |
| **CSS3** | - | Custom styling and responsive design |
| **Bootstrap** | 5.3.3 | Responsive grid system, components |
| **JavaScript (ES6+)** | - | Fetch API, DOM manipulation |
| **Google Fonts** | - | Roboto, Poppins, Raleway typography |
| **AOS** | Latest | Scroll-triggered animations |
| **GLightbox** | Latest | Image/video lightbox functionality |
| **Swiper** | Latest | Touch-enabled sliders |
| **PureCounter** | Latest | Animated statistics display |
| **Bootstrap Icons** | Latest | Iconography |

### Backend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.x | Backend scripting language |
| **Flask** | Latest | Lightweight web framework for APIs |
| **Flask-CORS** | Latest | Cross-Origin Resource Sharing |
| **OpenCV (cv2)** | Latest | Video capture and processing |
| **Ultralytics YOLO** | v10 | Object detection framework |
| **cvzone** | Latest | Computer vision helper utilities |

### AI/ML Models
| Model | Size | Classes | Purpose |
|-------|------|---------|---------|
| **YOLOv10n** | 5.8 MB | 80 | General object detection (nano version) |
| **Custom PPE** | 87.6 MB | 10 | PPE safety equipment detection |

**PPE Model Classes** (10 total):
- Hardhat
- Mask
- NO-Hardhat
- NO-Mask
- NO-Safety Vest
- Person
- Safety Cone
- Safety Vest
- Machinery
- Vehicle

---

## 🔧 Component Details

### 1. Frontend - `index.html`

**Purpose**: Responsive landing page showcasing the project with navigation to detection features.

**Key Sections**:
- **Header**: Fixed navigation bar with logo and menu
  - Links: Home, About Project, Features, Detection Techniques dropdown
  - Mobile-responsive hamburger menu
  
- **Hero Section**: 
  - Dark background with wave animations
  - Call-to-action buttons: "Know More" and "Watch Video"
  - Displays main value proposition

- **About Section**:
  - Technology overview
  - How it works explanation
  - Key benefits
  - Performance & accuracy metrics

- **Features Section**: Grid display of 8 key features
  - High Accuracy (98%)
  - Real-Time Processing (1 second)
  - Multi-Object Detection
  - Performance Monitoring
  - Error Handling & Recovery
  - Real-Time Video Processing
  - Network Integration
  - Performance Monitoring

- **Stats Section**: Animated counters
  - Detection Accuracy: 98%
  - Processing Speed: 1 second
  - Training Time: 1 hour

- **Details Section**: Four detailed feature cards with images
  1. Introduction to real-time object detection
  2. Algorithms and performance (YOLO, SSD)
  3. Integration with edge computing
  4. Benefits and applications

- **FAQ Section**: Expandable accordion
  - How It Works
  - Technology Stack
  - Case Studies

- **Footer**: 
  - Organization details (A. P. Shah Institute of Technology)
  - Useful links
  - Copyright information

**Integration Points**:
- Calls `startDetection()` for Object Detection
- Calls `Detection()` for PPE Safety Management

---

### 2. Frontend JavaScript - `assets/js/main.js`

**Purpose**: Handle frontend logic, animations, and communication with backend APIs.

**Key Functions**:

#### Detection Functions
```javascript
async function startDetection() {
  // Calls: http://127.0.0.1:5000/start-detection
  // Triggers general object detection
}

async function Detection() {
  // Calls: http://127.0.0.1:8000/detection
  // Triggers PPE safety detection
}
```

#### UI Enhancement Functions
- `toggleScrolled()`: Adds scrolled class to body
- `mobileNavToogle()`: Toggles mobile navigation
- `aosInit()`: Initializes Animate On Scroll
- `initSwiper()`: Initializes slider components
- `navmenuScrollspy()`: Highlights active navigation based on scroll position
- FAQ accordion toggle functionality
- Scroll-to-top button logic

**Event Listeners**: 205 lines handling scroll, click, load events

---

### 3. Backend - `Object_Detector/main.py`

**Purpose**: Flask API server to trigger general object detection.

**Port**: 5000

**Endpoint**: `/start-detection` (GET)

**Functionality**:
```python
@app.route('/start-detection', methods=['GET'])
def start_detection():
    # Opens detector.py in new terminal window
    # Windows: subprocess.Popen(['start', 'cmd', '/k', 'python', 'detector.py'])
    # Linux/macOS: subprocess.Popen(['python3', 'detector.py'])
    return {"message": "YOLO detection started in a new window."}
```

**CORS**: Enabled to allow frontend requests

---

### 4. Detection Script - `Object_Detector/detector.py`

**Purpose**: Real-time object detection using YOLOv10 model.

**Key Components**:

#### Model Initialization
```python
model = YOLO('yolov10n.pt')  # YOLOv10 nano model
```

#### Webcam Capture
```python
cap = cv2.VideoCapture(0)  # Index 0 = default webcam
```

#### Detection Loop
1. Read frame from webcam
2. Run YOLO inference with 0.25 confidence threshold
3. Extract bounding boxes, confidence scores, class names
4. Draw rectangles and labels on frame
5. Display in OpenCV window
6. Press 'q' to quit

**Performance**: Processes frames in real-time with minimal latency

---

### 5. Backend - `ppe_detection/detector.py`

**Purpose**: Flask API server to trigger PPE safety detection.

**Port**: 8000

**Endpoint**: `/detection` (GET)

**Functionality**:
```python
@app.route('/detection', methods=['GET'])
def start_detection():
    # Opens yolo_detector.py in new terminal window
    # Windows: subprocess.Popen(['start', 'cmd', '/k', 'python', 'yolo_detector.py'])
    return {"message": "YOLO detection started in a new window."}
```

---

### 6. PPE Detection Script - `ppe_detection/yolo_detector.py`

**Purpose**: Specialized detection for workplace safety equipment.

**Model**: Custom trained YOLO model (`ppe.pt`)

**Classes Detected** (10):
- Safety Equipment: Hardhat, Mask, Safety Vest
- Safety Violations: NO-Hardhat, NO-Mask, NO-Safety Vest
- Other: Person, Safety Cone, Machinery, Vehicle

**Color Coding**:
- 🔴 **Red** (0, 0, 255): Safety violations (NO-Hardhat, NO-Mask, NO-Safety Vest)
- 🟢 **Green** (0, 255, 0): Proper PPE usage (Hardhat, Mask, Safety Vest)
- 🔵 **Blue** (255, 0, 0): Other objects (Person, Cone, Machinery, Vehicle)

**Detection Loop**:
1. Capture webcam frame
2. Run PPE model inference
3. For each detected object:
   - Extract bounding box coordinates
   - Determine object class
   - Select appropriate color based on safety status
   - Draw labeled bounding box
4. Display real-time results
5. Press 'q' to quit

**Use Case**: Construction sites, manufacturing floors, laboratories

---

### 7. Alternative Script - `ppe_detection/PPE_Detection.py`

**Status**: Template/Reference implementation (not actively used)

**Notes**: 
- Contains commented webcam initialization
- Missing `cap` variable initialization in current form
- Video file input option commented out
- Includes confidence threshold filtering (>0.5)

---

### 8. Styling - `assets/css/main.css`

**Purpose**: Custom CSS for design and responsiveness.

**Features**:
- Responsive grid layouts
- Custom color scheme
- Animation declarations
- Typography settings
- Mobile-first media queries
- Dark background themes for hero sections
- Button hover effects
- Card component styles

**Size**: 37 KB of custom styles

---

### 9. Forms - `forms/contact.php` & `forms/newsletter.php`

**Purpose**: Server-side PHP handlers for contact and newsletter forms.

**Note**: These files are part of the Bootslander template but may require configuration for live deployment (SMTP settings, email validation, etc.).

---

## 📦 Setup & Installation

### Prerequisites
- Python 3.8 or higher
- Webcam/Camera device
- Modern web browser (Chrome, Firefox, Edge)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Frontend_Object_Detection
```

### Step 2: Install Python Dependencies

#### For Object Detector
```bash
cd Object_Detector
pip install -r requirements.txt
```

**Dependencies**:
- ultralytics
- cvzone
- opencv-python (installed as dependency)
- numpy (installed as dependency)

#### For PPE Detection
```bash
cd ../ppe_detection
pip install ultralytics cvzone opencv-python
```

### Step 3: Install Flask Dependencies
```bash
pip install flask flask-cors
```

### Step 4: Verify Model Files
Ensure the following model files exist:
- `Object_Detector/yolov10n.pt` (5.8 MB)
- `ppe_detection/ppe.pt` (87.6 MB)

**Note**: If model files are missing, you may need to train or download them separately.

---

## 🚀 Running the Application

### Method 1: Run Full Application

#### Step 1: Start Object Detection API
```bash
cd Object_Detector
python main.py
```
- Server runs on `http://127.0.0.1:5000`
- Keep this terminal open

#### Step 2: Start PPE Detection API (New Terminal)
```bash
cd ppe_detection
python detector.py
```
- Server runs on `http://127.0.0.1:8000`
- Keep this terminal open

#### Step 3: Open Frontend
- Open `index.html` directly in browser, OR
- Use a local server:
```bash
# Using Python's built-in server
python -m http.server 3000
# Access at http://localhost:3000
```

#### Step 4: Use the Application
1. Click **"Detection techniques"** dropdown in navigation
2. Select **"Object Detections"** for general object detection
3. Select **"Safety Management"** for PPE detection
4. A new terminal window will open with live camera feed
5. Press **'q'** in the detection window to stop

---

### Method 2: Run Detection Scripts Directly

#### General Object Detection
```bash
cd Object_Detector
python detector.py
```
- Opens webcam window immediately
- Detects 80 common objects

#### PPE Safety Detection
```bash
cd ppe_detection
python yolo_detector.py
```
- Opens webcam window immediately
- Detects PPE compliance

---

## 🌐 API Endpoints

### Object Detection API

**Base URL**: `http://127.0.0.1:5000`

#### `GET /start-detection`
Starts the general object detection process.

**Request**:
```javascript
fetch('http://127.0.0.1:5000/start-detection')
```

**Response**:
```json
{
  "message": "YOLO detection started in a new window."
}
```

**Error Response**:
```json
{
  "error": "Error message details"
}
```

---

### PPE Detection API

**Base URL**: `http://127.0.0.1:8000`

#### `GET /detection`
Starts the PPE safety detection process.

**Request**:
```javascript
fetch('http://127.0.0.1:8000/detection')
```

**Response**:
```json
{
  "message": "YOLO detection started in a new window."
}
```

**Error Response**:
```json
{
  "error": "Error message details"
}
```

---

## ✨ Features

### 1. High Accuracy Object Detection
- **98% accuracy** in controlled environments
- Confidence threshold filtering (25% for general, 50% for PPE)
- Real-time bounding box visualization

### 2. Real-Time Processing
- **1-second processing speed** per frame
- Low latency webcam capture
- Instant feedback and alerts

### 3. Multi-Object Detection
- Simultaneously detects multiple objects in single frame
- Handles overlapping objects with Non-Maximum Suppression
- Supports 80 object classes (YOLOv10) + 10 PPE classes

### 4. Dual Detection Systems
- **General Detection**: Everyday objects (person, car, dog, etc.)
- **Safety Detection**: Workplace PPE compliance monitoring

### 5. Color-Coded Safety Alerts
- Visual indicators for safety compliance
- Instant identification of violations
- Easy-to-understand status display

### 6. Responsive Web Interface
- Mobile-friendly design
- Smooth animations (AOS)
- Interactive FAQ and feature showcases
- Professional landing page

### 7. Cross-Platform Support
- Windows, Linux, macOS compatibility
- Automatic platform detection in code
- Browser-based frontend (universal access)

### 8. Modular Architecture
- Separate modules for different detection types
- Easy to extend with new models
- Independent API servers

---

## 🚧 Future Enhancements

### Planned Features
1. **Database Integration**
   - Store detection logs and timestamps
   - Track safety violations over time
   - Generate compliance reports

2. **Dashboard Analytics**
   - Real-time detection statistics
   - Violation frequency charts
   - Performance metrics visualization

3. **Multi-Camera Support**
   - Monitor multiple camera feeds simultaneously
   - Centralized control panel
   - Camera switching interface

4. **Email/SMS Alerts**
   - Automatic notifications for safety violations
   - Configurable alert thresholds
   - Integration with notification services

5. **Video Recording**
   - Save detection sessions
   - Timestamp violation events
   - Playback with annotation overlay

6. **Cloud Deployment**
   - Host APIs on cloud platforms (AWS, GCP, Azure)
   - WebRTC for browser-based camera access
   - Scalable architecture

7. **User Authentication**
   - Admin panel for managing users
   - Role-based access control
   - Session management

8. **Advanced YOLO Models**
   - YOLOv10 large/extra-large for higher accuracy
   - Custom model training interface
   - Transfer learning capabilities

9. **Edge Computing**
   - Raspberry Pi / Jetson Nano deployment
   - Local processing for data privacy
   - Reduced cloud costs

10. **Emotion & Gesture Detection**
    - Extend to facial emotion recognition
    - Hand gesture detection (commented in nav menu)
    - Behavior analysis

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Detection Accuracy** | 98% |
| **Processing Speed** | 1 second/frame |
| **Training Time** | 1 hour |
| **Total Lines of Code** | ~1,000+ |
| **Supported Object Classes** | 90 (80 general + 10 PPE) |
| **Model Size** | 93.4 MB total |
| **Frontend Libraries** | 6 major (Bootstrap, AOS, GLightbox, etc.) |
| **API Endpoints** | 2 |

---

## 🎓 Educational Institution

**Developed at**: A. P. Shah Institute of Technology, Thane - West

---

## 📝 Template Attribution

The frontend design is based on the **Bootslander** template:
- **Template Name**: Bootslander
- **Template URL**: https://bootstrapmade.com/bootslander-free-bootstrap-landing-page-template/
- **Author**: BootstrapMade.com
- **License**: https://bootstrapmade.com/license/

---

## 🔑 Key Files Quick Reference

| File | Path | Purpose |
|------|------|---------|
| Landing Page | `index.html` | Main website |
| Object Detection API | `Object_Detector/main.py` | Flask server (5000) |
| Object Detector | `Object_Detector/detector.py` | YOLO script |
| PPE Detection API | `ppe_detection/detector.py` | Flask server (8000) |
| PPE Detector | `ppe_detection/yolo_detector.py` | PPE YOLO script |
| Frontend Logic | `assets/js/main.js` | API calls & UI |
| Styling | `assets/css/main.css` | Custom CSS |
| YOLOv10 Model | `Object_Detector/yolov10n.pt` | Pre-trained weights |
| PPE Model | `ppe_detection/ppe.pt` | Custom PPE weights |

---

## 🐛 Troubleshooting

### Common Issues

#### 1. Webcam Not Opening
**Solution**: 
- Check if webcam is connected
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` or higher
- Ensure no other application is using the camera

#### 2. CORS Error in Browser
**Solution**: 
- Verify Flask-CORS is installed: `pip install flask-cors`
- Check that both Flask servers are running
- Use browser console to see exact error

#### 3. Model File Not Found
**Solution**:
- Verify `.pt` files exist in their respective directories
- Check file paths in Python scripts
- Download or retrain models if missing

#### 4. Subprocess Not Opening
**Solution**:
- On Windows, ensure Command Prompt is accessible
- On Linux/Mac, verify Python3 is in PATH
- Check subprocess shell permissions

#### 5. Low Frame Rate
**Solution**:
- Use YOLOv10n (nano) instead of larger models
- Reduce inference resolution
- Enable GPU acceleration if available

---

## 💻 System Requirements

### Minimum Requirements
- **OS**: Windows 10, Ubuntu 18.04, macOS 10.14
- **RAM**: 4 GB
- **CPU**: Intel i3 or equivalent
- **Webcam**: 720p resolution
- **Python**: 3.8+

### Recommended Requirements
- **OS**: Windows 11, Ubuntu 22.04, macOS 13
- **RAM**: 8 GB
- **CPU**: Intel i5 or equivalent
- **GPU**: NVIDIA GPU with CUDA support (optional, for faster processing)
- **Webcam**: 1080p resolution
- **Python**: 3.10+

---

## 📞 Contact & Support

For questions or support regarding this project:
- **Institution**: A. P. Shah Institute of Technology
- **Location**: Thane - West
- **Project Type**: Computer Vision / AI-based Object Detection

---

## 📜 License

Please refer to the template license for frontend components:
- **Frontend Template**: [BootstrapMade License](https://bootstrapmade.com/license/)
- **Backend/Models**: Check respective library licenses (Ultralytics, OpenCV, Flask)

---

**Last Updated**: December 2024

**Documentation Version**: 1.0

---

*This documentation provides a complete overview of the Real-Time Object Detection project. For specific implementation details, refer to the source code in the respective directories.*
