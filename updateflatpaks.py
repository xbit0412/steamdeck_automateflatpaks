#!/usr/bin/env python3
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e}")

commands = [
    "flatpak update --noninteractive --assumeyes",
    "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo",
    "flatpak install flathub com.anydesk.Anydesk --assumeyes",
    "flatpak install flathub io.github.peazip.PeaZip --assumeyes",
    "flatpak install flathub org.qbittorrent.qBittorrent --assumeyes",
    "flatpak install flathub net.davidotek.pupgui2 --assumeyes",
    "flatpak install flathub com.github.Matoking.protontricks --assumeyes",
    "flatpak install flathub com.heroicgameslauncher.hgl --assumeyes",
    "flatpak install flathub org.wireshark.Wireshark --assumeyes",
    "flatpak install flathub net.lutris.Lutris --assumeyes",
    "flatpak install flathub com.usebottles.bottles --assumeyes",
    "flatpak install flathub org.audacityteam.Audacity --assumeyes",
    "flatpak install flathub org.mozilla.Thunderbird --assumeyes",
    "flatpak install flathub com.ulduzsoft.Birdtray --assumeyes",
    "flatpak install flathub org.onlyoffice.desktopeditors --assumeyes",
    "flatpak install flathub org.libreoffice.LibreOffice --assumeyes",
    "flatpak install flathub org.videolan.VLC --assumeyes",
    "flatpak install flathub org.kde.haruna --assumeyes",
    "flatpak install flathub com.microsoft.Edge --assumeyes",
    "flatpak install flathub com.obsproject.Studio --assumeyes",
    "flatpak install flathub org.gimp.GIMP --assumeyes",
    "flatpak install flathub io.github.hakandundar34coding.system-monitoring-center --assumeyes",
    "flatpak install flathub com.leinardi.gst --assumeyes",
    "flatpak install flathub com.ulduzsoft.Birdtray --assumeyes",
    "flatpak install flathub com.brave.Browser --assumeyes",
    "flatpak install flathub com.steamgriddb.SGDBoop --assumeyes",
    "flatpak install flathub com.visualstudio.code --assumeyes",
    "flatpak install flathub com.bitwarden.desktop --assumeyes",
    "flatpak install flathub org.blender.Blender --assumeyes",
    "flatpak install flathub com.discordapp.Discord --assumeyes",
    "flatpak install flathub org.duckstation.DuckStation --assumeyes",
    "flatpak install flathub net.pcsx2.PCSX2 --assumeyes",
    "flatpak install flathub org.mozilla.firefox --assumeyes",
    "flatpak install flathub com.github.tchx84.Flatseal --assumeyes",
    "flatpak install flathub com.google.Chrome --assumeyes",
    "flatpak install flathub org.libretro.RetroArch --assumeyes",
    "flatpak install flathub net.rpcs3.RPCS3 --assumeyes",
    "flatpak install flathub com.spotify.Client --assumeyes",
    "flatpak install flathub org.telegram.desktop --assumeyes",
    "flatpak install flathub org.gnome.Weather --assumeyes"
]

# Run each command
for command in commands:
    run_command(command)

# Print success message
# print("Flatpaks installed and updated")

# Notify the user (for Linux systems, you can use the 'notify-send')
subprocess.run(['notify-send', "Flatpaks installed and or updated"])