from datetime import datetime, date, timedelta


class Py3status:

    def timetil10(self):

        ct = datetime.now()
        currentTime = datetime(year = ct.year, month = ct.month, day = ct.day, hour = ct.hour, minute = ct.minute, second = ct.second)
        tenPM = datetime(year = ct.year, month = ct.month, day = ct.day, hour = 22, minute = 0, second = 0)
        timeLeft = str(tenPM - currentTime)

        return {'full_text': timeLeft,
                'cached_until': self.py3.time_in(1)
            }
