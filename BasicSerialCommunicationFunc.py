import serial, sys, threading

ser = serial.Serial()
ser.baudrate=9600
ser.port=5
ser.open()
ser.timeout=0
      
##def readWriteFromCOM():
##      global ser
##      while True:
##            print ser.readline().strip()
##            outputFile.write(ser.readline().strip())
            
outputFile = open('C:/Users/will/Desktop/tempRawOutput', 'w')

try:
##      threading.Thread(target=readWriteFromCOM)
      raw_input("Press [ENTER] to download information from port %s..." % ser.port)
      ser.write("DataRequest^")
      while True:
            lastReadLine=ser.readline().strip()
            print lastReadLine
            outputFile.write(lastReadLine + "\n")
            if (lastReadTime - millis() >= 2000):
                  break
                             
except(KeyboardInterrupt, SystemExit):
      print("Closing")
      ser.close()
      outputFile.flush()
      outputFile.close()
      sys.exit(0)
      
finally:
      print("Unknown Error! Closing all objects! Jumping ship!")
      ser.close()
      outputFile.flush()
      outputFile.close()
