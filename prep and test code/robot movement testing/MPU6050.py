import math
import time
import smbus
import threading


# addresses and constants
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
scale_gyro = 1/131.0
scale_accel = 1/16384.0
address = 0x68
update_interval_value = 0.05

# pythagorean distance
def dist(a, b):
    return math.sqrt((a * a) + (b * b))

# orientation from accel readings
def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)
def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


class Reading:

    def __init__(self, gx, gy, gz, ax, ay, az):
        self.gyro_x = gx
        self.gyro_y = gy
        self.gyro_z = gz
        self.accel_x = ax
        self.accel_y = ay
        self.accel_z = az



class Gyroscope:

    # i2c reading functions
    def read_byte(self, adr):
        return self.bus.read_byte_data(address, adr)

    def read_word(self, adr):
        high = self.bus.read_byte_data(address, adr)
        low = self.bus.read_byte_data(address, adr + 1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val


    def __init__(self):
        self.angle = 0

        self.gyro_errx = 0
        self.gyro_erry = 0
        self.gyro_errz = 0

        self.accel_errx = 0
        self.accel_erry = 0
        self.accel_errz = 0

        # initialize i2c
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(address, power_mgmt_1, 0)

        self._angle = 0
        self.tprev = time.time_ns() / 1_000_000_000 # convert to seconds\

        self.calibrate()

        update_thread = threading.Thread(target = self.scheduled_update_interval)
        update_thread.start()



    # read 6dof values into object
    def update(self):
        # read values from 6dof module
        gyro_xout = self.read_word_2c(0x43)
        gyro_yout = self.read_word_2c(0x45)
        gyro_zout = self.read_word_2c(0x47)

        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        # scale values to get accurate readings
        gyro_x = gyro_xout*scale_gyro - self.gyro_errx
        gyro_y = gyro_yout*scale_gyro - self.gyro_erry
        gyro_z = gyro_zout*scale_gyro - self.gyro_errz

        accel_x = accel_xout*scale_accel - self.accel_errx
        accel_y = accel_yout*scale_accel - self.accel_erry
        accel_z = accel_zout*scale_accel - self.accel_errz

        tcur = time.time_ns() / 1_000_000_000
        self._angle += (tcur - self.tprev) * gyro_x
        self.angle = round(self._angle%360 if (self._angle%360) < 180 else -(360-(self._angle%360)))
        self.tprev = tcur

        return Reading(gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z)

    def scheduled_update_interval(self):
        while True:
            time.sleep(update_interval_value)
            self.update()


    def calibrate(self):
        # reset errors
        self.gyro_errx = 0
        self.gyro_erry = 0
        self.gyro_errz = 0

        self.accel_errx = 0
        self.accel_erry = 0
        self.accel_errz = 0

        # how many values to average over for calibration
        calibration_length = 20

        # temporary error array
        errs = [0] * 6


        for _ in range(calibration_length):
            time.sleep(0.01)

            current = self.update()

            errs[0] += current.gyro_x / calibration_length
            errs[1] += current.gyro_y / calibration_length
            errs[2] += current.gyro_z / calibration_length

            errs[3] += current.accel_x / calibration_length
            errs[4] += current.accel_y / calibration_length
            errs[5] += current.accel_z / calibration_length


        # update error offsets
        self.gyro_errx = errs[0]
        self.gyro_erry = errs[1]
        self.gyro_errz = errs[2]

        self.accel_errx = errs[3]
        self.accel_erry = errs[4]
        self.accel_errz = errs[5]

        # reset angle
        self.angle = 0
        self._angle = 0

