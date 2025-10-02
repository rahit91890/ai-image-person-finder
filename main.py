#!/usr/bin/env python3
"""
AI Image Person Finder
An educational tool for facial recognition and person identification using images.

WARNING: This tool is for educational purposes only.
Always respect privacy laws and obtain consent before processing personal images.
"""

import os
import sys
import cv2
import face_recognition
import numpy as np
from pathlib import Path
import argparse
import json
from datetime import datetime


class AIImagePersonFinder:
    """
    Main class for AI-powered person identification using facial recognition.
    Uses face_recognition library (built on dlib) for face detection and encoding.
    """
    
    def __init__(self, tolerance=0.6):
        """
        Initialize the person finder.
        
        Args:
            tolerance (float): Face matching tolerance (lower is more strict)
        """
        self.tolerance = tolerance
        self.known_faces = []
        self.known_names = []
        self.face_locations = []
        self.face_encodings = []
        
    def load_known_face(self, image_path, person_name):
        """
        Load a known face from an image file.
        
        Args:
            image_path (str): Path to the image file
            person_name (str): Name of the person in the image
        
        Returns:
            bool: True if face loaded successfully, False otherwise
        """
        try:
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            
            if len(encodings) > 0:
                self.known_faces.append(encodings[0])
                self.known_names.append(person_name)
                print(f"✓ Loaded face for: {person_name}")
                return True
            else:
                print(f"✗ No face found in: {image_path}")
                return False
        except Exception as e:
            print(f"✗ Error loading {image_path}: {str(e)}")
            return False
    
    def load_known_faces_from_directory(self, directory_path):
        """
        Load all known faces from a directory.
        Expected structure: directory/person_name/image.jpg
        
        Args:
            directory_path (str): Path to directory containing person folders
        """
        directory = Path(directory_path)
        
        if not directory.exists():
            print(f"✗ Directory not found: {directory_path}")
            return
        
        for person_folder in directory.iterdir():
            if person_folder.is_dir():
                person_name = person_folder.name
                for image_file in person_folder.glob("*.[jp][pn]g"):
                    self.load_known_face(str(image_file), person_name)
    
    def find_person_in_image(self, image_path):
        """
        Search for known persons in the given image.
        
        Args:
            image_path (str): Path to the image to search
        
        Returns:
            list: List of dictionaries containing match information
        """
        try:
            # Load the image
            image = face_recognition.load_image_file(image_path)
            
            # Find face locations and encodings
            self.face_locations = face_recognition.face_locations(image)
            self.face_encodings = face_recognition.face_encodings(image, self.face_locations)
            
            results = []
            
            # Compare each found face with known faces
            for i, face_encoding in enumerate(self.face_encodings):
                matches = face_recognition.compare_faces(
                    self.known_faces, face_encoding, tolerance=self.tolerance
                )
                face_distances = face_recognition.face_distance(
                    self.known_faces, face_encoding
                )
                
                if True in matches:
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_names[best_match_index]
                        confidence = 1 - face_distances[best_match_index]
                        location = self.face_locations[i]
                        
                        results.append({
                            'name': name,
                            'confidence': float(confidence),
                            'location': location,
                            'match_index': i
                        })
                else:
                    results.append({
                        'name': 'Unknown',
                        'confidence': 0.0,
                        'location': self.face_locations[i],
                        'match_index': i
                    })
            
            return results
            
        except Exception as e:
            print(f"✗ Error processing image {image_path}: {str(e)}")
            return []
    
    def annotate_image(self, image_path, results, output_path=None):
        """
        Annotate the image with face detection results.
        
        Args:
            image_path (str): Path to the input image
            results (list): Results from find_person_in_image
            output_path (str): Path to save annotated image (optional)
        """
        # Load image with OpenCV
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Draw rectangles and labels
        for result in results:
            top, right, bottom, left = result['location']
            name = result['name']
            confidence = result['confidence']
            
            # Draw rectangle
            color = (0, 255, 0) if name != 'Unknown' else (255, 0, 0)
            cv2.rectangle(image, (left, top), (right, bottom), color, 2)
            
            # Draw label
            label = f"{name} ({confidence:.2%})"
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            cv2.putText(image, label, (left + 6, bottom - 6),
                       cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)
        
        # Convert back to BGR for saving
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Save or display
        if output_path:
            cv2.imwrite(output_path, image)
            print(f"✓ Annotated image saved to: {output_path}")
        else:
            cv2.imshow('Results', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def main():
    """
    Main function to run the AI Image Person Finder from command line.
    """
    parser = argparse.ArgumentParser(
        description='AI Image Person Finder - Educational Tool',
        epilog='WARNING: Use responsibly and ethically. Respect privacy laws.'
    )
    
    parser.add_argument(
        '--known-faces', '-k',
        required=True,
        help='Directory containing known faces (structure: dir/person_name/*.jpg)'
    )
    
    parser.add_argument(
        '--search-image', '-s',
        required=True,
        help='Image file to search for persons'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output path for annotated image (optional)'
    )
    
    parser.add_argument(
        '--tolerance', '-t',
        type=float,
        default=0.6,
        help='Face matching tolerance (0.0-1.0, lower is stricter, default: 0.6)'
    )
    
    parser.add_argument(
        '--json', '-j',
        help='Save results as JSON file'
    )
    
    args = parser.parse_args()
    
    # Print ethical warning
    print("="*70)
    print("AI IMAGE PERSON FINDER - EDUCATIONAL TOOL")
    print("="*70)
    print("⚠️  ETHICAL USAGE WARNING:")
    print("   - Use only with proper consent and authorization")
    print("   - Respect privacy laws and regulations")
    print("   - This tool is for educational purposes only")
    print("   - Do not use for surveillance or unauthorized tracking")
    print("="*70)
    print()
    
    # Initialize finder
    finder = AIImagePersonFinder(tolerance=args.tolerance)
    
    # Load known faces
    print("📂 Loading known faces...")
    finder.load_known_faces_from_directory(args.known_faces)
    
    if len(finder.known_faces) == 0:
        print("✗ No known faces loaded. Exiting.")
        sys.exit(1)
    
    print(f"\n✓ Loaded {len(finder.known_faces)} known face(s)\n")
    
    # Search for persons in image
    print(f"🔍 Searching for persons in: {args.search_image}")
    results = finder.find_person_in_image(args.search_image)
    
    # Display results
    print(f"\n📊 Results: Found {len(results)} face(s)\n")
    
    for i, result in enumerate(results, 1):
        print(f"Face #{i}:")
        print(f"  Name: {result['name']}")
        print(f"  Confidence: {result['confidence']:.2%}")
        print(f"  Location: {result['location']}")
        print()
    
    # Save JSON if requested
    if args.json:
        json_data = {
            'timestamp': datetime.now().isoformat(),
            'search_image': args.search_image,
            'tolerance': args.tolerance,
            'total_faces_found': len(results),
            'results': results
        }
        
        with open(args.json, 'w') as f:
            json.dump(json_data, f, indent=2)
        
        print(f"✓ Results saved to JSON: {args.json}")
    
    # Annotate and save/display image
    if args.output or results:
        finder.annotate_image(args.search_image, results, args.output)


if __name__ == "__main__":
    main()
