from fastapi import FastAPI

from projeto_01 import Territory, AppointmentRequest, AppointmentUpdate
from main import home_01

territory = FastAPI()

@territory.get("/territories")
async def all_the_territory():
    territories = {}
    appointed_dates_01 = []
    appointed_dates_02 = []
    appointed_dates_03 = []
    appointed_dates_04 = []
    appointed_dates_05 = []
    appointed_dates_06 = []
    appointed_dates_07 = []
    appointed_dates_08 = []
    appointed_dates_09 = []
    appointed_dates_10 = []
    appointed_dates_11 = []
    appointed_dates_12 = []
    appointed_dates_13 = []
    appointed_dates_14 = []
    appointed_dates_15 = []
    appointed_dates_16 = []
    appointed_dates_17 = []
    for date in home_01.territory_01:
        appointed_dates_01.append(date)
    territories['Territory_ONE'] = appointed_dates_01
    for date in home_01.territory_02:
        appointed_dates_02.append(date)
    territories['Territory_TWO'] = appointed_dates_02
    for date in home_01.territory_03:
        appointed_dates_03.append(date)
    territories['Territory_THREE'] = appointed_dates_03
    for date in home_01.territory_04:
        appointed_dates_04.append(date)
    territories['Territory_FOUR'] = appointed_dates_04
    for date in home_01.territory_05:
        appointed_dates_05.append(date)
    territories['Territory_FIVE'] = appointed_dates_05
    for date in home_01.territory_06:
        appointed_dates_06.append(date)
    territories['Territory_SIX'] = appointed_dates_06
    for date in home_01.territory_07:
        appointed_dates_07.append(date)
    territories['Territory_SEVEN'] = appointed_dates_07
    for date in home_01.territory_08:
        appointed_dates_08.append(date)
    territories['Territory_EIGHT'] = appointed_dates_08
    for date in home_01.territory_09:
        appointed_dates_09.append(date)
    territories['Territory_NINE'] = appointed_dates_09
    for date in home_01.territory_10:
        appointed_dates_10.append(date)
    territories['Territory_TEN'] = appointed_dates_10
    for date in home_01.territory_11:
        appointed_dates_11.append(date)
    territories['Territory_ELEVEN'] = appointed_dates_11
    for date in home_01.territory_12:
        appointed_dates_12.append(date)
    territories['Territory_TWELVE'] = appointed_dates_12
    for date in home_01.territory_13:
        appointed_dates_13.append(date)
    territories['Territory_THIRTEEN'] = appointed_dates_13
    for date in home_01.territory_14:
        appointed_dates_14.append(date)
    territories['Territory_FOURTEEN'] = appointed_dates_14
    for date in home_01.territory_15:
        appointed_dates_15.append(date)
    territories['Territory_FIFTEEN'] = appointed_dates_15
    for date in home_01.territory_16:
        appointed_dates_16.append(date)
    territories['Territory_SIXTEEN'] = appointed_dates_16
    for date in home_01.territory_17:
        appointed_dates_17.append(date)
    territories['Territory_SEVENTEEN'] = appointed_dates_17
    return territories

@territory.get("/territories/{territory_NUMBER}")
async def search_for_territory(territory_NUMBER: str):
    territories = {}
    appointed_dates_01 = []
    appointed_dates_02 = []
    appointed_dates_03 = []
    appointed_dates_04 = []
    appointed_dates_05 = []
    appointed_dates_06 = []
    appointed_dates_07 = []
    appointed_dates_08 = []
    appointed_dates_09 = []
    appointed_dates_10 = []
    appointed_dates_11 = []
    appointed_dates_12 = []
    appointed_dates_13 = []
    appointed_dates_14 = []
    appointed_dates_15 = []
    appointed_dates_16 = []
    appointed_dates_17 = []
    for date in home_01.territory_01:
        appointed_dates_01.append(date)
    territories['Territory_ONE'] = appointed_dates_01
    for date in home_01.territory_02:
        appointed_dates_02.append(date)
    territories['Territory_TWO'] = appointed_dates_02
    for date in home_01.territory_03:
        appointed_dates_03.append(date)
    territories['Territory_THREE'] = appointed_dates_03
    for date in home_01.territory_04:
        appointed_dates_04.append(date)
    territories['Territory_FOUR'] = appointed_dates_04
    for date in home_01.territory_05:
        appointed_dates_05.append(date)
    territories['Territory_FIVE'] = appointed_dates_05
    for date in home_01.territory_06:
        appointed_dates_06.append(date)
    territories['Territory_SIX'] = appointed_dates_06
    for date in home_01.territory_07:
        appointed_dates_07.append(date)
    territories['Territory_SEVEN'] = appointed_dates_07
    for date in home_01.territory_08:
        appointed_dates_08.append(date)
    territories['Territory_EIGHT'] = appointed_dates_08
    for date in home_01.territory_09:
        appointed_dates_09.append(date)
    territories['Territory_NINE'] = appointed_dates_09
    for date in home_01.territory_10:
        appointed_dates_10.append(date)
    territories['Territory_TEN'] = appointed_dates_10
    for date in home_01.territory_11:
        appointed_dates_11.append(date)
    territories['Territory_ELEVEN'] = appointed_dates_11
    for date in home_01.territory_12:
        appointed_dates_12.append(date)
    territories['Territory_TWELVE'] = appointed_dates_12
    for date in home_01.territory_13:
        appointed_dates_13.append(date)
    territories['Territory_THIRTEEN'] = appointed_dates_13
    for date in home_01.territory_14:
        appointed_dates_14.append(date)
    territories['Territory_FOURTEEN'] = appointed_dates_14
    for date in home_01.territory_15:
        appointed_dates_15.append(date)
    territories['Territory_FIFTEEN'] = appointed_dates_15
    for date in home_01.territory_16:
        appointed_dates_16.append(date)
    territories['Territory_SIXTEEN'] = appointed_dates_16
    for date in home_01.territory_17:
        appointed_dates_17.append(date)
    territories['Territory_SEVENTEEN'] = appointed_dates_17

    for k, v in territories.items():
        if k.casefold() == territory_NUMBER.casefold():
            return k, v

@territory.get("/territories/")
def date_of_appointment(date_of_appointment: str):
    territories = {}
    appointed_dates_01 = []
    appointed_dates_02 = []
    appointed_dates_03 = []
    appointed_dates_04 = []
    appointed_dates_05 = []
    appointed_dates_06 = []
    appointed_dates_07 = []
    appointed_dates_08 = []
    appointed_dates_09 = []
    appointed_dates_10 = []
    appointed_dates_11 = []
    appointed_dates_12 = []
    appointed_dates_13 = []
    appointed_dates_14 = []
    appointed_dates_15 = []
    appointed_dates_16 = []
    appointed_dates_17 = []
    for date in home_01.territory_01:
        appointed_dates_01.append(date)
    territories['Territory_ONE'] = appointed_dates_01
    for date in home_01.territory_02:
        appointed_dates_02.append(date)
    territories['Territory_TWO'] = appointed_dates_02
    for date in home_01.territory_03:
        appointed_dates_03.append(date)
    territories['Territory_THREE'] = appointed_dates_03
    for date in home_01.territory_04:
        appointed_dates_04.append(date)
    territories['Territory_FOUR'] = appointed_dates_04
    for date in home_01.territory_05:
        appointed_dates_05.append(date)
    territories['Territory_FIVE'] = appointed_dates_05
    for date in home_01.territory_06:
        appointed_dates_06.append(date)
    territories['Territory_SIX'] = appointed_dates_06
    for date in home_01.territory_07:
        appointed_dates_07.append(date)
    territories['Territory_SEVEN'] = appointed_dates_07
    for date in home_01.territory_08:
        appointed_dates_08.append(date)
    territories['Territory_EIGHT'] = appointed_dates_08
    for date in home_01.territory_09:
        appointed_dates_09.append(date)
    territories['Territory_NINE'] = appointed_dates_09
    for date in home_01.territory_10:
        appointed_dates_10.append(date)
    territories['Territory_TEN'] = appointed_dates_10
    for date in home_01.territory_11:
        appointed_dates_11.append(date)
    territories['Territory_ELEVEN'] = appointed_dates_11
    for date in home_01.territory_12:
        appointed_dates_12.append(date)
    territories['Territory_TWELVE'] = appointed_dates_12
    for date in home_01.territory_13:
        appointed_dates_13.append(date)
    territories['Territory_THIRTEEN'] = appointed_dates_13
    for date in home_01.territory_14:
        appointed_dates_14.append(date)
    territories['Territory_FOURTEEN'] = appointed_dates_14
    for date in home_01.territory_15:
        appointed_dates_15.append(date)
    territories['Territory_FIFTEEN'] = appointed_dates_15
    for date in home_01.territory_16:
        appointed_dates_16.append(date)
    territories['Territory_SIXTEEN'] = appointed_dates_16
    for date in home_01.territory_17:
        appointed_dates_17.append(date)
    territories['Territory_SEVENTEEN'] = appointed_dates_17
    appointment = []
    for k,v in territories.items():
        for days in v:
            worked_days = str(days)
            if worked_days.casefold() == date_of_appointment.casefold():
                appointment_search = f"{k} has appointment on the date {date_of_appointment}"
                appointment.append(appointment_search)
    return appointment

@territory.get("/territories/menu_days_with_no_appointment")
def menu_with_no_appointment():
    result = home_01.menu_worked_days()
    return result

@territory.post("/territories/appoint_territory")
def appoint_territory(new_appointment: AppointmentRequest):
    Territory.appoint_territory(home_01, new_appointment.date, new_appointment.territory)
    return f"The territory {new_appointment.territory} received one appointment on the date of {new_appointment.date}"

@territory.put("/territories/update_appointment")
def update_appointment(update_appointment: AppointmentUpdate):
    Territory.update_territory(home_01, update_appointment.date, update_appointment.new_date, update_appointment.territory)
    return "The day of the appointment was modified!"

@territory.delete("/terittories/delete")
def delete_appointment(delete_appointment: AppointmentRequest):
    Territory.delete_territory(home_01, delete_appointment.date, delete_appointment.territory)
    return "The territory was deleted!"
"""
Commiting
"""





