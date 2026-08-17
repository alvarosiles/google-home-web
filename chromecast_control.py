"""
Control de Google Home / Chromecast: reproducir audio y enviar comandos.

Instalacion:
    pip install pychromecast

Uso:
    python chromecast_control.py --list
    python chromecast_control.py --device "Sala" --play "https://ejemplo.com/audio.mp3"
    python chromecast_control.py --device "Sala" --pause
    python chromecast_control.py --device "Sala" --resume
    python chromecast_control.py --device "Sala" --stop
    python chromecast_control.py --device "Sala" --volume 0.5
"""

import argparse
import sys
import time

import pychromecast


def list_devices():
    chromecasts, browser = pychromecast.get_chromecasts()
    for cc in chromecasts:
        print(f"- {cc.name}  ({cc.cast_info.host}:{cc.cast_info.port})")
    pychromecast.discovery.stop_discovery(browser)


def get_device(name: str):
    chromecasts, browser = pychromecast.get_chromecasts()
    match = next((cc for cc in chromecasts if cc.name.lower() == name.lower()), None)
    if not match:
        pychromecast.discovery.stop_discovery(browser)
        print(f"No se encontro el dispositivo '{name}'. Usa --list para ver los disponibles.")
        sys.exit(1)
    match.wait()
    return match, browser


def main():
    parser = argparse.ArgumentParser(description="Controla un Google Home / Chromecast")
    parser.add_argument("--device", help="Nombre del dispositivo (como aparece en --list)")
    parser.add_argument("--list", action="store_true", help="Lista los dispositivos disponibles")
    parser.add_argument("--play", metavar="URL", help="Reproduce el audio/stream en la URL indicada")
    parser.add_argument("--pause", action="store_true", help="Pausa la reproduccion")
    parser.add_argument("--resume", action="store_true", help="Reanuda la reproduccion")
    parser.add_argument("--stop", action="store_true", help="Detiene la reproduccion")
    parser.add_argument("--volume", type=float, metavar="0.0-1.0", help="Ajusta el volumen")
    args = parser.parse_args()

    if args.list:
        list_devices()
        return

    if not args.device:
        parser.error("--device es requerido (salvo con --list)")

    cast, browser = get_device(args.device)
    mc = cast.media_controller

    try:
        if args.play:
            cast.play_media(args.play, "audio/mp3")
            mc.block_until_active(timeout=10)
            print(f"Reproduciendo en {cast.name}: {args.play}")
        if args.pause:
            mc.pause()
            print("Pausado")
        if args.resume:
            mc.play()
            print("Reanudado")
        if args.stop:
            mc.stop()
            print("Detenido")
        if args.volume is not None:
            cast.set_volume(max(0.0, min(1.0, args.volume)))
            print(f"Volumen ajustado a {args.volume}")
    finally:
        time.sleep(1)
        pychromecast.discovery.stop_discovery(browser)


if __name__ == "__main__":
    main()
