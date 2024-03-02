import subprocess
import datetime
import time

def clip_video_nvenc(input_path, output_path, output_format='mp4', crf=23, max_framerate=30, resolution='1280x720',start_time=0,duration=0):
    # Reencoding options for ffmpeg with NVENC, CRF, max framerate, and resolution
    ffmpeg_options = [
        'ffmpeg',
        '-i', input_path,
        '-c:v', 'h264_nvenc',  # NVENC H.264 video codec
        '-b:v', '1000k',  # Set bitrate to 0 for CRF mode
        '-preset', 'fast',
        # '-crf', str(crf),  # Constant Rate Factor (adjust as needed)
        '-pix_fmt', 'yuv420p',
        '-profile:v', 'baseline',
        "-ss", str(start_time),  # Start time in seconds (string format)
        "-t", str(duration),    # Duration in seconds (string format)
        #'-level', '3.0',
        '-max_muxing_queue_size', '1024',  # Control peak framerate
        '-r', str(max_framerate),  # Set max output framerate
        '-s', resolution,  # Set output resolution
        '-c:a', 'aac',  # Audio codec
        '-strict', 'experimental',  # Allow using experimental codecs (needed for some audio codecs)
        '-b:a', '128k',  # Audio bitrate
        '-movflags', '+faststart',
        '-threads', '0',# if set to 0 ffmpeg will use the max amount of threads available
        output_path,  # Output file path
    ]
    try:
        # Run the ffmpeg command
        subprocess.run(ffmpeg_options, check=True)
        print("Video clip successfully created!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to clip video. Error code: {e.returncode}")

if __name__ == "__main__":
    input_path=f"""F:\\downloads\\res2.mp4"""
    output_path=f"result/clip.mp4"
    output_format=f"mp4"
    resolution="1280x720"
    framerate=30

    start_time_hours = 5
    start_time_minutes = 5
    start_time_seconds = 15
    start_time_in_seconds = start_time_hours*3600 + start_time_minutes*60 + start_time_seconds

    duration_time_hours = 0
    duration_time_minutes = 4
    duration_time_seconds = 9
    duration_time_in_seconds = duration_time_hours*3600 + duration_time_minutes*60 + duration_time_seconds

    prev=datetime.datetime.now()
    
    clip_video_nvenc(input_path,output_path,output_format,max_framerate=framerate,start_time=start_time_in_seconds,duration=duration_time_in_seconds)
    
    now=datetime.datetime.now()
    total=(now-prev).total_seconds()
    if total>60:
        print(f"completed in {int(total//60)} minutes {int(total%60)} seconds")
    else:
        print(f"completed in {int(total)} seconds")
    