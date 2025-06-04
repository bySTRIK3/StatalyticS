import os
import subprocess

# Create virtual environment
subprocess.run(["python", "-m", "venv", ".venv"])

# Provide instructions for manual activation
print("Virtual environment created. To activate it, run:")
print(".venv\\Scripts\\activate")

