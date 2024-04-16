import smbus
import time

# Initialize I2C (use '1' for Raspberry Pi 3 and newer, '0' for older models)
bus = smbus.SMBus(1)

# AD7746 I2C address
AD7746_ADDR = 0x48


# Configure AD7746 settings
def configure_ad7746():
    # Set configuration register for single-ended mode and enable measurement
    config = 0x00  # Replace with your desired configuration
    bus.write_byte_data(AD7746_ADDR, 0x07, config)

    # Set excitation voltage, reference capacitor value, etc. (replace with your values)
    bus.write_word_data(AD7746_ADDR, 0x08, 0x1234)
    bus.write_word_data(AD7746_ADDR, 0x0A, 0x5678)


# Read capacitance value from AD7746
def read_capacitance():
    # Read 24-bit capacitance data
    data = bus.read_i2c_block_data(AD7746_ADDR, 0x03, 3)

    # Convert data to capacitance value (replace with your calibration)
    capacitance = (data[0] << 16 | data[1] << 8 | data[2]) & 0xFFFFFF

    return capacitance


# Convert capacitance to length in centimeters (replace with your conversion)
def capacitance_to_length(capacitance):
    # Example conversion: replace with your calibration
    length_cm = capacitance * 0.01  # Adjust this conversion factor

    return length_cm


if __name__ == "__main__":
    try:
        # Configure AD7746
        configure_ad7746()

        while True:
            # Read capacitance
            capacitance = read_capacitance()

            # Convert capacitance to length in centimeters
            length_cm = capacitance_to_length(capacitance)

            # Print length in centimeters
            print(f"Length: {length_cm:.2f} cm")

            # Wait for some time before the next measurement
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
