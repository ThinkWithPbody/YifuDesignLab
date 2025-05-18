import math

def main():
    while True:
        target_radius = int(input("Input target body radius (km): [200] ") or "200")
        relay_input = int(input("Input number of relays: [3] ") or "3")

        altitude_tolerance = int(input("Input maneuvering tolerance (km): [5] ") or "5")
        hardware_altitude_min = int(input("Input minimum altitude for hardware (km): [70] ") or "70")
        hardware_altitude_max = int(input("Input maximum altitude for hardware (km): [250] ") or "250")

        def get_altitude(target_radius, relays):
            return round((target_radius / math.cos(math.radians(180 / relays)) - target_radius) * 100) / 100

        relay_minimum = 0
        for i in range(3,9):
            if get_altitude(target_radius, i) <= hardware_altitude_max:
                relay_minimum = i
                break

        # Ensure altitude_collect does not exceed hardware_altitude_max
        altitude_connect = get_altitude(target_radius, relay_input)
        while True:
            altitude_collect = get_altitude(target_radius, relay_minimum)
            if hardware_altitude_max - altitude_collect >= altitude_tolerance * 2:
                break
            relay_minimum += 1

        print(f"To maintain connectivity    you need {relay_input} relays at minimum altitude {altitude_connect}")
        print(f"To maintain data collection you need {relay_minimum} relays at altitude {altitude_collect} - {hardware_altitude_max}")

        use_connect = input("Calculate for connectivity only? [True] ") or "True"
        relays = 0
        eriapsis = 0
        if use_connect == "True":
            use_connect = True
            relays = int(relay_input)
            periapsis = input(f"Actual altitude to use: [{altitude_connect + altitude_tolerance}] ") or str(altitude_connect + altitude_tolerance)
        else:
            use_connect = False
            relays = int(relay_minimum)
            periapsis = input(f"Actual altitude to use: [{altitude_collect + altitude_tolerance}] ") or str(altitude_collect + altitude_tolerance)

        print(f"Create a circularization node at an altitude of {periapsis}km and record your post-burn period as Days-Hours-Minutes-Seconds(.Miliseconds).")
        time_input = input("D-H-M-S: ") or "0-1-45-45"
        time = time_input.split("-")
        time_input_seconds = ((float(time[0]) * 24 + float(time[1])) * 60 + float(time[2])) * 60 + float(time[3])
        time_seconds = round((time_input_seconds / int(relays) * (int(relays)+1)) * 1000) / 1000
        period_days, period_seconds = divmod(time_seconds, 24 * 60 * 60)
        period_hours, period_seconds = divmod(period_seconds, 60 * 60)
        period_minutes, period_seconds = divmod(period_seconds, 60)

        period_days = round(period_days)
        period_hours = round(period_hours)
        period_minutes = round(period_minutes)
        period_seconds = round(period_seconds * 1000) / 1000
        print(f"Adjust your apoapsis so that your period is {str(period_days)}D {str(period_hours)}H {str(period_minutes)}M {str(period_seconds)}S (resonant orbit of {relays + 1}/{relays}).")
        print(f"Then, detach one relay each time you're about to pass periapsis, and circularize it to an orbital period of {time[0]}D {time[1]}H {time[2]}M {time[3]}S.")
        print("Don't forget to put solar panels into optimal orientation and enable instruments!")

        restart = input("Restart? [True] ") or "True"
        if restart != "True":
            break

if __name__ == "__main__":
    main()