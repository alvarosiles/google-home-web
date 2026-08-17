"""
Pagina web para enviar un link de audio y reproducirlo en el Google Home Mini.

Instalacion:
    pip install flask pychromecast

Uso:
    python web_app.py
    Abre http://localhost:5000 en el navegador (o http://<IP-de-esta-PC>:5000 desde el celular)
"""

from flask import Flask, request, jsonify, render_template_string, send_file
from gtts import gTTS
import json
import os
import pychromecast
import re
import socket
import threading
import yt_dlp

app = Flask(__name__)

DEVICE_NAME = "Home"
_lock = threading.Lock()
_last_status = {"message": "Listo", "ok": True}

COMMANDS_FILE = os.path.join(os.path.dirname(__file__), "commands.json")

DEFAULT_COMMANDS = {
    "quien_es_mi_novia": {
        "phrase": "¿quién es mi novia?",
        "type": "speak",
        "text": "Se llama Julieta Siles",
    },
    "musica_romantica": {
        "phrase": "ponme música romántica",
        "type": "play",
        "url": "https://www.youtube.com/watch?v=YkuCkRtoZ1k&list=RDYkuCkRtoZ1k",
    },
}


def _load_commands() -> dict:
    if not os.path.exists(COMMANDS_FILE):
        _save_commands(DEFAULT_COMMANDS)
        return dict(DEFAULT_COMMANDS)
    with open(COMMANDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_commands(commands: dict) -> None:
    with open(COMMANDS_FILE, "w", encoding="utf-8") as f:
        json.dump(commands, f, ensure_ascii=False, indent=2)


def _slugify(phrase: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", phrase.strip().lower())
    return slug.strip("_") or "comando"


def _local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

PAGE = """
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reproducir en Google Home</title>
<style>
  body { font-family: system-ui, sans-serif; max-width: 480px; margin: 40px auto; padding: 0 16px; }
  h1 { font-size: 1.4rem; }
  input[type=url] { width: 100%; padding: 10px; font-size: 1rem; box-sizing: border-box; margin-bottom: 12px; }
  button { padding: 10px 16px; font-size: 1rem; margin-right: 8px; margin-bottom: 8px; cursor: pointer; }
  #status { margin-top: 16px; padding: 10px; border-radius: 6px; background: #eee; }
  .ok { background: #d4edda; }
  .err { background: #f8d7da; }
  h2 { font-size: 1.1rem; margin-top: 32px; }
  .cmd-row { display: flex; gap: 6px; margin-bottom: 8px; align-items: center; }
  .cmd-row span { flex: 1; }
  input[type=text], select { width: 100%; padding: 8px; font-size: 0.95rem; box-sizing: border-box; margin-bottom: 8px; }
  label { font-size: 0.85rem; color: #555; display: block; }
</style>
</head>
<body>
  <h1>🎵 Reproducir en {{ device }}</h1>
  <input type="url" id="url" placeholder="Link de audio o de YouTube" value="https://www.youtube.com/watch?v=PCGLiujm6Ag">
  <button onclick="playAudio()">▶ Reproducir</button>
  <button onclick="control('pause')">⏸ Pausar</button>
  <button onclick="control('resume')">⏵ Reanudar</button>
  <button onclick="control('stop')">⏹ Detener</button>
  <div id="status">Listo</div>

  <h2>Comandos</h2>
  <div id="cmdList">
  {% for key, cmd in commands.items() %}
  <div class="cmd-row" data-key="{{ key }}">
    <span>🎤 "OK Google, {{ cmd.phrase }}" → {{ '💬 ' + cmd.text if cmd.type == 'speak' else '🎵 musica' }}</span>
    <button onclick="runCommand('{{ key }}')">▶</button>
    <button onclick="deleteCommand('{{ key }}')">🗑</button>
  </div>
  {% endfor %}
  </div>

  <h2>Crear rutina</h2>
  <label>Persona dice</label>
  <input type="text" id="phrase" placeholder='ej: "quién es mi novia"'>

  <label>Google hace</label>
  <select id="actionType" onchange="toggleActionFields()">
    <option value="speak">💬 Hablar una respuesta</option>
    <option value="play">🎵 Reproducir musica/audio</option>
  </select>

  <div id="speakFields">
    <label>Google responde</label>
    <input type="text" id="response" placeholder='ej: "Se llama Julieta Siles"'>
  </div>

  <div id="playFields" style="display:none">
    <label>Link de YouTube o audio</label>
    <input type="text" id="routineUrl" placeholder="https://www.youtube.com/watch?v=...">
  </div>

  <button onclick="saveCommand()">💾 Crear / Actualizar rutina</button>

<script>
async function call(path, body) {
  const statusEl = document.getElementById('status');
  statusEl.textContent = 'Enviando...';
  statusEl.className = '';
  try {
    const res = await fetch(path, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body || {})
    });
    const data = await res.json();
    statusEl.textContent = data.message;
    statusEl.className = data.ok ? 'ok' : 'err';
  } catch (e) {
    statusEl.textContent = 'Error: ' + e;
    statusEl.className = 'err';
  }
}

function playAudio() {
  const url = document.getElementById('url').value.trim();
  if (!url) { alert('Ingresa un link'); return; }
  call('/play', {url});
}

function control(action) {
  call('/control', {action});
}

function runCommand(key) {
  call('/command', {key});
}

function toggleActionFields() {
  const type = document.getElementById('actionType').value;
  document.getElementById('speakFields').style.display = type === 'speak' ? 'block' : 'none';
  document.getElementById('playFields').style.display = type === 'play' ? 'block' : 'none';
}

function renderCommands(commands) {
  const list = document.getElementById('cmdList');
  list.innerHTML = '';
  for (const [key, cmd] of Object.entries(commands)) {
    const row = document.createElement('div');
    row.className = 'cmd-row';
    const responsePreview = cmd.type === 'speak' ? ('💬 ' + cmd.text) : '🎵 musica';
    row.innerHTML = `
      <span>🎤 "OK Google, ${cmd.phrase}" → ${responsePreview}</span>
      <button onclick="runCommand('${key}')">▶</button>
      <button onclick="deleteCommand('${key}')">🗑</button>
    `;
    list.appendChild(row);
  }
}

async function saveCommand() {
  const phrase = document.getElementById('phrase').value.trim();
  const type = document.getElementById('actionType').value;
  const response = document.getElementById('response').value.trim();
  const routineUrl = document.getElementById('routineUrl').value.trim();

  if (!phrase) { alert('Ingresa la frase'); return; }
  if (type === 'speak' && !response) { alert('Ingresa la respuesta de Google'); return; }
  if (type === 'play' && !routineUrl) { alert('Ingresa el link de audio/YouTube'); return; }

  const statusEl = document.getElementById('status');
  statusEl.textContent = 'Guardando...';
  try {
    const res = await fetch('/save_command', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({phrase, type, response, url: routineUrl})
    });
    const data = await res.json();
    statusEl.textContent = data.message;
    statusEl.className = data.ok ? 'ok' : 'err';
    if (data.ok) {
      renderCommands(data.commands);
      document.getElementById('phrase').value = '';
      document.getElementById('response').value = '';
      document.getElementById('routineUrl').value = '';
    }
  } catch (e) {
    statusEl.textContent = 'Error: ' + e;
    statusEl.className = 'err';
  }
}

async function deleteCommand(key) {
  const statusEl = document.getElementById('status');
  try {
    const res = await fetch('/delete_command', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({key})
    });
    const data = await res.json();
    statusEl.textContent = data.message;
    statusEl.className = data.ok ? 'ok' : 'err';
    if (data.ok) renderCommands(data.commands);
  } catch (e) {
    statusEl.textContent = 'Error: ' + e;
    statusEl.className = 'err';
  }
}
</script>
</body>
</html>
"""


YOUTUBE_ID_RE = re.compile(
    r"(?:youtube\.com/watch\?v=|youtube\.com/shorts/|youtu\.be/)([\w-]{11})"
)


def _extract_youtube_id(url: str) -> str | None:
    match = YOUTUBE_ID_RE.search(url)
    return match.group(1) if match else None


def _extract_youtube_audio_url(url: str) -> tuple[str, str]:
    """Devuelve (url_directa_de_audio, titulo) usando yt-dlp."""
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
        "extractor_args": {"youtube": {"player_client": ["android"]}},
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info["url"], info.get("title", "")


_cast = None
_browser = None


def _get_device():
    """Reutiliza la conexion existente al dispositivo; solo redescubre si hace falta."""
    global _cast, _browser
    if _cast is not None and _cast.socket_client.is_connected:
        return _cast

    chromecasts, browser = pychromecast.get_chromecasts()
    match = next((cc for cc in chromecasts if cc.name.lower() == DEVICE_NAME.lower()), None)
    if not match:
        pychromecast.discovery.stop_discovery(browser)
        return None
    match.wait()
    pychromecast.discovery.stop_discovery(browser)
    _cast = match
    return _cast


@app.route("/")
def index():
    return render_template_string(PAGE, device=DEVICE_NAME, commands=_load_commands())


@app.route("/tts/<text_id>.mp3")
def tts(text_id):
    text = _load_commands().get(text_id, {}).get("text")
    if not text:
        return "No encontrado", 404
    path = f"tts_{text_id}.mp3"
    gTTS(text=text, lang="es").save(path)
    return send_file(path, mimetype="audio/mpeg")


@app.route("/save_command", methods=["POST"])
def save_command():
    data = request.json or {}
    phrase = data.get("phrase", "").strip()
    action_type = data.get("type", "speak").strip()
    response = data.get("response", "").strip()
    url = data.get("url", "").strip()

    if not phrase:
        return jsonify(ok=False, message="Falta la frase")
    if action_type == "speak" and not response:
        return jsonify(ok=False, message="Falta la respuesta de Google")
    if action_type == "play" and not url:
        return jsonify(ok=False, message="Falta el link de audio/YouTube")

    commands = _load_commands()
    key = _slugify(phrase)
    if action_type == "play":
        commands[key] = {"phrase": phrase, "type": "play", "url": url}
    else:
        commands[key] = {"phrase": phrase, "type": "speak", "text": response}
    _save_commands(commands)
    tts_path = os.path.join(os.path.dirname(__file__), f"tts_{key}.mp3")
    if os.path.exists(tts_path):
        os.remove(tts_path)
    return jsonify(ok=True, message="Rutina guardada", commands=commands)


@app.route("/delete_command", methods=["POST"])
def delete_command():
    key = (request.json or {}).get("key", "")
    commands = _load_commands()
    if key in commands:
        del commands[key]
        _save_commands(commands)
        tts_path = os.path.join(os.path.dirname(__file__), f"tts_{key}.mp3")
        if os.path.exists(tts_path):
            os.remove(tts_path)
    return jsonify(ok=True, message="Comando eliminado", commands=commands)


@app.route("/command", methods=["POST"])
def command():
    key = (request.json or {}).get("key", "")
    cmd = _load_commands().get(key)
    if not cmd:
        return jsonify(ok=False, message="Comando desconocido")

    with _lock:
        cast = _get_device()
        if not cast:
            return jsonify(ok=False, message=f"No se encontro el dispositivo '{DEVICE_NAME}'")
        try:
            if cmd["type"] == "speak":
                audio_url = f"http://{_local_ip()}:5000/tts/{key}.mp3"
                cast.play_media(audio_url, "audio/mpeg")
                cast.media_controller.block_until_active(timeout=10)
                return jsonify(ok=True, message=f"Google dice: {cmd['text']}")
            elif cmd["type"] == "play":
                video_id = _extract_youtube_id(cmd["url"])
                audio_url, title = _extract_youtube_audio_url(cmd["url"])
                cast.play_media(audio_url, "audio/mp4")
                cast.media_controller.block_until_active(timeout=10)
                return jsonify(ok=True, message=f"Reproduciendo: {title or video_id}")
        except Exception as e:
            return jsonify(ok=False, message=f"Error: {e}")


@app.route("/play", methods=["POST"])
def play():
    url = (request.json or {}).get("url", "").strip()
    if not url:
        return jsonify(ok=False, message="Falta el link"), 400

    with _lock:
        cast = _get_device()
        if not cast:
            return jsonify(ok=False, message=f"No se encontro el dispositivo '{DEVICE_NAME}'")
        try:
            video_id = _extract_youtube_id(url)
            if video_id:
                audio_url, title = _extract_youtube_audio_url(url)
                cast.play_media(audio_url, "audio/mp4")
                cast.media_controller.block_until_active(timeout=10)
                return jsonify(ok=True, message=f"Reproduciendo audio de YouTube: {title or video_id}")
            else:
                cast.play_media(url, "audio/mp3")
                cast.media_controller.block_until_active(timeout=10)
                return jsonify(ok=True, message=f"Reproduciendo: {url}")
        except Exception as e:
            return jsonify(ok=False, message=f"Error: {e}")


@app.route("/control", methods=["POST"])
def control():
    action = (request.json or {}).get("action", "")
    with _lock:
        cast = _get_device()
        if not cast:
            return jsonify(ok=False, message=f"No se encontro el dispositivo '{DEVICE_NAME}'")
        try:
            mc = cast.media_controller
            if action in ("pause", "resume"):
                done = threading.Event()
                mc.update_status(callback_function=lambda *a, **kw: done.set())
                done.wait(timeout=5)
                if not mc.status.media_session_id:
                    return jsonify(ok=False, message="No hay reproduccion activa")
            if action == "pause":
                mc.pause()
                msg = "Pausado"
            elif action == "resume":
                mc.play()
                msg = "Reanudado"
            elif action == "stop":
                cast.quit_app()
                msg = "Detenido"
            else:
                return jsonify(ok=False, message="Accion invalida")
            return jsonify(ok=True, message=msg)
        except Exception as e:
            return jsonify(ok=False, message=f"Error: {e}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
