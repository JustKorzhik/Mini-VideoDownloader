import importlib
import yt_dlp

def checkImport(name):
    try:
        importlib.import_module(name)
        return True
    except ImportError:
        return False
    
def downloadVideo(url, path, height=720):
    ydl_opts = {
        'format': f'bestvideo[height<={height}]+bestaudio[acodec!=opus]',
        'outtmpl': f'{path}\\%(title).100s.%(ext)s',
        'merge_output_format': 'mp4',
        'windowsfilenames': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'forcemerge': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def checkVideo(url):
    ydl_opts = {
        'compat_opts': ['youtube-skip-nsig-check'],
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return f"Название: {info['title']}\nАвтор: {info['uploader']}\nДлительность: {info['duration']}\n"