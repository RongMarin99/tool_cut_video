from moviepy.editor import VideoFileClip, VideoClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.fx import mirror_x
import os
import glob
import pyfiglet

text = pyfiglet.figlet_format("Welcome")
print(text)
print("\t\t[1]. Cut Video")
ch = int(input("Enter Number : "))
match ch:
    case 1:
        segment_times = [(0, 10), (15, 30), (35, 50)]
        folder_path = './videos'
        output_folder = './edited'
        video_files = glob.glob(os.path.join(folder_path, "*.mp4"))
        # Loop through video files, extract segments, and save as separate video files
        for video_file in video_files:
            video_filename = os.path.basename(video_file)
            for i, (start_time, end_time) in enumerate(segment_times):
                output_video = f"output_{video_filename}__{i}.mp4"
                output_path = os.path.join(output_folder, output_video)
                ffmpeg_extract_subclip(
                    video_file, start_time, end_time, targetname=output_path)

                # Edit the video (e.g., flip it horizontally)
                clip = VideoFileClip(output_path).rotate(360)
                # edited_clip = clip.fx(VideoClip.fx.vfx.mirror_x)

                # Write the edited clip to the edited folder
                clip.write_videofile(output_path)
                # edited_clip.write_videofile(output_path)

        # video_filenames = [os.path.basename(file) for file in video_files]
        # print(video_filenames)
        # print("Welcome to Cut Video Tool")

        # segment_times = [(0, 10), (15, 30), (35, 50)]
        # for input_video, segment_times in video_filenames:
        #     for i, (start_time, end_time) in enumerate(segment_times):
        #         output_video = f"{os.path.splitext(input_video)[0]}_segment_{i}.mp4"
        #         ffmpeg_extract_subclip(
        #             input_video, start_time, end_time, targetname=output_video)

        # start_time = int(input("Enter Start Time: "))
        # end_time = int(input("Enter End Time : "))
        # ffmpeg_extract_subclip("test.mp4", start_time,
        #                        end_time, targetname='output_video.mp4')
        # clip = VideoFileClip('test.mp4').rotate(180)
        # clip.write_videofile('output_video.mp4', codec='libx264')
    case default:
        print("Invalid NUmber Not Found!")
