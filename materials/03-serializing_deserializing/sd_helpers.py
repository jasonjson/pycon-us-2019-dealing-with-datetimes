from datetime import datetime, timedelta, tzinfo
from dateutil import tz

from io import BytesIO
from base64 import b64decode

class ChileTzInfo(tzinfo):
    def __init__(self, access_date):
        super().__init__()
        if access_date < datetime(2016, 3, 20):
            self._tzinfo = SANTIAGO_2016
        else:
            self._tzinfo = SANTIAGO

    def tzname(self, dt):
        return self._tzinfo.tzname(dt)

    def utcoffset(self, dt):
        return self._tzinfo.utcoffset(dt)

    def dst(self, dt):
        return self._tzinfo.dst(dt)

    def __str__(self):
        return "America/Santiago"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._access_date!r})"


SANTIAGO_2016_DATA = BytesIO(b64decode("""
VFppZjIAAAAAAAAAAAAAAAAAAAAAAAAJAAAACQAAAAAAAAB0AAAACQAAABGAAAAAjzBHRptc5VCffOLG
oQBxwLBed8axdz1AskEA0LNYcMC0IjRQtTmkQLYDZ9C3GtfAt+SbULj9XMC5xyBQzBxuQMxs59DT3I/A
1BvJsNUzVcDVdpJA/dE8QP6S+rD/zM3AAHLcsAF1UMACQEmwA1UywAQgK7AFPk9ABgANsAcLvEAH3++w
CP4TQAm/0bAK3fVAC6juMAy910ANiNAwDp25QA9osjAQhtXAEUiUMBJmt8ATKHYwFEaZwBURkrAWJnvA
FvF0sBgGXcAY0VawGeY/wBqxOLAbz1xAHJEasB2vPkAecPywH48gQCB/AzAhbwJAIjn7MCNO5EAkGd0w
JTgAwCX5vzAm8vjAJ9mhMCj3xMApwr2wKtemwCuin7Ast4jALYKBsC6XasAvYmOwMICHQDFCRbAyYGlA
Mz3XMDRAS0A1C0QwNg24QDcG1bA4AA9AOMsIMDnpK8A6quowO8kNwDyKzDA9qO/APmquMD+I0cBAU8qw
QWizwEIzrLBDSJXARBOOsEUxskBF83CwRxGUQEfvAjBI8XZASbxvMErRWEBLuACwTLE6QE3GBzBOUILA
T5yusFBC2cBRfJCwUiv2QFNccrBUC9hAVTxUsAECAQMBBAIEAgQCBAIEAgMCAwUDAgMGBwYHBgcGBwYH
BgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYH
BgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYI//+9ugAA//+9ugAE//+5sAAI///HwAAI///HwAEM///V0AEM
///V0AEM///HwAAI///V0AAITE1UAFNNVABDTFQAQ0xTVAAAAAAAAAABAQEAAAAAAAABAQFUWmlmMgAA
AAAAAAAAAAAAAAAAAAAAAAkAAAAJAAAAAAAAAHQAAAAJAAAAEf////9phx3G/////48wR0b/////m1zl
UP////+ffOLG/////6EAccD/////sF53xv////+xdz1A/////7JBAND/////s1hwwP////+0IjRQ////
/7U5pED/////tgNn0P////+3GtfA/////7fkm1D/////uP1cwP////+5xyBQ/////8wcbkD/////zGzn
0P/////T3I/A/////9QbybD/////1TNVwP/////VdpJA//////3RPED//////pL6sP//////zM3AAAAA
AABy3LAAAAAAAXVQwAAAAAACQEmwAAAAAANVMsAAAAAABCArsAAAAAAFPk9AAAAAAAYADbAAAAAABwu8
QAAAAAAH3++wAAAAAAj+E0AAAAAACb/RsAAAAAAK3fVAAAAAAAuo7jAAAAAADL3XQAAAAAANiNAwAAAA
AA6duUAAAAAAD2iyMAAAAAAQhtXAAAAAABFIlDAAAAAAEma3wAAAAAATKHYwAAAAABRGmcAAAAAAFRGS
sAAAAAAWJnvAAAAAABbxdLAAAAAAGAZdwAAAAAAY0VawAAAAABnmP8AAAAAAGrE4sAAAAAAbz1xAAAAA
AByRGrAAAAAAHa8+QAAAAAAecPywAAAAAB+PIEAAAAAAIH8DMAAAAAAhbwJAAAAAACI5+zAAAAAAI07k
QAAAAAAkGd0wAAAAACU4AMAAAAAAJfm/MAAAAAAm8vjAAAAAACfZoTAAAAAAKPfEwAAAAAApwr2wAAAA
ACrXpsAAAAAAK6KfsAAAAAAst4jAAAAAAC2CgbAAAAAALpdqwAAAAAAvYmOwAAAAADCAh0AAAAAAMUJF
sAAAAAAyYGlAAAAAADM91zAAAAAANEBLQAAAAAA1C0QwAAAAADYNuEAAAAAANwbVsAAAAAA4AA9AAAAA
ADjLCDAAAAAAOekrwAAAAAA6quowAAAAADvJDcAAAAAAPIrMMAAAAAA9qO/AAAAAAD5qrjAAAAAAP4jR
wAAAAABAU8qwAAAAAEFos8AAAAAAQjOssAAAAABDSJXAAAAAAEQTjrAAAAAARTGyQAAAAABF83CwAAAA
AEcRlEAAAAAAR+8CMAAAAABI8XZAAAAAAEm8bzAAAAAAStFYQAAAAABLuACwAAAAAEyxOkAAAAAATcYH
MAAAAABOUILAAAAAAE+crrAAAAAAUELZwAAAAABRfJCwAAAAAFIr9kAAAAAAU1xysAAAAABUC9hAAAAA
AFU8VLABAgEDAQQCBAIEAgQCBAIDAgMFAwIDBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcG
BwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcGBwYHBgcG
CP//vboAAP//vboABP//ubAACP//x8AACP//x8ABDP//1dABDP//1dABDP//x8AACP//1dAACExNVABT
TVQAQ0xUAENMU1QAAAAAAAAAAQEBAAAAAAAAAQEBCkNMVDMK
""".replace('\n', '').strip().encode()))

SANTIAGO = tz.gettz("America/Santiago")
SANTIAGO_2016 = tz.tzfile(SANTIAGO_2016_DATA, filename="America/Santiago")
