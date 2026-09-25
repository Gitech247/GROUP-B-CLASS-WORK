"""Simple engineering asset models for subsea integrity screening."""

from dataclasses import dataclass

def _positive(value, name):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{name} must be numeric.")
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return float(value)

@dataclass
class SubseaJumper:
    asset_id: str
    design_pressure_psi: float
    operating_pressure_psi: float
    design_temperature_c: float
    operating_temperature_c: float
    design_length_m: float
    operating_length_m: float

    def __post_init__(self):
        if not self.asset_id:
            raise ValueError("asset_id is required.")
        for name in (
            "design_pressure_psi", "operating_pressure_psi",
            "design_temperature_c", "operating_temperature_c",
            "design_length_m", "operating_length_m"
        ):
            _positive(getattr(self, name), name)

    def pressure_utilisation(self):
        return self.operating_pressure_psi / self.design_pressure_psi

    def temperature_utilisation(self):
        return self.operating_temperature_c / self.design_temperature_c

    def length_utilisation(self):
        return self.operating_length_m / self.design_length_m

    def utilisation(self):
        return max(
            self.pressure_utilisation(),
            self.temperature_utilisation(),
            self.length_utilisation(),
        )

    def status(self, warning_limit=0.80, critical_limit=1.00):
        u = self.utilisation()
        if u >= critical_limit:
            return "CRITICAL"
        if u >= warning_limit:
            return "WARNING"
        return "NORMAL"

@dataclass
class RiserSystem:
    asset_id: str
    design_pressure_psi: float
    operating_pressure_psi: float
    design_temperature_c: float
    operating_temperature_c: float
    design_length_m: float
    operating_length_m: float
    design_tension_kN: float
    operating_tension_kN: float

    def __post_init__(self):
        if not self.asset_id:
            raise ValueError("asset_id is required.")
        for name in (
            "design_pressure_psi", "operating_pressure_psi",
            "design_temperature_c", "operating_temperature_c",
            "design_length_m", "operating_length_m",
            "design_tension_kN", "operating_tension_kN"
        ):
            _positive(getattr(self, name), name)

    def pressure_utilisation(self):
        return self.operating_pressure_psi / self.design_pressure_psi

    def temperature_utilisation(self):
        return self.operating_temperature_c / self.design_temperature_c

    def length_utilisation(self):
        return self.operating_length_m / self.design_length_m

    def tension_utilisation(self):
        return self.operating_tension_kN / self.design_tension_kN

    def utilisation(self):
        return max(
            self.pressure_utilisation(),
            self.temperature_utilisation(),
            self.length_utilisation(),
            self.tension_utilisation(),
        )

    def status(self, warning_limit=0.80, critical_limit=1.00):
        u = self.utilisation()
        if u >= critical_limit:
            return "CRITICAL"
        if u >= warning_limit:
            return "WARNING"
        return "NORMAL"
