#!/usr/bin/env python3
"""
Test script for verifying notebook output.
This script reads the setup-checker notebook and verifies that the existing output
contains the expected pattern: a hello message with username followed by 8 checkmarks.
"""

import json
import sys
import re
from pathlib import Path


def extract_notebook_output():
    """Extract the existing output from the notebook file."""
    try:
        # Read the notebook file
        with open('setup-checker.ipynb', 'r') as f:
            notebook = json.load(f)
        
        # Extract all output text from cells
        outputs = []
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                for output in cell.get('outputs', []):
                    if output['output_type'] == 'stream':
                        # Handle both string and list outputs
                        text = output['text']
                        if isinstance(text, list):
                            text = ''.join(text)
                        outputs.append(text)
                    elif output['output_type'] == 'execute_result':
                        if 'data' in output and 'text/plain' in output['data']:
                            text = output['data']['text/plain']
                            if isinstance(text, list):
                                text = ''.join(text)
                            outputs.append(text)
        
        return '\n'.join(outputs)
    except Exception as e:
        print(f"❌ Error extracting notebook output: {e}")
        return None


def verify_output_pattern(output_text):
    """
    Verify that the output contains the expected pattern:
    - A hello message with username
    - Followed by 8 checkmarks (✅)
    """
    if not output_text:
        print("❌ No output text to verify")
        return False
    
    print("📋 Notebook output:")
    print("-" * 50)
    print(output_text)
    print("-" * 50)
    
    # Check for hello message with username
    hello_pattern = r'👋 Hello, \w+!'
    hello_match = re.search(hello_pattern, output_text)
    
    if not hello_match:
        print("❌ Hello message with username not found")
        return False
    
    print(f"✅ Found hello message: {hello_match.group()}")
    
    # Count checkmarks
    checkmark_count = output_text.count('✅')
    print(f"✅ Found {checkmark_count} checkmarks")
    
    # Verify we have exactly 8 checkmarks
    if checkmark_count != 8:
        print(f"❌ Expected 8 checkmarks, found {checkmark_count}")
        return False
    
    print("✅ Correct number of checkmarks found")
    
    # Additional verification: check for specific expected outputs
    expected_patterns = [
        r'✅ Current python version:',
        r'✅ Current pip version:',
        r'✅ Current conda version:',
        r'✅ Current environment:',
        r'✅ Current dependencies:',
        r'✅ Current git version:',
        r'✅ Current directory is a git repository',
        r'✅ Current jupyter version:'
    ]
    
    missing_patterns = []
    for pattern in expected_patterns:
        if not re.search(pattern, output_text):
            missing_patterns.append(pattern)
    
    if missing_patterns:
        print("❌ Missing expected output patterns:")
        for pattern in missing_patterns:
            print(f"   - {pattern}")
        return False
    
    print("✅ All expected output patterns found")
    return True


def main():
    """Main test function."""
    print("🧪 Starting notebook output test...")
    
    # Check if notebook file exists
    if not Path('setup-checker.ipynb').exists():
        print("❌ setup-checker.ipynb not found")
        sys.exit(1)
    
    # Extract output from existing notebook
    print("📤 Extracting notebook output...")
    output_text = extract_notebook_output()
    
    if output_text is None:
        print("❌ Failed to extract notebook output")
        sys.exit(1)
    
    # Verify the output pattern
    print("🔍 Verifying output pattern...")
    if verify_output_pattern(output_text):
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("💥 Tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main() 