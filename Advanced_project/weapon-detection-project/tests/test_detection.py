import pytest
from src.detection import detect_weapons
import numpy as np


def test_weapon_detection_dummy():
    # Dummy frame banate hain (black image)
    frame = np.zeros((640, 480, 3), dtype=np.uint8)
    result = detect_weapons(frame)
    assert result is not None
