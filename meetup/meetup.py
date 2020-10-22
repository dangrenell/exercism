from datetime import date
from calendar import monthrange


class MeetupDayException(BaseException):
    pass


def meetup(year, month, week, day_of_week):
    day_of_week_dict = {'Monday': 1,
                        'Tuesday': 2,
                        'Wednesday': 3,
                        'Thursday': 4,
                        'Friday': 5,
                        'Saturday': 6,
                        'Sunday': 7}
    day = day_of_week_dict[day_of_week]

    days_in_month = monthrange(year, month)[1]
    week_dict = {'teenth': range(13, 20),
                 '1st': range(1, 8),
                 '2nd': range(8, 15),
                 '3rd': range(15, 22),
                 '4th': range(22, 29),
                 '5th': range(29, 32),
                 'last': range(days_in_month-6, days_in_month+1)}

    for i in week_dict[week]:
        try:
            if date(year, month, i).isoweekday() == day:
                return date(year, month, i)
        except:
            raise MeetupDayException("No go, bro!")

    return None
