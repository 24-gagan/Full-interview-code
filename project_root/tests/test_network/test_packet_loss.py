import pytest
from src.network_utils import get_packet_loss


@pytest.mark.parametrize("host", ["8.8.8.8", "1.1.1.1"])
def test_packet_loss(host):
    loss = get_packet_loss(host)
    assert loss == 0, f"Packet loss detected: {loss}% for host {host}"
