THRESHOLD_TEMP_inCelsius = 200

def network_alert_stub(celcius):
    print(f'Note : Stub code executed')
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius<=THRESHOLD_TEMP_inCelsius):    
      returnCode = 200     # Return 200 for ok
    elif(celcius>THRESHOLD_TEMP_inCelsius):
      returnCode = 500     # Return 500 for not-ok
    return returnCode
