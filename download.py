import os.path
import subprocess

vids = []
with open("video1.txt") as f:
    for line in f:
        code, title = line.split(" ", 1)
        title = title.strip()
        vids.append((code, title))

for code, title in vids:
    # if (any(title == title_iter and code > code_iter for code_iter, title_iter in vids)):
    #     print(code, title)
    # else:
    if 1:
        filename = f"videos/{title}-{code}.mp4"
        if not os.path.isfile(filename):
            url = subprocess.run(f"py -m youtube_dl --prefer-ffmpeg -f 22 -g {code}", stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
            command = f'ffmpeg -i "{url}" -t 00:00:30.00 -c copy "{filename}"'
            subprocess.run(command)
        subtitles_file = f"{title}-{code}.en.vtt"
        new_subtitles_file = f"subtitles/{title}-{code}.en.vtt"
        if not os.path.isfile(new_subtitles_file):
            proc = subprocess.run(f"py -m youtube_dl --skip-download --sub-lang en --sub-format vtt --write-auto-sub {code}")
            if os.path.isfile(subtitles_file):
                os.rename(subtitles_file, new_subtitles_file)
            else:
                print(f"Subtitle download failed for {code}-{title}")

# subprocess.run(f"ffmpeg -i \"{url}\" -t 00:00:10.00 -c copy out.mp4")
