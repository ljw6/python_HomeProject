import pyaudio
import logging as log
import wave
import logging as log
log.basicConfig(level=log.INFO,
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
def get_audio():
    Chunk = 1024
    Format = pyaudio.paInt16
    Channels = 2
    Rate = 16000
    Record_seconds = 10#时长
    Wave_Output_Filename = "out.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=Format,
                    channels=Channels,
                    rate=Rate,
                    input=True,
                    frames_per_buffer=Chunk)
    print("开始录音")
    frames=[]#将要写入二进制文本数据(hex表示)
    for i in range(0,int(Rate / Chunk * Record_seconds)):
        data=stream.read(Chunk)
        frames.append(data)
    print("录音结束")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(Wave_Output_Filename,"wb")
    wf.setnchannels(Channels)
    wf.setsampwidth(p.get_sample_size(Format))
    wf.setframerate(Rate)
    wf.writeframes(b''.join(frames))
    wf.close()
if __name__=="__main__":
    get_audio()