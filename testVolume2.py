import alsaaudio

volume = alsaaudio.Mixer()
current_volume = volume.getvolume()
volume.setvolume(100)
