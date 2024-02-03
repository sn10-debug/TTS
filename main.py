import subprocess

script_to_execute = 'inference.py'
sample_text = "ଶୁଣନ୍ତୁ ଆପଣ କେମିତି ଅଛନ୍ତି"
language = 'odia'
gender = 'male'
output_file = 'male_odia_output.wav'
conda_environment = 'tts-hs-hifigan'


try:
    subprocess.run(['conda', 'run', '-n', conda_environment, 'python', script_to_execute, '--sample_text', sample_text, '--language', language, '--gender', gender, '--output_file', output_file], check=True)
    print(f"The script '{script_to_execute}' was executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the script '{script_to_execute}': {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

