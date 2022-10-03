# Offical release by Nadohoi
# Ver 1.0

import board
import adafruit_mlx90614 # pip3 install adafruit-circuitpython-mlx90614
import busio as io

# Locating mlx90614's i2c
i2c = io.I2C(board.SCL,board.SCA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

while True:
    obj_temp = mlx.object_temperature
    amb_temp = mlx.ambient_temperature
    print("Obj: " + obj_temp + "Amb: " + amb_temp)
