import psutil

def kill_vlc():
    for proc in psutil.process_iter():
        if "vlc" in proc.name().lower() or "vlc.exe" in proc.name().lower():
            try:
                proc.terminate()  # Try terminating
                print("VLC media player terminated successfully.")
            except psutil.NoSuchProcess:
                pass  # Process might have terminated just before we tried to terminate it
            except Exception as e:
                print(f"Error occurred while terminating VLC: {e}")
    else:
        print("VLC media player is not running.")

if __name__ == "__main__":
    kill_vlc()