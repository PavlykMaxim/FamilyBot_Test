import disnake as discord
import youtube_dlc

from musicbot import linkutils
from musicbot import utils

from config import config
from musicbot.playlist import Playlist
from musicbot.songinfo import Song

from musicbot.utils import guild_to_settings


class AudioController(object):
    """ Управляет воспроизведением звука и последовательным воспроизведением песен.

            Attributes:
                bot: бот, который будет проигрывать музыку.
                playlist: Объект playlist, в котором хранится история и очередь песен..
                current_song: Объект Song, в котором хранятся сведения о текущей песне..
                guild: канал в котором работает AudioController.
        """

    def __init__(self, bot, guild):
        self.bot = bot
        self.playlist = Playlist()
        self.current_song = None
        self.guild = guild
        self.voice_client = None

        sett = utils.guild_to_settings[guild]
        self._volume = sett.get('default_volume')

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        try:
            self.voice_client.source.volume = float(value) / 100.0
        except Exception as e:
            pass

    async def register_voice_channel(self, channel):
        self.voice_client = await channel.connect(reconnect=True, timeout=None)

    def track_history(self):
        history_string = config.INFO_HISTORY_TITLE
        for trackname in self.playlist.trackname_history:
            history_string += "\n" + trackname
        return history_string

    def next_song(self, error):
        """Вызывается после завершения песни. Воспроизводит следующую песню, если она есть."""

        self.current_song = None
        next_song = self.playlist.next()

        if next_song is None:
            return

        coro = self.play_song(next_song)
        self.bot.loop.create_task(coro)

    async def play_song(self, song):
        """Воспроизводит объект песни"""

        if song.origin == linkutils.Origins.Playlist:
            if song.host == linkutils.Sites.Spotify:
                conversion = await self.search_youtube(linkutils.convert_spotify(song.info.webpage_url))
                song.info.webpage_url = conversion

            downloader = youtube_dlc.YoutubeDL(
                {'format': 'bestaudio', 'title': True, "cookiefile": config.COOKIE_PATH})
            r = downloader.extract_info(
                song.info.webpage_url, download=False)

            song.base_url = r.get('url')
            song.info.uploader = r.get('uploader')
            song.info.title = r.get('title')
            song.info.duration = r.get('duration')
            song.info.webpage_url = r.get('webpage_url')
            song.info.thumbnail = r.get('thumbnails')[0]['url']

        self.playlist.add_name(song.info.title)
        self.current_song = song

        self.voice_client.play(discord.FFmpegPCMAudio(
            song.base_url, before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'), after=lambda e: self.next_song(e))

        self.voice_client.source = discord.PCMVolumeTransformer(
            self.guild.voice_client.source)
        self.voice_client.source.volume = float(self.volume) / 100.0

    async def process_song(self, track):
        """Добавляет трек в экземпляр плейлиста и проигрывает его, если это первая песня"""

        host = linkutils.identify_url(track)
        is_playlist = linkutils.identify_playlist(track)

        if is_playlist != linkutils.Playlist_Types.Unknown:

            queue_scan = len(self.playlist.playque)

            await self.process_playlist(is_playlist, track)

            if queue_scan == 0:
                await self.play_song(self.playlist.playque[0])
                print("Играет {}".format(track))

            song = Song(linkutils.Origins.Playlist,
                        linkutils.Sites.Unknown)
            return song

        if host == linkutils.Sites.Unknown:
            if linkutils.get_url(track) is not None:
                return None

            track = await self.search_youtube(track)

        if host == linkutils.Sites.Spotify:
            title = linkutils.convert_spotify(track)
            track = await self.search_youtube(title)

        if host == linkutils.Sites.YouTube:
            track = track.split("&list=")[0]

        try:
            downloader = youtube_dlc.YoutubeDL(
                {'format': 'bestaudio', 'title': True, "cookiefile": config.COOKIE_PATH})
            r = downloader.extract_info(
                track, download=False)
        except:
            downloader = youtube_dlc.YoutubeDL(
                {'title': True, "cookiefile": config.COOKIE_PATH})
            r = downloader.extract_info(
                track, download=False)

        if r.get('thumbnails') is not None:
            thumbnail = r.get('thumbnails')[len(
                r.get('thumbnails')) - 1]['url']
        else:
            thumbnail = None

        song = Song(linkutils.Origins.Default, host, base_url=r.get('url'), uploader=r.get('uploader'), title=r.get(
            'title'), duration=r.get('duration'), webpage_url=r.get('webpage_url'), thumbnail=thumbnail)

        self.playlist.add(song)
        if len(self.playlist.playque) == 1:
            print("Играет {}".format(track))
            await self.play_song(song)

        return song

    async def process_playlist(self, playlist_type, url):

        if playlist_type == linkutils.Playlist_Types.YouTube_Playlist:

            if ("playlist?list=" in url):
                listid = url.split('=')[1]
            else:
                video = url.split('&')[0]
                await self.process_song(video)
                return

            options = {
                'format': 'bestaudio/best',
                'extract_flat': True,
                "cookiefile": config.COOKIE_PATH
            }

            with youtube_dlc.YoutubeDL(options) as ydl:
                r = ydl.extract_info(url, download=False)

                for entry in r['entries']:

                    link = "https://www.youtube.com/watch?v={}".format(
                        entry['id'])

                    song = Song(linkutils.Origins.Playlist,
                                linkutils.Sites.YouTube, webpage_url=link)

                    self.playlist.add(song)

        if playlist_type == linkutils.Playlist_Types.Spotify_Playlist:
            links = linkutils.get_spotify_playlist(url)
            for link in links:
                song = Song(linkutils.Origins.Playlist,
                            linkutils.Sites.Spotify, webpage_url=link)
                self.playlist.add(song)

        if playlist_type == linkutils.Playlist_Types.BandCamp_Playlist:
            options = {
                'format': 'bestaudio/best',
                'extract_flat': True
            }
            with youtube_dlc.YoutubeDL(options) as ydl:
                r = ydl.extract_info(url, download=False)

                for entry in r['entries']:

                    link = entry.get('url')

                    song = Song(linkutils.Origins.Playlist,
                                linkutils.Sites.Bandcamp, webpage_url=link)

                    self.playlist.add(song)

    async def search_youtube(self, title):
        """Ищет на YouTube название видео и возвращает ссылку на видео с первым результатом"""

        # if title is already a link
        if linkutils.get_url(title) is not None:
            return title

        options = {
            'format': 'bestaudio/best',
            'default_search': 'auto',
            'noplaylist': True,
            "cookiefile": config.COOKIE_PATH
        }

        with youtube_dlc.YoutubeDL(options) as ydl:
            r = ydl.extract_info(title, download=False)

        videocode = r['entries'][0]['id']

        return "https://www.youtube.com/watch?v={}".format(videocode)

    async def stop_player(self):
        """Останавливает проигрыватель и удаляет все песни из очереди"""
        if self.guild.voice_client is None or (
                not self.guild.voice_client.is_paused() and not self.guild.voice_client.is_playing()):
            return
        self.playlist.next()
        self.playlist.playque.clear()
        self.guild.voice_client.stop()

    async def prev_song(self):
        """Загружает последнюю песню из истории в очередь и запускает ее"""
        if len(self.playlist.playhistory) == 0:
            return None
        if self.guild.voice_client is None or (
                not self.guild.voice_client.is_paused() and not self.guild.voice_client.is_playing()):
            prev_song = self.playlist.prev()
            # The Dummy is used if there is no song in the history
            if prev_song == "Dummy":
                self.playlist.next()
                return None
            await self.play_youtube(prev_song)
        else:
            self.playlist.prev()
            self.playlist.prev()
            self.guild.voice_client.stop()

    def clear_queue(self):
        self.playlist.playque.clear()
