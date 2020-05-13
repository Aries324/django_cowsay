import subprocess


def get_text(text):
    user_text = subprocess.check_output(str(text), shell=True)
    return user_text