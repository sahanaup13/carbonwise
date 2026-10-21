def get_energy_data():
    return {
        "hours": [
            "06:00", "08:00", "10:00",
            "12:00", "14:00", "16:00",
            "18:00", "20:00"
        ],

        # Illustrative values in kW
        "solar": [
            2, 8, 15, 20, 18, 12, 4, 0
        ],

        "demand": [
            5, 8, 12, 14, 15, 13, 10, 7
        ],

        "battery": [
            60, 65, 75, 90, 95, 85, 70, 60
        ],

        "grid": [
            3, 2, 0, 0, 0, 1, 5, 7
        ],

        "price": [
            5, 5, 6, 6, 6, 7, 8, 7
        ],

        "unit": {
            "power": "kW",
            "battery": "%",
            "price": "₹/kWh"
        },

        "data_type": "SIMULATED"
    }