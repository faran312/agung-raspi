import thingspeak
import time
import RPi.GPIO as GPIO

#=================================Program Relay=============================================
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 21
#GPIO_TRIGGER = 18
#GPIO_ECHO = 24
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)
#=================================Program Relay=============================================

#==============================Chanel ID THingsspeak========================================
channel_id = 1030448 # PUT CHANNEL ID HERE
write_key  = 'Q4QD7S1ARAHYELT8' # PUT YOUR WRITE KEY HERE
read_key   = 'Y3NDCSUC0RG3MIG9' # PUT YOUR READ KEY HERE
#==============================Chanel ID THingsspeak========================================


def measure(channel):
  indikator_kirim = 0
  angka = 100
  try:
    # write
    response = channel_write.update({'field1':angka})
    # read
    pesanan = channel_read.get_field_last(1)
    sinyal_jalan = channel_read.get_field_last(2)

    #Pengolahan variabel
    jumlah_kata = len(pesanan)
    jumlah_kata2 = jumlah_kata - 2
    olahan_pesanan = pesanan[62:jumlah_kata2]
    olahan_pesanan = int(olahan_pesanan)

    jumlah_kata1 = len(sinyal_jalan)
    jumlah_kata12 = jumlah_kata1 - 2
    olahan_pesanan1 = sinyal_jalan[62:jumlah_kata12]
    olahan_pesanan1 = int(olahan_pesanan1)

    
    print(olahan_pesanan)
    print(olahan_pesanan1)
    
    
    if olahan_pesanan1 == 1:
      print("relay kerja")
      for i in range (1, olahan_pesanan):		#Start value, Exit value (loop won't run with this value as it exits, so needs to be desired final value + 1)
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
        print(i)
        time.sleep(1)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
      response = channel_write.update({'field2':0})
      
      

    else:
      print('Idle Position')
  except:
    print("Alat sedang mengalami masalah, tunggu beberapa saat lagi")

if __name__ == "__main__":
    channel_read = thingspeak.Channel(id=channel_id, api_key=read_key)
    channel_write = thingspeak.Channel(id=channel_id, api_key=write_key)
    
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)
