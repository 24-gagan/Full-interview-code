import subprocess
import platform
import re


def get_packet_loss(host="8.8.8.8", count=4):
    """
    Ping a host and return packet loss percentage.
    Works on Windows and Linux/Mac.
    """
    try:
        system = platform.system().lower()
        if system == "windows":
            cmd = ["ping", "-n", str(count), host]
        else:
            cmd = ["ping", "-c", str(count), host]

        result = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output = result.stdout

        # Windows parsing
        if system == "windows":
            match = re.search(r"Lost = \d+ \((\d+)% loss\)", output)
            if match:
                return int(match.group(1))

        # Linux/Mac parsing
        else:
            match = re.search(r"(\d+)% packet loss", output)
            if match:
                return int(match.group(1))

        return None
    except Exception:
        return None
