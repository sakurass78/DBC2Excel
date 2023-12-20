
from decimal import Decimal


# --- Force
def kpa_to_psi(value):
    """Kilopascal to Pound-force per square inch"""
    return float(Decimal(str(value)) * Decimal('0.145038'))


def kpa_to_bar(value):
    """Kilopascal to Bar"""
    return float(Decimal(str(value)) * Decimal('0.01'))


def kpa_to_pa(value):
    """Kilopascal to Pascal"""
    return float(Decimal(str(value)) * Decimal('1000.0'))


def bar_to_psi(value):
    """Bar to Pound-force per square inch"""
    return float(Decimal(str(value)) * Decimal('14.5038'))


def bar_to_kpa(value):
    """Bar to Kilopascal"""
    return float(Decimal(str(value)) * Decimal('100.0'))


def bar_to_pa(value):
    """Bar to Pascal"""
    return float(Decimal(str(value)) * Decimal('100000.0'))


def psi_to_kpa(value):
    """Pound-force per square inch to Kilopascal"""
    return float(Decimal(str(value)) * Decimal('6.89476'))


def psi_to_bar(value):
    """Pound-force per square inch to Bar"""
    return float(Decimal(str(value)) * Decimal('0.0689476'))


def psi_to_pa(value):
    """Pound-force per square inch to Pascal"""
    return float(Decimal(str(value)) * Decimal('6894.76'))


def pa_to_psi(value):
    """Pascal to Pound-force per square inch"""
    return float(Decimal(str(value)) * Decimal('0.000145038'))


def pa_to_kpa(value):
    """Pascal to Kilopascal"""
    return float(Decimal(str(value)) * Decimal('0.001'))


def pa_to_bar(value):
    """Pascal to Bar"""
    return float(Decimal(str(value)) * Decimal('1e-5'))


# --- Speed
def kph_to_mph(value):
    """Kilometer per hour to Mile per hour"""
    return float(Decimal(str(value)) * Decimal('0.621371'))


def kph_to_ftsec(value):
    """Kilometer per hour to Foot per second"""
    return float(Decimal(str(value)) * Decimal('0.911344'))


def kph_to_msec(value):
    """Kilometer per hour to Meter per second"""
    return float(Decimal(str(value)) * Decimal('0.277778'))


def mph_to_kph(value):
    """Mile per hour to Kilometer per hour"""
    return float(Decimal(str(value)) * Decimal('1.60934'))


def mph_to_ftsec(value):
    """Mile per hour to Foot per second"""
    return float(Decimal(str(value)) * Decimal('1.46667'))


def mph_to_msec(value):
    """Mile per hour to Meter per second"""
    return float(Decimal(str(value)) * Decimal('0.44704'))


def ftsec_to_mph(value):
    """Foot per second to Mile per hour"""
    return float(Decimal(str(value)) * Decimal('0.681818'))


def ftsec_to_kph(value):
    """Foot per second to Kilometer per hour"""
    return float(Decimal(str(value)) * Decimal('1.09728'))


def ftsec_to_msec(value):
    """Foot per second to Meter per second"""
    return float(Decimal(str(value)) * Decimal('0.3048'))


def msec_to_kph(value):
    """Meter per second to Kilometer per hour"""
    return float(Decimal(str(value)) * Decimal('3.6'))


def msec_to_mph(value):
    """Meter per second to Mile per hour"""
    return float(Decimal(str(value)) * Decimal('2.23694'))


def msec_to_ftsec(value):
    """Meter per second to Foot per second"""
    return float(Decimal(str(value)) * Decimal('3.28084'))


# --- Temperature
def c_to_f(value):
    """Celcius to Farenheit"""
    return float((Decimal(str(value)) * Decimal('9.0') / Decimal('5.0')) + Decimal('32.0'))


def f_to_c(value):
    """Farenheit to Celcius"""
    return float((Decimal(str(value)) - Decimal('32.0')) * Decimal('5.0') / Decimal('9.0'))


# --- Volume
def lh_to_gh(value):
    """Liter per hour to Gallon per hour"""
    return float(Decimal(str(value)) * Decimal('0.26'))


def gh_to_lh(value):
    """Gallon per hour to Liter per hour"""
    return float(Decimal(str(value)) * Decimal('3.78541178'))


# --- Weight
def gsec_to_lbm(value):
    """Gram per second to Pound a minute"""
    return float(Decimal(str(value)) * Decimal('0.132277'))


def lbm_to_gsec(value):
    """Pound a minute to Gram per second"""
    return float(Decimal(str(value)) * Decimal('7.5599'))


# Volume & Weight
def gsec_to_cfm(value):
    """Gram per second to Cubic foot a minute"""
    return float((Decimal(str(value)) * Decimal('4') * Decimal('60')) / Decimal('29.92'))


def cfm_to_gsec(value):
    """Cubic foot a minute to Gram per second"""
    return float(((Decimal(str(value)) * Decimal('29.92')) / Decimal('60.0')) / Decimal('4.0'))


def cfm_to_lbm(value):
    """Cubic foot a minute to Pound a minute"""
    return gsec_to_lbm(cfm_to_gsec(value))


def lbm_to_cfm(value):
    """Pound a minute to Cubic foot a minute"""
    return gsec_to_cfm(lbm_to_gsec(value))


# --- Distance
def km_to_mi(value):
    """Kilometer to Mile"""
    return float(Decimal(str(value)) * Decimal('0.621371'))


def mi_to_km(value):
    """Mile to Kilometer"""
    return float(Decimal(str(value)) * Decimal('1.60934'))
