import json
import subprocess


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅᴀʏs"]
    while count < 4:
        count += 1
        if count < 3:
            seconds, result = divmod(seconds, 60)
        else:
            seconds, result = divmod(seconds, 24)
        if seconds == 0 and result == 0:
            break
        time_list.append(f"{int(result)}{time_suffix_list[count - 1]}")
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


def convert_bytes(size: float) -> str:
    if not size:
        return ""
    power = 1024
    n = 0
    power_dict = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power and n < 4:
        size /= power
        n += 1
    return "{:.2f} {}B".format(size, power_dict[n])


async def int_to_alpha(user_id: int) -> str:
    alphabet = "abcdefghij"
    return "".join(alphabet[int(digit)] for digit in str(user_id))


async def alpha_to_int(user_id_alphabet: str) -> int:
    alphabet = "abcdefghij"
    return int("".join(str(alphabet.index(char)) for char in user_id_alphabet))


def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(":"))))


def seconds_to_min(seconds: int) -> str:
    if seconds is None:
        return "-"
    d, h, m, s = (
        seconds // 86400,
        seconds % 86400 // 3600,
        seconds % 3600 // 60,
        seconds % 60,
    )
    if d:
        return f"{d:02}:{h:02}:{m:02}:{s:02}"
    if h:
        return f"{h:02}:{m:02}:{s:02}"
    if m:
        return f"{m:02}:{s:02}"
    return f"00:{s:02}"


def speed_converter(seconds: int, speed: float):
    original = seconds
    speed = float(speed)
    if speed == 0.5:
        seconds *= 2
    elif speed == 0.75:
        seconds += seconds * 0.5
    elif speed == 1.5:
        seconds -= seconds * 0.25
    elif speed == 2.0:
        seconds -= seconds * 0.5
    return seconds_to_min(int(seconds)), original


def check_duration(file_path: str):
    command = [
        "ffprobe",
        "-loglevel", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
        file_path,
    ]
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, _ = pipe.communicate()
    try:
        data = json.loads(out)
        return float(data.get("format", {}).get("duration")) or \
               next((float(s["duration"]) for s in data.get("streams", []) if "duration" in s), "Unknown")
    except Exception:
        return "Unknown"


formats = list(set([
    "webm", "mkv", "flv", "vob", "ogv", "ogg", "rrc", "gifv", "mng", "mov",
    "avi", "qt", "wmv", "yuv", "rm", "asf", "amv", "mp4", "m4p", "m4v", "mpg",
    "mp2", "mpeg", "mpe", "mpv", "svi", "3gp", "3g2", "mxf", "roq", "nsv",
    "f4v", "f4p", "f4a", "f4b"
]))    collect = seconds
    if seconds is not None:
        seconds = int(seconds)
        d, h, m, s = (
            seconds // (3600 * 24),
            seconds // 3600 % 24,
            seconds % 3600 // 60,
            seconds % 3600 % 60,
        )
        if d > 0:
            convert = "{:02d}:{:02d}:{:02d}:{:02d}".format(d, h, m, s)
            return convert, collect
        elif h > 0:
            convert = "{:02d}:{:02d}:{:02d}".format(h, m, s)
            return convert, collect
        elif m > 0:
            convert = "{:02d}:{:02d}".format(m, s)
            return convert, collect
        elif s > 0:
            convert = "00:{:02d}".format(s)
            return convert, collect
    return "-"


def check_duration(file_path):
    command = [
        "ffprobe",
        "-loglevel",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        file_path,
    ]

    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = pipe.communicate()
    _json = json.loads(out)

    if "format" in _json:
        if "duration" in _json["format"]:
            return float(_json["format"]["duration"])

    if "streams" in _json:
        for s in _json["streams"]:
            if "duration" in s:
                return float(s["duration"])

    return "Unknown"


formats = [
    "webm",
    "mkv",
    "flv",
    "vob",
    "ogv",
    "ogg",
    "rrc",
    "gifv",
    "mng",
    "mov",
    "avi",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "asf",
    "amv",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m4v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "flv",
    "f4v",
    "f4p",
    "f4a",
    "f4b",
]

