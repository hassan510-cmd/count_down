import eel 
import time
from datetime import datetime , timedelta 

@eel.expose
def startTime():
    return str(datetime.now())


@eel.expose
def call_js():
    current_date=datetime.now()
    go_date ='6/10/2021'
    arrive_date = datetime.strptime(go_date, '%d/%m/%Y') + timedelta(days=45)
    t = (arrive_date-current_date).days*24*60*60
    t2=(arrive_date-current_date).seconds
    while t:
        mi,se=divmod(t2,60)
        ho,mi2=divmod(mi,60)
        da,ho2=divmod(ho,60)
        mins1, secs = divmod(t, 60)
        hours , mins2 = divmod(mins1,60)
        days , hours2=divmod(hours,24)
        # timer2 = '{:02d} day :{:02d} hours :{:02d} minutes :{:02d} seconds'.format(days,hours2,mins2, secs)
        timer = f'{days} day : {ho2} hours : {mi2} minutes : {se} seconds'
        print(f'{timer}', end="\r")
        eel.add_time(go_date,arrive_date.strftime( '%d/%m/%Y'),timer)
        time.sleep(1)
        t -= 1
        t2 -=1


if __name__ == "__main__":
    eel.init('/home/sedosona/Documents/ehab-life-time/web')
    eel.start('main.html')