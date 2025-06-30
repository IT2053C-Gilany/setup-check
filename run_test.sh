#!/bin/bash

# Run the notebook output test (no environment activation needed)
echo "🧪 Running notebook output test..."
python test_notebook_output.py

# Exit with the same code as the test script
exit $? 