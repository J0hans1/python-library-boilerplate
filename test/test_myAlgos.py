#write test for haversine function in myAlgos.py
from markusLib import myfunctions

def test_haversine():
    assert myfunctions.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 945793.4375088713
