import os
import shutil

def setup_directories():
    """Create necessary directories if they don't exist."""
    dirs = ['temp', 'output', 'assets']
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
    print("Directories initialized: temp, output, assets")

def clear_temp():
    """Clear the temp directory after use."""
    if os.path.exists('temp'):
        shutil.rmtree('temp')
        os.makedirs('temp')
    print("Temp directory cleared.")

def get_temp_path(filename):
    """Return path for a file in temp directory."""
    return os.path.join('temp', filename)

def get_output_path(filename):
    """Return path for a file in output directory."""
    return os.path.join('output', filename)
