from flask import Flask, send_file, render_template,request,send_from_directory,send_file
import subprocess
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_form', methods=['POST'])
def process_form():
    
    sample_text = request.form.get('sample_text')
    gender = request.form.get('gender')

 
    result_message = f"Text: {sample_text}, Gender: {gender}"
    print(result_message)


    script_to_execute = 'inference.py'
    language = 'odia'
    output_file = 'male_odia_output.wav'
    conda_environment = 'tts-hs-hifigan'


    try:

        subprocess.run(['conda', 'run', '-n', conda_environment, 'python', script_to_execute, '--sample_text', sample_text, '--language', language, '--gender', gender, '--output_file', output_file], check=True)
        print(f"The script '{script_to_execute}' was executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script '{script_to_execute}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return render_template('completed.html')

@app.route('/get_audio', methods=['GET'])
def get_audio():
    audio_file_path = 'male_odia_output.wav'
    
    content_type = 'audio/wav'

    return send_file(audio_file_path, mimetype=content_type, as_attachment=True)

@app.route('/stream/<filename>')
def stream_file(filename):
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
