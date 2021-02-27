import pyaudio
import sys
import wave
import numpy as np
import time
import concurrent.futures
import random
import pygame

frame_rate = 0.05
chunk_size = 1024
height = 4320
width = 7680

pygame.init()

win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

pygame.display.set_caption("Twisted Visualiser")


class Audio_Data:

    frames = 0
    all_frames = 0
    rate = 0
    channels = 0
    wf = ""
    audio_array = []
    visualised_chunk = []
    array_width = len(visualised_chunk)

    def __init__(self, filename, chunk, timer):
        self.filename = filename
        self.chunk = chunk
        self.timer = timer

        self.wf = wave.open(self.filename, "rb")
        self.frames = self.wf.getnframes()
        self.all_frames = self.wf.readframes(self.frames)
        self.rate = self.wf.getframerate()
        self.channels = self.wf.getnchannels()
        self.wf.close()
        self.wf = ""

    def play_til_end(self):
        self.wf = wave.open(self.filename, "rb")
        p = pyaudio.PyAudio()
        stream = p.open(
            format=p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.channels,
            rate=self.rate,
            output=True,
        )
        data = self.wf.readframes(self.chunk)
        try:
            count = 0
            while data != "":
                stream.write(data)
                data = self.wf.readframes(self.chunk)
                x = 50
                y = 50
                global width
                audio_array = np.frombuffer(data, dtype=np.uint8)
                # new_width = int(len(audio_array) * 0.25)
                # print(audio_array)
                for position in range(0, len(audio_array) - 6, 6):
                    """if count % 2 == 0:
                    pygame.draw.rect(
                        win,
                        (
                            audio_array[position * 3 + 3],
                            audio_array[position * 4],
                            audio_array[position * 4 - 20],
                        ),
                        (
                            position / new_width * width * 100,
                            600,
                            new_width / width * 10,
                            audio_array[position] / 255 * height * 5,
                        ),
                    )"""
                    """if (
                        audio_array[position * 4] > 25
                        and audio_array[position * 4] < 225
                    ) and count % 2 == 0:"""
                    pygame.draw.circle(
                        win,
                        (
                            audio_array[position],
                            audio_array[position + 1],
                            audio_array[position + 2],
                        ),
                        (
                            audio_array[position + 3] / 255 * position,
                            audio_array[position + 4] / 255 * height,
                        ),
                        audio_array[position + 5] / 255 * width / 50,
                    )

                pygame.display.update()
                pygame.image.save(win, f"{count}.png")
                win.fill((255, 255, 255))

                """if count % 8 == 0 and (
                    (audio_array[512] > 100 and audio_array[512] > 200)
                    or (audio_array[1024] > 100 and audio_array[1024] > 200)
                ):
                    win.fill(
                        (
                            audio_array[512],
                            1,
                            audio_array[1024],
                        )
                    )"""
                count += 1

        except KeyboardInterrupt:
            stream.close()
            p.terminate


file_data = Audio_Data("Twisted Remix Demo 1.wav", 1837, frame_rate)

file_data.play_til_end()
