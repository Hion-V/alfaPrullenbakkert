#from ctypes import cast, POINTER
#from comtypes import CLSCTX_ALL
#from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from gtts import gTTS
import os
import mpg123
# define variables
s = "Smerige kankerjunk"
file = "file.mp3"


#devices = AudioUtilities.GetSpeakers()
#interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.SetMasterVolumeLevel(-20, None)


# initialize tts, create mp3 and play
tts = gTTS(s, 'nl')
tts.save(file)
os.system("mpg123 " + file)
