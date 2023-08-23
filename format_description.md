    Bundesamt f�r Seeschifffahrt und Hydrographie (BSH), Hamburg      23.12.2019
    Federal Maritime and Hydrogaphic Agency, Hamburg, Germany
    section: M11 Tides

                    description of BSH E-Format
                   =============================

********************************************************************************

    header lines:
    --------------

    I_E DE__508P2019 begin of dataset  +BSH gauge number+year
    A01 Hersteller : producer
    A02 Daten-Art  : type of data       Vorausberechnungen = predictions
                                          Beobachtungen      = observations
    A03 PegelNr.   : gauge number of BSH
    A04 GT-Name    : gauge name
    A06 GT-Jahr    : year of prediction
    A07 Def.-Jahr  : water level observations - methodically last year and
                     total number of years
    A08 Position   : geographic coordinates
    A11 Zeitzone   : legal time zone
    A12 Position GK: Gauss Kr�ger Coordinates or UTM
    A13 Messstelle : gauge number of Federal Waterways and Shipping
                                     Administration (WSV)
    B01 Sommerzeit : Daylight Saving Time
    C01 Analyse-Ber: method of analysis (independent or with refernce station)
                     + number of tidal constituents
    C02 Datenumfang: data extent
    C03 H�henniveau: reference level     PNP = zero level of the gauge
                                         NHN = normal high zero,
                                               german vertical geodetic datum
                                         SKN = chart datum
    C04 EinheitZeit: unit of time     StdMin = hours,minutes
    C05 EinheitH�he: unit of height        m = metre
                                          dm = decimetre
                                          cm = centimetre
                                          mm = millimetre
                                          ft = foot
    D01 PNP u. NHN : PNP relative to NHN
    D02 SKN u. NHN : SKN relative to NHN
    D03 SKN �. PNP : SKN relative to PNP
    F01 MHWI       : mean high water lunitidal interval
    F02 MNWI       : mean low water lunitidal interval
    G01 MHW        : mean high water
    G02 MNW        : mean low water
    LLL            : separating line between header and data
    #              : column separator
    EEE            : end of data

********************************************************************************

    data lines:
    ------------

       column
         1- 3  line code                VB1 = data without heights
                                        VB2 = data including heights
         5-12  gauge number     column  5-6 = country code
                                          7 = underline
                                       8-11 = number
                                         12 = always a letter oder underline
           14  phases of the moon         0 = new moon    1 = first quarter
                                          2 = full moon   3 = last quarter
           16  H = high water             N = low water   K = curve data
        18-19  day of the week
        21-30  date                           [day.month.year]
        32-36  time                           [hours:minutes]
        38-43  height                         [metre]
           45  quality flag:              1 = uncertain data  7 = outlier
        47-49  number of day
        51-56  time zone                      time difference to UTC
        58-64  transit number (for HW and LW)
           69  1 = HW upper transit       2 = LW upper transit
               3 = HW lower transit       4 = LW lower transit
        71-84  Julian Date, time zone UTC

********************************************************************************

    example lines:
    ===============

I_E#DE__508P2019#
A01#Hersteller :#M1103/BSH-Hamburg, 26.06.2018  09:59:01#
A02#Daten-Art  :#Vorausberechnungen#
A03#PegelNr.   :#DE__508P#
A04#GT-Name    :#Hamburg, St. Pauli, Elbe#
A06#GT-Jahr    :#      2019#
A07#Def.-Jahr  :#2016#19#
A08#Position   :#53�32'44''N   9�58'12''E WGS84#
A11#Zeitzone   :#UTC+ 1h00min (MEZ)#
A12#Position GK:# 35 64369.60 R  59 35349.57 H#
A13#Messstelle :#304     #
C01#Analyse-Ber:#selbst�ndig#43#
C02#Datenumfang:#Zeiten u. H�hen: HW NW      #
C03#H�henniveau:#PNP#
C04#EinheitZeit:#StdMin#
C05#EinheitH�he:# m#
D01#PNP u. NHN :#- 5.00 #
D02#SKN u. NHN :#- 1.90 #
D03#SKN �. PNP :#  3.10 #
F01#MHWI       :#15:22   #
F02#MNWI       :#22:31   #
G01#MHW        :#  7.12 #
G02#MNW        :#  3.33 #
LLL#
         1         2         3         4         5         6         7         8
123456789a123456789b123456789c123456789d123456789e123456789f123456789g123456789h12345

VB2#DE__508P# #H#Di# 1. 1.2019# 0:00# 6.87 # #  1#+ 1:00#  24348#   1#2458484.458495#
VB2#DE__508P# #N#Di# 1. 1.2019# 7:03# 3.65 # #  1#+ 1:00#  24348#   2#2458484.751963#
VB2#DE__508P# #H#Di# 1. 1.2019#12:21# 7.18 # #  1#+ 1:00#  24348#   3#2458484.972882#
VB2#DE__508P# #N#Di# 1. 1.2019#19:52# 3.55 # #  1#+ 1:00#  24348#   4#2458485.286364#
VB2#DE__508P# #H#Mi# 2. 1.2019# 1:09# 6.94 # #  2#+ 1:00#  24349#   1#2458485.506404#
VB2#DE__508P# #N#Mi# 2. 1.2019# 8:16# 3.67 # #  2#+ 1:00#  24349#   2#2458485.803083#
VB2#DE__508P# #H#Mi# 2. 1.2019#13:33# 7.18 # #  2#+ 1:00#  24349#   3#2458486.023161#
VB2#DE__508P# #N#Mi# 2. 1.2019#21:00# 3.60 # #  2#+ 1:00#  24349#   4#2458486.333625#
VB2#DE__508P# #H#Do# 3. 1.2019# 2:15# 7.07 # #  3#+ 1:00#  24350#   1#2458486.552047#
VB2#DE__508P# #N#Do# 3. 1.2019# 9:28# 3.67 # #  3#+ 1:00#  24350#   2#2458486.852503#
VB2#DE__508P# #H#Do# 3. 1.2019#14:40# 7.20 # #  3#+ 1:00#  24350#   3#2458487.069239#
VB2#DE__508P# #N#Do# 3. 1.2019#22:01# 3.61 # #  3#+ 1:00#  24350#   4#2458487.375526#
VB2#DE__508P# #H#Fr# 4. 1.2019# 3:11# 7.17 # #  4#+ 1:00#  24351#   1#2458487.590879#
.
.
VB2#DE__508P# #H#Sa#28.12.2019#18:02# 7.09 # #362#+ 1:00#  24697#   3#2458846.209959#
VB2#DE__508P# #N#So#29.12.2019# 1:09# 3.50 # #363#+ 1:00#  24697#   4#2458846.506019#
VB2#DE__508P# #H#So#29.12.2019# 6:12# 7.30 # #363#+ 1:00#  24698#   1#2458846.716883#
VB2#DE__508P# #N#So#29.12.2019#13:39# 3.44 # #363#+ 1:00#  24698#   2#2458847.027426#
VB2#DE__508P# #H#So#29.12.2019#18:42# 7.06 # #363#+ 1:00#  24698#   3#2458847.237466#
VB2#DE__508P# #N#Mo#30.12.2019# 1:46# 3.54 # #364#+ 1:00#  24698#   4#2458847.531789#
VB2#DE__508P# #H#Mo#30.12.2019# 6:50# 7.32 # #364#+ 1:00#  24699#   1#2458847.742762#
VB2#DE__508P# #N#Mo#30.12.2019#14:19# 3.47 # #364#+ 1:00#  24699#   2#2458848.054674#
VB2#DE__508P# #H#Mo#30.12.2019#19:21# 6.99 # #364#+ 1:00#  24699#   3#2458848.264506#
VB2#DE__508P# #N#Di#31.12.2019# 2:21# 3.54 # #365#+ 1:00#  24699#   4#2458848.556464#
VB2#DE__508P# #H#Di#31.12.2019# 7:27# 7.32 # #365#+ 1:00#  24700#   1#2458848.768621#
VB2#DE__508P# #N#Di#31.12.2019#14:55# 3.50 # #365#+ 1:00#  24700#   2#2458849.079914#
VB2#DE__508P# #H#Di#31.12.2019#19:57# 6.90 # #365#+ 1:00#  24700#   3#2458849.289523#
EEE#
