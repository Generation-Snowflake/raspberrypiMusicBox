import alsaaudio

scan = alsaaudio.cards()
print("cards:", scan)
for card in scan:
    scanMixers = alsaaudio.mixers(scan.index(card))
    print("mixers:", scanMixers)

m = alsaaudio.Mixer('Headphones')
current_volume = m.getvolume()
print(current_volume)
m.setvolume(100)
print(current_volume)
