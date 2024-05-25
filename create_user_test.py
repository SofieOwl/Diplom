#София Базыкина, 16-я когорта - Финальный проект. Инженер по тестированию плюс
import pytest
import configuration
import sender_stand_request
import requests


def track_order():
    track_number = sender_stand_request.new_order()
    assert track_number is not None, "No track number"
    return track_number

def test_track ():
    response = requests.get(f"{configuration.URL_SERVICE + configuration.TRACK}?t={track_order()}")
    assert response.status_code == 200, f"Status code not 200, {response.status_code}"


