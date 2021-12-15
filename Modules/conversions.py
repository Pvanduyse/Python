import numpy as np

SQR_SQR = lambda X, LEN_CONV: LEN_CONV(X**(1/2))**2
CUB_CUB = lambda X, LEN_CONV: LEN_CONV(X**(1/3))**3

def CHAIN_CONV(X, CONVERSIONS):
    RES = X
    for CONV in CONVERSIONS:
        RES = CONV(RES)
    return RES

# -------------------
#  METRIC CONVERIONS
# -------------------

PREFIXES = {
    "TERA":10**12,
    "GIGA":10**9,
    "MEGA":10**6,
    "KILO":10**3,
    "HECTO":10**2,
    "DECA":10**1,
    "DECI":10**-1,
    "CENTI":10**-2,
    "MILLI":10**-3,
    "MICRO":10**-6,
    "NANO":10**-9,
    "PICO":10**-12
}

PRE_METRIC = lambda X, PRE: X*PREFIXES[PRE]
METRIC_PRE = lambda X, PRE: X/PREFIXES[PRE]
PRE2_METRIC2 = lambda X, PRE: SQR_SQR(X, lambda Y: PRE_METRIC(Y, PRE))
METRIC2_PRE2 = lambda X, PRE: SQR_SQR(X, lambda Y: METRIC_PRE(Y, PRE))
PRE3_METRIC3 = lambda X, PRE: CUB_CUB(X, lambda Y: PRE_METRIC(Y, PRE))
METRIC3_PRE3 = lambda X, PRE: CUB_CUB(X, lambda Y: METRIC_PRE(Y, PRE))

# length
μm_m = lambda X: PRE_METRIC(X, "MICRO")
mm_m = lambda X: PRE_METRIC(X, "MILLI")
cm_m = lambda X: PRE_METRIC(X, "CENTI")
km_m = lambda X: PRE_METRIC(X, "KILO")

m_μm = lambda X: METRIC_PRE(X, "MICRO")
m_mm = lambda X: METRIC_PRE(X, "MILLI")
m_cm = lambda X: METRIC_PRE(X, "CENTI")
m_km = lambda X: METRIC_PRE(X, "KILO")


# area
μm2_m2 = lambda X: PRE2_METRIC2(X, "MICRO")
mm2_m2 = lambda X: PRE2_METRIC2(X, "MILLI")
cm2_m2 = lambda X: PRE2_METRIC2(X, "CENTI")
km2_m2 = lambda X: PRE2_METRIC2(X, "KILO")

m2_μm2 = lambda X: METRIC2_PRE2(X, "MICRO")
m2_mm2 = lambda X: METRIC2_PRE2(X, "MILLI")
m2_cm2 = lambda X: METRIC2_PRE2(X, "CENTI")
m2_km2 = lambda X: METRIC2_PRE2(X, "KILO")


# volume
μm3_m3 = lambda X: PRE3_METRIC3(X, "MICRO")
mm3_m3 = lambda X: PRE3_METRIC3(X, "MILLI")
cm3_m3 = lambda X: PRE3_METRIC3(X, "CENTI")
km3_m3 = lambda X: PRE3_METRIC3(X, "KILO")

m3_μm3 = lambda X: METRIC3_PRE3(X, "MICRO")
m3_mm3 = lambda X: METRIC3_PRE3(X, "MILLI")
m3_cm3 = lambda X: METRIC3_PRE3(X, "CENTI")
m3_km3 = lambda X: METRIC3_PRE3(X, "KILO")


#mass
kg_g = lambda X: PRE_METRIC(X, "KILO")
g_kg = lambda X: METRIC_PRE(X, "KILO")

# energy
kJ_J = lambda X: PRE_METRIC(X, "KILO")
J_kJ = lambda X: METRIC_PRE(X, "KILO")

# ----------------------
#  IMPERIAL CONVERSIONS
# ----------------------

# length
in_ft = lambda X: X/12
ft_yd = lambda X: X/3
yd_mi = lambda X: X/1760
ft_mi = lambda X: CHAIN_CONV(X, (ft_yd,yd_mi))

ft_in = lambda X: X*12
yd_ft = lambda X: X*3
mi_yd = lambda X: X*1760
mi_ft = lambda X: CHAIN_CONV(X, (mi_yd,yd_ft))


# areas
in2_ft2 = lambda X: SQR_SQR(X, in_ft)
ft2_yd2 = lambda X: SQR_SQR(X, ft_yd)
ft2_mi2 = lambda X: SQR_SQR(X, ft_mi)
yd2_mi2 = lambda X: SQR_SQR(X, yd_mi)

mi2_yd2 = lambda X: SQR_SQR(X, mi_yd)
mi2_ft2 = lambda X: SQR_SQR(X, mi_ft)
yd2_ft2 = lambda X: SQR_SQR(X, yd_ft)
ft2_in2 = lambda X: SQR_SQR(X, ft_in)


# volumes
in3_ft3 = lambda X: CUB_CUB(X, in_ft)
ft3_yd3 = lambda X: CUB_CUB(X, ft_yd)
yd3_mi3 = lambda X: CUB_CUB(X, yd_mi)
ft3_mi3 = lambda X: CUB_CUB(X, ft_mi)

mi3_yd3 = lambda X: CUB_CUB(X, mi_yd)
mi3_ft3 = lambda X: CUB_CUB(X, mi_ft)
yd3_ft3 = lambda X: CUB_CUB(X, yd_ft)
ft3_in3 = lambda X: CUB_CUB(X, ft_in)

# --------------------------
#  COMMON INTER CONVERSIONS
# --------------------------

m_ft = lambda X: X*3.2808
ft_m = lambda X: X/3.2808

km_mi = lambda X: CHAIN_CONV(X, (km_m,m_ft,ft_mi))
mi_km = lambda X: CHAIN_CONV(X, (mi_ft,ft_m,m_km))

C_K = lambda X: X+273.15
K_C = lambda X: X-273.15
C_F = lambda X: X*9/5 + 32
F_C = lambda X: (X - 32) * 5/9
K_F = lambda X: CHAIN_CONV(X, (K_C,C_F))
F_K = lambda X: CHAIN_CONV(X, (F_C,C_K))
