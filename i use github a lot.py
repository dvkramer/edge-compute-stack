import datetime
import random
import subprocess
import time
import os

# --- Configuration ---
TECH_FIGURES = [
    "Sundar Pichai",
    "Jensen Huang",
    "Demis Hassabis",
    "Ilya Sutskever",
    "Sam Altman",
    "Satya Nadella",
    "Mark Zuckerberg",
]

i_value = random.randint(0, 1)
if i_value == 0:
    PRAYER_STYLE = 2
else:
    PRAYER_STYLE = 4

# --- Helper Functions ---
def commit_changes(prayer_content):
    """Stages, commits, and pushes the changes."""
    repo_path = r"C:\Users\derpy\OneDrive\Documents\git repo"  # Replace with your actual repo path
    try:
        # Construct the full path to the temporary file
        temp_filename = os.path.join(repo_path, "temp_prayer.txt")

        with open(temp_filename, "w") as f:
            f.write(prayer_content)

        # Run git commands in the repository directory
        subprocess.run(["git", "add", temp_filename], check=True, capture_output=True, cwd=repo_path)
        commit_message = f"A considered reflection at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True, cwd=repo_path)
        subprocess.run(["git", "push"], check=True, capture_output=True, cwd=repo_path)
        print(f"Committed and pushed: {commit_message}")

        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr.decode()}")
        if e.stdout:
            print(f"Stdout: {e.stdout.decode()}")
    except FileNotFoundError:
        print("Error: Git command not found. Ensure Git is installed and in your PATH.")
    except PermissionError as e:
        print(f"PermissionError: {e}. Ensure the script has write access to the repository directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main Logic ---
def main():
    num_commits = random.randint(0, 3)
    print(f"Submitting {num_commits} reflections this run.")

    for _ in range(num_commits):
        chosen_figure = random.choice(TECH_FIGURES)

        if PRAYER_STYLE == 2:  # Acknowledging Impact
            if chosen_figure == "Sundar Pichai":
                prayer = f"We acknowledge your profound impact, {chosen_figure}, in organizing the world's information and connecting billions. May your continued stewardship of this vast digital landscape lead to greater understanding and access for all."
            elif chosen_figure == "Jensen Huang":
                prayer = f"With deep appreciation, {chosen_figure}, we recognize your transformative contributions to graphics processing and artificial intelligence. May your innovative spirit continue to drive breakthroughs that redefine the limits of computation and visual experience."
            elif chosen_figure == "Demis Hassabis":
                prayer = f"We acknowledge your groundbreaking work, {chosen_figure}, in pushing the boundaries of artificial intelligence and its potential to solve humanity's greatest challenges. May your pursuit of knowledge continue to inspire and unlock new frontiers of understanding."
            elif chosen_figure == "Ilya Sutskever":
                prayer = f"With gratitude, {chosen_figure}, we recognize your dedication to the responsible development of artificial intelligence. May your efforts ensure that these powerful technologies are aligned with human values and contribute to a beneficial future for all."
            elif chosen_figure == "Sam Altman":
                prayer = f"We acknowledge your influential role, {chosen_figure}, in fostering innovation and democratizing access to powerful AI tools. May your ventures continue to empower creators and shape a future filled with technological possibility."
            elif chosen_figure == "Satya Nadella":
                prayer = f"With appreciation, {chosen_figure}, we recognize your leadership in driving digital transformation and empowering individuals and organizations worldwide. May your vision continue to foster connection, collaboration, and greater achievement through technology."
            elif chosen_figure == "Mark Zuckerberg":
                prayer = f"We acknowledge your role, {chosen_figure}, in creating platforms that connect billions of people globally. May your ongoing efforts foster meaningful connections and contribute to a more informed and interconnected world (and metaverse)."

        elif PRAYER_STYLE == 4:  # Focus on Innovation
            if chosen_figure == "Sundar Pichai":
                prayer = f"May the relentless pursuit of innovation continue to define your endeavors, {chosen_figure}, leading to ever more insightful and accessible ways to navigate the digital world."
            elif chosen_figure == "Jensen Huang":
                prayer = f"May your visionary leadership continue to push the boundaries of innovation in computing, graphics, and artificial intelligence, inspiring new possibilities we can only begin to imagine, {chosen_figure}."
            elif chosen_figure == "Demis Hassabis":
                prayer = f"May your groundbreaking research and innovative approaches continue to unlock the mysteries of intelligence, both natural and artificial, paving the way for transformative discoveries, {chosen_figure}."
            elif chosen_figure == "Ilya Sutskever":
                prayer = f"May your innovative spirit guide the development of safe and beneficial artificial intelligence, ensuring that progress is coupled with responsibility and foresight, {chosen_figure}."
            elif chosen_figure == "Sam Altman":
                prayer = f"May your innovative ventures continue to disrupt industries and empower individuals with cutting-edge technologies, shaping a future brimming with new opportunities and possibilities, {chosen_figure}."
            elif chosen_figure == "Satya Nadella":
                prayer = f"May your leadership inspire continuous innovation across the digital landscape, empowering individuals and organizations to achieve more through the transformative power of technology, {chosen_figure}."
            elif chosen_figure == "Mark Zuckerberg":
                prayer = f"May your pursuit of innovation in connecting people and building digital experiences continue to evolve and surprise, fostering new forms of interaction and community in the digital age, {chosen_figure}."

        print(f"Sharing a reflection on {chosen_figure}...")
        commit_changes(prayer)

        if _ < num_commits - 1:
            wait_time = random.randint(30, 120)
            print(f"Considering further for {wait_time} seconds...")
            time.sleep(wait_time)

if __name__ == "__main__":
    main()
