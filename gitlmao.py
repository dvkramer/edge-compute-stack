import datetime
import random
import subprocess
import time

# --- Helper Functions ---

def commit_changes():
    """Stages, commits, and pushes the changes."""
    try:
        # Stage all changes in the current directory
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        commit_message = f"Random commit at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True)
        # Uncomment the line below if you want the script to also push the commits
        # subprocess.run(["git", "push"], check=True, capture_output=True)
        print(f"Committed: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr.decode()}")
        if e.stdout:
            print(f"Stdout: {e.stdout.decode()}")
    except FileNotFoundError:
        print("Error: Git command not found. Make sure Git is installed and in your PATH.")

# --- Main Logic ---

def main():
    num_commits = random.randint(0, 3)
    print(f"Making {num_commits} commits this run.")

    for i in range(num_commits):
        # Make a small change (you can customize this)
        # For example, you could create a temporary file or modify an existing one
        # Here's a simple example of creating and deleting a temporary file:
        temp_filename = f"temp_commit_file_{i}.txt"
        try:
            with open(temp_filename, "w") as f:
                f.write(f"This is a temporary file for commit {i} at {datetime.datetime.now()}")
            commit_changes()
        finally:
            import os
            try:
                os.remove(temp_filename)
            except FileNotFoundError:
                pass  # It's okay if the file wasn't created for some reason

        if i < num_commits - 1:
            wait_time = random.randint(30, 60)  # Wait between 30 to 60 seconds
            print(f"Waiting {wait_time} seconds before the next commit...")
            time.sleep(wait_time)

if __name__ == "__main__":
    main()