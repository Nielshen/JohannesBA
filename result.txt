Ergebnisse:

Ursprüngliche Anzahl Zeilen: 164
Zeilen nach Attention Check: 160

Deskriptive Statistiken pro Frage:
         Mittelwert  Std.-Abweichung
DF01_01        4.27             0.62
DF01_02        4.32             0.67
DF01_03        4.29             0.63
DF02_01        4.29             0.63
DF02_02        4.28             0.64
DF02_03        4.24             0.67
IC01_01        3.98             0.75
IC01_02        4.12             0.70
IC01_03        4.04             0.79
IC01_04        4.03             0.72
IC01_05        4.01             0.80
IC01_06        3.74             0.93
IC01_07        3.94             0.79
IC02_08        4.09             0.73
IC02_09        4.03             0.81
IC02_10        3.91             0.76
IC02_11        4.04             0.79
IC02_12        4.08             0.73
IC02_13        4.13             0.73
JC01_01        3.68             1.14
JC01_02        3.50             1.22
JC01_03        3.52             1.20
JC01_04        3.46             1.24
PS01_01        3.78             1.08
PS01_02        3.67             0.97
PS01_03        3.34             0.95
PS01_04        4.12             1.14
PS01_05        3.82             0.94
SS01_01        4.06             0.81
SS01_02        4.04             0.81
SS01_03        3.76             0.96
WF01_01        4.19             0.90
WF01_02        3.94             1.05
WF01_03        3.48             1.28
WF01_04        3.54             1.21
WF01_05        3.26             1.28
WF01_06        3.55             1.15
WM01_01        3.89             0.89
WM01_02        3.96             0.83
WM01_03        3.91             0.85

Demografische Daten:
Gender Verteilung (PF01):
Kategorie 1.0: 85 Teilnehmer (53.1%)
Kategorie 2.0: 73 Teilnehmer (45.6%)
Kategorie 3.0: 1 Teilnehmer (0.6%)
Kategorie -1.0: 1 Teilnehmer (0.6%)

Alter (PF02_01):
Durchschnitt: 38.7
Standardabweichung: 11.1
Minimum: 19.0
Maximum: 69.0

Gruppenmittelwerte und Standardabweichungen:
                       Mittelwert  Std.-Abweichung
Digital_Fluency              4.28             0.52
Individual_Creativity        4.01             0.53
Job_Complexity               3.54             1.07
Psychological_Safety         3.75             0.65
Supervisor_Support           3.95             0.75
Work_Flexibility             3.66             0.87
Work_Method_Autonomy         3.92             0.77

Korrelationsmatrix mit Signifikanzniveaus:
Anmerkung: *p < 0.05; **p < 0.01
                      Digital_Fluency Individual_Creativity Job_Complexity Psychological_Safety Supervisor_Support Work_Flexibility Work_Method_Autonomy  Alter Geschlecht
Digital_Fluency                 1.0**                0.25**          0.16*                0.19*             0.34**             0.02                 0.14  -0.12      0.16*
Individual_Creativity          0.25**                 1.0**           -0.0               0.37**             0.42**            0.17*               0.37**   0.03       0.15
Job_Complexity                  0.16*                  -0.0          1.0**                 0.14            -0.21**            -0.05                -0.04   0.11      -0.14
Psychological_Safety            0.19*                0.37**           0.14                1.0**             0.41**             0.02               0.36**   0.02       -0.0
Supervisor_Support             0.34**                0.42**        -0.21**               0.41**              1.0**           0.25**               0.41**  -0.03       0.14
Work_Flexibility                 0.02                 0.17*          -0.05                 0.02             0.25**            1.0**               0.35**  -0.02      -0.01
Work_Method_Autonomy             0.14                0.37**          -0.04               0.36**             0.41**           0.35**                1.0**   0.07       0.03
Alter                           -0.12                  0.03           0.11                 0.02              -0.03            -0.02                 0.07  1.0**       0.07
Geschlecht                      0.16*                  0.15          -0.14                 -0.0               0.14            -0.01                 0.03   0.07      1.0**



Modell 1 - Kontrollvariablen:
==========================================================================================
                             coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------
const                      3.8044      0.108     35.274      0.000       3.591       4.018
Alter_z                   -0.0032      0.038     -0.085      0.932      -0.078       0.072
Geschlecht                 0.1419      0.069      2.042      0.043       0.005       0.279
Psychological_Safety_z     0.1467      0.041      3.601      0.000       0.066       0.227
Job_Complexity_z          -0.0065      0.039     -0.169      0.866      -0.083       0.070
Work_Method_Autonomy_z     0.1398      0.040      3.455      0.001       0.060       0.220
==========================================================================================

Modell 2 - Haupteffekte:
==========================================================================================
                             coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------
const                      3.8595      0.107     35.987      0.000       3.648       4.071
Alter_z                    0.0112      0.038      0.298      0.766      -0.063       0.086
Geschlecht                 0.1041      0.069      1.503      0.135      -0.033       0.241
Psychological_Safety_z     0.1053      0.043      2.445      0.016       0.020       0.190
Job_Complexity_z           0.0088      0.041      0.216      0.829      -0.072       0.089
Work_Method_Autonomy_z     0.0941      0.044      2.162      0.032       0.008       0.180
Work_Flexibility_z         0.0247      0.040      0.615      0.539      -0.055       0.104
Digital_Fluency_z          0.0527      0.041      1.275      0.204      -0.029       0.134
Supervisor_Support_z       0.1095      0.047      2.308      0.022       0.016       0.203
==========================================================================================

Modell 3 - Interaktionseffekte:
==========================================================================================
                             coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------
const                      3.8617      0.107     36.143      0.000       3.651       4.073
Alter_z                   -0.0046      0.038     -0.122      0.903      -0.080       0.070
Geschlecht                 0.1119      0.069      1.629      0.105      -0.024       0.248
Psychological_Safety_z     0.1101      0.043      2.569      0.011       0.025       0.195
Job_Complexity_z           0.0160      0.040      0.395      0.693      -0.064       0.096
Work_Method_Autonomy_z     0.0904      0.043      2.099      0.038       0.005       0.175
Work_Flexibility_z         0.0253      0.040      0.635      0.526      -0.053       0.104
Digital_Fluency_z          0.0531      0.041      1.299      0.196      -0.028       0.134
Supervisor_Support_z       0.1085      0.047      2.310      0.022       0.016       0.201
WF_x_DF                   -0.0541      0.038     -1.437      0.153      -0.128       0.020
WF_x_SS                   -0.0502      0.040     -1.269      0.206      -0.128       0.028
==========================================================================================

R-Quadrat Werte:
Modell 1 R²: 0.223
Modell 2 R²: 0.276
Modell 3 R²: 0.301