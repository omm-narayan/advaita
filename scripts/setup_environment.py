#!/usr/bin/env python3

import subprocess
import sys

def run_command(command):
    """Run shell command and handle errors"""
    try:
        result = subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running: {command}")
        return False

def main():
    print("🚀 Setting up Advaita development environment...")
    
    # Create virtual environment
    commands = [
        "python -m venv advaita_env",
        "source advaita_env/bin/activate && pip install --upgrade pip",
        "source advaita_env/bin/activate && pip install -r requirements.txt",
        "echo '✅ Environment setup complete!'",
        "echo 'Activate with: source advaita_env/bin/activate'"
    ]
    
    for cmd in commands:
        if not run_command(cmd):
            sys.exit(1)

if __name__ == "__main__":
    main()