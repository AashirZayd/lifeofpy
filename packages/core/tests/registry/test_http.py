import pytest
from unittest.mock import patch, MagicMock
from core.registry.http import HttpClient
from core.registry.exceptions import NetworkError, RegistryUnavailableError
from core.logging.logger import DefaultLogger


@pytest.fixture
def logger():
    return DefaultLogger()


@pytest.fixture
def http(logger):
    return HttpClient(logger, retries=1)


@patch("urllib.request.urlopen")
def test_http_request_json_success(mock_urlopen, http):
    mock_response = MagicMock()
    mock_response.read.return_value = b'{"success": true}'
    mock_response.__enter__.return_value = mock_response
    mock_urlopen.return_value = mock_response

    data = http.request_json("http://test.com")
    assert data["success"] is True


@patch("urllib.request.urlopen")
def test_http_request_404(mock_urlopen, http):
    import urllib.error

    mock_urlopen.side_effect = urllib.error.HTTPError("http://test.com", 404, "Not Found", {}, None)

    with pytest.raises(RegistryUnavailableError):
        http.request_bytes("http://test.com")


@patch("urllib.request.urlopen")
def test_http_request_timeout(mock_urlopen, logger):
    import urllib.error

    # Setup retries so we can see the timeout failure
    client = HttpClient(logger, retries=2)
    mock_urlopen.side_effect = urllib.error.URLError(TimeoutError("Timed out"))

    with pytest.raises(NetworkError) as exc:
        client.request_bytes("http://test.com")

    assert "Timeout" in str(exc.value)
