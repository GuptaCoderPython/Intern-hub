#first install the pytube using pip
from pytube import YouTube

def download_video():
    url = input("Enter the YouTube URL: ")
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print("Available Streams:")
        for stream in yt.streams.filter(progressive=True).order_by('resolution'):
            print(stream)

        stream_itag = input("Enter the itag of the desired stream: ")
        stream = yt.streams.get_by_itag(stream_itag)
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("YouTube Video Downloader")
    download_video()

if __name__ == "__main__":
    main()
