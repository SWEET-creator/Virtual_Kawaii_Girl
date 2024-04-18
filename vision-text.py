import threading
import vision
import core

def handle_camera_stream():
    vision.main()

def handle_voice_interaction():
    core.main()


# Creating threads
thread_voice = threading.Thread(target=handle_voice_interaction)
thread_camera = threading.Thread(target=handle_camera_stream)

# Starting threads
thread_voice.start()
thread_camera.start()

# Joining threads to wait for them to finish
thread_voice.join()
thread_camera.join()