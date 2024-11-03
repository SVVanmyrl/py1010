# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:48:58 2024

Dette er løsning for arbeidskrav 1 i fag PY1010 ved USN

@author: Ann Karin Halvorsen - ann.karin.halvorsen@vegvesen.no
"""
# Felles parametere for begge biler

KM = 10000  # Antall kilometer kjørt i året
D = 365  # Antall dager i regnestykket (nå er det år)
TFA = round(8.38 * D,1)  # Trafikkforsikring per år (begge biler)

# Kostnader ved elbil
EF = 5000  # Pris på forsikring Elbil
DE = 0.2 * 2.0 * KM  # Drivstoff for elbil
BE = 0.1 * KM  # Bompenger elbil

# Kostnader ved bensinbil
BF = 7500  # Pris på forsikring bensinbil
DB = 1 * KM  # Drivstoff for bensinbil
BB = 0.3 * KM  # Bompenger bensinbil


# Årlig pris for elbil
KE = EF + TFA + DE + BE
print("Årlig kostnad for elbil ved", KM, "kilometer i året er:", KE,'\n' "Av dette er det forsikringskostnader på", EF,'\n' "Trafikkforsikringsavgift", TFA,'\n' "Drivstoffkostnader", DE, '\n'"Bompenger koster", BE)

# Årlig pris for bensinbil
KB = BF + TFA + DB + BB
print("Årlig kostnad for bensinbil ved", KM, "kilometer i året er:", KB, '\n'"Av dette er det forsikringskostnader på", BF,'\n' "Trafikkforsikringsavgift", TFA, '\n'"Drivstoffkostnader", DB, '\n'"Bompenger koster", BB)

Diff = KE - KB
print('\n'"Det er en differanse i året på", Diff, "på å kjøre elbil kontra bensinbil")
