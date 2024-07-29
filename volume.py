from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re
import comtypes


def set_volume(volume_level):
    comtypes.CoInitialize()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)
    comtypes.CoUninitialize()

def extract_volume_percentage(command):
    match = re.search(r'(\d+)', command)
    
    if match:
        percentage = int(match.group(1))
        if percentage>100:
           percentage = 100
           volume_value = percentage / 100.0
        else:
           volume_value = percentage / 100.0
        return volume_value
    else:
        return None
