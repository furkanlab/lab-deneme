from rplidar import RPLidar, RPLidarException

import numpy as np

lidar = RPLidar('/dev/ttyUSB0')

lidar.__init__('/dev/ttyUSB0', 115200, 3, None)

lidar.connect()

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

try:
    for i, scan in enumerate(lidar.iter_scans()):
        scan_data = []
        for d in scan:
            engel = 0          
            #d[0] : Quality of the measurement
            if 330 <= d[1] <= 360 or 0 <= d[1] <= 30:     #d[1] : Angle of the measurement
                #print("Açı: ", d[1], "Mesafe: ", d[2] / 10)  #d[2] : Distance of the measurement

                if (d[2]/10) <= 100:
                    #engel = 1                       
                    print("Engel var!")
                                        
                # Polar koordinatları güncelle
                #polar_angle = np.deg2rad(d[1])  # Açıyı dereceden radyana dönüştür
                #polar_distance = d[2] / 10  # Mesafeyi güncelle (mm cinsinden, cm'ye dönüştür)

                # Güncellenmiş polar koordinatları sakla
                #scan_data.append((polar_angle, polar_distance))

                #print("Aci: ", polar_angle, "Mesfe: ", polar_distance)
                #print(engel)

        if False:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            break
except KeyboardInterrupt as err:
    print('key board interupt')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

except RPLidarException as err:
    print(err)
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
except AttributeError:
    print('hi attribute error')