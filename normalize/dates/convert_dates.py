
import datetime


class ConvertDates():

    def __init__(self, format):
        if not format:
            raise ValueError('Format not defined')
        self.__format = format

    def convert(self, data):
        print(data)
        if not isinstance(data, str):
            raise ValueError("Invalid date type, send strings only")
        data = data.split('-')
        if self.__format == "/br":
            result = self.format_date_br(data[0], data[1], data[2])
        elif self.__format == "full_br":
            result = self.format_date_full_br(data[0], data[1], data[2])
        elif self.__format == "full_us":
            result = self.format_date_full_us(data[0], data[1], data[2])
        else:
            raise ValueError('Invalid format')

        return result

    def format_date_br(self, year, month, day):
        if int(day) < 1 or int(day) > 31:
            raise ValueError("Insert a valid day")
        return f"{day}/{month}/{year}"

    def format_date_full_br(self, year, month, day):
        if int(day) < 1 or int(day) > 31:
            raise ValueError("Insert a valid day")
        return f"{day} de {self.__get_month_name(month, 'br')} de {year}"

    def format_date_full_us(self, year, month, day):
        __day = self.__get_us_day(day)
        __month = self.__get_month_name(month, 'us')
        upper_month = str(__month).title()

        return f"{upper_month} {__day}, {year}"

    def __get_us_day(self, day):

        if int(day) < 1 or int(day) > 31:
            raise ValueError("Insert a valid day")

        if day == '31':
            __day = f"{day}st"
        elif day == '01':
            __day = f'{day.replace("0", "", 1)}st'
        elif day == '02':
            __day = f'{day.replace("0", "", 1)}nd'
        elif day == '03':
            __day = f'{day.replace("0", "", 1)}rd'
        elif day == '04':
            __day = f'{day.replace("0", "", 1)}th'
        elif day == '05':
            __day = f'{day.replace("0", "", 1)}th'
        elif day == '06':
            __day = f'{day.replace("0", "", 1)}th'
        elif day == '07':
            __day = f'{day.replace("0", "", 1)}th'
        elif day == '08':
            __day = f'{day.replace("0", "", 1)}th'
        elif day == '09':
            __day = f'{day.replace("0", "", 1)}th'
        else:
            __day = f"{day}th"

        return __day

    def __get_month_name(self, month, format):
        if format == "br":
            if month == "01":
                __month = 'janeiro'
            elif month == "02":
                __month = 'fevereiro'
            elif month == "03":
                __month = 'março'
            elif month == "04":
                __month = 'abril'
            elif month == "05":
                __month = 'maio'
            elif month == "06":
                __month = 'junho'
            elif month == "07":
                __month = 'julho'
            elif month == "08":
                __month = 'agosto'
            elif month == "09":
                __month = 'setembro'
            elif month == "10":
                __month = 'outubro'
            elif month == "11":
                __month = 'novembro'
            elif month == "12":
                __month = 'dezembro'
            else:
                raise ValueError('Invalid Month')
        elif format == "us":
            if month == "01":
                __month = 'January'
            elif month == "02":
                __month = 'February'
            elif month == "03":
                __month = 'March'
            elif month == "04":
                __month = 'April'
            elif month == "05":
                __month = 'May'
            elif month == "06":
                __month = 'June'
            elif month == "07":
                __month = 'July'
            elif month == "08":
                __month = 'August'
            elif month == "09":
                __month = 'September'
            elif month == "10":
                __month = 'October'
            elif month == "11":
                __month = 'November'
            elif month == "12":
                __month = 'December'
            else:
                raise ValueError('Invalid Month')
        else:
            raise ValueError('Invalid format')

        return __month
