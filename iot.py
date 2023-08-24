import serial

# Function to categorize and write the received data to respective template
def writeHtml( data ):
    if data[0] == 't':
        f = open('templates/temprature.html', 'w')
        f.write('<span style="color: green;">'+data[1:]+'</span>')
        f.close()
    elif data[0] =='l':
        f = open('templates/light.html', 'w')
        f.write('<span style="color: blue;">'+data[1:]+'</span>')
        f.close() 
    elif data[0] =='b':
        f = open('templates/button.html', 'w')
        f.write('<span style="color: red;">'+data[1:]+'</span>')
        f.close() 

try:
    serialPort = 'COM3' #! HAVE TO UPDATE -> this is your port
    with serial.Serial(serialPort, baudrate=115200, timeout=1, stopbits=1) as ser:
        #Loop to check for data recieved on serialPort
        while True:
            data = ser.readline().decode().strip()
            if data :
                # Write new data to html templates
                writeHtml(data)

except serial.SerialException:
    print(f"Failed {serialPort}.")

