import os
import numpy as np
from PIL import Image as PILImage
from moviepy import VideoFileClip, ImageSequenceClip

def gif_to_video(gif_path, output_path):
    try:
        img = PILImage.open(gif_path)
        frames = []

        if not getattr(img, 'is_animated', False):
            return None

        for i in range(img.n_frames):
            img.seek(i)
            frames.append(np.array(img.convert('RGB')))

        duration = img.info.get('duration', 100) / 1000.0
        fps = 1.0 / duration if duration > 0 else 10

        clip = ImageSequenceClip(frames, fps=fps)
        clip.write_videofile(output_path, codec='libx264', audio=False, logger=None)
        clip.close()

        return output_path
    except Exception as e:
        print(f" GIF to video error: {e}")
        return None


def extract_video_frame(video_path, output_image, time_sec=0.5):
    try:
        clip = VideoFileClip(video_path)
        t = min(time_sec, clip.duration / 2)
        clip.save_frame(output_image, t=t)
        clip.close()
        return output_image
    except Exception:
        return None
