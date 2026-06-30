"""
Runs a project's original .py file exactly as if you typed `python script.py`
in its own folder - no imports, no modification, no awareness it's being
called from Streamlit.

How it works:
1. Copies the project's folder into a temp directory (so the script's own
   relative file reads/writes don't touch your real repo).
2. Drops the uploaded file into that temp directory as the filename the
   script expects (e.g. "file.txt").
3. Runs the script with that temp directory as the working directory.
4. Reads back whatever output file the script wrote (e.g. "word_counts.json")
   and returns it.
"""

import subprocess
import shutil
import tempfile
import os


def run_script_with_file_io(
    project_folder: str,
    script_filename: str,
    uploaded_file_bytes: bytes,
    input_filename: str,
    output_filename: str,
    timeout_seconds: int = 15,
):
    """
    Returns (success: bool, stdout: str, stderr: str, output_bytes: bytes | None)
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Copy the whole project folder so any other files the script expects are present
        for item in os.listdir(project_folder):
            src = os.path.join(project_folder, item)
            dst = os.path.join(tmp_dir, item)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        # Drop the uploaded file in as the expected input filename
        with open(os.path.join(tmp_dir, input_filename), "wb") as f:
            f.write(uploaded_file_bytes)

        try:
            result = subprocess.run(
                ["python3", script_filename],
                cwd=tmp_dir,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return False, "", "Script timed out.", None

        output_path = os.path.join(tmp_dir, output_filename)
        output_bytes = None
        if os.path.exists(output_path):
            with open(output_path, "rb") as f:
                output_bytes = f.read()

        success = result.returncode == 0 and output_bytes is not None
        return success, result.stdout, result.stderr, output_bytes
