# 🔍 AI Image Person Finder

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Face Recognition](https://img.shields.io/badge/AI-Face%20Recognition-orange.svg)](https://github.com/ageitgey/face_recognition)

An AI-powered educational tool for facial recognition and person identification using deep learning. This project demonstrates the capabilities and limitations of modern facial recognition technology while emphasizing ethical considerations.

## ⚠️ IMPORTANT: Ethical and Legal Disclaimer

**This tool is STRICTLY for educational purposes only.**

### Legal and Ethical Requirements
- ✅ **Obtain explicit consent** before processing anyone's images
- ✅ **Comply with privacy laws** (GDPR, CCPA, BIPA, etc.)
- ✅ **Use responsibly** and ethically
- ❌ **DO NOT use** for surveillance or unauthorized tracking
- ❌ **DO NOT use** to violate anyone's privacy rights
- ❌ **DO NOT use** for discriminatory purposes

### Privacy Considerations
- Facial recognition technology raises significant privacy concerns
- Always inform individuals before processing their biometric data
- Store and handle facial data securely
- Delete data when no longer needed
- Be aware of local laws regarding biometric data

## 🎯 Features

- **Facial Detection**: Automatically detect faces in images using state-of-the-art algorithms
- **Face Recognition**: Match faces against a database of known persons
- **Confidence Scoring**: Get probability scores for each match
- **Image Annotation**: Visualize results with bounding boxes and labels
- **Batch Processing**: Process multiple images efficiently
- **JSON Export**: Export results in structured format for further analysis
- **Command-Line Interface**: Easy-to-use CLI for automation

## 🚀 How It Works

This tool uses:
1. **dlib's face detection** (HOG + CNN models)
2. **face_recognition library** (built on dlib)
3. **128-dimensional face encodings** for identification
4. **OpenCV** for image processing and visualization

### Technical Approach

```
Input Image → Face Detection → Face Encoding → 
Compare with Known Faces → Calculate Distances → 
Match/Identify → Annotate Results
```

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- CMake (required for dlib)
- C++ compiler

#### System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install cmake build-essential python3-dev
```

**macOS:**
```bash
brew install cmake
```

**Windows:**
- Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)
- Install [CMake](https://cmake.org/download/)

### Python Dependencies

1. Clone this repository:
```bash
git clone https://github.com/rahit91890/ai-image-person-finder.git
cd ai-image-person-finder
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

**Note:** Installing `dlib` can take several minutes as it compiles from source.

## 💻 Usage

### Basic Example

1. **Prepare your known faces directory structure:**
```
known_faces/
├── person1/
│   ├── photo1.jpg
│   └── photo2.jpg
├── person2/
│   ├── photo1.jpg
│   └── photo2.jpg
└── person3/
    └── photo1.jpg
```

2. **Run the person finder:**
```bash
python main.py --known-faces ./known_faces --search-image ./test_image.jpg --output ./result.jpg
```

### Command-Line Arguments

```bash
python main.py [OPTIONS]

Required Arguments:
  -k, --known-faces PATH    Directory containing known faces
  -s, --search-image PATH   Image file to search for persons

Optional Arguments:
  -o, --output PATH         Save annotated image to this path
  -t, --tolerance FLOAT     Face matching tolerance (0.0-1.0, default: 0.6)
                           Lower = stricter matching
  -j, --json PATH          Save results as JSON file
  -h, --help               Show help message
```

### Advanced Examples

**Strict matching with JSON output:**
```bash
python main.py \
  --known-faces ./database \
  --search-image ./group_photo.jpg \
  --output ./annotated.jpg \
  --tolerance 0.5 \
  --json ./results.json
```

**Display results without saving:**
```bash
python main.py -k ./known_faces -s ./test.jpg
```

## 📊 Output Example

### Console Output
```
======================================================================
AI IMAGE PERSON FINDER - EDUCATIONAL TOOL
======================================================================
⚠️  ETHICAL USAGE WARNING:
   - Use only with proper consent and authorization
   - Respect privacy laws and regulations
   - This tool is for educational purposes only
   - Do not use for surveillance or unauthorized tracking
======================================================================

📂 Loading known faces...
✓ Loaded face for: John Doe
✓ Loaded face for: Jane Smith
✓ Loaded face for: Bob Wilson

✓ Loaded 3 known face(s)

🔍 Searching for persons in: group_photo.jpg

📊 Results: Found 2 face(s)

Face #1:
  Name: John Doe
  Confidence: 94.32%
  Location: (top=150, right=350, bottom=450, left=50)

Face #2:
  Name: Jane Smith
  Confidence: 91.28%
  Location: (top=180, right=700, bottom=480, left=400)

✓ Annotated image saved to: annotated.jpg
```

### JSON Output
```json
{
  "timestamp": "2025-10-02T13:38:00.000000",
  "search_image": "group_photo.jpg",
  "tolerance": 0.6,
  "total_faces_found": 2,
  "results": [
    {
      "name": "John Doe",
      "confidence": 0.9432,
      "location": [150, 350, 450, 50],
      "match_index": 0
    },
    {
      "name": "Jane Smith",
      "confidence": 0.9128,
      "location": [180, 700, 480, 400],
      "match_index": 1
    }
  ]
}
```

## 🎓 Educational Use Cases

1. **Computer Vision Learning**: Understand face detection and recognition algorithms
2. **AI Ethics Education**: Explore ethical implications of facial recognition
3. **Privacy Research**: Study privacy concerns in biometric systems
4. **Security Training**: Learn about authentication and identification systems
5. **Academic Projects**: Use as foundation for research projects

## ⚙️ How It Works (Technical Details)

### Face Detection
- Uses HOG (Histogram of Oriented Gradients) or CNN for face detection
- Identifies face locations in images

### Face Encoding
- Generates 128-dimensional embeddings for each face
- Based on deep learning models trained on millions of faces

### Face Comparison
- Calculates Euclidean distance between face encodings
- Lower distance = higher similarity
- Tolerance parameter controls matching strictness

## 🔧 Troubleshooting

### Common Issues

**dlib installation fails:**
- Ensure CMake and C++ compiler are installed
- Try: `pip install dlib --no-cache-dir`
- On Windows, install Visual Studio Build Tools

**No faces detected:**
- Ensure images have clear, front-facing faces
- Try different images with better lighting
- Faces should be at least 80x80 pixels

**Low confidence scores:**
- Add more reference images per person
- Use high-quality reference images
- Ensure consistent lighting conditions

**Memory errors:**
- Process smaller images
- Reduce number of known faces loaded
- Close other applications

## 📝 Limitations

- **Accuracy**: Not 100% accurate; can produce false positives/negatives
- **Lighting**: Performance varies with lighting conditions
- **Angles**: Works best with frontal face images
- **Resolution**: Requires sufficient image quality
- **Occlusion**: Masks, sunglasses, or obstructions reduce accuracy
- **Bias**: May have bias issues inherent to training data

## 🔒 Security and Privacy

### Data Handling
- Face encodings are stored in memory only during execution
- No data is sent to external servers
- All processing is done locally

### Recommendations
- Don't store facial encodings without consent
- Use encryption for stored biometric data
- Implement access controls
- Follow data minimization principles
- Comply with relevant regulations

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure any contributions maintain ethical standards.

## 📚 Resources and Further Reading

- [face_recognition library](https://github.com/ageitgey/face_recognition)
- [dlib C++ library](http://dlib.net/)
- [OpenCV documentation](https://docs.opencv.org/)
- [GDPR and Biometric Data](https://gdpr.eu/)
- [Facial Recognition Ethics](https://www.eff.org/issues/face-recognition)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Rahit Biswas**
- GitHub: [@rahit91890](https://github.com/rahit91890)
- Website: [codaphics.com](https://codaphics.com)
- LinkedIn: [rahit-biswas-786939153](https://www.linkedin.com/in/rahit-biswas-786939153)

## ⭐ Acknowledgments

- Adam Geitgey for the excellent [face_recognition](https://github.com/ageitgey/face_recognition) library
- Davis King for [dlib](http://dlib.net/)
- OpenCV community for computer vision tools

## 🙏 Support

If you find this project helpful for learning:
- ⭐ Star this repository
- 🔄 Share with others
- 📝 Provide feedback
- 🐛 Report issues

---

**Remember: With great power comes great responsibility. Use AI ethically! 🤖💚**
