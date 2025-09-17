# Analysis Summary

## Feature Summary Table

| Feature                         | Day1_Median_IQR            | Day1_Mean_SD        | Day5_Median_IQR           | Day5_Mean_SD        | Median_Change_Pct   | Mean_Change_Pct   | Overall_Median_IQR         | Overall_Mean_SD     |   P_value | Test     |   Effect_size |   Sign_test_p |   Sign_test_es |   Wilcoxon_P |   TTest_P |   SignTest_P |   Cohens_d |
|:--------------------------------|:---------------------------|:--------------------|:--------------------------|:--------------------|:--------------------|:------------------|:---------------------------|:--------------------|----------:|:---------|--------------:|--------------:|---------------:|-------------:|----------:|-------------:|-----------:|
| pnn50                           | 32.5 (18.4�43.3)           | 32.0 � 17.6         | 22.5 (13.1�29.5)          | 23.6 � 14.5         | -30.5%              | -26.3%            | 27.8 (17.3�39.4)           | 27.8 � 16.7         |     0.031 | t-test   |          0.49 |         0.004 |           0.82 |      nan     |     0.031 |        0.004 |      0.51  |
| hrv_triangular_index            | 4.5 (3.8�4.8)              | 4.2 � 0.7           | 4.6 (3.4�5.0)             | 4.3 � 0.9           | 2.4%                | 2.1%              | 4.5 (3.6�4.9)              | 4.3 � 0.8           |     0.706 | t-test   |         -0.08 |         1     |           0.5  |      nan     |     0.706 |        1     |     -0.108 |
| systolic_slope                  | 1.3 (1.2�1.5)              | 1.3 � 0.2           | 1.4 (1.4�1.5)             | 1.4 � 0.2           | 5.9%                | 5.5%              | 1.4 (1.3�1.5)              | 1.3 � 0.2           |     0.308 | t-test   |         -0.22 |         0.523 |           0.41 |      nan     |     0.308 |        0.523 |     -0.357 |
| dfa                             | 1.0 (1.0�1.1)              | 1.0 � 0.1           | 1.0 (0.9�1.1)             | 1.0 � 0.1           | -3.3%               | -4.5%             | 1.0 (0.9�1.1)              | 1.0 � 0.1           |     0.03  | t-test   |          0.5  |         0.523 |           0.59 |      nan     |     0.03  |        0.523 |      0.493 |
| lf_power                        | 34266.4 (15486.9�77589.2)  | 69244.0 � 83558.5   | 12497.5 (2212.3�49179.4)  | 42591.4 � 62955.8   | -63.5%              | -38.5%            | 23645.5 (6234.0�76317.6)   | 55917.7 � 75168.6   |     0.337 | Wilcoxon |          0.65 |         0.832 |           0.55 |        0.337 |   nan     |        0.832 |      0.352 |
| diastolic_slope                 | -1.5 (-1.5�-1.4)           | -1.4 � 0.1          | -1.5 (-1.6�-1.5)          | -1.5 � 0.1          | 2.7%                | 5.1%              | -1.5 (-1.5�-1.4)           | -1.5 � 0.1          |     0.043 | t-test   |          0.46 |         0.134 |           0.68 |      nan     |     0.043 |        0.134 |      0.66  |
| hf_power                        | 66031.2 (29992.1�260816.6) | 281197.3 � 501312.3 | 21071.1 (4177.9�78529.6)  | 116881.0 � 191717.1 | -68.1%              | -58.4%            | 40162.4 (11502.4�236169.5) | 199039.2 � 388310.1 |     0.129 | Wilcoxon |          0.67 |         0.523 |           0.59 |        0.129 |   nan     |        0.523 |      0.423 |
| poincare_sd1                    | 613.3 (424.4�1281.0)       | 1229.9 � 1329.3     | 474.1 (144.0�816.9)       | 570.7 � 524.9       | -22.7%              | -53.6%            | 580.7 (233.8�932.5)        | 900.3 � 1063.0      |     0.063 | Wilcoxon |          0.64 |         0.286 |           0.64 |        0.063 |   nan     |        0.286 |      0.637 |
| peak_trend_slope                | 103.6 (80.3�133.8)         | 129.3 � 80.7        | 85.2 (73.5�100.4)         | 92.5 � 30.0         | -17.8%              | -28.4%            | 89.8 (78.3�119.9)          | 110.9 � 63.6        |     0.028 | Wilcoxon |          0.65 |         0.134 |           0.68 |        0.028 |   nan     |        0.134 |      0.59  |
| systolic_area                   | 14215.2 (12512.6�16603.6)  | 15602.4 � 5869.1    | 12489.2 (11208.1�14703.4) | 13233.7 � 2660.2    | -12.1%              | -15.2%            | 13835.3 (11395.4�15838.0)  | 14418.1 � 4707.9    |     0.063 | Wilcoxon |          0.64 |         0.523 |           0.59 |        0.063 |   nan     |        0.523 |      0.508 |
| signal_skewness                 | 0.1 (0.0�0.2)              | 0.1 � 0.2           | 0.1 (0.0�0.2)             | 0.1 � 0.1           | -16.5%              | -23.4%            | 0.1 (0.0�0.2)              | 0.1 � 0.2           |     0.36  | t-test   |          0.2  |         0.134 |           0.68 |      nan     |     0.36  |        0.134 |      0.214 |
| systolic_duration               | 0.5 (0.4�0.8)              | 0.7 � 0.4           | 0.5 (0.4�0.5)             | 0.5 � 0.2           | -12.7%              | -23.6%            | 0.5 (0.4�0.6)              | 0.6 � 0.3           |     0.098 | Wilcoxon |          0.67 |         0.134 |           0.68 |        0.098 |   nan     |        0.134 |      0.486 |
| poincare_sd2                    | 631.6 (429.7�1293.5)       | 1188.5 � 1248.2     | 482.7 (164.9�864.4)       | 567.8 � 478.7       | -23.6%              | -52.2%            | 550.4 (233.1�1022.2)       | 878.1 � 994.9       |     0.068 | Wilcoxon |          0.65 |         0.286 |           0.64 |        0.068 |   nan     |        0.286 |      0.641 |
| diastolic_area                  | 41100.0 (32234.6�49929.1)  | 46282.4 � 20953.9   | 35787.6 (27280.1�41745.6) | 37891.1 � 11546.6   | -12.9%              | -18.1%            | 39488.1 (30650.8�47376.9)  | 42086.7 � 17429.8   |     0.063 | Wilcoxon |          0.63 |         0.052 |           0.73 |        0.063 |   nan     |        0.052 |      0.485 |
| sdnn                            | 618.7 (426.5�1258.7)       | 1228.1 � 1366.1     | 479.9 (151.8�838.6)       | 574.2 � 514.2       | -22.4%              | -53.2%            | 578.0 (234.0�979.0)        | 901.1 � 1082.7      |     0.085 | Wilcoxon |          0.64 |         0.286 |           0.64 |        0.085 |   nan     |        0.286 |      0.619 |
| diastolic_amplitude_variability | 7552.5 (6232.6�8946.0)     | 7729.7 � 1938.8     | 6799.8 (6220.9�7536.2)    | 7152.0 � 1686.9     | -10.0%              | -7.5%             | 6951.4 (6164.1�8143.2)     | 7440.9 � 1840.0     |     0.296 | t-test   |          0.23 |         0.832 |           0.55 |      nan     |     0.296 |        0.832 |      0.311 |
| nn50                            | 74.5 (48.5�104.8)          | 75.4 � 35.9         | 66.5 (42.4�90.5)          | 70.8 � 38.3         | -10.7%              | -6.1%             | 67.9 (44.2�103.4)          | 73.1 � 37.2         |     0.276 | Wilcoxon |          0.56 |         0.134 |           0.68 |        0.276 |   nan     |        0.134 |      0.122 |
| rmssd                           | 863.0 (595.2�1782.2)       | 1831.4 � 2218.7     | 668.8 (203.4�1148.2)      | 814.0 � 773.4       | -22.5%              | -55.6%            | 817.4 (330.2�1308.6)       | 1322.7 � 1737.6     |     0.085 | Wilcoxon |          0.64 |         0.523 |           0.59 |        0.085 |   nan     |        0.523 |      0.598 |
| diastolic_duration              | 0.5 (0.4�0.6)              | 0.6 � 0.3           | 0.4 (0.3�0.5)             | 0.4 � 0.1           | -16.3%              | -23.5%            | 0.4 (0.3�0.5)              | 0.5 � 0.2           |     0.011 | Wilcoxon |          0.65 |         0.017 |           0.77 |        0.011 |   nan     |        0.017 |      0.543 |
| systolic_amplitude_variability  | 8301.5 (6891.2�9036.1)     | 8299.2 � 1597.0     | 7645.8 (6546.0�8371.9)    | 7716.3 � 1338.4     | -7.9%               | -7.0%             | 8065.4 (6692.9�8642.2)     | 8007.8 � 1501.9     |     0.218 | t-test   |          0.27 |         0.286 |           0.64 |      nan     |     0.218 |        0.286 |      0.387 |

## Catecholamine Summary

| Feature                 | Statistic                   | Grouped by ANSD   | Grouped by ANSD.1   | Grouped by ANSD.2   | Grouped by ANSD.3   | Grouped by ANSD.4   | Grouped by ANSD.5   | Grouped by ANSD.6   | Day     |
|:------------------------|:----------------------------|:------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------|
| nan                     | nan                         | Missing           | Overall             | 0                   | 1                   | SMD (0,1)           | P-Value             | Test                | nan     |
| n                       | nan                         | nan               | 22                  | 16                  | 6                   | nan                 | nan                 | nan                 | Day1    |
| Adrenalin, mean (SD)    | nan                         | 0                 | 5830.68 (7792.89)   | 4640.12 (4707.33)   | 9005.50 (13113.12)  | 0.443               | 0.459               | Welch�s T-test      | Day1    |
| Noradrenalin, mean (SD) | nan                         | 0                 | 41314.27 (58935.61) | 19995.88 (33876.42) | 98163.33 (76242.87) | 1.325               | 0.053               | Welch�s T-test      | Day1    |
| Dopamin, mean (SD)      | nan                         | 0                 | 67677.00 (44837.94) | 62130.56 (48490.01) | 82467.50 (32078.92) | 0.495               | 0.274               | Welch�s T-test      | Day1    |
| n                       | nan                         | nan               | 22                  | 16                  | 6                   | nan                 | nan                 | nan                 | Day5    |
| Adrenalin, mean (SD)    | nan                         | 0                 | 5830.68 (7792.89)   | 4640.12 (4707.33)   | 9005.50 (13113.12)  | 0.443               | 0.459               | Welch�s T-test      | Day5    |
| Noradrenalin, mean (SD) | nan                         | 0                 | 41314.27 (58935.61) | 19995.88 (33876.42) | 98163.33 (76242.87) | 1.325               | 0.053               | Welch�s T-test      | Day5    |
| Dopamin, mean (SD)      | nan                         | 0                 | 67677.00 (44837.94) | 62130.56 (48490.01) | 82467.50 (32078.92) | 0.495               | 0.274               | Welch�s T-test      | Day5    |
| Adrenalin               | Mean Change (Day5 - Day1)   | nan               | nan                 | 0.00                | 0.00                | nan                 | nan                 | nan                 | Change  |
| Adrenalin               | Median Change (Day5 - Day1) | nan               | nan                 | 0.00                | 0.00                | nan                 | nan                 | nan                 | Change  |
| Noradrenalin            | Mean Change (Day5 - Day1)   | nan               | nan                 | 0.00                | 0.00                | nan                 | nan                 | nan                 | Change  |
| Noradrenalin            | Median Change (Day5 - Day1) | nan               | nan                 | 0.00                | 0.00                | nan                 | nan                 | nan                 | Change  |
| Dopamin                 | Mean Change (Day5 - Day1)   | nan               | nan                 | 0.00                | 0.00                | nan                 | nan                 | nan                 | Change  |
| Dopamin                 | Median Change (Day5 - Day1) | nan               | nan                 | 0.00                | 0.00                | nan                 | nan                 | nan                 | Change  |
| n                       | nan                         | nan               | 44                  | 32                  | 12                  | nan                 | nan                 | nan                 | Overall |
| Adrenalin, mean (SD)    | nan                         | 0                 | 5830.68 (7701.74)   | 4640.12 (4630.79)   | 9005.50 (12502.87)  | 0.463               | 0.261               | Welch�s T-test      | Overall |
| Noradrenalin, mean (SD) | nan                         | 0                 | 41314.27 (58246.28) | 19995.88 (33325.55) | 98163.33 (72694.73) | 1.382               | 0.003               | Welch�s T-test      | Overall |
| Dopamin, mean (SD)      | nan                         | 0                 | 67677.00 (44313.50) | 62130.56 (47701.50) | 82467.50 (30586.05) | 0.508               | 0.106               | Welch�s T-test      | Overall |

## General Analysis for Adrenalin

### Pair Plot

![Pair Plot](plots\general\adrenalin\pair_plot.png)

Description of pair_plot.png:
This pair plot shows pairwise relationships between Adrenalin and PPG features.
Diagonal: KDE distributions for each variable.
Off-diagonal: Scatter plots with regression lines for correlations.

### Correlation Heatmap

![Correlation Heatmap](plots\general\adrenalin\correlation_heatmap.png)

Description of correlation_heatmap.png:
This heatmap shows Pearson correlations between Adrenalin and PPG features.
Colors range from blue (negative) to red (positive), with values annotated.
Strong correlations (close to ±1) indicate linear relationships.

### Feature Analysis Table

| Feature                         |   Day1_Spearman_R |   Day1_Spearman_P |   Day1_N_Samples |   Day5_Spearman_R |   Day5_Spearman_P |   Day5_N_Samples |   Overall_Spearman_R |   Overall_Spearman_P |   Overall_N_Samples |   MannWhitney_P |     Cohen_d |   High_Group_N |   Low_Group_N |
|:--------------------------------|------------------:|------------------:|-----------------:|------------------:|------------------:|-----------------:|---------------------:|---------------------:|--------------------:|----------------:|------------:|---------------:|--------------:|
| sdnn                            |        -0.211745  |         0.344157  |               22 |        -0.394692  |         0.0690906 |               22 |           -0.275055  |            0.0707601 |                  44 |      0.135786   |  -0.482045  |             22 |            22 |
| rmssd                           |        -0.218521  |         0.328569  |               22 |        -0.38227   |         0.0791342 |               22 |           -0.276747  |            0.0689742 |                  44 |      0.135786   |  -0.482045  |             22 |            22 |
| poincare_sd1                    |        -0.204969  |         0.360171  |               22 |        -0.38227   |         0.0791342 |               22 |           -0.273362  |            0.0725823 |                  44 |      0.135786   |  -0.482045  |             22 |            22 |
| poincare_sd2                    |        -0.207228  |         0.354786  |               22 |        -0.343874  |         0.117117  |               22 |           -0.25841   |            0.0903307 |                  44 |      0.226364   |  -0.321428  |             22 |            22 |
| systolic_duration               |        -0.381141  |         0.0800988 |               22 |        -0.373235  |         0.0870993 |               22 |           -0.374639  |            0.012227  |                  44 |      0.0445937  |  -0.537079  |             22 |            22 |
| diastolic_duration              |        -0.230943  |         0.301112  |               22 |        -0.383399  |         0.0781784 |               22 |           -0.298752  |            0.0488509 |                  44 |      0.0316017  |  -0.588592  |             22 |            22 |
| systolic_slope                  |         0.0344438 |         0.879053  |               22 |         0.147374  |         0.512799  |               22 |            0.119049  |            0.441482  |                  44 |      0.192322   |   0.463217  |             22 |            22 |
| diastolic_slope                 |        -0.20271   |         0.365603  |               22 |        -0.167702  |         0.455677  |               22 |           -0.199732  |            0.193644  |                  44 |      0.431315   |   0.0452165 |             22 |            22 |
| heart_rate                      |         0.339356  |         0.122328  |               22 |         0.313382  |         0.155561  |               22 |            0.29847   |            0.0490749 |                  44 |      0.12389    |   0.310515  |             22 |            22 |
| sample_entropy                  |       nan         |       nan         |              nan |       nan         |       nan         |              nan |          nan         |          nan         |                 nan |    nan          | nan         |            nan |           nan |
| nn50                            |        -0.325805  |         0.138959  |               22 |        -0.299831  |         0.175203  |               22 |           -0.309754  |            0.0407413 |                  44 |      0.0445937  |  -0.546126  |             22 |            22 |
| pnn50                           |        -0.337098  |         0.124995  |               22 |        -0.36533   |         0.0945453 |               22 |           -0.334579  |            0.0264277 |                  44 |      0.244912   |  -0.322898  |             22 |            22 |
| hrv_triangular_index            |         0.0852626 |         0.70598   |               22 |         0.133823  |         0.552696  |               22 |            0.123845  |            0.423168  |                  44 |      0.613522   |  -0.0768427 |             22 |            22 |
| lf_power                        |        -0.281762  |         0.203955  |               22 |        -0.359684  |         0.100145  |               22 |           -0.297059  |            0.0502071 |                  44 |      0.135786   |  -0.14597   |             22 |            22 |
| hf_power                        |        -0.303219  |         0.17014   |               22 |        -0.261434  |         0.2399    |               22 |           -0.262924  |            0.0846507 |                  44 |      0.0280638  |  -0.553711  |             22 |            22 |
| signal_skewness                 |         0.307736  |         0.163548  |               22 |        -0.28515   |         0.198337  |               22 |            0.0166443 |            0.914603  |                  44 |      0.681007   |   0.294643  |             22 |            22 |
| peak_trend_slope                |        -0.295313  |         0.182113  |               22 |        -0.44777   |         0.0366426 |               22 |           -0.375767  |            0.011948  |                  44 |      0.00767116 |  -0.640807  |             22 |            22 |
| systolic_area                   |        -0.281762  |         0.203955  |               22 |        -0.453416  |         0.0340615 |               22 |           -0.322731  |            0.0326252 |                  44 |      0.0618287  |  -0.178123  |             22 |            22 |
| diastolic_area                  |        -0.314512  |         0.153997  |               22 |        -0.427442  |         0.0472279 |               22 |           -0.373228  |            0.0125835 |                  44 |      0.0115611  |  -0.622567  |             22 |            22 |
| systolic_amplitude_variability  |        -0.0818746 |         0.717189  |               22 |        -0.0491248 |         0.828133  |               22 |           -0.0778616 |            0.615407  |                  44 |      0.646901   |   0.0737561 |             22 |            22 |
| diastolic_amplitude_variability |        -0.207228  |         0.354786  |               22 |        -0.281762  |         0.203955  |               22 |           -0.261514  |            0.0863949 |                  44 |      0.378368   |  -0.321513  |             22 |            22 |

### Feature Correlations Heatmap

![Feature Correlations](plots\general\adrenalin\adrenalin_feature_correlations.png)

#### sdnn by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\sdnn_adrenalin_quartiles.png)

Description of sdnn_adrenalin_quartiles.png:
This boxplot shows SDNN across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how sdnn varies with Adrenalin levels.

#### rmssd by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\rmssd_adrenalin_quartiles.png)

Description of rmssd_adrenalin_quartiles.png:
This boxplot shows RMSSD across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how rmssd varies with Adrenalin levels.

#### poincare_sd1 by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\poincare_sd1_adrenalin_quartiles.png)

Description of poincare_sd1_adrenalin_quartiles.png:
This boxplot shows POINCARE_SD1 across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how poincare_sd1 varies with Adrenalin levels.

#### poincare_sd2 by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\poincare_sd2_adrenalin_quartiles.png)

Description of poincare_sd2_adrenalin_quartiles.png:
This boxplot shows POINCARE_SD2 across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how poincare_sd2 varies with Adrenalin levels.

#### systolic_duration by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\systolic_duration_adrenalin_quartiles.png)

Description of systolic_duration_adrenalin_quartiles.png:
This boxplot shows SYSTOLIC_DURATION across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_duration varies with Adrenalin levels.

#### diastolic_duration by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\diastolic_duration_adrenalin_quartiles.png)

Description of diastolic_duration_adrenalin_quartiles.png:
This boxplot shows DIASTOLIC_DURATION across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_duration varies with Adrenalin levels.

#### systolic_slope by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\systolic_slope_adrenalin_quartiles.png)

Description of systolic_slope_adrenalin_quartiles.png:
This boxplot shows SYSTOLIC_SLOPE across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_slope varies with Adrenalin levels.

#### diastolic_slope by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\diastolic_slope_adrenalin_quartiles.png)

Description of diastolic_slope_adrenalin_quartiles.png:
This boxplot shows DIASTOLIC_SLOPE across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_slope varies with Adrenalin levels.

#### heart_rate by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\heart_rate_adrenalin_quartiles.png)

Description of heart_rate_adrenalin_quartiles.png:
This boxplot shows HEART_RATE across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how heart_rate varies with Adrenalin levels.

#### sample_entropy by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\sample_entropy_adrenalin_quartiles.png)

Description of sample_entropy_adrenalin_quartiles.png:
This boxplot shows SAMPLE_ENTROPY across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how sample_entropy varies with Adrenalin levels.

#### nn50 by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\nn50_adrenalin_quartiles.png)

Description of nn50_adrenalin_quartiles.png:
This boxplot shows NN50 across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how nn50 varies with Adrenalin levels.

#### pnn50 by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\pnn50_adrenalin_quartiles.png)

Description of pnn50_adrenalin_quartiles.png:
This boxplot shows PNN50 across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how pnn50 varies with Adrenalin levels.

#### hrv_triangular_index by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\hrv_triangular_index_adrenalin_quartiles.png)

Description of hrv_triangular_index_adrenalin_quartiles.png:
This boxplot shows HRV_TRIANGULAR_INDEX across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how hrv_triangular_index varies with Adrenalin levels.

#### lf_power by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\lf_power_adrenalin_quartiles.png)

Description of lf_power_adrenalin_quartiles.png:
This boxplot shows LF_POWER across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how lf_power varies with Adrenalin levels.

#### hf_power by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\hf_power_adrenalin_quartiles.png)

Description of hf_power_adrenalin_quartiles.png:
This boxplot shows HF_POWER across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how hf_power varies with Adrenalin levels.

#### signal_skewness by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\signal_skewness_adrenalin_quartiles.png)

Description of signal_skewness_adrenalin_quartiles.png:
This boxplot shows SIGNAL_SKEWNESS across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how signal_skewness varies with Adrenalin levels.

#### peak_trend_slope by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\peak_trend_slope_adrenalin_quartiles.png)

Description of peak_trend_slope_adrenalin_quartiles.png:
This boxplot shows PEAK_TREND_SLOPE across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how peak_trend_slope varies with Adrenalin levels.

#### systolic_area by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\systolic_area_adrenalin_quartiles.png)

Description of systolic_area_adrenalin_quartiles.png:
This boxplot shows SYSTOLIC_AREA across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_area varies with Adrenalin levels.

#### diastolic_area by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\diastolic_area_adrenalin_quartiles.png)

Description of diastolic_area_adrenalin_quartiles.png:
This boxplot shows DIASTOLIC_AREA across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_area varies with Adrenalin levels.

#### systolic_amplitude_variability by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\systolic_amplitude_variability_adrenalin_quartiles.png)

Description of systolic_amplitude_variability_adrenalin_quartiles.png:
This boxplot shows SYSTOLIC_AMPLITUDE_VARIABILITY across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_amplitude_variability varies with Adrenalin levels.

#### diastolic_amplitude_variability by Adrenalin Quartiles

![Boxplot](plots\general\adrenalin\diastolic_amplitude_variability_adrenalin_quartiles.png)

Description of diastolic_amplitude_variability_adrenalin_quartiles.png:
This boxplot shows DIASTOLIC_AMPLITUDE_VARIABILITY across Adrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_amplitude_variability varies with Adrenalin levels.

#### Scatter Plot: Adrenalin vs sdnn

![Scatter](plots\general\adrenalin\adrenalin_vs_sdnn.png)

#### Scatter Plot: Adrenalin vs rmssd

![Scatter](plots\general\adrenalin\adrenalin_vs_rmssd.png)

#### Scatter Plot: Adrenalin vs poincare_sd1

![Scatter](plots\general\adrenalin\adrenalin_vs_poincare_sd1.png)

#### Scatter Plot: Adrenalin vs poincare_sd2

![Scatter](plots\general\adrenalin\adrenalin_vs_poincare_sd2.png)

#### Scatter Plot: Adrenalin vs systolic_duration

![Scatter](plots\general\adrenalin\adrenalin_vs_systolic_duration.png)

#### Scatter Plot: Adrenalin vs diastolic_duration

![Scatter](plots\general\adrenalin\adrenalin_vs_diastolic_duration.png)

#### Scatter Plot: Adrenalin vs systolic_slope

![Scatter](plots\general\adrenalin\adrenalin_vs_systolic_slope.png)

#### Scatter Plot: Adrenalin vs diastolic_slope

![Scatter](plots\general\adrenalin\adrenalin_vs_diastolic_slope.png)

#### Scatter Plot: Adrenalin vs heart_rate

![Scatter](plots\general\adrenalin\adrenalin_vs_heart_rate.png)

#### Scatter Plot: Adrenalin vs sample_entropy

![Scatter](plots\general\adrenalin\adrenalin_vs_sample_entropy.png)

#### Scatter Plot: Adrenalin vs nn50

![Scatter](plots\general\adrenalin\adrenalin_vs_nn50.png)

#### Scatter Plot: Adrenalin vs pnn50

![Scatter](plots\general\adrenalin\adrenalin_vs_pnn50.png)

#### Scatter Plot: Adrenalin vs hrv_triangular_index

![Scatter](plots\general\adrenalin\adrenalin_vs_hrv_triangular_index.png)

#### Scatter Plot: Adrenalin vs lf_power

![Scatter](plots\general\adrenalin\adrenalin_vs_lf_power.png)

#### Scatter Plot: Adrenalin vs hf_power

![Scatter](plots\general\adrenalin\adrenalin_vs_hf_power.png)

#### Scatter Plot: Adrenalin vs signal_skewness

![Scatter](plots\general\adrenalin\adrenalin_vs_signal_skewness.png)

#### Scatter Plot: Adrenalin vs peak_trend_slope

![Scatter](plots\general\adrenalin\adrenalin_vs_peak_trend_slope.png)

#### Scatter Plot: Adrenalin vs systolic_area

![Scatter](plots\general\adrenalin\adrenalin_vs_systolic_area.png)

#### Scatter Plot: Adrenalin vs diastolic_area

![Scatter](plots\general\adrenalin\adrenalin_vs_diastolic_area.png)

#### Scatter Plot: Adrenalin vs systolic_amplitude_variability

![Scatter](plots\general\adrenalin\adrenalin_vs_systolic_amplitude_variability.png)

#### Scatter Plot: Adrenalin vs diastolic_amplitude_variability

![Scatter](plots\general\adrenalin\adrenalin_vs_diastolic_amplitude_variability.png)

## General Analysis for Noradrenalin

### Pair Plot

![Pair Plot](plots\general\noradrenalin\pair_plot.png)

Description of pair_plot.png:
This pair plot shows pairwise relationships between Noradrenalin and PPG features.
Diagonal: KDE distributions for each variable.
Off-diagonal: Scatter plots with regression lines for correlations.

### Correlation Heatmap

![Correlation Heatmap](plots\general\noradrenalin\correlation_heatmap.png)

Description of correlation_heatmap.png:
This heatmap shows Pearson correlations between Noradrenalin and PPG features.
Colors range from blue (negative) to red (positive), with values annotated.
Strong correlations (close to ±1) indicate linear relationships.

### Feature Analysis Table

| Feature                         |   Day1_Spearman_R |   Day1_Spearman_P |   Day1_N_Samples |   Day5_Spearman_R |   Day5_Spearman_P |   Day5_N_Samples |   Overall_Spearman_R |   Overall_Spearman_P |   Overall_N_Samples |   MannWhitney_P |     Cohen_d |   High_Group_N |   Low_Group_N |
|:--------------------------------|------------------:|------------------:|-----------------:|------------------:|------------------:|-----------------:|---------------------:|---------------------:|--------------------:|----------------:|------------:|---------------:|--------------:|
| sdnn                            |       -0.361942   |       0.0978766   |               22 |      -0.296443    |        0.180368   |               22 |           -0.343607  |          0.0223929   |                  44 |     0.0171107   |  -0.488432  |             22 |            22 |
| rmssd                           |       -0.381141   |       0.0800988   |               22 |      -0.260305    |        0.242011   |               22 |           -0.336836  |          0.0253662   |                  44 |     0.0171107   |  -0.488432  |             22 |            22 |
| poincare_sd1                    |       -0.359684   |       0.100145    |               22 |      -0.260305    |        0.242011   |               22 |           -0.331476  |          0.0279474   |                  44 |     0.0171107   |  -0.488432  |             22 |            22 |
| poincare_sd2                    |       -0.351779   |       0.108389    |               22 |      -0.335968    |        0.126344   |               22 |           -0.349249  |          0.0201435   |                  44 |     0.00767116  |  -0.557801  |             22 |            22 |
| systolic_duration               |       -0.470356   |       0.0271683   |               22 |      -0.270469    |        0.223449   |               22 |           -0.347274  |          0.0209081   |                  44 |     0.0248726   |  -0.406387  |             22 |            22 |
| diastolic_duration              |       -0.677019   |       0.000538964 |               22 |      -0.570864    |        0.00552541 |               22 |           -0.620354  |          7.06723e-06 |                  44 |     5.48107e-06 |  -0.922106  |             22 |            22 |
| systolic_slope                  |        0.123659   |       0.583509    |               22 |      -0.418408    |        0.0526322  |               22 |           -0.123281  |          0.4253      |                  44 |     0.404323    |  -0.213267  |             22 |            22 |
| diastolic_slope                 |       -0.20271    |       0.365603    |               22 |      -0.000564653 |        0.99801    |               22 |           -0.0981734 |          0.526084    |                  44 |     0.934473    |   0.0114657 |             22 |            22 |
| heart_rate                      |        0.5607     |       0.00663806  |               22 |       0.621683    |        0.00201053 |               22 |            0.589322  |          2.5668e-05  |                  44 |     0.00234962  |   0.446191  |             22 |            22 |
| sample_entropy                  |      nan          |     nan           |              nan |     nan           |      nan          |              nan |          nan         |        nan           |                 nan |   nan           | nan         |            nan |           nan |
| nn50                            |       -0.637493   |       0.00141607  |               22 |      -0.120271    |        0.593941   |               22 |           -0.355173  |          0.0179892   |                  44 |     0.0115611   |  -0.124827  |             22 |            22 |
| pnn50                           |       -0.726708   |       0.000127893 |               22 |      -0.116883    |        0.604451   |               22 |           -0.483532  |          0.000884062 |                  44 |     0.135786    |  -0.0611984 |             22 |            22 |
| hrv_triangular_index            |       -0.0920384  |       0.683739    |               22 |      -0.526821    |        0.011766   |               22 |           -0.350377  |          0.0197172   |                  44 |     0.0555558   |  -0.508848  |             22 |            22 |
| lf_power                        |       -0.525692   |       0.0119809   |               22 |      -0.36646     |        0.0934538  |               22 |           -0.392411  |          0.00842275  |                  44 |     0.0115611   |  -0.339198  |             22 |            22 |
| hf_power                        |       -0.551666   |       0.00777712  |               22 |      -0.418408    |        0.0526322  |               22 |           -0.431906  |          0.00341637  |                  44 |     0.00145753  |  -0.587858  |             22 |            22 |
| signal_skewness                 |        0.351779   |       0.108389    |               22 |       0.565217    |        0.0061226  |               22 |            0.468863  |          0.00132632  |                  44 |     0.0150447   |   0.487726  |             22 |            22 |
| peak_trend_slope                |       -0.617165   |       0.0022148   |               22 |      -0.435347    |        0.0428613  |               22 |           -0.50864   |          0.000422842 |                  44 |     0.000311139 |  -0.633734  |             22 |            22 |
| systolic_area                   |       -0.579898   |       0.004671    |               22 |      -0.369848    |        0.090235   |               22 |           -0.486353  |          0.00081602  |                  44 |     0.002008    |  -0.537769  |             22 |            22 |
| diastolic_area                  |       -0.630717   |       0.0016494   |               22 |      -0.436477    |        0.0422641  |               22 |           -0.513718  |          0.000361706 |                  44 |     0.00145753  |  -0.570099  |             22 |            22 |
| systolic_amplitude_variability  |       -0.00282326 |       0.990051    |               22 |       0.181254    |        0.419523   |               22 |            0.0953523 |          0.538097    |                  44 |     0.613522    |   0.124654  |             22 |            22 |
| diastolic_amplitude_variability |       -0.176736   |       0.431398    |               22 |       0.157538    |        0.483816   |               22 |            0.023697  |          0.878647    |                  44 |     0.8972      |  -0.0818172 |             22 |            22 |

### Feature Correlations Heatmap

![Feature Correlations](plots\general\noradrenalin\noradrenalin_feature_correlations.png)

#### sdnn by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\sdnn_noradrenalin_quartiles.png)

Description of sdnn_noradrenalin_quartiles.png:
This boxplot shows SDNN across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how sdnn varies with Noradrenalin levels.

#### rmssd by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\rmssd_noradrenalin_quartiles.png)

Description of rmssd_noradrenalin_quartiles.png:
This boxplot shows RMSSD across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how rmssd varies with Noradrenalin levels.

#### poincare_sd1 by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\poincare_sd1_noradrenalin_quartiles.png)

Description of poincare_sd1_noradrenalin_quartiles.png:
This boxplot shows POINCARE_SD1 across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how poincare_sd1 varies with Noradrenalin levels.

#### poincare_sd2 by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\poincare_sd2_noradrenalin_quartiles.png)

Description of poincare_sd2_noradrenalin_quartiles.png:
This boxplot shows POINCARE_SD2 across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how poincare_sd2 varies with Noradrenalin levels.

#### systolic_duration by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\systolic_duration_noradrenalin_quartiles.png)

Description of systolic_duration_noradrenalin_quartiles.png:
This boxplot shows SYSTOLIC_DURATION across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_duration varies with Noradrenalin levels.

#### diastolic_duration by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\diastolic_duration_noradrenalin_quartiles.png)

Description of diastolic_duration_noradrenalin_quartiles.png:
This boxplot shows DIASTOLIC_DURATION across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_duration varies with Noradrenalin levels.

#### systolic_slope by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\systolic_slope_noradrenalin_quartiles.png)

Description of systolic_slope_noradrenalin_quartiles.png:
This boxplot shows SYSTOLIC_SLOPE across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_slope varies with Noradrenalin levels.

#### diastolic_slope by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\diastolic_slope_noradrenalin_quartiles.png)

Description of diastolic_slope_noradrenalin_quartiles.png:
This boxplot shows DIASTOLIC_SLOPE across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_slope varies with Noradrenalin levels.

#### heart_rate by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\heart_rate_noradrenalin_quartiles.png)

Description of heart_rate_noradrenalin_quartiles.png:
This boxplot shows HEART_RATE across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how heart_rate varies with Noradrenalin levels.

#### sample_entropy by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\sample_entropy_noradrenalin_quartiles.png)

Description of sample_entropy_noradrenalin_quartiles.png:
This boxplot shows SAMPLE_ENTROPY across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how sample_entropy varies with Noradrenalin levels.

#### nn50 by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\nn50_noradrenalin_quartiles.png)

Description of nn50_noradrenalin_quartiles.png:
This boxplot shows NN50 across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how nn50 varies with Noradrenalin levels.

#### pnn50 by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\pnn50_noradrenalin_quartiles.png)

Description of pnn50_noradrenalin_quartiles.png:
This boxplot shows PNN50 across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how pnn50 varies with Noradrenalin levels.

#### hrv_triangular_index by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\hrv_triangular_index_noradrenalin_quartiles.png)

Description of hrv_triangular_index_noradrenalin_quartiles.png:
This boxplot shows HRV_TRIANGULAR_INDEX across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how hrv_triangular_index varies with Noradrenalin levels.

#### lf_power by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\lf_power_noradrenalin_quartiles.png)

Description of lf_power_noradrenalin_quartiles.png:
This boxplot shows LF_POWER across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how lf_power varies with Noradrenalin levels.

#### hf_power by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\hf_power_noradrenalin_quartiles.png)

Description of hf_power_noradrenalin_quartiles.png:
This boxplot shows HF_POWER across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how hf_power varies with Noradrenalin levels.

#### signal_skewness by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\signal_skewness_noradrenalin_quartiles.png)

Description of signal_skewness_noradrenalin_quartiles.png:
This boxplot shows SIGNAL_SKEWNESS across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how signal_skewness varies with Noradrenalin levels.

#### peak_trend_slope by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\peak_trend_slope_noradrenalin_quartiles.png)

Description of peak_trend_slope_noradrenalin_quartiles.png:
This boxplot shows PEAK_TREND_SLOPE across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how peak_trend_slope varies with Noradrenalin levels.

#### systolic_area by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\systolic_area_noradrenalin_quartiles.png)

Description of systolic_area_noradrenalin_quartiles.png:
This boxplot shows SYSTOLIC_AREA across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_area varies with Noradrenalin levels.

#### diastolic_area by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\diastolic_area_noradrenalin_quartiles.png)

Description of diastolic_area_noradrenalin_quartiles.png:
This boxplot shows DIASTOLIC_AREA across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_area varies with Noradrenalin levels.

#### systolic_amplitude_variability by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\systolic_amplitude_variability_noradrenalin_quartiles.png)

Description of systolic_amplitude_variability_noradrenalin_quartiles.png:
This boxplot shows SYSTOLIC_AMPLITUDE_VARIABILITY across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how systolic_amplitude_variability varies with Noradrenalin levels.

#### diastolic_amplitude_variability by Noradrenalin Quartiles

![Boxplot](plots\general\noradrenalin\diastolic_amplitude_variability_noradrenalin_quartiles.png)

Description of diastolic_amplitude_variability_noradrenalin_quartiles.png:
This boxplot shows DIASTOLIC_AMPLITUDE_VARIABILITY across Noradrenalin quartiles (Q1 to Q4, low to high).
Boxes represent IQR, with median lines and whiskers (1.5*IQR).
Differences in medians or spread suggest how diastolic_amplitude_variability varies with Noradrenalin levels.

#### Scatter Plot: Noradrenalin vs sdnn

![Scatter](plots\general\noradrenalin\noradrenalin_vs_sdnn.png)

#### Scatter Plot: Noradrenalin vs rmssd

![Scatter](plots\general\noradrenalin\noradrenalin_vs_rmssd.png)

#### Scatter Plot: Noradrenalin vs poincare_sd1

![Scatter](plots\general\noradrenalin\noradrenalin_vs_poincare_sd1.png)

#### Scatter Plot: Noradrenalin vs poincare_sd2

![Scatter](plots\general\noradrenalin\noradrenalin_vs_poincare_sd2.png)

#### Scatter Plot: Noradrenalin vs systolic_duration

![Scatter](plots\general\noradrenalin\noradrenalin_vs_systolic_duration.png)

#### Scatter Plot: Noradrenalin vs diastolic_duration

![Scatter](plots\general\noradrenalin\noradrenalin_vs_diastolic_duration.png)

#### Scatter Plot: Noradrenalin vs systolic_slope

![Scatter](plots\general\noradrenalin\noradrenalin_vs_systolic_slope.png)

#### Scatter Plot: Noradrenalin vs diastolic_slope

![Scatter](plots\general\noradrenalin\noradrenalin_vs_diastolic_slope.png)

#### Scatter Plot: Noradrenalin vs heart_rate

![Scatter](plots\general\noradrenalin\noradrenalin_vs_heart_rate.png)

#### Scatter Plot: Noradrenalin vs sample_entropy

![Scatter](plots\general\noradrenalin\noradrenalin_vs_sample_entropy.png)

#### Scatter Plot: Noradrenalin vs nn50

![Scatter](plots\general\noradrenalin\noradrenalin_vs_nn50.png)

#### Scatter Plot: Noradrenalin vs pnn50

![Scatter](plots\general\noradrenalin\noradrenalin_vs_pnn50.png)

#### Scatter Plot: Noradrenalin vs hrv_triangular_index

![Scatter](plots\general\noradrenalin\noradrenalin_vs_hrv_triangular_index.png)

#### Scatter Plot: Noradrenalin vs lf_power

![Scatter](plots\general\noradrenalin\noradrenalin_vs_lf_power.png)

#### Scatter Plot: Noradrenalin vs hf_power

![Scatter](plots\general\noradrenalin\noradrenalin_vs_hf_power.png)

#### Scatter Plot: Noradrenalin vs signal_skewness

![Scatter](plots\general\noradrenalin\noradrenalin_vs_signal_skewness.png)

#### Scatter Plot: Noradrenalin vs peak_trend_slope

![Scatter](plots\general\noradrenalin\noradrenalin_vs_peak_trend_slope.png)

#### Scatter Plot: Noradrenalin vs systolic_area

![Scatter](plots\general\noradrenalin\noradrenalin_vs_systolic_area.png)

#### Scatter Plot: Noradrenalin vs diastolic_area

![Scatter](plots\general\noradrenalin\noradrenalin_vs_diastolic_area.png)

#### Scatter Plot: Noradrenalin vs systolic_amplitude_variability

![Scatter](plots\general\noradrenalin\noradrenalin_vs_systolic_amplitude_variability.png)

#### Scatter Plot: Noradrenalin vs diastolic_amplitude_variability

![Scatter](plots\general\noradrenalin\noradrenalin_vs_diastolic_amplitude_variability.png)

# Feature: SDNN

## Day Comparison

![Day Comparison](plots\sdnn\sdnn_day_comparison.png)

Description of sdnn_day_comparison.png:
Boxplot with connected lines showing SDNN from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 8, Decrease: 14, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for sdnn:
Total patients: 22
Increasing: 8 (36.4%)
Decreasing: 14 (63.6%)
No change: 0
Mean change: -653.86
Median change: -285.75
Paired test (Wilcoxon): p = 0.085, effect size = 0.64

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.085).
The change shows an overall decrease with medium effect size (0.64).
36.4% of patients showed increase, suggesting potential trend in sdnn.

```

### Change Histogram

![Change Histogram](plots\sdnn\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in SDNN from Day1 to Day5.
Centered around -285.75, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\sdnn\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in SDNN to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\sdnn\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for SDNN on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   sdnn   R-squared:                       0.002
Model:                            OLS   Adj. R-squared:                 -0.047
Method:                 Least Squares   F-statistic:                   0.04970
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.826
Time:                        09:45:27   Log-Likelihood:                -190.02
No. Observations:                  22   AIC:                             384.0
Df Residuals:                      20   BIC:                             386.2
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1175.9663    384.275      3.060      0.006     374.383    1977.550
Adrenalin      0.0089      0.040      0.223      0.826      -0.075       0.093
==============================================================================
Omnibus:                       12.741   Durbin-Watson:                   1.938
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               10.980
Skew:                           1.587   Prob(JB):                      0.00413
Kurtosis:                       4.382   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for sdnn (Linear OLS) on Day1:
R-squared: 0.002 - Explains 0.2% of variance.
Coefficient for Adrenalin: 0.009 (p=0.826)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.844, p=0.174
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 3.684 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\sdnn\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for sdnn using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\sdnn\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of sdnn (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\sdnn\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for sdnn (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\sdnn\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for sdnn (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\sdnn\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SDNN vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\sdnn\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SDNN vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   sdnn   R-squared:                       0.030
Model:                            OLS   Adj. R-squared:                 -0.019
Method:                 Least Squares   F-statistic:                    0.6136
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.443
Time:                        09:45:30   Log-Likelihood:                -168.22
No. Observations:                  22   AIC:                             340.4
Df Residuals:                      20   BIC:                             342.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    642.1313    142.644      4.502      0.000     344.580     939.682
Adrenalin     -0.0117      0.015     -0.783      0.443      -0.043       0.019
==============================================================================
Omnibus:                        6.215   Durbin-Watson:                   2.369
Prob(Omnibus):                  0.045   Jarque-Bera (JB):                4.213
Skew:                           1.031   Prob(JB):                        0.122
Kurtosis:                       3.585   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for sdnn (Linear OLS) on Day5:
R-squared: 0.030 - Explains 3.0% of variance.
Coefficient for Adrenalin: -0.012 (p=0.443)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.032, p=0.310
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.005
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.502 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\sdnn\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for sdnn using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\sdnn\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of sdnn (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\sdnn\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for sdnn (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\sdnn\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for sdnn (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\sdnn\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SDNN vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\sdnn\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SDNN vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   sdnn   R-squared:                       0.081
Model:                            OLS   Adj. R-squared:                  0.035
Method:                 Least Squares   F-statistic:                     1.763
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.199
Time:                        09:48:34   Log-Likelihood:                -189.12
No. Observations:                  22   AIC:                             382.2
Df Residuals:                      20   BIC:                             384.4
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     1507.0057    360.416      4.181      0.000     755.192    2258.819
Noradrenalin    -0.0068      0.005     -1.328      0.199      -0.017       0.004
==============================================================================
Omnibus:                       12.227   Durbin-Watson:                   2.103
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               10.279
Skew:                           1.507   Prob(JB):                      0.00586
Kurtosis:                       4.461   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for sdnn (Linear OLS) on Day1:
R-squared: 0.081 - Explains 8.1% of variance.
Coefficient for Noradrenalin: -0.007 (p=0.199)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.070, p=0.301
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.280 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\sdnn\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for sdnn using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\sdnn\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of sdnn (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\sdnn\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for sdnn (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\sdnn\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for sdnn (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\sdnn\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SDNN vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\sdnn\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SDNN vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   sdnn   R-squared:                       0.006
Model:                            OLS   Adj. R-squared:                 -0.044
Method:                 Least Squares   F-statistic:                    0.1136
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.740
Time:                        09:48:41   Log-Likelihood:                -168.49
No. Observations:                  22   AIC:                             341.0
Df Residuals:                      20   BIC:                             343.2
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      601.9219    141.107      4.266      0.000     307.577     896.267
Noradrenalin    -0.0007      0.002     -0.337      0.740      -0.005       0.003
==============================================================================
Omnibus:                        8.552   Durbin-Watson:                   2.361
Prob(Omnibus):                  0.014   Jarque-Bera (JB):                6.236
Skew:                           1.206   Prob(JB):                       0.0443
Kurtosis:                       3.994   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for sdnn (Linear OLS) on Day5:
R-squared: 0.006 - Explains 0.6% of variance.
Coefficient for Noradrenalin: -0.001 (p=0.740)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.065, p=0.799
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.007
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.429 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\sdnn\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for sdnn using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\sdnn\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of sdnn (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\sdnn\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for sdnn (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\sdnn\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for sdnn (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\sdnn\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SDNN vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\sdnn\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SDNN vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: RMSSD

## Day Comparison

![Day Comparison](plots\rmssd\rmssd_day_comparison.png)

Description of rmssd_day_comparison.png:
Boxplot with connected lines showing RMSSD from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 9, Decrease: 13, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for rmssd:
Total patients: 22
Increasing: 9 (40.9%)
Decreasing: 13 (59.1%)
No change: 0
Mean change: -1017.43
Median change: -374.23
Paired test (Wilcoxon): p = 0.085, effect size = 0.64

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.085).
The change shows an overall decrease with medium effect size (0.64).
40.9% of patients showed increase, suggesting potential trend in rmssd.

```

### Change Histogram

![Change Histogram](plots\rmssd\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in RMSSD from Day1 to Day5.
Centered around -374.23, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\rmssd\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in RMSSD to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\rmssd\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for RMSSD on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  rmssd   R-squared:                       0.009
Model:                            OLS   Adj. R-squared:                 -0.040
Method:                 Least Squares   F-statistic:                    0.1830
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.673
Time:                        09:45:33   Log-Likelihood:                -200.62
No. Observations:                  22   AIC:                             405.2
Df Residuals:                      20   BIC:                             407.4
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1669.6336    622.037      2.684      0.014     372.088    2967.179
Adrenalin      0.0277      0.065      0.428      0.673      -0.108       0.163
==============================================================================
Omnibus:                       17.025   Durbin-Watson:                   1.978
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               17.347
Skew:                           1.778   Prob(JB):                     0.000171
Kurtosis:                       5.507   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for rmssd (Linear OLS) on Day1:
R-squared: 0.009 - Explains 0.9% of variance.
Coefficient for Adrenalin: 0.028 (p=0.673)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=2.858, p=0.091
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 4.969 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\rmssd\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for rmssd using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\rmssd\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of rmssd (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\rmssd\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for rmssd (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\rmssd\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for rmssd (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\rmssd\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of RMSSD vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\rmssd\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of RMSSD vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  rmssd   R-squared:                       0.032
Model:                            OLS   Adj. R-squared:                 -0.016
Method:                 Least Squares   F-statistic:                    0.6652
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.424
Time:                        09:45:36   Log-Likelihood:                -177.18
No. Observations:                  22   AIC:                             358.4
Df Residuals:                      20   BIC:                             360.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    920.2711    214.300      4.294      0.000     473.249    1367.294
Adrenalin     -0.0182      0.022     -0.816      0.424      -0.065       0.028
==============================================================================
Omnibus:                       10.804   Durbin-Watson:                   2.398
Prob(Omnibus):                  0.005   Jarque-Bera (JB):                8.583
Skew:                           1.300   Prob(JB):                       0.0137
Kurtosis:                       4.615   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for rmssd (Linear OLS) on Day5:
R-squared: 0.032 - Explains 3.2% of variance.
Coefficient for Adrenalin: -0.018 (p=0.424)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.878, p=0.349
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.002
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.533 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\rmssd\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for rmssd using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\rmssd\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of rmssd (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\rmssd\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for rmssd (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\rmssd\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for rmssd (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\rmssd\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of RMSSD vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\rmssd\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of RMSSD vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  rmssd   R-squared:                       0.073
Model:                            OLS   Adj. R-squared:                  0.027
Method:                 Least Squares   F-statistic:                     1.586
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.222
Time:                        09:48:50   Log-Likelihood:                -199.88
No. Observations:                  22   AIC:                             403.8
Df Residuals:                      20   BIC:                             405.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     2262.9516    587.739      3.850      0.001    1036.949    3488.954
Noradrenalin    -0.0104      0.008     -1.259      0.222      -0.028       0.007
==============================================================================
Omnibus:                       19.088   Durbin-Watson:                   2.141
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               21.794
Skew:                           1.847   Prob(JB):                     1.85e-05
Kurtosis:                       6.183   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for rmssd (Linear OLS) on Day1:
R-squared: 0.073 - Explains 7.3% of variance.
Coefficient for Noradrenalin: -0.010 (p=0.222)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.719, p=0.397
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.309 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\rmssd\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for rmssd using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\rmssd\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of rmssd (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\rmssd\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for rmssd (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\rmssd\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for rmssd (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\rmssd\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of RMSSD vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\rmssd\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of RMSSD vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  rmssd   R-squared:                       0.003
Model:                            OLS   Adj. R-squared:                 -0.047
Method:                 Least Squares   F-statistic:                   0.05308
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.820
Time:                        09:48:57   Log-Likelihood:                -177.51
No. Observations:                  22   AIC:                             359.0
Df Residuals:                      20   BIC:                             361.2
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      842.5525    212.577      3.964      0.001     399.125    1285.980
Noradrenalin    -0.0007      0.003     -0.230      0.820      -0.007       0.006
==============================================================================
Omnibus:                       13.236   Durbin-Watson:                   2.421
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               11.704
Skew:                           1.469   Prob(JB):                      0.00287
Kurtosis:                       5.035   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for rmssd (Linear OLS) on Day5:
R-squared: 0.003 - Explains 0.3% of variance.
Coefficient for Noradrenalin: -0.001 (p=0.820)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.039, p=0.844
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.002
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.397 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\rmssd\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for rmssd using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\rmssd\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of rmssd (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\rmssd\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for rmssd (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\rmssd\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for rmssd (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\rmssd\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of RMSSD vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\rmssd\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of RMSSD vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: POINCARE_SD1

## Day Comparison

![Day Comparison](plots\poincare_sd1\poincare_sd1_day_comparison.png)

Description of poincare_sd1_day_comparison.png:
Boxplot with connected lines showing POINCARE_SD1 from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 8, Decrease: 14, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for poincare_sd1:
Total patients: 22
Increasing: 8 (36.4%)
Decreasing: 14 (63.6%)
No change: 0
Mean change: -659.20
Median change: -309.14
Paired test (Wilcoxon): p = 0.063, effect size = 0.64

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.063).
The change shows an overall decrease with medium effect size (0.64).
36.4% of patients showed increase, suggesting potential trend in poincare_sd1.

```

### Change Histogram

![Change Histogram](plots\poincare_sd1\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in POINCARE_SD1 from Day1 to Day5.
Centered around -309.14, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\poincare_sd1\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in POINCARE_SD1 to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\poincare_sd1\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for POINCARE_SD1 on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd1   R-squared:                       0.000
Model:                            OLS   Adj. R-squared:                 -0.050
Method:                 Least Squares   F-statistic:                  0.003563
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.953
Time:                        09:45:39   Log-Likelihood:                -189.45
No. Observations:                  22   AIC:                             382.9
Df Residuals:                      20   BIC:                             385.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1243.4442    374.360      3.322      0.003     462.543    2024.345
Adrenalin     -0.0023      0.039     -0.060      0.953      -0.084       0.079
==============================================================================
Omnibus:                        8.150   Durbin-Watson:                   1.754
Prob(Omnibus):                  0.017   Jarque-Bera (JB):                6.748
Skew:                           1.351   Prob(JB):                       0.0342
Kurtosis:                       3.241   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd1 (Linear OLS) on Day1:
R-squared: 0.000 - Explains 0.0% of variance.
Coefficient for Adrenalin: -0.002 (p=0.953)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.595, p=0.441
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 2.100 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd1\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd1 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd1\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of poincare_sd1 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd1\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd1 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd1\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for poincare_sd1 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd1\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of POINCARE_SD1 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd1\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of POINCARE_SD1 vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd1   R-squared:                       0.032
Model:                            OLS   Adj. R-squared:                 -0.016
Method:                 Least Squares   F-statistic:                    0.6670
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.424
Time:                        09:45:41   Log-Likelihood:                -168.65
No. Observations:                  22   AIC:                             341.3
Df Residuals:                      20   BIC:                             343.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    642.8748    145.432      4.420      0.000     339.509     946.240
Adrenalin     -0.0124      0.015     -0.817      0.424      -0.044       0.019
==============================================================================
Omnibus:                        7.059   Durbin-Watson:                   2.372
Prob(Omnibus):                  0.029   Jarque-Bera (JB):                4.874
Skew:                           1.088   Prob(JB):                       0.0874
Kurtosis:                       3.762   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd1 (Linear OLS) on Day5:
R-squared: 0.032 - Explains 3.2% of variance.
Coefficient for Adrenalin: -0.012 (p=0.424)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.054, p=0.305
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.004
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.524 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd1\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd1 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd1\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of poincare_sd1 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd1\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd1 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd1\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for poincare_sd1 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd1\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of POINCARE_SD1 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd1\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of POINCARE_SD1 vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd1   R-squared:                       0.090
Model:                            OLS   Adj. R-squared:                  0.044
Method:                 Least Squares   F-statistic:                     1.968
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.176
Time:                        09:49:03   Log-Likelihood:                -188.42
No. Observations:                  22   AIC:                             380.8
Df Residuals:                      20   BIC:                             383.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     1515.3396    349.068      4.341      0.000     787.196    2243.483
Noradrenalin    -0.0069      0.005     -1.403      0.176      -0.017       0.003
==============================================================================
Omnibus:                        5.790   Durbin-Watson:                   1.903
Prob(Omnibus):                  0.055   Jarque-Bera (JB):                4.736
Skew:                           1.135   Prob(JB):                       0.0937
Kurtosis:                       2.884   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd1 (Linear OLS) on Day1:
R-squared: 0.090 - Explains 9.0% of variance.
Coefficient for Noradrenalin: -0.007 (p=0.176)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=2.025, p=0.155
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.331 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd1\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd1 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd1\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of poincare_sd1 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd1\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd1 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd1\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for poincare_sd1 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd1\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of POINCARE_SD1 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd1\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of POINCARE_SD1 vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd1   R-squared:                       0.002
Model:                            OLS   Adj. R-squared:                 -0.048
Method:                 Least Squares   F-statistic:                   0.04166
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.840
Time:                        09:49:07   Log-Likelihood:                -168.98
No. Observations:                  22   AIC:                             342.0
Df Residuals:                      20   BIC:                             344.2
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      587.8317    144.309      4.073      0.001     286.807     888.856
Noradrenalin    -0.0004      0.002     -0.204      0.840      -0.005       0.004
==============================================================================
Omnibus:                        9.454   Durbin-Watson:                   2.408
Prob(Omnibus):                  0.009   Jarque-Bera (JB):                7.112
Skew:                           1.263   Prob(JB):                       0.0285
Kurtosis:                       4.174   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd1 (Linear OLS) on Day5:
R-squared: 0.002 - Explains 0.2% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.840)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.133, p=0.716
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.005
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.466 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd1\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd1 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd1\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of poincare_sd1 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd1\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd1 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd1\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for poincare_sd1 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd1\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of POINCARE_SD1 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd1\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of POINCARE_SD1 vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: POINCARE_SD2

## Day Comparison

![Day Comparison](plots\poincare_sd2\poincare_sd2_day_comparison.png)

Description of poincare_sd2_day_comparison.png:
Boxplot with connected lines showing POINCARE_SD2 from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 8, Decrease: 14, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for poincare_sd2:
Total patients: 22
Increasing: 8 (36.4%)
Decreasing: 14 (63.6%)
No change: 0
Mean change: -620.62
Median change: -336.31
Paired test (Wilcoxon): p = 0.068, effect size = 0.65

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.068).
The change shows an overall decrease with medium effect size (0.65).
36.4% of patients showed increase, suggesting potential trend in poincare_sd2.

```

### Change Histogram

![Change Histogram](plots\poincare_sd2\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in POINCARE_SD2 from Day1 to Day5.
Centered around -336.31, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\poincare_sd2\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in POINCARE_SD2 to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\poincare_sd2\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for POINCARE_SD2 on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd2   R-squared:                       0.001
Model:                            OLS   Adj. R-squared:                 -0.049
Method:                 Least Squares   F-statistic:                   0.01854
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.893
Time:                        09:45:44   Log-Likelihood:                -188.05
No. Observations:                  22   AIC:                             380.1
Df Residuals:                      20   BIC:                             382.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1217.5411    351.383      3.465      0.002     484.569    1950.513
Adrenalin     -0.0050      0.037     -0.136      0.893      -0.081       0.071
==============================================================================
Omnibus:                       12.245   Durbin-Watson:                   1.885
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               10.425
Skew:                           1.568   Prob(JB):                      0.00545
Kurtosis:                       4.243   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd2 (Linear OLS) on Day1:
R-squared: 0.001 - Explains 0.1% of variance.
Coefficient for Adrenalin: -0.005 (p=0.893)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.106, p=0.744
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.675 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd2\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd2 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd2\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of poincare_sd2 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd2\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd2 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd2\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for poincare_sd2 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd2\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of POINCARE_SD2 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd2\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of POINCARE_SD2 vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd2   R-squared:                       0.025
Model:                            OLS   Adj. R-squared:                 -0.023
Method:                 Least Squares   F-statistic:                    0.5203
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.479
Time:                        09:45:47   Log-Likelihood:                -166.70
No. Observations:                  22   AIC:                             337.4
Df Residuals:                      20   BIC:                             339.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    626.2047    133.109      4.704      0.000     348.545     903.865
Adrenalin     -0.0100      0.014     -0.721      0.479      -0.039       0.019
==============================================================================
Omnibus:                        2.553   Durbin-Watson:                   2.306
Prob(Omnibus):                  0.279   Jarque-Bera (JB):                2.125
Skew:                           0.719   Prob(JB):                        0.346
Kurtosis:                       2.498   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd2 (Linear OLS) on Day5:
R-squared: 0.025 - Explains 2.5% of variance.
Coefficient for Adrenalin: -0.010 (p=0.479)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.356, p=0.244
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.009
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.464 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd2\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd2 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd2\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of poincare_sd2 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd2\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd2 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd2\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for poincare_sd2 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd2\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of POINCARE_SD2 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd2\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of POINCARE_SD2 vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd2   R-squared:                       0.086
Model:                            OLS   Adj. R-squared:                  0.040
Method:                 Least Squares   F-statistic:                     1.871
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.187
Time:                        09:49:12   Log-Likelihood:                -187.08
No. Observations:                  22   AIC:                             378.2
Df Residuals:                      20   BIC:                             380.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     1450.4092    328.491      4.415      0.000     765.189    2135.629
Noradrenalin    -0.0063      0.005     -1.368      0.187      -0.016       0.003
==============================================================================
Omnibus:                        9.931   Durbin-Watson:                   2.015
Prob(Omnibus):                  0.007   Jarque-Bera (JB):                7.826
Skew:                           1.383   Prob(JB):                       0.0200
Kurtosis:                       3.942   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd2 (Linear OLS) on Day1:
R-squared: 0.086 - Explains 8.6% of variance.
Coefficient for Noradrenalin: -0.006 (p=0.187)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.298, p=0.255
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.001
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.296 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd2\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd2 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd2\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of poincare_sd2 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd2\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd2 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd2\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for poincare_sd2 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd2\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of POINCARE_SD2 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd2\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of POINCARE_SD2 vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           poincare_sd2   R-squared:                       0.010
Model:                            OLS   Adj. R-squared:                 -0.040
Method:                 Least Squares   F-statistic:                    0.1989
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.660
Time:                        09:49:17   Log-Likelihood:                -166.87
No. Observations:                  22   AIC:                             337.7
Df Residuals:                      20   BIC:                             339.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      601.9154    131.098      4.591      0.000     328.449     875.382
Noradrenalin    -0.0008      0.002     -0.446      0.660      -0.005       0.003
==============================================================================
Omnibus:                        3.907   Durbin-Watson:                   2.263
Prob(Omnibus):                  0.142   Jarque-Bera (JB):                2.927
Skew:                           0.892   Prob(JB):                        0.231
Kurtosis:                       2.884   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for poincare_sd2 (Linear OLS) on Day5:
R-squared: 0.010 - Explains 1.0% of variance.
Coefficient for Noradrenalin: -0.001 (p=0.660)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.143, p=0.705
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.015
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.477 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\poincare_sd2\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for poincare_sd2 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\poincare_sd2\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of poincare_sd2 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\poincare_sd2\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for poincare_sd2 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\poincare_sd2\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for poincare_sd2 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\poincare_sd2\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of POINCARE_SD2 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\poincare_sd2\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of POINCARE_SD2 vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: SYSTOLIC_DURATION

## Day Comparison

![Day Comparison](plots\systolic_duration\systolic_duration_day_comparison.png)

Description of systolic_duration_day_comparison.png:
Boxplot with connected lines showing SYSTOLIC_DURATION from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 7, Decrease: 15, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for systolic_duration:
Total patients: 22
Increasing: 7 (31.8%)
Decreasing: 15 (68.2%)
No change: 0
Mean change: -0.16
Median change: -0.04
Paired test (Wilcoxon): p = 0.098, effect size = 0.67

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.098).
The change shows an overall decrease with medium effect size (0.67).
31.8% of patients showed increase, suggesting potential trend in systolic_duration.

```

### Change Histogram

![Change Histogram](plots\systolic_duration\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in SYSTOLIC_DURATION from Day1 to Day5.
Centered around -0.04, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\systolic_duration\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in SYSTOLIC_DURATION to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\systolic_duration\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for SYSTOLIC_DURATION on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      systolic_duration   R-squared:                       0.004
Model:                            OLS   Adj. R-squared:                 -0.046
Method:                 Least Squares   F-statistic:                   0.07319
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.790
Time:                        09:45:50   Log-Likelihood:                -9.7825
No. Observations:                  22   AIC:                             23.56
Df Residuals:                      20   BIC:                             25.75
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.6578      0.106      6.187      0.000       0.436       0.880
Adrenalin   2.999e-06   1.11e-05      0.271      0.790   -2.01e-05    2.61e-05
==============================================================================
Omnibus:                       16.390   Durbin-Watson:                   1.976
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               16.342
Skew:                           1.722   Prob(JB):                     0.000283
Kurtosis:                       5.442   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_duration (Linear OLS) on Day1:
R-squared: 0.004 - Explains 0.4% of variance.
Coefficient for Adrenalin: 0.000 (p=0.790)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=2.617, p=0.106
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 3.795 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_duration\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_duration using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_duration\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_duration (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_duration\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_duration (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_duration\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_duration (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_duration\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_DURATION vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_duration\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_DURATION vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      systolic_duration   R-squared:                       0.046
Model:                            OLS   Adj. R-squared:                 -0.001
Method:                 Least Squares   F-statistic:                    0.9709
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.336
Time:                        09:45:53   Log-Likelihood:               -0.14400
No. Observations:                  22   AIC:                             4.288
Df Residuals:                      20   BIC:                             6.470
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.5570      0.069      8.119      0.000       0.414       0.700
Adrenalin  -7.048e-06   7.15e-06     -0.985      0.336    -2.2e-05    7.87e-06
==============================================================================
Omnibus:                       41.115   Durbin-Watson:                   2.463
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              136.141
Skew:                           3.173   Prob(JB):                     2.74e-30
Kurtosis:                      13.404   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_duration (Linear OLS) on Day5:
R-squared: 0.046 - Explains 4.6% of variance.
Coefficient for Adrenalin: -0.000 (p=0.336)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.496, p=0.481
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.738 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_duration\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_duration using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_duration\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_duration (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_duration\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_duration (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_duration\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_duration (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_duration\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_DURATION vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_duration\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_DURATION vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      systolic_duration   R-squared:                       0.074
Model:                            OLS   Adj. R-squared:                  0.028
Method:                 Least Squares   F-statistic:                     1.609
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.219
Time:                        09:49:21   Log-Likelihood:                -8.9716
No. Observations:                  22   AIC:                             21.94
Df Residuals:                      20   BIC:                             24.13
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        0.7493      0.100      7.484      0.000       0.540       0.958
Noradrenalin -1.792e-06   1.41e-06     -1.268      0.219   -4.74e-06    1.16e-06
==============================================================================
Omnibus:                       17.602   Durbin-Watson:                   2.166
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               18.799
Skew:                           1.757   Prob(JB):                     8.28e-05
Kurtosis:                       5.857   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_duration (Linear OLS) on Day1:
R-squared: 0.074 - Explains 7.4% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.219)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.520, p=0.471
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.466 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_duration\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_duration using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_duration\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_duration (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_duration\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_duration (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_duration\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_duration (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_duration\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_DURATION vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_duration\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_DURATION vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      systolic_duration   R-squared:                       0.000
Model:                            OLS   Adj. R-squared:                 -0.050
Method:                 Least Squares   F-statistic:                  0.001133
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.973
Time:                        09:49:25   Log-Likelihood:               -0.66481
No. Observations:                  22   AIC:                             5.330
Df Residuals:                      20   BIC:                             7.512
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        0.5172      0.069      7.535      0.000       0.374       0.660
Noradrenalin -3.259e-08   9.68e-07     -0.034      0.973   -2.05e-06    1.99e-06
==============================================================================
Omnibus:                       42.584   Durbin-Watson:                   2.483
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              147.765
Skew:                           3.298   Prob(JB):                     8.19e-33
Kurtosis:                      13.849   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_duration (Linear OLS) on Day5:
R-squared: 0.000 - Explains 0.0% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.973)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.005, p=0.944
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.417 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_duration\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_duration using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_duration\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_duration (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_duration\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_duration (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_duration\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_duration (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_duration\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_DURATION vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_duration\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_DURATION vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: DIASTOLIC_DURATION

## Day Comparison

![Day Comparison](plots\diastolic_duration\diastolic_duration_day_comparison.png)

Description of diastolic_duration_day_comparison.png:
Boxplot with connected lines showing DIASTOLIC_DURATION from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 5, Decrease: 17, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for diastolic_duration:
Total patients: 22
Increasing: 5 (22.7%)
Decreasing: 17 (77.3%)
No change: 0
Mean change: -0.13
Median change: -0.08
Paired test (Wilcoxon): p = 0.011, effect size = 0.65

Interpretation:
There is a significant difference between Day1 and Day5 (p=0.011).
The change shows an overall decrease with medium effect size (0.65).
22.7% of patients showed increase, suggesting potential trend in diastolic_duration.

```

### Change Histogram

![Change Histogram](plots\diastolic_duration\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in DIASTOLIC_DURATION from Day1 to Day5.
Centered around -0.08, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\diastolic_duration\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in DIASTOLIC_DURATION to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\diastolic_duration\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for DIASTOLIC_DURATION on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:     diastolic_duration   R-squared:                       0.024
Model:                            OLS   Adj. R-squared:                 -0.025
Method:                 Least Squares   F-statistic:                    0.4933
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.491
Time:                        09:45:56   Log-Likelihood:                -4.8248
No. Observations:                  22   AIC:                             13.65
Df Residuals:                      20   BIC:                             15.83
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.5920      0.085      6.976      0.000       0.415       0.769
Adrenalin  -6.215e-06   8.85e-06     -0.702      0.491   -2.47e-05    1.22e-05
==============================================================================
Omnibus:                       29.235   Durbin-Watson:                   2.156
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               56.659
Skew:                           2.382   Prob(JB):                     4.97e-13
Kurtosis:                       9.254   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_duration (Linear OLS) on Day1:
R-squared: 0.024 - Explains 2.4% of variance.
Coefficient for Adrenalin: -0.000 (p=0.491)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.265, p=0.607
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.374 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_duration\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_duration using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_duration\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_duration (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_duration\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_duration (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_duration\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_duration (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_duration\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_DURATION vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_duration\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_DURATION vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:     diastolic_duration   R-squared:                       0.116
Model:                            OLS   Adj. R-squared:                  0.072
Method:                 Least Squares   F-statistic:                     2.621
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.121
Time:                        09:45:59   Log-Likelihood:                 14.620
No. Observations:                  22   AIC:                            -25.24
Df Residuals:                      20   BIC:                            -23.06
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.4595      0.035     13.106      0.000       0.386       0.533
Adrenalin  -5.919e-06   3.66e-06     -1.619      0.121   -1.35e-05    1.71e-06
==============================================================================
Omnibus:                        1.999   Durbin-Watson:                   2.221
Prob(Omnibus):                  0.368   Jarque-Bera (JB):                1.609
Skew:                           0.632   Prob(JB):                        0.447
Kurtosis:                       2.603   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_duration (Linear OLS) on Day5:
R-squared: 0.116 - Explains 11.6% of variance.
Coefficient for Adrenalin: -0.000 (p=0.121)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.818, p=0.178
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.215
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.352 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_duration\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_duration using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_duration\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_duration (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_duration\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_duration (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_duration\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_duration (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_duration\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_DURATION vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_duration\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_DURATION vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:     diastolic_duration   R-squared:                       0.098
Model:                            OLS   Adj. R-squared:                  0.053
Method:                 Least Squares   F-statistic:                     2.178
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.156
Time:                        09:49:29   Log-Likelihood:                -3.9559
No. Observations:                  22   AIC:                             11.91
Df Residuals:                      20   BIC:                             14.09
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        0.6243      0.080      7.832      0.000       0.458       0.791
Noradrenalin  -1.66e-06   1.12e-06     -1.476      0.156   -4.01e-06    6.86e-07
==============================================================================
Omnibus:                       30.323   Durbin-Watson:                   2.281
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               62.206
Skew:                           2.443   Prob(JB):                     3.11e-14
Kurtosis:                       9.633   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_duration (Linear OLS) on Day1:
R-squared: 0.098 - Explains 9.8% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.156)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.322, p=0.570
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.520 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_duration\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_duration using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_duration\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_duration (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_duration\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_duration (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_duration\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_duration (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_duration\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_DURATION vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_duration\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_DURATION vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:     diastolic_duration   R-squared:                       0.166
Model:                            OLS   Adj. R-squared:                  0.125
Method:                 Least Squares   F-statistic:                     3.986
Date:                Thu, 31 Jul 2025   Prob (F-statistic):             0.0597
Time:                        09:49:34   Log-Likelihood:                 15.265
No. Observations:                  22   AIC:                            -26.53
Df Residuals:                      20   BIC:                            -24.35
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        0.4638      0.033     13.938      0.000       0.394       0.533
Noradrenalin -9.374e-07    4.7e-07     -1.997      0.060   -1.92e-06     4.2e-08
==============================================================================
Omnibus:                        2.433   Durbin-Watson:                   2.214
Prob(Omnibus):                  0.296   Jarque-Bera (JB):                1.587
Skew:                           0.658   Prob(JB):                        0.452
Kurtosis:                       2.959   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_duration (Linear OLS) on Day5:
R-squared: 0.166 - Explains 16.6% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.060)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.927, p=0.336
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.348
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.385 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_duration\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_duration using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_duration\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_duration (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_duration\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_duration (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_duration\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_duration (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_duration\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_DURATION vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_duration\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_DURATION vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: SYSTOLIC_SLOPE

## Day Comparison

![Day Comparison](plots\systolic_slope\systolic_slope_day_comparison.png)

Description of systolic_slope_day_comparison.png:
Boxplot with connected lines showing SYSTOLIC_SLOPE from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 13, Decrease: 9, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for systolic_slope:
Total patients: 22
Increasing: 13 (59.1%)
Decreasing: 9 (40.9%)
No change: 0
Mean change: 0.07
Median change: 0.06
Paired test (t-test): p = 0.308, effect size = -0.22

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.308).
The change shows an overall increase with small effect size (-0.22).
59.1% of patients showed increase, suggesting potential trend in systolic_slope.

```

### Change Histogram

![Change Histogram](plots\systolic_slope\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in SYSTOLIC_SLOPE from Day1 to Day5.
Centered around 0.06, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\systolic_slope\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in SYSTOLIC_SLOPE to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\systolic_slope\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for SYSTOLIC_SLOPE on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         systolic_slope   R-squared:                       0.001
Model:                            OLS   Adj. R-squared:                 -0.048
Method:                 Least Squares   F-statistic:                   0.02980
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.865
Time:                        09:46:02   Log-Likelihood:                 3.3942
No. Observations:                  22   AIC:                            -2.788
Df Residuals:                      20   BIC:                           -0.6063
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      1.3010      0.058     22.275      0.000       1.179       1.423
Adrenalin   1.051e-06   6.09e-06      0.173      0.865   -1.17e-05    1.38e-05
==============================================================================
Omnibus:                        5.215   Durbin-Watson:                   1.775
Prob(Omnibus):                  0.074   Jarque-Bera (JB):                3.590
Skew:                          -0.978   Prob(JB):                        0.166
Kurtosis:                       3.300   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_slope (Linear OLS) on Day1:
R-squared: 0.001 - Explains 0.1% of variance.
Coefficient for Adrenalin: 0.000 (p=0.865)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.131, p=0.717
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.025
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 2.316 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_slope\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_slope using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_slope\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_slope (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_slope\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_slope (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_slope\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_slope (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_slope\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_SLOPE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_slope\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_SLOPE vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         systolic_slope   R-squared:                       0.040
Model:                            OLS   Adj. R-squared:                 -0.008
Method:                 Least Squares   F-statistic:                    0.8349
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.372
Time:                        09:46:05   Log-Likelihood:                 5.9704
No. Observations:                  22   AIC:                            -7.941
Df Residuals:                      20   BIC:                            -5.759
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      1.3507      0.052     25.999      0.000       1.242       1.459
Adrenalin    4.95e-06   5.42e-06      0.914      0.372   -6.35e-06    1.63e-05
==============================================================================
Omnibus:                       28.043   Durbin-Watson:                   1.620
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               51.997
Skew:                          -2.295   Prob(JB):                     5.12e-12
Kurtosis:                       8.972   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_slope (Linear OLS) on Day5:
R-squared: 0.040 - Explains 4.0% of variance.
Coefficient for Adrenalin: 0.000 (p=0.372)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.962, p=0.327
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.634 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_slope\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_slope using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_slope\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_slope (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_slope\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_slope (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_slope\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_slope (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_slope\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_SLOPE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_slope\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_SLOPE vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         systolic_slope   R-squared:                       0.041
Model:                            OLS   Adj. R-squared:                 -0.007
Method:                 Least Squares   F-statistic:                    0.8460
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.369
Time:                        09:49:38   Log-Likelihood:                 3.8335
No. Observations:                  22   AIC:                            -3.667
Df Residuals:                      20   BIC:                            -1.485
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        1.2771      0.056     22.829      0.000       1.160       1.394
Noradrenalin  7.261e-07   7.89e-07      0.920      0.369   -9.21e-07    2.37e-06
==============================================================================
Omnibus:                        3.848   Durbin-Watson:                   1.834
Prob(Omnibus):                  0.146   Jarque-Bera (JB):                2.716
Skew:                          -0.861   Prob(JB):                        0.257
Kurtosis:                       3.009   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_slope (Linear OLS) on Day1:
R-squared: 0.041 - Explains 4.1% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.369)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.856, p=0.355
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.028
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.221 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_slope\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_slope using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_slope\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_slope (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_slope\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_slope (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_slope\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_slope (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_slope\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_SLOPE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_slope\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_SLOPE vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         systolic_slope   R-squared:                       0.188
Model:                            OLS   Adj. R-squared:                  0.148
Method:                 Least Squares   F-statistic:                     4.642
Date:                Thu, 31 Jul 2025   Prob (F-statistic):             0.0436
Time:                        09:49:43   Log-Likelihood:                 7.8163
No. Observations:                  22   AIC:                            -11.63
Df Residuals:                      20   BIC:                            -9.451
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        1.4382      0.047     30.809      0.000       1.341       1.536
Noradrenalin -1.419e-06   6.59e-07     -2.154      0.044   -2.79e-06   -4.51e-08
==============================================================================
Omnibus:                       20.978   Durbin-Watson:                   2.460
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               27.599
Skew:                          -1.877   Prob(JB):                     1.02e-06
Kurtosis:                       7.002   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_slope (Linear OLS) on Day5:
R-squared: 0.188 - Explains 18.8% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.044)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=3.956, p=0.047
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.001
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.270 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_slope\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_slope using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_slope\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_slope (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_slope\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_slope (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_slope\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_slope (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_slope\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_SLOPE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_slope\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_SLOPE vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: DIASTOLIC_SLOPE

## Day Comparison

![Day Comparison](plots\diastolic_slope\diastolic_slope_day_comparison.png)

Description of diastolic_slope_day_comparison.png:
Boxplot with connected lines showing DIASTOLIC_SLOPE from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 7, Decrease: 15, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for diastolic_slope:
Total patients: 22
Increasing: 7 (31.8%)
Decreasing: 15 (68.2%)
No change: 0
Mean change: -0.07
Median change: -0.04
Paired test (t-test): p = 0.043, effect size = 0.46

Interpretation:
There is a significant difference between Day1 and Day5 (p=0.043).
The change shows an overall decrease with small effect size (0.46).
31.8% of patients showed increase, suggesting potential trend in diastolic_slope.

```

### Change Histogram

![Change Histogram](plots\diastolic_slope\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in DIASTOLIC_SLOPE from Day1 to Day5.
Centered around -0.04, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\diastolic_slope\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in DIASTOLIC_SLOPE to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\diastolic_slope\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for DIASTOLIC_SLOPE on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        diastolic_slope   R-squared:                       0.001
Model:                            OLS   Adj. R-squared:                 -0.049
Method:                 Least Squares   F-statistic:                   0.02534
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.875
Time:                        09:46:08   Log-Likelihood:                 12.542
No. Observations:                  22   AIC:                            -21.08
Df Residuals:                      20   BIC:                            -18.90
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -1.4378      0.039    -37.310      0.000      -1.518      -1.357
Adrenalin   6.397e-07   4.02e-06      0.159      0.875   -7.74e-06    9.02e-06
==============================================================================
Omnibus:                       13.678   Durbin-Watson:                   1.994
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               12.192
Skew:                           1.545   Prob(JB):                      0.00225
Kurtosis:                       4.939   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_slope (Linear OLS) on Day1:
R-squared: 0.001 - Explains 0.1% of variance.
Coefficient for Adrenalin: 0.000 (p=0.875)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=2.596, p=0.107
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.002
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 5.078 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_slope\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_slope using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_slope\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_slope (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_slope\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_slope (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_slope\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_slope (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_slope\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_SLOPE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_slope\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_SLOPE vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        diastolic_slope   R-squared:                       0.001
Model:                            OLS   Adj. R-squared:                 -0.049
Method:                 Least Squares   F-statistic:                   0.01286
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.911
Time:                        09:46:12   Log-Likelihood:                 28.125
No. Observations:                  22   AIC:                            -52.25
Df Residuals:                      20   BIC:                            -50.07
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -1.5056      0.019    -79.334      0.000      -1.545      -1.466
Adrenalin  -2.244e-07   1.98e-06     -0.113      0.911   -4.35e-06     3.9e-06
==============================================================================
Omnibus:                       13.512   Durbin-Watson:                   2.289
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               11.923
Skew:                           1.559   Prob(JB):                      0.00258
Kurtosis:                       4.812   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_slope (Linear OLS) on Day5:
R-squared: 0.001 - Explains 0.1% of variance.
Coefficient for Adrenalin: -0.000 (p=0.911)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.881, p=0.348
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.255 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_slope\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_slope using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_slope\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_slope (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_slope\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_slope (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_slope\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_slope (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_slope\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_SLOPE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_slope\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_SLOPE vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        diastolic_slope   R-squared:                       0.061
Model:                            OLS   Adj. R-squared:                  0.014
Method:                 Least Squares   F-statistic:                     1.301
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.267
Time:                        09:49:47   Log-Likelihood:                 13.221
No. Observations:                  22   AIC:                            -22.44
Df Residuals:                      20   BIC:                            -20.26
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       -1.4098      0.037    -38.612      0.000      -1.486      -1.334
Noradrenalin -5.877e-07   5.15e-07     -1.141      0.267   -1.66e-06    4.87e-07
==============================================================================
Omnibus:                       13.098   Durbin-Watson:                   2.153
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               11.481
Skew:                           1.469   Prob(JB):                      0.00321
Kurtosis:                       4.972   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_slope (Linear OLS) on Day1:
R-squared: 0.061 - Explains 6.1% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.267)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.934, p=0.334
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.003
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.267 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_slope\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_slope using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_slope\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_slope (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_slope\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_slope (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_slope\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_slope (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_slope\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_SLOPE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_slope\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_SLOPE vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        diastolic_slope   R-squared:                       0.020
Model:                            OLS   Adj. R-squared:                 -0.029
Method:                 Least Squares   F-statistic:                    0.4091
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.530
Time:                        09:49:51   Log-Likelihood:                 28.341
No. Observations:                  22   AIC:                            -52.68
Df Residuals:                      20   BIC:                            -50.50
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       -1.5138      0.018    -82.432      0.000      -1.552      -1.475
Noradrenalin  1.657e-07   2.59e-07      0.640      0.530   -3.75e-07    7.06e-07
==============================================================================
Omnibus:                       11.926   Durbin-Watson:                   2.528
Prob(Omnibus):                  0.003   Jarque-Bera (JB):                9.890
Skew:                           1.448   Prob(JB):                      0.00712
Kurtosis:                       4.549   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_slope (Linear OLS) on Day5:
R-squared: 0.020 - Explains 2.0% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.530)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.341, p=0.247
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.002
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.105 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_slope\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_slope using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_slope\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_slope (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_slope\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_slope (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_slope\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_slope (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_slope\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_SLOPE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_slope\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_SLOPE vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: HEART_RATE

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:             heart_rate   R-squared:                       0.036
Model:                            OLS   Adj. R-squared:                 -0.012
Method:                 Least Squares   F-statistic:                    0.7465
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.398
Time:                        09:46:15   Log-Likelihood:                -88.541
No. Observations:                  22   AIC:                             181.1
Df Residuals:                      20   BIC:                             183.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     73.6091      3.814     19.302      0.000      65.654      81.564
Adrenalin      0.0003      0.000      0.864      0.398      -0.000       0.001
==============================================================================
Omnibus:                        0.557   Durbin-Watson:                   1.334
Prob(Omnibus):                  0.757   Jarque-Bera (JB):                0.420
Skew:                           0.310   Prob(JB):                        0.811
Kurtosis:                       2.728   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for heart_rate (Linear OLS) on Day1:
R-squared: 0.036 - Explains 3.6% of variance.
Coefficient for Adrenalin: 0.000 (p=0.398)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.176, p=0.675
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.616
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 2.317 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\heart_rate\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for heart_rate using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\heart_rate\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of heart_rate (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\heart_rate\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for heart_rate (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\heart_rate\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for heart_rate (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\heart_rate\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of HEART_RATE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\heart_rate\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of HEART_RATE vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:             heart_rate   R-squared:                       0.160
Model:                            OLS   Adj. R-squared:                  0.118
Method:                 Least Squares   F-statistic:                     3.807
Date:                Thu, 31 Jul 2025   Prob (F-statistic):             0.0652
Time:                        09:46:18   Log-Likelihood:                -87.039
No. Observations:                  22   AIC:                             178.1
Df Residuals:                      20   BIC:                             180.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     77.5565      3.562     21.774      0.000      70.127      84.986
Adrenalin      0.0007      0.000      1.951      0.065   -5.01e-05       0.001
==============================================================================
Omnibus:                        0.604   Durbin-Watson:                   1.926
Prob(Omnibus):                  0.739   Jarque-Bera (JB):                0.644
Skew:                          -0.143   Prob(JB):                        0.725
Kurtosis:                       2.212   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for heart_rate (Linear OLS) on Day5:
R-squared: 0.160 - Explains 16.0% of variance.
Coefficient for Adrenalin: 0.001 (p=0.065)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.542, p=0.214
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.893
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.125 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\heart_rate\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for heart_rate using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\heart_rate\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of heart_rate (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\heart_rate\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for heart_rate (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\heart_rate\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for heart_rate (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\heart_rate\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of HEART_RATE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\heart_rate\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of HEART_RATE vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:             heart_rate   R-squared:                       0.053
Model:                            OLS   Adj. R-squared:                  0.006
Method:                 Least Squares   F-statistic:                     1.123
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.302
Time:                        09:49:56   Log-Likelihood:                -88.343
No. Observations:                  22   AIC:                             180.7
Df Residuals:                      20   BIC:                             182.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       73.3307      3.693     19.857      0.000      65.627      81.034
Noradrenalin  5.523e-05   5.21e-05      1.060      0.302   -5.35e-05       0.000
==============================================================================
Omnibus:                        0.318   Durbin-Watson:                   1.319
Prob(Omnibus):                  0.853   Jarque-Bera (JB):                0.262
Skew:                           0.227   Prob(JB):                        0.877
Kurtosis:                       2.719   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for heart_rate (Linear OLS) on Day1:
R-squared: 0.053 - Explains 5.3% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.302)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.120, p=0.729
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.769
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.628 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\heart_rate\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for heart_rate using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\heart_rate\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of heart_rate (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\heart_rate\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for heart_rate (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\heart_rate\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for heart_rate (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\heart_rate\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of HEART_RATE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\heart_rate\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of HEART_RATE vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:             heart_rate   R-squared:                       0.186
Model:                            OLS   Adj. R-squared:                  0.145
Method:                 Least Squares   F-statistic:                     4.573
Date:                Thu, 31 Jul 2025   Prob (F-statistic):             0.0450
Time:                        09:50:00   Log-Likelihood:                -86.691
No. Observations:                  22   AIC:                             177.4
Df Residuals:                      20   BIC:                             179.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       77.5109      3.426     22.626      0.000      70.365      84.657
Noradrenalin     0.0001   4.83e-05      2.139      0.045    2.54e-06       0.000
==============================================================================
Omnibus:                        1.201   Durbin-Watson:                   1.922
Prob(Omnibus):                  0.549   Jarque-Bera (JB):                0.837
Skew:                          -0.031   Prob(JB):                        0.658
Kurtosis:                       2.047   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for heart_rate (Linear OLS) on Day5:
R-squared: 0.186 - Explains 18.6% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.045)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.334, p=0.563
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.861
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.711 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\heart_rate\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for heart_rate using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\heart_rate\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of heart_rate (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\heart_rate\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for heart_rate (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\heart_rate\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for heart_rate (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\heart_rate\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of HEART_RATE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\heart_rate\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of HEART_RATE vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: SAMPLE_ENTROPY

## Vs Adrenalin

### Day1

### Day5

## Vs Noradrenalin

### Day1

### Day5

# Feature: NN50

## Day Comparison

![Day Comparison](plots\nn50\nn50_day_comparison.png)

Description of nn50_day_comparison.png:
Boxplot with connected lines showing NN50 from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 7, Decrease: 15, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for nn50:
Total patients: 22
Increasing: 7 (31.8%)
Decreasing: 15 (68.2%)
No change: 0
Mean change: -4.62
Median change: -9.05
Paired test (Wilcoxon): p = 0.276, effect size = 0.56

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.276).
The change shows an overall decrease with medium effect size (0.56).
31.8% of patients showed increase, suggesting potential trend in nn50.

```

### Change Histogram

![Change Histogram](plots\nn50\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in NN50 from Day1 to Day5.
Centered around -9.05, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\nn50\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in NN50 to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\nn50\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for NN50 on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   nn50   R-squared:                       0.072
Model:                            OLS   Adj. R-squared:                  0.026
Method:                 Least Squares   F-statistic:                     1.554
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.227
Time:                        09:46:22   Log-Likelihood:                -109.14
No. Observations:                  22   AIC:                             222.3
Df Residuals:                      20   BIC:                             224.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     82.7702      9.728      8.508      0.000      62.478     103.063
Adrenalin     -0.0013      0.001     -1.247      0.227      -0.003       0.001
==============================================================================
Omnibus:                        0.530   Durbin-Watson:                   1.784
Prob(Omnibus):                  0.767   Jarque-Bera (JB):                0.055
Skew:                           0.116   Prob(JB):                        0.973
Kurtosis:                       3.077   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for nn50 (Linear OLS) on Day1:
R-squared: 0.072 - Explains 7.2% of variance.
Coefficient for Adrenalin: -0.001 (p=0.227)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.345, p=0.557
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.704
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.600 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\nn50\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for nn50 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\nn50\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of nn50 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\nn50\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for nn50 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\nn50\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for nn50 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\nn50\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of NN50 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\nn50\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of NN50 vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   nn50   R-squared:                       0.047
Model:                            OLS   Adj. R-squared:                 -0.000
Method:                 Least Squares   F-statistic:                    0.9905
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.332
Time:                        09:46:25   Log-Likelihood:                -110.90
No. Observations:                  22   AIC:                             225.8
Df Residuals:                      20   BIC:                             228.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     77.1530     10.535      7.323      0.000      55.177      99.129
Adrenalin     -0.0011      0.001     -0.995      0.332      -0.003       0.001
==============================================================================
Omnibus:                        1.167   Durbin-Watson:                   1.948
Prob(Omnibus):                  0.558   Jarque-Bera (JB):                1.038
Skew:                           0.471   Prob(JB):                        0.595
Kurtosis:                       2.506   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for nn50 (Linear OLS) on Day5:
R-squared: 0.047 - Explains 4.7% of variance.
Coefficient for Adrenalin: -0.001 (p=0.332)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.455, p=0.500
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.453
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.155 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\nn50\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for nn50 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\nn50\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of nn50 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\nn50\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for nn50 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\nn50\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for nn50 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\nn50\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of NN50 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\nn50\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of NN50 vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   nn50   R-squared:                       0.062
Model:                            OLS   Adj. R-squared:                  0.015
Method:                 Least Squares   F-statistic:                     1.328
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.263
Time:                        09:50:04   Log-Likelihood:                -109.26
No. Observations:                  22   AIC:                             222.5
Df Residuals:                      20   BIC:                             224.7
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       81.8158      9.556      8.562      0.000      61.882     101.750
Noradrenalin    -0.0002      0.000     -1.152      0.263      -0.000       0.000
==============================================================================
Omnibus:                        0.311   Durbin-Watson:                   1.495
Prob(Omnibus):                  0.856   Jarque-Bera (JB):                0.031
Skew:                           0.088   Prob(JB):                        0.985
Kurtosis:                       2.949   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for nn50 (Linear OLS) on Day1:
R-squared: 0.062 - Explains 6.2% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.263)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.204, p=0.651
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.628
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.063 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\nn50\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for nn50 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\nn50\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of nn50 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\nn50\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for nn50 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\nn50\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for nn50 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\nn50\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of NN50 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\nn50\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of NN50 vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   nn50   R-squared:                       0.029
Model:                            OLS   Adj. R-squared:                 -0.020
Method:                 Least Squares   F-statistic:                    0.5958
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.449
Time:                        09:50:08   Log-Likelihood:                -111.11
No. Observations:                  22   AIC:                             226.2
Df Residuals:                      20   BIC:                             228.4
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       66.1013     10.393      6.360      0.000      44.422      87.780
Noradrenalin     0.0001      0.000      0.772      0.449      -0.000       0.000
==============================================================================
Omnibus:                        1.598   Durbin-Watson:                   2.175
Prob(Omnibus):                  0.450   Jarque-Bera (JB):                1.049
Skew:                           0.530   Prob(JB):                        0.592
Kurtosis:                       2.858   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for nn50 (Linear OLS) on Day5:
R-squared: 0.029 - Explains 2.9% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.449)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.000, p=0.985
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.412
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.789 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\nn50\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for nn50 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\nn50\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of nn50 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\nn50\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for nn50 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\nn50\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for nn50 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\nn50\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of NN50 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\nn50\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of NN50 vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: PNN50

## Day Comparison

![Day Comparison](plots\pnn50\pnn50_day_comparison.png)

Description of pnn50_day_comparison.png:
Boxplot with connected lines showing PNN50 from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 4, Decrease: 18, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for pnn50:
Total patients: 22
Increasing: 4 (18.2%)
Decreasing: 18 (81.8%)
No change: 0
Mean change: -8.42
Median change: -7.31
Paired test (t-test): p = 0.031, effect size = 0.49

Interpretation:
There is a significant difference between Day1 and Day5 (p=0.031).
The change shows an overall decrease with small effect size (0.49).
18.2% of patients showed increase, suggesting potential trend in pnn50.

```

### Change Histogram

![Change Histogram](plots\pnn50\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in PNN50 from Day1 to Day5.
Centered around -7.31, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\pnn50\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in PNN50 to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\pnn50\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for PNN50 on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  pnn50   R-squared:                       0.055
Model:                            OLS   Adj. R-squared:                  0.008
Method:                 Least Squares   F-statistic:                     1.168
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.293
Time:                        09:46:29   Log-Likelihood:                -93.707
No. Observations:                  22   AIC:                             191.4
Df Residuals:                      20   BIC:                             193.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     35.1800      4.823      7.294      0.000      25.120      45.240
Adrenalin     -0.0005      0.001     -1.081      0.293      -0.002       0.001
==============================================================================
Omnibus:                        0.350   Durbin-Watson:                   2.146
Prob(Omnibus):                  0.839   Jarque-Bera (JB):                0.498
Skew:                           0.034   Prob(JB):                        0.780
Kurtosis:                       2.266   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for pnn50 (Linear OLS) on Day1:
R-squared: 0.055 - Explains 5.5% of variance.
Coefficient for Adrenalin: -0.001 (p=0.293)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.746, p=0.388
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.842
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.171 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\pnn50\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for pnn50 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\pnn50\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of pnn50 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\pnn50\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for pnn50 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\pnn50\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for pnn50 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\pnn50\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of PNN50 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\pnn50\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of PNN50 vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  pnn50   R-squared:                       0.063
Model:                            OLS   Adj. R-squared:                  0.016
Method:                 Least Squares   F-statistic:                     1.350
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.259
Time:                        09:46:32   Log-Likelihood:                -89.332
No. Observations:                  22   AIC:                             182.7
Df Residuals:                      20   BIC:                             184.8
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     26.3837      3.953      6.674      0.000      18.138      34.630
Adrenalin     -0.0005      0.000     -1.162      0.259      -0.001       0.000
==============================================================================
Omnibus:                        6.288   Durbin-Watson:                   2.123
Prob(Omnibus):                  0.043   Jarque-Bera (JB):                3.981
Skew:                           0.857   Prob(JB):                        0.137
Kurtosis:                       4.185   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for pnn50 (Linear OLS) on Day5:
R-squared: 0.063 - Explains 6.3% of variance.
Coefficient for Adrenalin: -0.000 (p=0.259)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.368, p=0.544
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.174
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.271 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\pnn50\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for pnn50 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\pnn50\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of pnn50 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\pnn50\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for pnn50 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\pnn50\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for pnn50 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\pnn50\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of PNN50 vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\pnn50\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of PNN50 vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  pnn50   R-squared:                       0.127
Model:                            OLS   Adj. R-squared:                  0.084
Method:                 Least Squares   F-statistic:                     2.917
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.103
Time:                        09:50:12   Log-Likelihood:                -92.834
No. Observations:                  22   AIC:                             189.7
Df Residuals:                      20   BIC:                             191.8
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       36.5203      4.529      8.063      0.000      27.072      45.968
Noradrenalin    -0.0001   6.39e-05     -1.708      0.103      -0.000    2.42e-05
==============================================================================
Omnibus:                        0.119   Durbin-Watson:                   2.033
Prob(Omnibus):                  0.942   Jarque-Bera (JB):                0.334
Skew:                           0.083   Prob(JB):                        0.846
Kurtosis:                       2.420   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for pnn50 (Linear OLS) on Day1:
R-squared: 0.127 - Explains 12.7% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.103)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.094, p=0.759
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.857
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 2.130 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\pnn50\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for pnn50 using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\pnn50\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of pnn50 (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\pnn50\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for pnn50 (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\pnn50\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for pnn50 (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\pnn50\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of PNN50 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\pnn50\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of PNN50 vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  pnn50   R-squared:                       0.001
Model:                            OLS   Adj. R-squared:                 -0.049
Method:                 Least Squares   F-statistic:                   0.01679
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.898
Time:                        09:50:16   Log-Likelihood:                -90.041
No. Observations:                  22   AIC:                             184.1
Df Residuals:                      20   BIC:                             186.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       23.8922      3.989      5.989      0.000      15.571      32.214
Noradrenalin -7.293e-06   5.63e-05     -0.130      0.898      -0.000       0.000
==============================================================================
Omnibus:                        6.955   Durbin-Watson:                   2.221
Prob(Omnibus):                  0.031   Jarque-Bera (JB):                4.592
Skew:                           0.918   Prob(JB):                        0.101
Kurtosis:                       4.281   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for pnn50 (Linear OLS) on Day5:
R-squared: 0.001 - Explains 0.1% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.898)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.534, p=0.465
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.092
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.302 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\pnn50\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for pnn50 using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\pnn50\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of pnn50 (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\pnn50\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for pnn50 (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\pnn50\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for pnn50 (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\pnn50\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of PNN50 vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\pnn50\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of PNN50 vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: HRV_TRIANGULAR_INDEX

## Day Comparison

![Day Comparison](plots\hrv_triangular_index\hrv_triangular_index_day_comparison.png)

Description of hrv_triangular_index_day_comparison.png:
Boxplot with connected lines showing HRV_TRIANGULAR_INDEX from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 11, Decrease: 11, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for hrv_triangular_index:
Total patients: 22
Increasing: 11 (50.0%)
Decreasing: 11 (50.0%)
No change: 0
Mean change: 0.09
Median change: 0.11
Paired test (t-test): p = 0.706, effect size = -0.08

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.706).
The change shows an overall increase with small effect size (-0.08).
50.0% of patients showed increase, suggesting potential trend in hrv_triangular_index.

```

### Change Histogram

![Change Histogram](plots\hrv_triangular_index\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in HRV_TRIANGULAR_INDEX from Day1 to Day5.
Centered around 0.11, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\hrv_triangular_index\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in HRV_TRIANGULAR_INDEX to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\hrv_triangular_index\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for HRV_TRIANGULAR_INDEX on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                             OLS Regression Results                             
================================================================================
Dep. Variable:     hrv_triangular_index   R-squared:                       0.020
Model:                              OLS   Adj. R-squared:                 -0.029
Method:                   Least Squares   F-statistic:                    0.4105
Date:                  Thu, 31 Jul 2025   Prob (F-statistic):              0.529
Time:                          09:46:35   Log-Likelihood:                -23.048
No. Observations:                    22   AIC:                             50.10
Df Residuals:                        20   BIC:                             52.28
Df Model:                             1                                         
Covariance Type:              nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      4.1395      0.194     21.306      0.000       3.734       4.545
Adrenalin   1.298e-05   2.03e-05      0.641      0.529   -2.93e-05    5.52e-05
==============================================================================
Omnibus:                        2.581   Durbin-Watson:                   1.149
Prob(Omnibus):                  0.275   Jarque-Bera (JB):                2.077
Skew:                          -0.633   Prob(JB):                        0.354
Kurtosis:                       2.186   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hrv_triangular_index (Linear OLS) on Day1:
R-squared: 0.020 - Explains 2.0% of variance.
Coefficient for Adrenalin: 0.000 (p=0.529)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.302, p=0.582
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.023
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 3.318 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hrv_triangular_index\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for hrv_triangular_index using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hrv_triangular_index\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of hrv_triangular_index (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hrv_triangular_index\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hrv_triangular_index (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hrv_triangular_index\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for hrv_triangular_index (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hrv_triangular_index\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of HRV_TRIANGULAR_INDEX vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hrv_triangular_index\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of HRV_TRIANGULAR_INDEX vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                             OLS Regression Results                             
================================================================================
Dep. Variable:     hrv_triangular_index   R-squared:                       0.001
Model:                              OLS   Adj. R-squared:                 -0.048
Method:                   Least Squares   F-statistic:                   0.02937
Date:                  Thu, 31 Jul 2025   Prob (F-statistic):              0.866
Time:                          09:46:39   Log-Likelihood:                -28.574
No. Observations:                    22   AIC:                             61.15
Df Residuals:                        20   BIC:                             63.33
Df Model:                             1                                         
Covariance Type:              nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      4.3296      0.250     17.335      0.000       3.809       4.851
Adrenalin  -4.463e-06    2.6e-05     -0.171      0.866   -5.88e-05    4.99e-05
==============================================================================
Omnibus:                        5.852   Durbin-Watson:                   1.563
Prob(Omnibus):                  0.054   Jarque-Bera (JB):                2.252
Skew:                          -0.432   Prob(JB):                        0.324
Kurtosis:                       1.693   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hrv_triangular_index (Linear OLS) on Day5:
R-squared: 0.001 - Explains 0.1% of variance.
Coefficient for Adrenalin: -0.000 (p=0.866)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=2.702, p=0.100
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.022
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.794 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hrv_triangular_index\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for hrv_triangular_index using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hrv_triangular_index\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of hrv_triangular_index (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hrv_triangular_index\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hrv_triangular_index (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hrv_triangular_index\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for hrv_triangular_index (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hrv_triangular_index\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of HRV_TRIANGULAR_INDEX vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hrv_triangular_index\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of HRV_TRIANGULAR_INDEX vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                             OLS Regression Results                             
================================================================================
Dep. Variable:     hrv_triangular_index   R-squared:                       0.004
Model:                              OLS   Adj. R-squared:                 -0.046
Method:                   Least Squares   F-statistic:                   0.07989
Date:                  Thu, 31 Jul 2025   Prob (F-statistic):              0.780
Time:                          09:50:21   Log-Likelihood:                -23.228
No. Observations:                    22   AIC:                             50.46
Df Residuals:                        20   BIC:                             52.64
Df Model:                             1                                         
Covariance Type:              nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        4.1836      0.191     21.857      0.000       3.784       4.583
Noradrenalin  7.634e-07    2.7e-06      0.283      0.780   -4.87e-06     6.4e-06
==============================================================================
Omnibus:                        2.116   Durbin-Watson:                   1.104
Prob(Omnibus):                  0.347   Jarque-Bera (JB):                1.690
Skew:                          -0.535   Prob(JB):                        0.430
Kurtosis:                       2.165   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hrv_triangular_index (Linear OLS) on Day1:
R-squared: 0.004 - Explains 0.4% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.780)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.000, p=0.990
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.081
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.261 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hrv_triangular_index\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for hrv_triangular_index using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hrv_triangular_index\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of hrv_triangular_index (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hrv_triangular_index\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hrv_triangular_index (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hrv_triangular_index\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for hrv_triangular_index (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hrv_triangular_index\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of HRV_TRIANGULAR_INDEX vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hrv_triangular_index\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of HRV_TRIANGULAR_INDEX vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                             OLS Regression Results                             
================================================================================
Dep. Variable:     hrv_triangular_index   R-squared:                       0.331
Model:                              OLS   Adj. R-squared:                  0.297
Method:                   Least Squares   F-statistic:                     9.893
Date:                  Thu, 31 Jul 2025   Prob (F-statistic):            0.00509
Time:                          09:50:25   Log-Likelihood:                -24.169
No. Observations:                    22   AIC:                             52.34
Df Residuals:                        20   BIC:                             54.52
Df Model:                             1                                         
Covariance Type:              nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        4.6699      0.200     23.376      0.000       4.253       5.087
Noradrenalin -8.866e-06   2.82e-06     -3.145      0.005   -1.47e-05   -2.99e-06
==============================================================================
Omnibus:                        2.386   Durbin-Watson:                   1.886
Prob(Omnibus):                  0.303   Jarque-Bera (JB):                1.693
Skew:                          -0.487   Prob(JB):                        0.429
Kurtosis:                       2.053   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hrv_triangular_index (Linear OLS) on Day5:
R-squared: 0.331 - Explains 33.1% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.005)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.018, p=0.892
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.125
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.405 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hrv_triangular_index\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for hrv_triangular_index using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hrv_triangular_index\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of hrv_triangular_index (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hrv_triangular_index\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hrv_triangular_index (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hrv_triangular_index\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for hrv_triangular_index (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hrv_triangular_index\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of HRV_TRIANGULAR_INDEX vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hrv_triangular_index\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of HRV_TRIANGULAR_INDEX vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: LF_POWER

## Day Comparison

![Day Comparison](plots\lf_power\lf_power_day_comparison.png)

Description of lf_power_day_comparison.png:
Boxplot with connected lines showing LF_POWER from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 10, Decrease: 12, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for lf_power:
Total patients: 22
Increasing: 10 (45.5%)
Decreasing: 12 (54.5%)
No change: 0
Mean change: -26652.60
Median change: -10409.04
Paired test (Wilcoxon): p = 0.337, effect size = 0.65

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.337).
The change shows an overall decrease with medium effect size (0.65).
45.5% of patients showed increase, suggesting potential trend in lf_power.

```

### Change Histogram

![Change Histogram](plots\lf_power\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in LF_POWER from Day1 to Day5.
Centered around -10409.04, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\lf_power\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in LF_POWER to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\lf_power\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for LF_POWER on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               lf_power   R-squared:                       0.040
Model:                            OLS   Adj. R-squared:                 -0.008
Method:                 Least Squares   F-statistic:                    0.8418
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.370
Time:                        09:46:43   Log-Likelihood:                -280.10
No. Observations:                  22   AIC:                             564.2
Df Residuals:                      20   BIC:                             566.4
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    8.21e+04   2.31e+04      3.561      0.002     3.4e+04     1.3e+05
Adrenalin     -2.2056      2.404     -0.918      0.370      -7.220       2.809
==============================================================================
Omnibus:                       14.676   Durbin-Watson:                   1.754
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               13.577
Skew:                           1.630   Prob(JB):                      0.00113
Kurtosis:                       5.046   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for lf_power (Linear OLS) on Day1:
R-squared: 0.040 - Explains 4.0% of variance.
Coefficient for Adrenalin: -2.206 (p=0.370)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.807, p=0.369
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.261 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\lf_power\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for lf_power using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\lf_power\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of lf_power (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\lf_power\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for lf_power (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\lf_power\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for lf_power (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\lf_power\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of LF_POWER vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\lf_power\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of LF_POWER vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               lf_power   R-squared:                       0.048
Model:                            OLS   Adj. R-squared:                  0.000
Method:                 Least Squares   F-statistic:                     1.000
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.329
Time:                        09:46:46   Log-Likelihood:                -273.78
No. Observations:                  22   AIC:                             551.6
Df Residuals:                      20   BIC:                             553.7
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   5.311e+04   1.73e+04      3.070      0.006     1.7e+04    8.92e+04
Adrenalin     -1.8048      1.804     -1.000      0.329      -5.569       1.959
==============================================================================
Omnibus:                       23.815   Durbin-Watson:                   2.235
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               35.401
Skew:                           2.064   Prob(JB):                     2.05e-08
Kurtosis:                       7.646   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for lf_power (Linear OLS) on Day5:
R-squared: 0.048 - Explains 4.8% of variance.
Coefficient for Adrenalin: -1.805 (p=0.329)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.799, p=0.371
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.878 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\lf_power\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for lf_power using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\lf_power\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of lf_power (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\lf_power\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for lf_power (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\lf_power\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for lf_power (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\lf_power\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of LF_POWER vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\lf_power\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of LF_POWER vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               lf_power   R-squared:                       0.102
Model:                            OLS   Adj. R-squared:                  0.057
Method:                 Least Squares   F-statistic:                     2.268
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.148
Time:                        09:50:30   Log-Likelihood:                -279.37
No. Observations:                  22   AIC:                             562.7
Df Residuals:                      20   BIC:                             564.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     8.838e+04   2.18e+04      4.055      0.001    4.29e+04    1.34e+05
Noradrenalin    -0.4631      0.308     -1.506      0.148      -1.105       0.178
==============================================================================
Omnibus:                       13.613   Durbin-Watson:                   1.742
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               12.073
Skew:                           1.556   Prob(JB):                      0.00239
Kurtosis:                       4.869   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for lf_power (Linear OLS) on Day1:
R-squared: 0.102 - Explains 10.2% of variance.
Coefficient for Noradrenalin: -0.463 (p=0.148)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.080, p=0.299
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.001
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.582 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\lf_power\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for lf_power using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\lf_power\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of lf_power (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\lf_power\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for lf_power (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\lf_power\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for lf_power (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\lf_power\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of LF_POWER vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\lf_power\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of LF_POWER vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               lf_power   R-squared:                       0.014
Model:                            OLS   Adj. R-squared:                 -0.035
Method:                 Least Squares   F-statistic:                    0.2920
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.595
Time:                        09:50:34   Log-Likelihood:                -274.16
No. Observations:                  22   AIC:                             552.3
Df Residuals:                      20   BIC:                             554.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     3.717e+04   1.72e+04      2.161      0.043    1291.897    7.31e+04
Noradrenalin     0.1312      0.243      0.540      0.595      -0.375       0.637
==============================================================================
Omnibus:                       21.739   Durbin-Watson:                   2.582
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               28.686
Skew:                           1.969   Prob(JB):                     5.90e-07
Kurtosis:                       6.974   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for lf_power (Linear OLS) on Day5:
R-squared: 0.014 - Explains 1.4% of variance.
Coefficient for Noradrenalin: 0.131 (p=0.595)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=3.392, p=0.066
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.327 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\lf_power\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for lf_power using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\lf_power\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of lf_power (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\lf_power\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for lf_power (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\lf_power\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for lf_power (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\lf_power\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of LF_POWER vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\lf_power\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of LF_POWER vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: HF_POWER

## Day Comparison

![Day Comparison](plots\hf_power\hf_power_day_comparison.png)

Description of hf_power_day_comparison.png:
Boxplot with connected lines showing HF_POWER from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 9, Decrease: 13, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for hf_power:
Total patients: 22
Increasing: 9 (40.9%)
Decreasing: 13 (59.1%)
No change: 0
Mean change: -164316.29
Median change: -23965.69
Paired test (Wilcoxon): p = 0.129, effect size = 0.67

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.129).
The change shows an overall decrease with medium effect size (0.67).
40.9% of patients showed increase, suggesting potential trend in hf_power.

```

### Change Histogram

![Change Histogram](plots\hf_power\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in HF_POWER from Day1 to Day5.
Centered around -23965.69, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\hf_power\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in HF_POWER to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\hf_power\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for HF_POWER on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               hf_power   R-squared:                       0.029
Model:                            OLS   Adj. R-squared:                 -0.019
Method:                 Least Squares   F-statistic:                    0.6062
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.445
Time:                        09:46:51   Log-Likelihood:                -319.64
No. Observations:                  22   AIC:                             643.3
Df Residuals:                      20   BIC:                             645.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    3.47e+05   1.39e+05      2.495      0.021    5.69e+04    6.37e+05
Adrenalin    -11.2929     14.505     -0.779      0.445     -41.549      18.964
==============================================================================
Omnibus:                       25.192   Durbin-Watson:                   0.997
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               35.980
Skew:                           2.301   Prob(JB):                     1.54e-08
Kurtosis:                       7.252   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hf_power (Linear OLS) on Day1:
R-squared: 0.029 - Explains 2.9% of variance.
Coefficient for Adrenalin: -11.293 (p=0.445)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.765, p=0.382
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.397 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hf_power\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for hf_power using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hf_power\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of hf_power (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hf_power\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hf_power (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hf_power\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for hf_power (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hf_power\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of HF_POWER vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hf_power\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of HF_POWER vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               hf_power   R-squared:                       0.025
Model:                            OLS   Adj. R-squared:                 -0.023
Method:                 Least Squares   F-statistic:                    0.5188
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.480
Time:                        09:47:00   Log-Likelihood:                -298.54
No. Observations:                  22   AIC:                             601.1
Df Residuals:                      20   BIC:                             603.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1.402e+05   5.33e+04      2.630      0.016     2.9e+04    2.51e+05
Adrenalin     -4.0040      5.559     -0.720      0.480     -15.600       7.592
==============================================================================
Omnibus:                       16.126   Durbin-Watson:                   2.127
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               15.662
Skew:                           1.775   Prob(JB):                     0.000397
Kurtosis:                       5.119   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hf_power (Linear OLS) on Day5:
R-squared: 0.025 - Explains 2.5% of variance.
Coefficient for Adrenalin: -4.004 (p=0.480)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.530, p=0.467
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.286 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hf_power\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for hf_power using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hf_power\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of hf_power (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hf_power\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hf_power (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hf_power\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for hf_power (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hf_power\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of HF_POWER vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hf_power\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of HF_POWER vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               hf_power   R-squared:                       0.086
Model:                            OLS   Adj. R-squared:                  0.041
Method:                 Least Squares   F-statistic:                     1.889
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.185
Time:                        09:50:40   Log-Likelihood:                -318.97
No. Observations:                  22   AIC:                             641.9
Df Residuals:                      20   BIC:                             644.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     3.869e+05   1.32e+05      2.933      0.008    1.12e+05    6.62e+05
Noradrenalin    -2.5573      1.861     -1.374      0.185      -6.439       1.324
==============================================================================
Omnibus:                       24.288   Durbin-Watson:                   1.051
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               33.749
Skew:                           2.224   Prob(JB):                     4.69e-08
Kurtosis:                       7.126   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hf_power (Linear OLS) on Day1:
R-squared: 0.086 - Explains 8.6% of variance.
Coefficient for Noradrenalin: -2.557 (p=0.185)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.200, p=0.273
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.381 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hf_power\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for hf_power using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hf_power\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of hf_power (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hf_power\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hf_power (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hf_power\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for hf_power (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hf_power\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of HF_POWER vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hf_power\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of HF_POWER vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               hf_power   R-squared:                       0.007
Model:                            OLS   Adj. R-squared:                 -0.043
Method:                 Least Squares   F-statistic:                    0.1358
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.716
Time:                        09:50:45   Log-Likelihood:                -298.75
No. Observations:                  22   AIC:                             601.5
Df Residuals:                      20   BIC:                             603.7
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     1.282e+05   5.26e+04      2.438      0.024    1.85e+04    2.38e+05
Noradrenalin    -0.2734      0.742     -0.369      0.716      -1.821       1.274
==============================================================================
Omnibus:                       16.941   Durbin-Watson:                   2.006
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               16.942
Skew:                           1.839   Prob(JB):                     0.000210
Kurtosis:                       5.227   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for hf_power (Linear OLS) on Day5:
R-squared: 0.007 - Explains 0.7% of variance.
Coefficient for Noradrenalin: -0.273 (p=0.716)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.105, p=0.745
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.424 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\hf_power\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for hf_power using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\hf_power\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of hf_power (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\hf_power\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for hf_power (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\hf_power\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for hf_power (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\hf_power\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of HF_POWER vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\hf_power\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of HF_POWER vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: SIGNAL_SKEWNESS

## Day Comparison

![Day Comparison](plots\signal_skewness\signal_skewness_day_comparison.png)

Description of signal_skewness_day_comparison.png:
Boxplot with connected lines showing SIGNAL_SKEWNESS from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 7, Decrease: 15, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for signal_skewness:
Total patients: 22
Increasing: 7 (31.8%)
Decreasing: 15 (68.2%)
No change: 0
Mean change: -0.03
Median change: -0.06
Paired test (t-test): p = 0.360, effect size = 0.20

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.360).
The change shows an overall decrease with small effect size (0.20).
31.8% of patients showed increase, suggesting potential trend in signal_skewness.

```

### Change Histogram

![Change Histogram](plots\signal_skewness\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in SIGNAL_SKEWNESS from Day1 to Day5.
Centered around -0.06, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\signal_skewness\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in SIGNAL_SKEWNESS to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\signal_skewness\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for SIGNAL_SKEWNESS on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        signal_skewness   R-squared:                       0.055
Model:                            OLS   Adj. R-squared:                  0.008
Method:                 Least Squares   F-statistic:                     1.168
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.293
Time:                        09:47:08   Log-Likelihood:                 10.205
No. Observations:                  22   AIC:                            -16.41
Df Residuals:                      20   BIC:                            -14.23
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.1124      0.043      2.623      0.016       0.023       0.202
Adrenalin   4.829e-06   4.47e-06      1.081      0.293   -4.49e-06    1.42e-05
==============================================================================
Omnibus:                        3.770   Durbin-Watson:                   1.747
Prob(Omnibus):                  0.152   Jarque-Bera (JB):                1.947
Skew:                           0.621   Prob(JB):                        0.378
Kurtosis:                       3.761   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for signal_skewness (Linear OLS) on Day1:
R-squared: 0.055 - Explains 5.5% of variance.
Coefficient for Adrenalin: 0.000 (p=0.293)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.717, p=0.397
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.746
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.182 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\signal_skewness\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for signal_skewness using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\signal_skewness\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of signal_skewness (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\signal_skewness\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for signal_skewness (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\signal_skewness\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for signal_skewness (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\signal_skewness\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SIGNAL_SKEWNESS vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\signal_skewness\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SIGNAL_SKEWNESS vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        signal_skewness   R-squared:                       0.009
Model:                            OLS   Adj. R-squared:                 -0.041
Method:                 Least Squares   F-statistic:                    0.1790
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.677
Time:                        09:47:16   Log-Likelihood:                 11.411
No. Observations:                  22   AIC:                            -18.82
Df Residuals:                      20   BIC:                            -16.64
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.1180      0.041      2.909      0.009       0.033       0.203
Adrenalin   -1.79e-06   4.23e-06     -0.423      0.677   -1.06e-05    7.03e-06
==============================================================================
Omnibus:                        0.631   Durbin-Watson:                   2.120
Prob(Omnibus):                  0.729   Jarque-Bera (JB):                0.692
Skew:                          -0.237   Prob(JB):                        0.708
Kurtosis:                       2.272   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for signal_skewness (Linear OLS) on Day5:
R-squared: 0.009 - Explains 0.9% of variance.
Coefficient for Adrenalin: -0.000 (p=0.677)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.492, p=0.483
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.935
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 3.296 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\signal_skewness\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for signal_skewness using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\signal_skewness\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of signal_skewness (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\signal_skewness\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for signal_skewness (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\signal_skewness\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for signal_skewness (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\signal_skewness\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SIGNAL_SKEWNESS vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\signal_skewness\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SIGNAL_SKEWNESS vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        signal_skewness   R-squared:                       0.012
Model:                            OLS   Adj. R-squared:                 -0.037
Method:                 Least Squares   F-statistic:                    0.2521
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.621
Time:                        09:50:50   Log-Likelihood:                 9.7191
No. Observations:                  22   AIC:                            -15.44
Df Residuals:                      20   BIC:                            -13.26
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        0.1280      0.043      2.990      0.007       0.039       0.217
Noradrenalin  3.033e-07   6.04e-07      0.502      0.621   -9.57e-07    1.56e-06
==============================================================================
Omnibus:                        1.020   Durbin-Watson:                   1.758
Prob(Omnibus):                  0.601   Jarque-Bera (JB):                0.329
Skew:                           0.291   Prob(JB):                        0.848
Kurtosis:                       3.145   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for signal_skewness (Linear OLS) on Day1:
R-squared: 0.012 - Explains 1.2% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.621)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.527, p=0.217
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.993
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.048 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\signal_skewness\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for signal_skewness using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\signal_skewness\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of signal_skewness (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\signal_skewness\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for signal_skewness (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\signal_skewness\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for signal_skewness (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\signal_skewness\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SIGNAL_SKEWNESS vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\signal_skewness\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SIGNAL_SKEWNESS vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        signal_skewness   R-squared:                       0.235
Model:                            OLS   Adj. R-squared:                  0.196
Method:                 Least Squares   F-statistic:                     6.132
Date:                Thu, 31 Jul 2025   Prob (F-statistic):             0.0223
Time:                        09:50:55   Log-Likelihood:                 14.255
No. Observations:                  22   AIC:                            -24.51
Df Residuals:                      20   BIC:                            -22.33
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        0.0573      0.035      1.645      0.116      -0.015       0.130
Noradrenalin  1.217e-06   4.92e-07      2.476      0.022    1.92e-07    2.24e-06
==============================================================================
Omnibus:                        0.183   Durbin-Watson:                   2.616
Prob(Omnibus):                  0.913   Jarque-Bera (JB):                0.384
Skew:                           0.117   Prob(JB):                        0.825
Kurtosis:                       2.396   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for signal_skewness (Linear OLS) on Day5:
R-squared: 0.235 - Explains 23.5% of variance.
Coefficient for Noradrenalin: 0.000 (p=0.022)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.777, p=0.378
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.873
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.610 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\signal_skewness\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for signal_skewness using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\signal_skewness\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of signal_skewness (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\signal_skewness\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for signal_skewness (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\signal_skewness\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for signal_skewness (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\signal_skewness\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SIGNAL_SKEWNESS vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\signal_skewness\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SIGNAL_SKEWNESS vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: PEAK_TREND_SLOPE

## Day Comparison

![Day Comparison](plots\peak_trend_slope\peak_trend_slope_day_comparison.png)

Description of peak_trend_slope_day_comparison.png:
Boxplot with connected lines showing PEAK_TREND_SLOPE from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 7, Decrease: 15, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for peak_trend_slope:
Total patients: 22
Increasing: 7 (31.8%)
Decreasing: 15 (68.2%)
No change: 0
Mean change: -36.75
Median change: -14.70
Paired test (Wilcoxon): p = 0.028, effect size = 0.65

Interpretation:
There is a significant difference between Day1 and Day5 (p=0.028).
The change shows an overall decrease with medium effect size (0.65).
31.8% of patients showed increase, suggesting potential trend in peak_trend_slope.

```

### Change Histogram

![Change Histogram](plots\peak_trend_slope\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in PEAK_TREND_SLOPE from Day1 to Day5.
Centered around -14.70, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\peak_trend_slope\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in PEAK_TREND_SLOPE to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\peak_trend_slope\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for PEAK_TREND_SLOPE on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:       peak_trend_slope   R-squared:                       0.010
Model:                            OLS   Adj. R-squared:                 -0.040
Method:                 Least Squares   F-statistic:                    0.1999
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.660
Time:                        09:47:24   Log-Likelihood:                -127.70
No. Observations:                  22   AIC:                             259.4
Df Residuals:                      20   BIC:                             261.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    123.1417     22.611      5.446      0.000      75.975     170.308
Adrenalin      0.0011      0.002      0.447      0.660      -0.004       0.006
==============================================================================
Omnibus:                       19.680   Durbin-Watson:                   2.214
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               22.467
Skew:                           1.937   Prob(JB):                     1.32e-05
Kurtosis:                       6.083   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for peak_trend_slope (Linear OLS) on Day1:
R-squared: 0.010 - Explains 1.0% of variance.
Coefficient for Adrenalin: 0.001 (p=0.660)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=2.380, p=0.123
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 4.235 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\peak_trend_slope\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for peak_trend_slope using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\peak_trend_slope\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of peak_trend_slope (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\peak_trend_slope\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for peak_trend_slope (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\peak_trend_slope\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for peak_trend_slope (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\peak_trend_slope\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of PEAK_TREND_SLOPE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\peak_trend_slope\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of PEAK_TREND_SLOPE vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:       peak_trend_slope   R-squared:                       0.093
Model:                            OLS   Adj. R-squared:                  0.047
Method:                 Least Squares   F-statistic:                     2.043
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.168
Time:                        09:47:31   Log-Likelihood:                -105.00
No. Observations:                  22   AIC:                             214.0
Df Residuals:                      20   BIC:                             216.2
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     99.5404      8.058     12.354      0.000      82.733     116.348
Adrenalin     -0.0012      0.001     -1.429      0.168      -0.003       0.001
==============================================================================
Omnibus:                       24.141   Durbin-Watson:                   2.576
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               39.168
Skew:                           1.998   Prob(JB):                     3.12e-09
Kurtosis:                       8.173   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for peak_trend_slope (Linear OLS) on Day5:
R-squared: 0.093 - Explains 9.3% of variance.
Coefficient for Adrenalin: -0.001 (p=0.168)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.635, p=0.425
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.001
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.713 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\peak_trend_slope\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for peak_trend_slope using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\peak_trend_slope\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of peak_trend_slope (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\peak_trend_slope\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for peak_trend_slope (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\peak_trend_slope\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for peak_trend_slope (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\peak_trend_slope\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of PEAK_TREND_SLOPE vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\peak_trend_slope\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of PEAK_TREND_SLOPE vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:       peak_trend_slope   R-squared:                       0.083
Model:                            OLS   Adj. R-squared:                  0.037
Method:                 Least Squares   F-statistic:                     1.813
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.193
Time:                        09:51:01   Log-Likelihood:                -126.85
No. Observations:                  22   AIC:                             257.7
Df Residuals:                      20   BIC:                             259.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      145.9773     21.262      6.866      0.000     101.625     190.330
Noradrenalin    -0.0004      0.000     -1.346      0.193      -0.001       0.000
==============================================================================
Omnibus:                       22.209   Durbin-Watson:                   2.432
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               28.548
Skew:                           2.074   Prob(JB):                     6.32e-07
Kurtosis:                       6.734   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for peak_trend_slope (Linear OLS) on Day1:
R-squared: 0.083 - Explains 8.3% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.193)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.478, p=0.489
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.388 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\peak_trend_slope\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for peak_trend_slope using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\peak_trend_slope\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of peak_trend_slope (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\peak_trend_slope\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for peak_trend_slope (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\peak_trend_slope\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for peak_trend_slope (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\peak_trend_slope\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of PEAK_TREND_SLOPE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\peak_trend_slope\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of PEAK_TREND_SLOPE vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:       peak_trend_slope   R-squared:                       0.031
Model:                            OLS   Adj. R-squared:                 -0.017
Method:                 Least Squares   F-statistic:                    0.6500
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.430
Time:                        09:51:06   Log-Likelihood:                -105.72
No. Observations:                  22   AIC:                             215.4
Df Residuals:                      20   BIC:                             217.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       96.3611      8.135     11.846      0.000      79.392     113.330
Noradrenalin -9.255e-05      0.000     -0.806      0.430      -0.000       0.000
==============================================================================
Omnibus:                       25.999   Durbin-Watson:                   2.488
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               44.168
Skew:                           2.159   Prob(JB):                     2.56e-10
Kurtosis:                       8.434   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for peak_trend_slope (Linear OLS) on Day5:
R-squared: 0.031 - Explains 3.1% of variance.
Coefficient for Noradrenalin: -0.000 (p=0.430)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.046, p=0.830
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.320 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\peak_trend_slope\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for peak_trend_slope using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\peak_trend_slope\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of peak_trend_slope (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\peak_trend_slope\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for peak_trend_slope (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\peak_trend_slope\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for peak_trend_slope (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\peak_trend_slope\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of PEAK_TREND_SLOPE vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\peak_trend_slope\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of PEAK_TREND_SLOPE vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: SYSTOLIC_AREA

## Day Comparison

![Day Comparison](plots\systolic_area\systolic_area_day_comparison.png)

Description of systolic_area_day_comparison.png:
Boxplot with connected lines showing SYSTOLIC_AREA from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 9, Decrease: 13, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for systolic_area:
Total patients: 22
Increasing: 9 (40.9%)
Decreasing: 13 (59.1%)
No change: 0
Mean change: -2368.68
Median change: -2491.49
Paired test (Wilcoxon): p = 0.063, effect size = 0.64

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.063).
The change shows an overall decrease with medium effect size (0.64).
40.9% of patients showed increase, suggesting potential trend in systolic_area.

```

### Change Histogram

![Change Histogram](plots\systolic_area\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in SYSTOLIC_AREA from Day1 to Day5.
Centered around -2491.49, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\systolic_area\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in SYSTOLIC_AREA to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\systolic_area\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for SYSTOLIC_AREA on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:          systolic_area   R-squared:                       0.016
Model:                            OLS   Adj. R-squared:                 -0.033
Method:                 Least Squares   F-statistic:                    0.3217
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.577
Time:                        09:47:38   Log-Likelihood:                -221.95
No. Observations:                  22   AIC:                             447.9
Df Residuals:                      20   BIC:                             450.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1.617e+04   1639.866      9.859      0.000    1.27e+04    1.96e+04
Adrenalin     -0.0970      0.171     -0.567      0.577      -0.454       0.260
==============================================================================
Omnibus:                       29.061   Durbin-Watson:                   1.879
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               56.511
Skew:                           2.358   Prob(JB):                     5.35e-13
Kurtosis:                       9.278   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_area (Linear OLS) on Day1:
R-squared: 0.016 - Explains 1.6% of variance.
Coefficient for Adrenalin: -0.097 (p=0.577)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.259, p=0.611
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.371 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_area\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_area using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_area\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_area (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_area\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_area (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_area\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_area (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_area\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_AREA vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_area\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_AREA vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:          systolic_area   R-squared:                       0.130
Model:                            OLS   Adj. R-squared:                  0.086
Method:                 Least Squares   F-statistic:                     2.983
Date:                Thu, 31 Jul 2025   Prob (F-statistic):             0.0996
Time:                        09:47:45   Log-Likelihood:                -203.18
No. Observations:                  22   AIC:                             410.4
Df Residuals:                      20   BIC:                             412.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   1.397e+04    698.917     19.985      0.000    1.25e+04    1.54e+04
Adrenalin     -0.1259      0.073     -1.727      0.100      -0.278       0.026
==============================================================================
Omnibus:                        6.483   Durbin-Watson:                   2.222
Prob(Omnibus):                  0.039   Jarque-Bera (JB):                4.322
Skew:                           1.019   Prob(JB):                        0.115
Kurtosis:                       3.747   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_area (Linear OLS) on Day5:
R-squared: 0.130 - Explains 13.0% of variance.
Coefficient for Adrenalin: -0.126 (p=0.100)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.943, p=0.331
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.066
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.509 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_area\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_area using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_area\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_area (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_area\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_area (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_area\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_area (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_area\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_AREA vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_area\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_AREA vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:          systolic_area   R-squared:                       0.073
Model:                            OLS   Adj. R-squared:                  0.026
Method:                 Least Squares   F-statistic:                     1.564
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.226
Time:                        09:51:12   Log-Likelihood:                -221.29
No. Observations:                  22   AIC:                             446.6
Df Residuals:                      20   BIC:                             448.8
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     1.674e+04   1555.565     10.759      0.000    1.35e+04       2e+04
Noradrenalin    -0.0274      0.022     -1.251      0.226      -0.073       0.018
==============================================================================
Omnibus:                       29.508   Durbin-Watson:                   1.975
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               58.228
Skew:                           2.393   Prob(JB):                     2.27e-13
Kurtosis:                       9.373   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_area (Linear OLS) on Day1:
R-squared: 0.073 - Explains 7.3% of variance.
Coefficient for Noradrenalin: -0.027 (p=0.226)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.270, p=0.603
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.000
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.542 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_area\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_area using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_area\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_area (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_area\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_area (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_area\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_area (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_area\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_AREA vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_area\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_AREA vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:          systolic_area   R-squared:                       0.057
Model:                            OLS   Adj. R-squared:                  0.010
Method:                 Least Squares   F-statistic:                     1.219
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.283
Time:                        09:51:17   Log-Likelihood:                -204.06
No. Observations:                  22   AIC:                             412.1
Df Residuals:                      20   BIC:                             414.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     1.369e+04    710.758     19.263      0.000    1.22e+04    1.52e+04
Noradrenalin    -0.0111      0.010     -1.104      0.283      -0.032       0.010
==============================================================================
Omnibus:                        6.873   Durbin-Watson:                   2.169
Prob(Omnibus):                  0.032   Jarque-Bera (JB):                4.575
Skew:                           1.016   Prob(JB):                        0.102
Kurtosis:                       3.929   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_area (Linear OLS) on Day5:
R-squared: 0.057 - Explains 5.7% of variance.
Coefficient for Noradrenalin: -0.011 (p=0.283)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.492, p=0.483
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.056
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.330 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_area\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_area using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_area\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_area (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_area\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_area (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_area\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_area (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_area\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_AREA vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_area\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_AREA vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: DIASTOLIC_AREA

## Day Comparison

![Day Comparison](plots\diastolic_area\diastolic_area_day_comparison.png)

Description of diastolic_area_day_comparison.png:
Boxplot with connected lines showing DIASTOLIC_AREA from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 6, Decrease: 16, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for diastolic_area:
Total patients: 22
Increasing: 6 (27.3%)
Decreasing: 16 (72.7%)
No change: 0
Mean change: -8391.29
Median change: -6044.29
Paired test (Wilcoxon): p = 0.063, effect size = 0.63

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.063).
The change shows an overall decrease with medium effect size (0.63).
27.3% of patients showed increase, suggesting potential trend in diastolic_area.

```

### Change Histogram

![Change Histogram](plots\diastolic_area\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in DIASTOLIC_AREA from Day1 to Day5.
Centered around -6044.29, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\diastolic_area\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in DIASTOLIC_AREA to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\diastolic_area\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for DIASTOLIC_AREA on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         diastolic_area   R-squared:                       0.005
Model:                            OLS   Adj. R-squared:                 -0.045
Method:                 Least Squares   F-statistic:                   0.09465
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.762
Time:                        09:47:52   Log-Likelihood:                -250.07
No. Observations:                  22   AIC:                             504.1
Df Residuals:                      20   BIC:                             506.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   4.518e+04   5887.641      7.674      0.000    3.29e+04    5.75e+04
Adrenalin      0.1889      0.614      0.308      0.762      -1.092       1.470
==============================================================================
Omnibus:                       17.691   Durbin-Watson:                   2.203
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               19.368
Skew:                           1.722   Prob(JB):                     6.23e-05
Kurtosis:                       6.044   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_area (Linear OLS) on Day1:
R-squared: 0.005 - Explains 0.5% of variance.
Coefficient for Adrenalin: 0.189 (p=0.762)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=3.071, p=0.080
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.001
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 4.191 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_area\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_area using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_area\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_area (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_area\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_area (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_area\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_area (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_area\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_AREA vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_area\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_AREA vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         diastolic_area   R-squared:                       0.131
Model:                            OLS   Adj. R-squared:                  0.088
Method:                 Least Squares   F-statistic:                     3.027
Date:                Thu, 31 Jul 2025   Prob (F-statistic):             0.0973
Time:                        09:47:58   Log-Likelihood:                -235.46
No. Observations:                  22   AIC:                             474.9
Df Residuals:                      20   BIC:                             477.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    4.11e+04   3030.770     13.560      0.000    3.48e+04    4.74e+04
Adrenalin     -0.5498      0.316     -1.740      0.097      -1.209       0.109
==============================================================================
Omnibus:                        2.247   Durbin-Watson:                   2.684
Prob(Omnibus):                  0.325   Jarque-Bera (JB):                1.723
Skew:                           0.669   Prob(JB):                        0.423
Kurtosis:                       2.698   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_area (Linear OLS) on Day5:
R-squared: 0.131 - Explains 13.1% of variance.
Coefficient for Adrenalin: -0.550 (p=0.097)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=2.157, p=0.142
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.142
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.485 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_area\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_area using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_area\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_area (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_area\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_area (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_area\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_area (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_area\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_AREA vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_area\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_AREA vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         diastolic_area   R-squared:                       0.107
Model:                            OLS   Adj. R-squared:                  0.062
Method:                 Least Squares   F-statistic:                     2.392
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.138
Time:                        09:51:22   Log-Likelihood:                -248.88
No. Observations:                  22   AIC:                             501.8
Df Residuals:                      20   BIC:                             503.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      5.12e+04   5450.014      9.394      0.000    3.98e+04    6.26e+04
Noradrenalin    -0.1189      0.077     -1.547      0.138      -0.279       0.041
==============================================================================
Omnibus:                       21.058   Durbin-Watson:                   2.468
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               27.377
Skew:                           1.903   Prob(JB):                     1.14e-06
Kurtosis:                       6.921   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_area (Linear OLS) on Day1:
R-squared: 0.107 - Explains 10.7% of variance.
Coefficient for Noradrenalin: -0.119 (p=0.138)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.247, p=0.619
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.001
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.680 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_area\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_area using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_area\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_area (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_area\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_area (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_area\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_area (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_area\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_AREA vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_area\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_AREA vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         diastolic_area   R-squared:                       0.025
Model:                            OLS   Adj. R-squared:                 -0.023
Method:                 Least Squares   F-statistic:                    0.5186
Date:                Thu, 31 Jul 2025   Prob (F-statistic):              0.480
Time:                        09:51:27   Log-Likelihood:                -236.73
No. Observations:                  22   AIC:                             477.5
Df Residuals:                      20   BIC:                             479.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     3.921e+04   3137.329     12.497      0.000    3.27e+04    4.58e+04
Noradrenalin    -0.0319      0.044     -0.720      0.480      -0.124       0.060
==============================================================================
Omnibus:                        6.408   Durbin-Watson:                   2.545
Prob(Omnibus):                  0.041   Jarque-Bera (JB):                4.591
Skew:                           1.099   Prob(JB):                        0.101
Kurtosis:                       3.424   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_area (Linear OLS) on Day5:
R-squared: 0.025 - Explains 2.5% of variance.
Coefficient for Noradrenalin: -0.032 (p=0.480)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.926, p=0.336
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.010
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.651 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_area\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_area using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_area\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_area (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_area\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_area (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_area\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_area (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_area\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_AREA vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_area\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_AREA vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: SYSTOLIC_AMPLITUDE_VARIABILITY

## Day Comparison

![Day Comparison](plots\systolic_amplitude_variability\systolic_amplitude_variability_day_comparison.png)

Description of systolic_amplitude_variability_day_comparison.png:
Boxplot with connected lines showing SYSTOLIC_AMPLITUDE_VARIABILITY from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 8, Decrease: 14, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for systolic_amplitude_variability:
Total patients: 22
Increasing: 8 (36.4%)
Decreasing: 14 (63.6%)
No change: 0
Mean change: -582.95
Median change: -704.81
Paired test (t-test): p = 0.218, effect size = 0.27

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.218).
The change shows an overall decrease with small effect size (0.27).
36.4% of patients showed increase, suggesting potential trend in systolic_amplitude_variability.

```

### Change Histogram

![Change Histogram](plots\systolic_amplitude_variability\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in SYSTOLIC_AMPLITUDE_VARIABILITY from Day1 to Day5.
Centered around -704.81, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\systolic_amplitude_variability\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in SYSTOLIC_AMPLITUDE_VARIABILITY to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\systolic_amplitude_variability\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for SYSTOLIC_AMPLITUDE_VARIABILITY on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                                  OLS Regression Results                                  
==========================================================================================
Dep. Variable:     systolic_amplitude_variability   R-squared:                       0.004
Model:                                        OLS   Adj. R-squared:                 -0.046
Method:                             Least Squares   F-statistic:                   0.07088
Date:                            Thu, 31 Jul 2025   Prob (F-statistic):              0.793
Time:                                    09:48:05   Log-Likelihood:                -193.45
No. Observations:                              22   AIC:                             390.9
Df Residuals:                                  20   BIC:                             393.1
Df Model:                                       1                                         
Covariance Type:                        nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   8371.9146    449.003     18.646      0.000    7435.310    9308.519
Adrenalin     -0.0125      0.047     -0.266      0.793      -0.110       0.085
==============================================================================
Omnibus:                        1.066   Durbin-Watson:                   1.905
Prob(Omnibus):                  0.587   Jarque-Bera (JB):                0.706
Skew:                           0.428   Prob(JB):                        0.703
Kurtosis:                       2.808   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_amplitude_variability (Linear OLS) on Day1:
R-squared: 0.004 - Explains 0.4% of variance.
Coefficient for Adrenalin: -0.012 (p=0.793)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.208, p=0.648
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.635
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 2.508 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_amplitude_variability\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_amplitude_variability using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_amplitude_variability\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_amplitude_variability (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_amplitude_variability\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_amplitude_variability (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_amplitude_variability\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_amplitude_variability (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_amplitude_variability\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_amplitude_variability\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                                  OLS Regression Results                                  
==========================================================================================
Dep. Variable:     systolic_amplitude_variability   R-squared:                       0.002
Model:                                        OLS   Adj. R-squared:                 -0.047
Method:                             Least Squares   F-statistic:                   0.04983
Date:                            Thu, 31 Jul 2025   Prob (F-statistic):              0.826
Time:                                    09:48:12   Log-Likelihood:                -189.57
No. Observations:                              22   AIC:                             383.1
Df Residuals:                                  20   BIC:                             385.3
Df Model:                                       1                                         
Covariance Type:                        nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   7665.1906    376.473     20.361      0.000    6879.881    8450.500
Adrenalin      0.0088      0.039      0.223      0.826      -0.073       0.091
==============================================================================
Omnibus:                        4.039   Durbin-Watson:                   2.160
Prob(Omnibus):                  0.133   Jarque-Bera (JB):                2.462
Skew:                           0.799   Prob(JB):                        0.292
Kurtosis:                       3.362   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_amplitude_variability (Linear OLS) on Day5:
R-squared: 0.002 - Explains 0.2% of variance.
Coefficient for Adrenalin: 0.009 (p=0.826)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.799, p=0.371
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.203
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.359 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_amplitude_variability\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_amplitude_variability using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_amplitude_variability\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_amplitude_variability (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_amplitude_variability\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_amplitude_variability (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_amplitude_variability\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_amplitude_variability (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_amplitude_variability\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_amplitude_variability\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                                  OLS Regression Results                                  
==========================================================================================
Dep. Variable:     systolic_amplitude_variability   R-squared:                       0.009
Model:                                        OLS   Adj. R-squared:                 -0.041
Method:                             Least Squares   F-statistic:                    0.1745
Date:                            Thu, 31 Jul 2025   Prob (F-statistic):              0.681
Time:                                    09:51:33   Log-Likelihood:                -193.39
No. Observations:                              22   AIC:                             390.8
Df Residuals:                                  20   BIC:                             393.0
Df Model:                                       1                                         
Covariance Type:                        nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     8405.8208    437.617     19.208      0.000    7492.967    9318.674
Noradrenalin    -0.0026      0.006     -0.418      0.681      -0.015       0.010
==============================================================================
Omnibus:                        0.476   Durbin-Watson:                   1.881
Prob(Omnibus):                  0.788   Jarque-Bera (JB):                0.461
Skew:                           0.299   Prob(JB):                        0.794
Kurtosis:                       2.617   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_amplitude_variability (Linear OLS) on Day1:
R-squared: 0.009 - Explains 0.9% of variance.
Coefficient for Noradrenalin: -0.003 (p=0.681)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.953, p=0.162
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.695
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.212 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_amplitude_variability\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for systolic_amplitude_variability using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_amplitude_variability\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of systolic_amplitude_variability (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_amplitude_variability\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_amplitude_variability (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_amplitude_variability\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for systolic_amplitude_variability (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_amplitude_variability\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of SYSTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_amplitude_variability\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of SYSTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                                  OLS Regression Results                                  
==========================================================================================
Dep. Variable:     systolic_amplitude_variability   R-squared:                       0.007
Model:                                        OLS   Adj. R-squared:                 -0.042
Method:                             Least Squares   F-statistic:                    0.1493
Date:                            Thu, 31 Jul 2025   Prob (F-statistic):              0.703
Time:                                    09:51:39   Log-Likelihood:                -189.52
No. Observations:                              22   AIC:                             383.0
Df Residuals:                                  20   BIC:                             385.2
Df Model:                                       1                                         
Covariance Type:                        nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     7633.6221    366.964     20.802      0.000    6868.149    8399.095
Noradrenalin     0.0020      0.005      0.386      0.703      -0.009       0.013
==============================================================================
Omnibus:                        3.500   Durbin-Watson:                   2.208
Prob(Omnibus):                  0.174   Jarque-Bera (JB):                2.116
Skew:                           0.748   Prob(JB):                        0.347
Kurtosis:                       3.261   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for systolic_amplitude_variability (Linear OLS) on Day5:
R-squared: 0.007 - Explains 0.7% of variance.
Coefficient for Noradrenalin: 0.002 (p=0.703)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=0.065, p=0.799
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.188
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 1.109 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\systolic_amplitude_variability\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for systolic_amplitude_variability using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\systolic_amplitude_variability\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of systolic_amplitude_variability (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\systolic_amplitude_variability\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for systolic_amplitude_variability (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\systolic_amplitude_variability\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for systolic_amplitude_variability (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\systolic_amplitude_variability\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of SYSTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\systolic_amplitude_variability\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of SYSTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

# Feature: DIASTOLIC_AMPLITUDE_VARIABILITY

## Day Comparison

![Day Comparison](plots\diastolic_amplitude_variability\diastolic_amplitude_variability_day_comparison.png)

Description of diastolic_amplitude_variability_day_comparison.png:
Boxplot with connected lines showing DIASTOLIC_AMPLITUDE_VARIABILITY from Day1 to Day5.
Green lines indicate increase, red decrease, gray no change.
Strip points show individual values.
Counts: Increase: 10, Decrease: 12, No Change: 0.
This quantifies the number of patients with each change type.

### Change Statistics

```
Change Statistics for diastolic_amplitude_variability:
Total patients: 22
Increasing: 10 (45.5%)
Decreasing: 12 (54.5%)
No change: 0
Mean change: -577.65
Median change: -458.70
Paired test (t-test): p = 0.296, effect size = 0.23

Interpretation:
There is a not significant difference between Day1 and Day5 (p=0.296).
The change shows an overall decrease with small effect size (0.23).
45.5% of patients showed increase, suggesting potential trend in diastolic_amplitude_variability.

```

### Change Histogram

![Change Histogram](plots\diastolic_amplitude_variability\change_histogram.png)

Description of change_histogram.png:
This histogram with KDE shows the distribution of changes in DIASTOLIC_AMPLITUDE_VARIABILITY from Day1 to Day5.
Centered around -458.70, skewness indicates asymmetry in changes.

### Change QQ Plot

![Change QQ](plots\diastolic_amplitude_variability\change_qq.png)

Description of change_qq.png:
This QQ plot compares changes in DIASTOLIC_AMPLITUDE_VARIABILITY to a normal distribution.
Green points should align with the red line for normality.
Deviations at ends indicate skewness or heavy tails.

### Day KDE Comparison

![Day KDE](plots\diastolic_amplitude_variability\day_kde_comparison.png)

Description of day_kde_comparison.png:
This plot shows overlapping kernel density estimates (KDE) for DIASTOLIC_AMPLITUDE_VARIABILITY on Day1 (blue) and Day5 (green).
Filled areas represent density, allowing easy comparison of distributions.
Shifts in peaks or shapes indicate changes in the feature over time.

## Vs Adrenalin

### Day1

#### Model Summary

```
                                   OLS Regression Results                                  
===========================================================================================
Dep. Variable:     diastolic_amplitude_variability   R-squared:                       0.026
Model:                                         OLS   Adj. R-squared:                 -0.023
Method:                              Least Squares   F-statistic:                    0.5312
Date:                             Thu, 31 Jul 2025   Prob (F-statistic):              0.475
Time:                                     09:48:18   Log-Likelihood:                -197.46
No. Observations:                               22   AIC:                             398.9
Df Residuals:                                   20   BIC:                             401.1
Df Model:                                        1                                         
Covariance Type:                         nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   7968.4964    538.935     14.786      0.000    6844.298    9092.695
Adrenalin     -0.0410      0.056     -0.729      0.475      -0.158       0.076
==============================================================================
Omnibus:                        2.650   Durbin-Watson:                   2.181
Prob(Omnibus):                  0.266   Jarque-Bera (JB):                1.965
Skew:                           0.724   Prob(JB):                        0.374
Kurtosis:                       2.781   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_amplitude_variability (Linear OLS) on Day1:
R-squared: 0.026 - Explains 2.6% of variance.
Coefficient for Adrenalin: -0.041 (p=0.475)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.383, p=0.240
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.250
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 2.551 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_amplitude_variability\adrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_amplitude_variability using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_amplitude_variability\adrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_amplitude_variability (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_amplitude_variability\adrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_amplitude_variability (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_amplitude_variability\adrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_amplitude_variability (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_amplitude_variability\adrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_amplitude_variability\adrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                                   OLS Regression Results                                  
===========================================================================================
Dep. Variable:     diastolic_amplitude_variability   R-squared:                       0.048
Model:                                         OLS   Adj. R-squared:                  0.000
Method:                              Least Squares   F-statistic:                     1.010
Date:                             Thu, 31 Jul 2025   Prob (F-statistic):              0.327
Time:                                     09:48:25   Log-Likelihood:                -194.15
No. Observations:                               22   AIC:                             392.3
Df Residuals:                                   20   BIC:                             394.5
Df Model:                                        1                                         
Covariance Type:                         nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   7435.3449    463.548     16.040      0.000    6468.401    8402.289
Adrenalin     -0.0486      0.048     -1.005      0.327      -0.149       0.052
==============================================================================
Omnibus:                        8.524   Durbin-Watson:                   1.902
Prob(Omnibus):                  0.014   Jarque-Bera (JB):                6.154
Skew:                           1.177   Prob(JB):                       0.0461
Kurtosis:                       4.085   Cond. No.                     1.21e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.21e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_amplitude_variability (Linear OLS) on Day5:
R-squared: 0.048 - Explains 4.8% of variance.
Coefficient for Adrenalin: -0.049 (p=0.327)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.020, p=0.312
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.010
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.215 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_amplitude_variability\adrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_amplitude_variability using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_amplitude_variability\adrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_amplitude_variability (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_amplitude_variability\adrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_amplitude_variability (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_amplitude_variability\adrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_amplitude_variability (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_amplitude_variability\adrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_amplitude_variability\adrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_AMPLITUDE_VARIABILITY vs Adrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Vs Noradrenalin

### Day1

#### Model Summary

```
                                   OLS Regression Results                                  
===========================================================================================
Dep. Variable:     diastolic_amplitude_variability   R-squared:                       0.050
Model:                                         OLS   Adj. R-squared:                  0.002
Method:                              Least Squares   F-statistic:                     1.042
Date:                             Thu, 31 Jul 2025   Prob (F-statistic):              0.320
Time:                                     09:51:45   Log-Likelihood:                -197.19
No. Observations:                               22   AIC:                             398.4
Df Residuals:                                   20   BIC:                             400.6
Df Model:                                        1                                         
Covariance Type:                         nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     8039.1901    520.196     15.454      0.000    6954.081    9124.299
Noradrenalin    -0.0075      0.007     -1.021      0.320      -0.023       0.008
==============================================================================
Omnibus:                        1.314   Durbin-Watson:                   2.139
Prob(Omnibus):                  0.518   Jarque-Bera (JB):                1.134
Skew:                           0.386   Prob(JB):                        0.567
Kurtosis:                       2.200   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_amplitude_variability (Linear OLS) on Day1:
R-squared: 0.050 - Explains 5.0% of variance.
Coefficient for Noradrenalin: -0.007 (p=0.320)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.141, p=0.285
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.463
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.327 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_amplitude_variability\noradrenalin\residuals_day1.png)

Description of residuals_day1.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_amplitude_variability using linear OLS on Day1.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_amplitude_variability\noradrenalin\qq_day1.png)

Description of qq_day1.png:
This QQ plot compares residuals of diastolic_amplitude_variability (from linear OLS) to a normal distribution on Day1.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_amplitude_variability\noradrenalin\leverage_day1.png)

Description of leverage_day1.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_amplitude_variability (linear OLS) on Day1.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_amplitude_variability\noradrenalin\residual_histogram_day1.png)

Description of residual_histogram_day1.png:
This histogram with KDE shows the distribution of residuals for diastolic_amplitude_variability (linear OLS) on Day1.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_amplitude_variability\noradrenalin\joint_plot_day1.png)

Description of joint_plot_day1.png:
This joint plot shows the scatter of DIASTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day1.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_amplitude_variability\noradrenalin\hexbin_plot_day1.png)

Description of hexbin_plot_day1.png:
This hexbin plot visualizes the density of DIASTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin data points on Day1.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

### Day5

#### Model Summary

```
                                   OLS Regression Results                                  
===========================================================================================
Dep. Variable:     diastolic_amplitude_variability   R-squared:                       0.057
Model:                                         OLS   Adj. R-squared:                  0.009
Method:                              Least Squares   F-statistic:                     1.201
Date:                             Thu, 31 Jul 2025   Prob (F-statistic):              0.286
Time:                                     09:51:51   Log-Likelihood:                -194.05
No. Observations:                               22   AIC:                             392.1
Df Residuals:                                   20   BIC:                             394.3
Df Model:                                        1                                         
Covariance Type:                         nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept     6863.9272    450.916     15.222      0.000    5923.334    7804.521
Noradrenalin     0.0070      0.006      1.096      0.286      -0.006       0.020
==============================================================================
Omnibus:                        8.765   Durbin-Watson:                   2.407
Prob(Omnibus):                  0.012   Jarque-Bera (JB):                6.349
Skew:                           1.151   Prob(JB):                       0.0418
Kurtosis:                       4.276   Cond. No.                     8.72e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.72e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Model Interpretation for diastolic_amplitude_variability (Linear OLS) on Day5:
R-squared: 0.057 - Explains 5.7% of variance.
Coefficient for Noradrenalin: 0.007 (p=0.286)
If p < 0.05, significant linear relationship.

Diagnostics:
Heteroscedasticity (Breusch-Pagan test): LM=1.454, p=0.228
If p < 0.05, residuals have non-constant variance (heteroscedastic).
Normality of residuals (Shapiro-Wilk): p=0.028
If p < 0.05, residuals not normally distributed.
Outliers/Influence: Max Cook's distance 0.769 (threshold ~1 or 4/n=0.182)

```

#### Residuals Plot

![Residuals](plots\diastolic_amplitude_variability\noradrenalin\residuals_day5.png)

Description of residuals_day5.png:
This plot shows residuals (prediction errors) against fitted values for diastolic_amplitude_variability using linear OLS on Day5.
Green points: residuals within 1 SD.
Orange points: residuals between 1-2 SD.
Red points: residuals beyond 2 SD (potential outliers).
The blue LOWESS trend line highlights patterns like curvature (non-linearity) or changing spread (heteroscedasticity).
Ideal: random scatter around zero with a flat blue line, indicating no systematic errors.

#### QQ Plot

![QQ Plot](plots\diastolic_amplitude_variability\noradrenalin\qq_day5.png)

Description of qq_day5.png:
This QQ plot compares residuals of diastolic_amplitude_variability (from linear OLS) to a normal distribution on Day5.
Blue points represent sample quantiles vs theoretical normal quantiles.
Points along the red line indicate normality.
Deviations at ends suggest skewness or heavy tails in residuals.

#### Leverage Plot

![Leverage](plots\diastolic_amplitude_variability\noradrenalin\leverage_day5.png)

Description of leverage_day5.png:
This influence plot shows leverage (x-axis) vs studentized residuals (y-axis) for diastolic_amplitude_variability (linear OLS) on Day5.
Point size reflects Cook's distance, indicating influence.
Large or distant points are potentially influential outliers.

#### Residual Histogram

![Residual Histogram](plots\diastolic_amplitude_variability\noradrenalin\residual_histogram_day5.png)

Description of residual_histogram_day5.png:
This histogram with KDE shows the distribution of residuals for diastolic_amplitude_variability (linear OLS) on Day5.
A normal distribution centered at zero supports OLS assumptions.
Skewness or multimodality may indicate model issues.

#### Joint Plot

![Joint Plot](plots\diastolic_amplitude_variability\noradrenalin\joint_plot_day5.png)

Description of joint_plot_day5.png:
This joint plot shows the scatter of DIASTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin colored by ANSD: red for Yes_ANSD, blue for No_ANSD on Day5.
Marginal histograms with KDE show variable distributions, colored by ANSD.
The red regression line indicates the strength and direction of the relationship, with red CI shade.
A green LOWESS line is added as an additional trend trace.

#### Hexbin Plot

![Hexbin Plot](plots\diastolic_amplitude_variability\noradrenalin\hexbin_plot_day5.png)

Description of hexbin_plot_day5.png:
This hexbin plot visualizes the density of DIASTOLIC_AMPLITUDE_VARIABILITY vs Noradrenalin data points on Day5.
Darker hexagons indicate higher point density.
Useful for identifying clusters or patterns in dense datasets.

## Outliers Summary for Adrenalin

| Day   | patient_id   |    sdnn |   rmssd |    pnn50 |   lf_power |         hf_power |   poincare_sd1 |   poincare_sd2 |   systolic_duration |   diastolic_duration |   systolic_area |   diastolic_area |   systolic_slope |   diastolic_slope |   signal_skewness |   peak_trend_slope |   systolic_amplitude_variability |   diastolic_amplitude_variability |   sdnn_Day1 |   rmssd_Day1 |   poincare_sd1_Day1 |   poincare_sd2_Day1 |   systolic_duration_Day1 |   diastolic_duration_Day1 |   systolic_slope_Day1 |   diastolic_slope_Day1 |   pnn50_Day1 |   lf_power_Day1 |    hf_power_Day1 |   signal_skewness_Day1 |   peak_trend_slope_Day1 |   systolic_area_Day1 |   diastolic_area_Day1 |   systolic_amplitude_variability_Day1 |   diastolic_amplitude_variability_Day1 |   sdnn_Day5 |   rmssd_Day5 |   poincare_sd1_Day5 |   poincare_sd2_Day5 |   systolic_duration_Day5 |   diastolic_duration_Day5 |   systolic_slope_Day5 |   diastolic_slope_Day5 |   pnn50_Day5 |   lf_power_Day5 |   hf_power_Day5 |   signal_skewness_Day5 |   peak_trend_slope_Day5 |   systolic_area_Day5 |   diastolic_area_Day5 |   systolic_amplitude_variability_Day5 |   diastolic_amplitude_variability_Day5 |   sdnn_Change_Pct |   rmssd_Change_Pct |   poincare_sd1_Change_Pct |   poincare_sd2_Change_Pct |   systolic_duration_Change_Pct |   diastolic_duration_Change_Pct |   systolic_slope_Change_Pct |   diastolic_slope_Change_Pct |   pnn50_Change_Pct |   lf_power_Change_Pct |   hf_power_Change_Pct |   signal_skewness_Change_Pct |   peak_trend_slope_Change_Pct |   systolic_area_Change_Pct |   diastolic_area_Change_Pct |   systolic_amplitude_variability_Change_Pct |   diastolic_amplitude_variability_Change_Pct |   Adrenalin |   ANSD | OUTCOME   | Plot                            |   Deviation | Explanation                                                                                                                                         |
|:------|:-------------|--------:|--------:|---------:|-----------:|-----------------:|---------------:|---------------:|--------------------:|---------------------:|----------------:|-----------------:|-----------------:|------------------:|------------------:|-------------------:|---------------------------------:|----------------------------------:|------------:|-------------:|--------------------:|--------------------:|-------------------------:|--------------------------:|----------------------:|-----------------------:|-------------:|----------------:|-----------------:|-----------------------:|------------------------:|---------------------:|----------------------:|--------------------------------------:|---------------------------------------:|------------:|-------------:|--------------------:|--------------------:|-------------------------:|--------------------------:|----------------------:|-----------------------:|-------------:|----------------:|----------------:|-----------------------:|------------------------:|---------------------:|----------------------:|--------------------------------------:|---------------------------------------:|------------------:|-------------------:|--------------------------:|--------------------------:|-------------------------------:|--------------------------------:|----------------------------:|-----------------------------:|-------------------:|----------------------:|----------------------:|-----------------------------:|------------------------------:|---------------------------:|----------------------------:|--------------------------------------------:|---------------------------------------------:|------------:|-------:|:----------|:--------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| Day1  | 24EI-003-038 | 3882.36 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     3882.36 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     106.717 |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -97.2512  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | sdnn                            |     2.33411 | Value 3882.36 on Day1 is 2.33 SD from median (median=618.72, IQR=[426.46, 1258.66]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-045 | 3370.42 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     3370.42 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     248.571 |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -92.6249  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          23 |      0 | DISCHARGE | sdnn                            |     1.96797 | Value 3370.42 on Day1 is 1.97 SD from median (median=618.72, IQR=[426.46, 1258.66]). Adrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-047 | 2985.39 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     2985.39 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |    1018.95  |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -65.8688  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        4326 |      0 | DISCHARGE | sdnn                            |     1.69261 | Value 2985.39 on Day1 is 1.69 SD from median (median=618.72, IQR=[426.46, 1258.66]). Adrenalin=4326.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-064 | 5276.9  |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     5276.9  |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     565.556 |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -89.2824  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | sdnn                            |     3.33146 | Value 5276.90 on Day1 is 3.33 SD from median (median=618.72, IQR=[426.46, 1258.66]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day5  | 24EI-003-039 | 2038.02 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     2066.01 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |    2038.02  |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |          -1.35459 |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | sdnn                            |     2.96072 | Value 2038.02 on Day5 is 2.96 SD from median (median=479.86, IQR=[151.83, 838.65]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.           |
| Day1  | 24EI-003-038 |  nan    | 5164.59 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      5164.59 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      102.768 |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -98.0101  |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | rmssd                           |     1.89426 | Value 5164.59 on Day1 is 1.89 SD from median (median=862.95, IQR=[595.19, 1782.19]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-045 |  nan    | 5001.01 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      5001.01 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      342.141 |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -93.1586  |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          23 |      0 | DISCHARGE | rmssd                           |     1.82222 | Value 5001.01 on Day1 is 1.82 SD from median (median=862.95, IQR=[595.19, 1782.19]). Adrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-047 |  nan    | 4694.32 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      4694.32 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |     1415.82  |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -69.8397  |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        4326 |      0 | DISCHARGE | rmssd                           |     1.68717 | Value 4694.32 on Day1 is 1.69 SD from median (median=862.95, IQR=[595.19, 1782.19]). Adrenalin=4326.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-064 |  nan    | 9237.55 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      9237.55 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      807.913 |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -91.254   |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | rmssd                           |     3.68782 | Value 9237.55 on Day1 is 3.69 SD from median (median=862.95, IQR=[595.19, 1782.19]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day5  | 24EI-003-039 |  nan    | 3213.41 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      3161.21 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |     3213.41  |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |            1.65152 |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | rmssd                           |     3.21433 | Value 3213.41 on Day5 is 3.21 SD from median (median=668.82, IQR=[203.37, 1148.20]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |        3621.79 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             3621.79 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |             72.7719 |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -97.9907 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | poincare_sd1                    |     2.21118 | Value 3621.79 on Day1 is 2.21 SD from median (median=613.27, IQR=[424.39, 1281.00]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |        nan |    nan           |        3739.8  |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             3739.8  |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            242.312  |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -93.5207 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          23 |      0 | DISCHARGE | poincare_sd1                    |     2.29792 | Value 3739.80 on Day1 is 2.30 SD from median (median=613.27, IQR=[424.39, 1281.00]). Adrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |    nan           |        3561.51 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             3561.51 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |           1003.52   |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -71.8231 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        4326 |      0 | DISCHARGE | poincare_sd1                    |     2.16688 | Value 3561.51 on Day1 is 2.17 SD from median (median=613.27, IQR=[424.39, 1281.00]). Adrenalin=4326.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |        4458.83 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             4458.83 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            572.527  |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -87.1597 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | poincare_sd1                    |     2.82638 | Value 4458.83 on Day1 is 2.83 SD from median (median=613.27, IQR=[424.39, 1281.00]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |        2076.03 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             2423.04 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |           2076.03   |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -14.3214 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | poincare_sd1                    |     2.98159 | Value 2076.03 on Day5 is 2.98 SD from median (median=474.14, IQR=[143.97, 816.87]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.           |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |        4652.96 |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |             4652.96 |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             129.659 |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  -97.2134 |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | poincare_sd2                    |     3.14771 | Value 4652.96 on Day1 is 3.15 SD from median (median=631.56, IQR=[429.66, 1293.48]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |        3238.07 |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |             3238.07 |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             253.894 |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  -92.1591 |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          23 |      0 | DISCHARGE | poincare_sd2                    |     2.04022 | Value 3238.07 on Day1 is 2.04 SD from median (median=631.56, IQR=[429.66, 1293.48]). Adrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |        3891.1  |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |             3891.1  |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             554.665 |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  -85.7453 |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | poincare_sd2                    |     2.55137 | Value 3891.10 on Day1 is 2.55 SD from median (median=631.56, IQR=[429.66, 1293.48]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |             1.91383 |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |                 1.91383  |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |                 0.465935 |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       -75.6544 |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | systolic_duration               |     3.58767 | Value 1.91 on Day1 is 3.59 SD from median (median=0.53, IQR=[0.43, 0.85]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.                   |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |             1.55557 |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |                 0.956985 |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |                 1.55557  |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                        62.5487 |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | systolic_duration               |     4.29778 | Value 1.56 on Day5 is 4.30 SD from median (median=0.46, IQR=[0.39, 0.54]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.                    |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |             0.81518 |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |                 0.42582  |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |                 0.81518  |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                        91.4376 |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         320 |      0 | DISCHARGE | systolic_duration               |     1.39738 | Value 0.82 on Day5 is 1.40 SD from median (median=0.46, IQR=[0.39, 0.54]). Adrenalin=320.00, Patient ANSD=0, OUTCOME=DISCHARGE.                     |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |             1.70287  |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                  1.70287  |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                  0.437897 |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        -74.2847 |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | diastolic_duration              |     3.99238 | Value 1.70 on Day1 is 3.99 SD from median (median=0.46, IQR=[0.39, 0.60]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.                    |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |             0.985893 |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                  0.985893 |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                  0.625582 |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        -36.5466 |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        4326 |      0 | DISCHARGE | diastolic_duration              |     1.69568 | Value 0.99 on Day1 is 1.70 SD from median (median=0.46, IQR=[0.39, 0.60]). Adrenalin=4326.00, Patient ANSD=0, OUTCOME=DISCHARGE.                    |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |         1.06356  |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |               1.22109 |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |              1.06356  |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    -12.9013 |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | systolic_slope                  |    -1.88828 | Value 1.06 on Day5 is -1.89 SD from median (median=1.43, IQR=[1.35, 1.48]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.                   |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |         0.670304 |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |               1.55903 |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |              0.670304 |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    -57.0051 |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         320 |      0 | DISCHARGE | systolic_slope                  |    -3.92901 | Value 0.67 on Day5 is -3.93 SD from median (median=1.43, IQR=[1.35, 1.48]). Adrenalin=320.00, Patient ANSD=0, OUTCOME=DISCHARGE.                    |
| Day1  | 24EI-003-044 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.18788 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.18788 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.53488 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                     29.2118  |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2581 |      0 | DISCHARGE | diastolic_slope                 |     2.08733 | Value -1.19 on Day1 is 2.09 SD from median (median=-1.48, IQR=[-1.53, -1.41]). Adrenalin=2581.00, Patient ANSD=0, OUTCOME=DISCHARGE.                |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.00712 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.00712 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.44002 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                     42.9836  |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | diastolic_slope                 |     3.37714 | Value -1.01 on Day1 is 3.38 SD from median (median=-1.48, IQR=[-1.53, -1.41]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.               |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.32548 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.40514 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.32548 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                     -5.66937 |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | diastolic_slope                 |     2.82919 | Value -1.33 on Day5 is 2.83 SD from median (median=-1.52, IQR=[-1.56, -1.49]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.                |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.32729 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.54282 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.32729 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    -13.9695  |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         320 |      0 | DISCHARGE | diastolic_slope                 |     2.80289 | Value -1.33 on Day5 is 2.80 SD from median (median=-1.52, IQR=[-1.56, -1.49]). Adrenalin=320.00, Patient ANSD=0, OUTCOME=DISCHARGE.                 |
| Day5  | 24EI-003-033 |  nan    |  nan    |  66.5955 |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |      69.4296 |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |      66.5955 |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |           -4.08204 |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1242 |      0 | DISCHARGE | pnn50                           |     2.96761 | Value 66.60 on Day5 is 2.97 SD from median (median=22.55, IQR=[13.15, 29.49]). Adrenalin=1242.00, Patient ANSD=0, OUTCOME=DISCHARGE.                |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |     219905 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        219905   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |         2692.89 |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             -98.7754  |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | lf_power                        |     2.17058 | Value 219904.77 on Day1 is 2.17 SD from median (median=34266.44, IQR=[15486.88, 77589.25]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-044 |  nan    |  nan    | nan      |     329424 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        329424   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |        50686.5  |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             -84.6136  |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2581 |      0 | DISCHARGE | lf_power                        |     3.45113 | Value 329423.90 on Day1 is 3.45 SD from median (median=34266.44, IQR=[15486.88, 77589.25]). Adrenalin=2581.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |     213644 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        213644   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |         6611.25 |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             -96.9055  |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          23 |      0 | DISCHARGE | lf_power                        |     2.09738 | Value 213644.24 on Day1 is 2.10 SD from median (median=34266.44, IQR=[15486.88, 77589.25]). Adrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.     |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |     128551 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        124224   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |       128551    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |               3.48383 |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | lf_power                        |     1.80103 | Value 128551.34 on Day5 is 1.80 SD from median (median=12497.48, IQR=[2212.33, 49179.39]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |     271576 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |         19784.1 |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |       271576    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |            1272.7     |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         320 |      0 | DISCHARGE | lf_power                        |     4.02062 | Value 271575.85 on Day5 is 4.02 SD from median (median=12497.48, IQR=[2212.33, 49179.39]). Adrenalin=320.00, Patient ANSD=0, OUTCOME=DISCHARGE.     |
| Day1  | 24EI-003-044 |  nan    |  nan    | nan      |        nan | 628892           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   | 628892           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |         83059.6 |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -86.7927 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        2581 |      0 | DISCHARGE | hf_power                        |     1.09696 | Value 628891.52 on Day1 is 1.10 SD from median (median=66031.19, IQR=[29992.06, 260816.60]). Adrenalin=2581.00, Patient ANSD=0, OUTCOME=DISCHARGE.  |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |        nan |      1.94379e+06 |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |      1.94379e+06 |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |         12683.9 |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -99.3475 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          23 |      0 | DISCHARGE | hf_power                        |     3.65956 | Value 1943787.80 on Day1 is 3.66 SD from median (median=66031.19, IQR=[29992.06, 260816.60]). Adrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |      1.60387e+06 |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |      1.60387e+06 |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        301129   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -81.2249 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        4326 |      0 | DISCHARGE | hf_power                        |     2.9971  | Value 1603873.71 on Day1 is 3.00 SD from median (median=66031.19, IQR=[29992.06, 260816.60]). Adrenalin=4326.00, Patient ANSD=0, OUTCOME=DISCHARGE. |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan | 231933           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   | 264796           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        231933   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -12.4106 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | hf_power                        |     1.07457 | Value 231933.15 on Day5 is 1.07 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-047 |  nan    |  nan    | nan      |        nan | 301129           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |      1.60387e+06 |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        301129   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -81.2249 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        4326 |      0 | DISCHARGE | hf_power                        |     1.4272  | Value 301129.48 on Day5 is 1.43 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Adrenalin=4326.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-049 |  nan    |  nan    | nan      |        nan | 469293           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |  95433.3         |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        469293   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              391.75   |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        9481 |      0 | DISCHARGE | hf_power                        |     2.28418 | Value 469293.43 on Day5 is 2.28 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Adrenalin=9481.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-051 |  nan    |  nan    | nan      |        nan | 712112           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |  90622.4         |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        712112   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              685.801  |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        1565 |      0 | DISCHARGE | hf_power                        |     3.52161 | Value 712111.68 on Day5 is 3.52 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Adrenalin=1565.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan | 465100           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |  38231.7         |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        465100   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |             1116.53   |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         320 |      0 | DISCHARGE | hf_power                        |     2.26281 | Value 465100.26 on Day5 is 2.26 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Adrenalin=320.00, Patient ANSD=0, OUTCOME=DISCHARGE.     |
| Day1  | 24EI-003-030 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |          0.543097 |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |               0.543097 |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |               0.261445 |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     -51.8603 |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |        3639 |      1 | DIESOON   | signal_skewness                 |     2.56099 | Value 0.54 on Day1 is 2.56 SD from median (median=0.13, IQR=[0.03, 0.23]). Adrenalin=3639.00, Patient ANSD=1, OUTCOME=DIESOON.                      |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            321.101 |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 321.101 |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                 82.3574 |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      -74.3515 |                   nan      |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | peak_trend_slope                |     2.63385 | Value 321.10 on Day1 is 2.63 SD from median (median=103.59, IQR=[80.30, 133.77]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.             |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            393.251 |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 393.251 |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                 80.3053 |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      -79.5791 |                   nan      |                    nan      |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | peak_trend_slope                |     3.50752 | Value 393.25 on Day1 is 3.51 SD from median (median=103.59, IQR=[80.30, 133.77]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            201.664 |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 129.881 |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                201.664  |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                       55.2682 |                   nan      |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | peak_trend_slope                |     3.78867 | Value 201.66 on Day5 is 3.79 SD from median (median=85.19, IQR=[73.51, 100.39]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.              |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |         37621.9 |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |              37621.9 |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |              12188.9 |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   -67.6015 |                    nan      |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | systolic_area                   |     3.89643 | Value 37621.95 on Day1 is 3.90 SD from median (median=14215.17, IQR=[12512.55, 16603.60]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |         24960.7 |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |              24960.7 |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |              16371.6 |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   -34.4106 |                    nan      |                                    nan      |                                     nan      |        4326 |      0 | DISCHARGE | systolic_area                   |     1.78877 | Value 24960.71 on Day1 is 1.79 SD from median (median=14215.17, IQR=[12512.55, 16603.60]). Adrenalin=4326.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |         20862   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |              14038.8 |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |              20862   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                    48.6024 |                    nan      |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | systolic_area                   |     3.07513 | Value 20862.01 on Day5 is 3.08 SD from median (median=12489.15, IQR=[11208.09, 14703.43]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |          83255.9 |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |               83255.9 |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |               35609.1 |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    -57.2293 |                                    nan      |                                     nan      |        2805 |      0 | DISCHARGE | diastolic_area                  |     1.96558 | Value 83255.92 on Day1 is 1.97 SD from median (median=41099.95, IQR=[32234.64, 49929.12]). Adrenalin=2805.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |         117333   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |              117333   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |               32562.3 |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    -72.2479 |                                    nan      |                                     nan      |       18185 |      0 | DISCHARGE | diastolic_area                  |     3.55447 | Value 117332.75 on Day1 is 3.55 SD from median (median=41099.95, IQR=[32234.64, 49929.12]). Adrenalin=18185.00, Patient ANSD=0, OUTCOME=DISCHARGE.  |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |          64902.3 |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |               46025.9 |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |               64902.3 |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                     41.0128 |                                    nan      |                                     nan      |        1181 |      0 | DISCHARGE | diastolic_area                  |     2.46353 | Value 64902.34 on Day5 is 2.46 SD from median (median=35787.55, IQR=[27280.11, 41745.63]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                          11256.3 |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                               9949.33 |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                               11256.3 |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                     13.1363 |                                     nan      |        1181 |      0 | DISCHARGE | systolic_amplitude_variability  |     2.63569 | Value 11256.30 on Day5 is 2.64 SD from median (median=7645.77, IQR=[6546.00, 8371.89]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.       |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                           11629.5 |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                9003.58 |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                11629.5 |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                      29.1658 |        1181 |      0 | DISCHARGE | diastolic_amplitude_variability |     2.79722 | Value 11629.54 on Day5 is 2.80 SD from median (median=6799.79, IQR=[6220.86, 7536.15]). Adrenalin=1181.00, Patient ANSD=0, OUTCOME=DISCHARGE.       |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                           11385.4 |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                6655.49 |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                11385.4 |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                      71.0683 |         320 |      0 | DISCHARGE | diastolic_amplitude_variability |     2.65584 | Value 11385.44 on Day5 is 2.66 SD from median (median=6799.79, IQR=[6220.86, 7536.15]). Adrenalin=320.00, Patient ANSD=0, OUTCOME=DISCHARGE.        |

## Outliers Summary for Noradrenalin

| Day   | patient_id   |    sdnn |   rmssd |    pnn50 |   lf_power |         hf_power |   poincare_sd1 |   poincare_sd2 |   systolic_duration |   diastolic_duration |   systolic_area |   diastolic_area |   systolic_slope |   diastolic_slope |   signal_skewness |   peak_trend_slope |   systolic_amplitude_variability |   diastolic_amplitude_variability |   sdnn_Day1 |   rmssd_Day1 |   poincare_sd1_Day1 |   poincare_sd2_Day1 |   systolic_duration_Day1 |   diastolic_duration_Day1 |   systolic_slope_Day1 |   diastolic_slope_Day1 |   pnn50_Day1 |   lf_power_Day1 |    hf_power_Day1 |   signal_skewness_Day1 |   peak_trend_slope_Day1 |   systolic_area_Day1 |   diastolic_area_Day1 |   systolic_amplitude_variability_Day1 |   diastolic_amplitude_variability_Day1 |   sdnn_Day5 |   rmssd_Day5 |   poincare_sd1_Day5 |   poincare_sd2_Day5 |   systolic_duration_Day5 |   diastolic_duration_Day5 |   systolic_slope_Day5 |   diastolic_slope_Day5 |   pnn50_Day5 |   lf_power_Day5 |   hf_power_Day5 |   signal_skewness_Day5 |   peak_trend_slope_Day5 |   systolic_area_Day5 |   diastolic_area_Day5 |   systolic_amplitude_variability_Day5 |   diastolic_amplitude_variability_Day5 |   sdnn_Change_Pct |   rmssd_Change_Pct |   poincare_sd1_Change_Pct |   poincare_sd2_Change_Pct |   systolic_duration_Change_Pct |   diastolic_duration_Change_Pct |   systolic_slope_Change_Pct |   diastolic_slope_Change_Pct |   pnn50_Change_Pct |   lf_power_Change_Pct |   hf_power_Change_Pct |   signal_skewness_Change_Pct |   peak_trend_slope_Change_Pct |   systolic_area_Change_Pct |   diastolic_area_Change_Pct |   systolic_amplitude_variability_Change_Pct |   diastolic_amplitude_variability_Change_Pct |   Noradrenalin |   ANSD | OUTCOME   | Plot                            |   Deviation | Explanation                                                                                                                                            |
|:------|:-------------|--------:|--------:|---------:|-----------:|-----------------:|---------------:|---------------:|--------------------:|---------------------:|----------------:|-----------------:|-----------------:|------------------:|------------------:|-------------------:|---------------------------------:|----------------------------------:|------------:|-------------:|--------------------:|--------------------:|-------------------------:|--------------------------:|----------------------:|-----------------------:|-------------:|----------------:|-----------------:|-----------------------:|------------------------:|---------------------:|----------------------:|--------------------------------------:|---------------------------------------:|------------:|-------------:|--------------------:|--------------------:|-------------------------:|--------------------------:|----------------------:|-----------------------:|-------------:|----------------:|----------------:|-----------------------:|------------------------:|---------------------:|----------------------:|--------------------------------------:|---------------------------------------:|------------------:|-------------------:|--------------------------:|--------------------------:|-------------------------------:|--------------------------------:|----------------------------:|-----------------------------:|-------------------:|----------------------:|----------------------:|-----------------------------:|------------------------------:|---------------------------:|----------------------------:|--------------------------------------------:|---------------------------------------------:|---------------:|-------:|:----------|:--------------------------------|------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Day1  | 24EI-003-038 | 3882.36 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     3882.36 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     106.717 |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -97.2512  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | sdnn                            |     2.33411 | Value 3882.36 on Day1 is 2.33 SD from median (median=618.72, IQR=[426.46, 1258.66]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day1  | 24EI-003-045 | 3370.42 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     3370.42 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     248.571 |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -92.6249  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |             23 |      0 | DISCHARGE | sdnn                            |     1.96797 | Value 3370.42 on Day1 is 1.97 SD from median (median=618.72, IQR=[426.46, 1258.66]). Noradrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-047 | 2985.39 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     2985.39 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |    1018.95  |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -65.8688  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           5368 |      0 | DISCHARGE | sdnn                            |     1.69261 | Value 2985.39 on Day1 is 1.69 SD from median (median=618.72, IQR=[426.46, 1258.66]). Noradrenalin=5368.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-064 | 5276.9  |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     5276.9  |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     565.556 |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         -89.2824  |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | sdnn                            |     3.33146 | Value 5276.90 on Day1 is 3.33 SD from median (median=618.72, IQR=[426.46, 1258.66]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day5  | 24EI-003-039 | 2038.02 |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |     2066.01 |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |    2038.02  |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |          -1.35459 |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | sdnn                            |     2.96072 | Value 2038.02 on Day5 is 2.96 SD from median (median=479.86, IQR=[151.83, 838.65]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-038 |  nan    | 5164.59 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      5164.59 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      102.768 |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -98.0101  |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | rmssd                           |     1.89426 | Value 5164.59 on Day1 is 1.89 SD from median (median=862.95, IQR=[595.19, 1782.19]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day1  | 24EI-003-045 |  nan    | 5001.01 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      5001.01 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      342.141 |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -93.1586  |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |             23 |      0 | DISCHARGE | rmssd                           |     1.82222 | Value 5001.01 on Day1 is 1.82 SD from median (median=862.95, IQR=[595.19, 1782.19]). Noradrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-047 |  nan    | 4694.32 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      4694.32 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |     1415.82  |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -69.8397  |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           5368 |      0 | DISCHARGE | rmssd                           |     1.68717 | Value 4694.32 on Day1 is 1.69 SD from median (median=862.95, IQR=[595.19, 1782.19]). Noradrenalin=5368.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-064 |  nan    | 9237.55 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      9237.55 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      807.913 |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          -91.254   |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | rmssd                           |     3.68782 | Value 9237.55 on Day1 is 3.69 SD from median (median=862.95, IQR=[595.19, 1782.19]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day5  | 24EI-003-039 |  nan    | 3213.41 | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |      3161.21 |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |     3213.41  |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |            1.65152 |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | rmssd                           |     3.21433 | Value 3213.41 on Day5 is 3.21 SD from median (median=668.82, IQR=[203.37, 1148.20]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |        3621.79 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             3621.79 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |             72.7719 |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -97.9907 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | poincare_sd1                    |     2.21118 | Value 3621.79 on Day1 is 2.21 SD from median (median=613.27, IQR=[424.39, 1281.00]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |        nan |    nan           |        3739.8  |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             3739.8  |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            242.312  |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -93.5207 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |             23 |      0 | DISCHARGE | poincare_sd1                    |     2.29792 | Value 3739.80 on Day1 is 2.30 SD from median (median=613.27, IQR=[424.39, 1281.00]). Noradrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |    nan           |        3561.51 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             3561.51 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |           1003.52   |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -71.8231 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           5368 |      0 | DISCHARGE | poincare_sd1                    |     2.16688 | Value 3561.51 on Day1 is 2.17 SD from median (median=613.27, IQR=[424.39, 1281.00]). Noradrenalin=5368.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |        4458.83 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             4458.83 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            572.527  |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -87.1597 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | poincare_sd1                    |     2.82638 | Value 4458.83 on Day1 is 2.83 SD from median (median=613.27, IQR=[424.39, 1281.00]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |        2076.03 |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |             2423.04 |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |           2076.03   |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  -14.3214 |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | poincare_sd1                    |     2.98159 | Value 2076.03 on Day5 is 2.98 SD from median (median=474.14, IQR=[143.97, 816.87]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.          |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |        4652.96 |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |             4652.96 |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             129.659 |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  -97.2134 |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | poincare_sd2                    |     3.14771 | Value 4652.96 on Day1 is 3.15 SD from median (median=631.56, IQR=[429.66, 1293.48]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |        3238.07 |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |             3238.07 |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             253.894 |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  -92.1591 |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |             23 |      0 | DISCHARGE | poincare_sd2                    |     2.04022 | Value 3238.07 on Day1 is 2.04 SD from median (median=631.56, IQR=[429.66, 1293.48]). Noradrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |        3891.1  |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |             3891.1  |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             554.665 |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  -85.7453 |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | poincare_sd2                    |     2.55137 | Value 3891.10 on Day1 is 2.55 SD from median (median=631.56, IQR=[429.66, 1293.48]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.         |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |             1.91383 |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |                 1.91383  |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |                 0.465935 |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       -75.6544 |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | systolic_duration               |     3.58767 | Value 1.91 on Day1 is 3.59 SD from median (median=0.53, IQR=[0.43, 0.85]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.                   |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |             1.55557 |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |                 0.956985 |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |                 1.55557  |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                        62.5487 |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | systolic_duration               |     4.29778 | Value 1.56 on Day5 is 4.30 SD from median (median=0.46, IQR=[0.39, 0.54]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.                   |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |             0.81518 |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |                 0.42582  |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |                 0.81518  |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                        91.4376 |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         135934 |      0 | DISCHARGE | systolic_duration               |     1.39738 | Value 0.82 on Day5 is 1.40 SD from median (median=0.46, IQR=[0.39, 0.54]). Noradrenalin=135934.00, Patient ANSD=0, OUTCOME=DISCHARGE.                  |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |             1.70287  |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                  1.70287  |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                  0.437897 |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        -74.2847 |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | diastolic_duration              |     3.99238 | Value 1.70 on Day1 is 3.99 SD from median (median=0.46, IQR=[0.39, 0.60]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.                   |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |             0.985893 |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                  0.985893 |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                  0.625582 |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        -36.5466 |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           5368 |      0 | DISCHARGE | diastolic_duration              |     1.69568 | Value 0.99 on Day1 is 1.70 SD from median (median=0.46, IQR=[0.39, 0.60]). Noradrenalin=5368.00, Patient ANSD=0, OUTCOME=DISCHARGE.                    |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |         1.06356  |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |               1.22109 |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |              1.06356  |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    -12.9013 |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | systolic_slope                  |    -1.88828 | Value 1.06 on Day5 is -1.89 SD from median (median=1.43, IQR=[1.35, 1.48]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.                  |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |         0.670304 |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |               1.55903 |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |              0.670304 |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    -57.0051 |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         135934 |      0 | DISCHARGE | systolic_slope                  |    -3.92901 | Value 0.67 on Day5 is -3.93 SD from median (median=1.43, IQR=[1.35, 1.48]). Noradrenalin=135934.00, Patient ANSD=0, OUTCOME=DISCHARGE.                 |
| Day1  | 24EI-003-044 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.18788 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.18788 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.53488 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                     29.2118  |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           2926 |      0 | DISCHARGE | diastolic_slope                 |     2.08733 | Value -1.19 on Day1 is 2.09 SD from median (median=-1.48, IQR=[-1.53, -1.41]). Noradrenalin=2926.00, Patient ANSD=0, OUTCOME=DISCHARGE.                |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.00712 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.00712 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.44002 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                     42.9836  |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | diastolic_slope                 |     3.37714 | Value -1.01 on Day1 is 3.38 SD from median (median=-1.48, IQR=[-1.53, -1.41]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.               |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.32548 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.40514 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.32548 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                     -5.66937 |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | diastolic_slope                 |     2.82919 | Value -1.33 on Day5 is 2.83 SD from median (median=-1.52, IQR=[-1.56, -1.49]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.               |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |          -1.32729 |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |               -1.54282 |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |               -1.32729 |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    -13.9695  |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         135934 |      0 | DISCHARGE | diastolic_slope                 |     2.80289 | Value -1.33 on Day5 is 2.80 SD from median (median=-1.52, IQR=[-1.56, -1.49]). Noradrenalin=135934.00, Patient ANSD=0, OUTCOME=DISCHARGE.              |
| Day5  | 24EI-003-033 |  nan    |  nan    |  66.5955 |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |      69.4296 |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |      66.5955 |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |           -4.08204 |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           2057 |      0 | DISCHARGE | pnn50                           |     2.96761 | Value 66.60 on Day5 is 2.97 SD from median (median=22.55, IQR=[13.15, 29.49]). Noradrenalin=2057.00, Patient ANSD=0, OUTCOME=DISCHARGE.                |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |     219905 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        219905   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |         2692.89 |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             -98.7754  |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | lf_power                        |     2.17058 | Value 219904.77 on Day1 is 2.17 SD from median (median=34266.44, IQR=[15486.88, 77589.25]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.  |
| Day1  | 24EI-003-044 |  nan    |  nan    | nan      |     329424 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        329424   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |        50686.5  |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             -84.6136  |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           2926 |      0 | DISCHARGE | lf_power                        |     3.45113 | Value 329423.90 on Day1 is 3.45 SD from median (median=34266.44, IQR=[15486.88, 77589.25]). Noradrenalin=2926.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |     213644 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        213644   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |         6611.25 |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             -96.9055  |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |             23 |      0 | DISCHARGE | lf_power                        |     2.09738 | Value 213644.24 on Day1 is 2.10 SD from median (median=34266.44, IQR=[15486.88, 77589.25]). Noradrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.     |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |     128551 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |        124224   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |       128551    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |               3.48383 |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | lf_power                        |     1.80103 | Value 128551.34 on Day5 is 1.80 SD from median (median=12497.48, IQR=[2212.33, 49179.39]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |     271576 |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |         19784.1 |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |       271576    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |            1272.7     |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         135934 |      0 | DISCHARGE | lf_power                        |     4.02062 | Value 271575.85 on Day5 is 4.02 SD from median (median=12497.48, IQR=[2212.33, 49179.39]). Noradrenalin=135934.00, Patient ANSD=0, OUTCOME=DISCHARGE.  |
| Day1  | 24EI-003-044 |  nan    |  nan    | nan      |        nan | 628892           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   | 628892           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |         83059.6 |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -86.7927 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           2926 |      0 | DISCHARGE | hf_power                        |     1.09696 | Value 628891.52 on Day1 is 1.10 SD from median (median=66031.19, IQR=[29992.06, 260816.60]). Noradrenalin=2926.00, Patient ANSD=0, OUTCOME=DISCHARGE.  |
| Day1  | 24EI-003-045 |  nan    |  nan    | nan      |        nan |      1.94379e+06 |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |      1.94379e+06 |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |         12683.9 |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -99.3475 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |             23 |      0 | DISCHARGE | hf_power                        |     3.65956 | Value 1943787.80 on Day1 is 3.66 SD from median (median=66031.19, IQR=[29992.06, 260816.60]). Noradrenalin=23.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |      1.60387e+06 |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |      1.60387e+06 |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        301129   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -81.2249 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           5368 |      0 | DISCHARGE | hf_power                        |     2.9971  | Value 1603873.71 on Day1 is 3.00 SD from median (median=66031.19, IQR=[29992.06, 260816.60]). Noradrenalin=5368.00, Patient ANSD=0, OUTCOME=DISCHARGE. |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan | 231933           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   | 264796           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        231933   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -12.4106 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | hf_power                        |     1.07457 | Value 231933.15 on Day5 is 1.07 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day5  | 24EI-003-047 |  nan    |  nan    | nan      |        nan | 301129           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |      1.60387e+06 |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        301129   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              -81.2249 |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           5368 |      0 | DISCHARGE | hf_power                        |     1.4272  | Value 301129.48 on Day5 is 1.43 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Noradrenalin=5368.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-049 |  nan    |  nan    | nan      |        nan | 469293           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |  95433.3         |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        469293   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              391.75   |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           7886 |      0 | DISCHARGE | hf_power                        |     2.28418 | Value 469293.43 on Day5 is 2.28 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Noradrenalin=7886.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-051 |  nan    |  nan    | nan      |        nan | 712112           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |  90622.4         |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        712112   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              685.801  |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |           2557 |      0 | DISCHARGE | hf_power                        |     3.52161 | Value 712111.68 on Day5 is 3.52 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Noradrenalin=2557.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan | 465100           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |  38231.7         |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |        465100   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |             1116.53   |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |         135934 |      0 | DISCHARGE | hf_power                        |     2.26281 | Value 465100.26 on Day5 is 2.26 SD from median (median=21071.09, IQR=[4177.91, 78529.59]). Noradrenalin=135934.00, Patient ANSD=0, OUTCOME=DISCHARGE.  |
| Day1  | 24EI-003-030 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |          0.543097 |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |               0.543097 |                 nan     |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |               0.261445 |                nan      |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     -51.8603 |                      nan      |                   nan      |                    nan      |                                    nan      |                                     nan      |          93084 |      1 | DIESOON   | signal_skewness                 |     2.56099 | Value 0.54 on Day1 is 2.56 SD from median (median=0.13, IQR=[0.03, 0.23]). Noradrenalin=93084.00, Patient ANSD=1, OUTCOME=DIESOON.                     |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            321.101 |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 321.101 |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                 82.3574 |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      -74.3515 |                   nan      |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | peak_trend_slope                |     2.63385 | Value 321.10 on Day1 is 2.63 SD from median (median=103.59, IQR=[80.30, 133.77]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            393.251 |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 393.251 |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                 80.3053 |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      -79.5791 |                   nan      |                    nan      |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | peak_trend_slope                |     3.50752 | Value 393.25 on Day1 is 3.51 SD from median (median=103.59, IQR=[80.30, 133.77]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.            |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            201.664 |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 129.881 |                nan   |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                201.664  |                nan   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                       55.2682 |                   nan      |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | peak_trend_slope                |     3.78867 | Value 201.66 on Day5 is 3.79 SD from median (median=85.19, IQR=[73.51, 100.39]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.             |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |         37621.9 |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |              37621.9 |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |              12188.9 |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   -67.6015 |                    nan      |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | systolic_area                   |     3.89643 | Value 37621.95 on Day1 is 3.90 SD from median (median=14215.17, IQR=[12512.55, 16603.60]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-047 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |         24960.7 |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |              24960.7 |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |              16371.6 |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   -34.4106 |                    nan      |                                    nan      |                                     nan      |           5368 |      0 | DISCHARGE | systolic_area                   |     1.78877 | Value 24960.71 on Day1 is 1.79 SD from median (median=14215.17, IQR=[12512.55, 16603.60]). Noradrenalin=5368.00, Patient ANSD=0, OUTCOME=DISCHARGE.    |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |         20862   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |              14038.8 |                 nan   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |              20862   |                 nan   |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                    48.6024 |                    nan      |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | systolic_area                   |     3.07513 | Value 20862.01 on Day5 is 3.08 SD from median (median=12489.15, IQR=[11208.09, 14703.43]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-038 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |          83255.9 |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |               83255.9 |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |               35609.1 |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    -57.2293 |                                    nan      |                                     nan      |          11161 |      0 | DISCHARGE | diastolic_area                  |     1.96558 | Value 83255.92 on Day1 is 1.97 SD from median (median=41099.95, IQR=[32234.64, 49929.12]). Noradrenalin=11161.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day1  | 24EI-003-064 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |         117333   |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |              117333   |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |               32562.3 |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    -72.2479 |                                    nan      |                                     nan      |          15716 |      0 | DISCHARGE | diastolic_area                  |     3.55447 | Value 117332.75 on Day1 is 3.55 SD from median (median=41099.95, IQR=[32234.64, 49929.12]). Noradrenalin=15716.00, Patient ANSD=0, OUTCOME=DISCHARGE.  |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |          64902.3 |       nan        |         nan       |        nan        |            nan     |                            nan   |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |               46025.9 |                                nan    |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |               64902.3 |                                 nan   |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                     41.0128 |                                    nan      |                                     nan      |          27969 |      0 | DISCHARGE | diastolic_area                  |     2.46353 | Value 64902.34 on Day5 is 2.46 SD from median (median=35787.55, IQR=[27280.11, 41745.63]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.   |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                          11256.3 |                             nan   |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                               9949.33 |                                 nan    |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                               11256.3 |                                  nan   |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                     13.1363 |                                     nan      |          27969 |      0 | DISCHARGE | systolic_amplitude_variability  |     2.63569 | Value 11256.30 on Day5 is 2.64 SD from median (median=7645.77, IQR=[6546.00, 8371.89]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.      |
| Day5  | 24EI-003-039 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                           11629.5 |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                9003.58 |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                11629.5 |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                      29.1658 |          27969 |      0 | DISCHARGE | diastolic_amplitude_variability |     2.79722 | Value 11629.54 on Day5 is 2.80 SD from median (median=6799.79, IQR=[6220.86, 7536.15]). Noradrenalin=27969.00, Patient ANSD=0, OUTCOME=DISCHARGE.      |
| Day5  | 24EI-003-053 |  nan    |  nan    | nan      |        nan |    nan           |         nan    |         nan    |           nan       |           nan        |           nan   |            nan   |       nan        |         nan       |        nan        |            nan     |                            nan   |                           11385.4 |      nan    |       nan    |              nan    |              nan    |               nan        |                nan        |             nan       |              nan       |     nan      |           nan   |    nan           |             nan        |                 nan     |                nan   |                 nan   |                                nan    |                                6655.49 |     nan     |      nan     |            nan      |             nan     |               nan        |                nan        |            nan        |              nan       |     nan      |          nan    |           nan   |             nan        |                nan      |                nan   |                 nan   |                                 nan   |                                11385.4 |         nan       |          nan       |                  nan      |                  nan      |                       nan      |                        nan      |                    nan      |                    nan       |          nan       |             nan       |              nan      |                     nan      |                      nan      |                   nan      |                    nan      |                                    nan      |                                      71.0683 |         135934 |      0 | DISCHARGE | diastolic_amplitude_variability |     2.65584 | Value 11385.44 on Day5 is 2.66 SD from median (median=6799.79, IQR=[6220.86, 7536.15]). Noradrenalin=135934.00, Patient ANSD=0, OUTCOME=DISCHARGE.     |

## Feature Changes

| patient_id      |   sdnn_Day1 |   sdnn_Day5 |   rmssd_Day1 |   rmssd_Day5 |   poincare_sd1_Day1 |   poincare_sd1_Day5 |   poincare_sd2_Day1 |   poincare_sd2_Day5 |   systolic_duration_Day1 |   systolic_duration_Day5 |   diastolic_duration_Day1 |   diastolic_duration_Day5 |   systolic_slope_Day1 |   systolic_slope_Day5 |   diastolic_slope_Day1 |   diastolic_slope_Day5 |   nn50_Day1 |   nn50_Day5 |   pnn50_Day1 |   pnn50_Day5 |   hrv_triangular_index_Day1 |   hrv_triangular_index_Day5 |   lf_power_Day1 |   lf_power_Day5 |    hf_power_Day1 |   hf_power_Day5 |   signal_skewness_Day1 |   signal_skewness_Day5 |   peak_trend_slope_Day1 |   peak_trend_slope_Day5 |   systolic_area_Day1 |   systolic_area_Day5 |   diastolic_area_Day1 |   diastolic_area_Day5 |   systolic_amplitude_variability_Day1 |   systolic_amplitude_variability_Day5 |   diastolic_amplitude_variability_Day1 |   diastolic_amplitude_variability_Day5 |   sdnn_pct_change |   rmssd_pct_change |   poincare_sd1_pct_change |   poincare_sd2_pct_change |   systolic_duration_pct_change |   diastolic_duration_pct_change |   systolic_slope_pct_change |   diastolic_slope_pct_change |   nn50_pct_change |   pnn50_pct_change |   hrv_triangular_index_pct_change |   lf_power_pct_change |   hf_power_pct_change |   signal_skewness_pct_change |   peak_trend_slope_pct_change |   systolic_area_pct_change |   diastolic_area_pct_change |   systolic_amplitude_variability_pct_change |   diastolic_amplitude_variability_pct_change | sdnn_Overall_Median_IQR   | sdnn_Overall_Mean_SD   | rmssd_Overall_Median_IQR   | rmssd_Overall_Mean_SD   | poincare_sd1_Overall_Median_IQR   | poincare_sd1_Overall_Mean_SD   | poincare_sd2_Overall_Median_IQR   | poincare_sd2_Overall_Mean_SD   | systolic_duration_Overall_Median_IQR   | systolic_duration_Overall_Mean_SD   | diastolic_duration_Overall_Median_IQR   | diastolic_duration_Overall_Mean_SD   | systolic_slope_Overall_Median_IQR   | systolic_slope_Overall_Mean_SD   | diastolic_slope_Overall_Median_IQR   | diastolic_slope_Overall_Mean_SD   |   heart_rate_Day1 |   heart_rate_Day5 |   heart_rate_pct_change | heart_rate_Overall_Median_IQR   | heart_rate_Overall_Mean_SD   |   sample_entropy_Overall_Median_IQR |   sample_entropy_Overall_Mean_SD | nn50_Overall_Median_IQR   | nn50_Overall_Mean_SD   | pnn50_Overall_Median_IQR   | pnn50_Overall_Mean_SD   | hrv_triangular_index_Overall_Median_IQR   | hrv_triangular_index_Overall_Mean_SD   | lf_power_Overall_Median_IQR   | lf_power_Overall_Mean_SD   | hf_power_Overall_Median_IQR   | hf_power_Overall_Mean_SD   | signal_skewness_Overall_Median_IQR   | signal_skewness_Overall_Mean_SD   | peak_trend_slope_Overall_Median_IQR   | peak_trend_slope_Overall_Mean_SD   | systolic_area_Overall_Median_IQR   | systolic_area_Overall_Mean_SD   | diastolic_area_Overall_Median_IQR   | diastolic_area_Overall_Mean_SD   | systolic_amplitude_variability_Overall_Median_IQR   | systolic_amplitude_variability_Overall_Mean_SD   | diastolic_amplitude_variability_Overall_Median_IQR   | diastolic_amplitude_variability_Overall_Mean_SD   |
|:----------------|------------:|------------:|-------------:|-------------:|--------------------:|--------------------:|--------------------:|--------------------:|-------------------------:|-------------------------:|--------------------------:|--------------------------:|----------------------:|----------------------:|-----------------------:|-----------------------:|------------:|------------:|-------------:|-------------:|----------------------------:|----------------------------:|----------------:|----------------:|-----------------:|----------------:|-----------------------:|-----------------------:|------------------------:|------------------------:|---------------------:|---------------------:|----------------------:|----------------------:|--------------------------------------:|--------------------------------------:|---------------------------------------:|---------------------------------------:|------------------:|-------------------:|--------------------------:|--------------------------:|-------------------------------:|--------------------------------:|----------------------------:|-----------------------------:|------------------:|-------------------:|----------------------------------:|----------------------:|----------------------:|-----------------------------:|------------------------------:|---------------------------:|----------------------------:|--------------------------------------------:|---------------------------------------------:|:--------------------------|:-----------------------|:---------------------------|:------------------------|:----------------------------------|:-------------------------------|:----------------------------------|:-------------------------------|:---------------------------------------|:------------------------------------|:----------------------------------------|:-------------------------------------|:------------------------------------|:---------------------------------|:-------------------------------------|:----------------------------------|------------------:|------------------:|------------------------:|:--------------------------------|:-----------------------------|------------------------------------:|---------------------------------:|:--------------------------|:-----------------------|:---------------------------|:------------------------|:------------------------------------------|:---------------------------------------|:------------------------------|:---------------------------|:------------------------------|:---------------------------|:-------------------------------------|:----------------------------------|:--------------------------------------|:-----------------------------------|:-----------------------------------|:--------------------------------|:------------------------------------|:---------------------------------|:----------------------------------------------------|:-------------------------------------------------|:-----------------------------------------------------|:--------------------------------------------------|
| 24EI-003-030    |    484.292  |    177.3    |     642.954  |     260.688  |            455.87   |            184.607  |             510.198 |            169.251  |                 0.395169 |                 0.552125 |                  0.295622 |                  0.333718 |              1.09228  |              1.35186  |               -1.41075 |               -1.53746 |    63.8     |    103.813  |     18.3326  |     28.3856  |                     2.97678 |                     2.7063  |        13776.7  |        2195.26  |  28436.7         |         4071.62 |             0.543097   |             0.261445   |                 67.2316 |                 88.4075 |              9945.91 |              11377.9 |               24494.4 |               39112.3 |                               7886.58 |                               7235.64 |                                8263.08 |                                9210.91 |         -63.3898  |          -59.4547  |                  -59.5045 |                  -66.8264 |                       39.7187  |                       12.887    |                    23.7648  |                     8.98192  |          62.7167  |           54.8369  |                         -9.0863   |             -84.0654  |             -85.6818  |                    -51.8603  |                      31.497   |                   14.3976  |                    59.6785  |                                   -8.25372  |                                     11.4706  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-032    |   1055.77   |    144.685  |    1345.84   |     202.652  |            953.213  |            143.462  |            1251.57  |            145.328  |                 0.432787 |                 0.369084 |                  0.368274 |                  0.284402 |              1.31597  |              1.47484  |               -1.45661 |               -1.55037 |    40.7019  |     31.3837 |     14.6117  |      7.60614 |                     4.08881 |                     3.4286  |        44630    |        1315.8   | 248879           |         2511.6  |             0.232542   |             0.118093   |                 74.6289 |                 65.0875 |             14391.5  |              11397.8 |               32416   |               24807   |                               9321.96 |                               8563.26 |                                7001.83 |                                6120.01 |         -86.2957  |          -84.9423  |                  -84.9497 |                  -88.3884 |                      -14.7193  |                      -22.7745   |                    12.0724  |                     6.43659  |         -22.8938  |          -47.9448  |                        -16.1467   |             -97.0518  |             -98.9908  |                    -49.2167  |                     -12.7851  |                  -20.8023  |                   -23.473   |                                   -8.13876  |                                    -12.5941  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-033    |    459.307  |    660.532  |     648.452  |     928.41   |            439.962  |            658.091  |             451.252 |            664.387  |                 0.501066 |                 0.558834 |                  0.726449 |                  0.699658 |              1.50177  |              1.44626  |               -1.50139 |               -1.50335 |   166.023   |    158.007  |     69.4296  |     66.5955  |                     4.83579 |                     4.79604 |        15816.8  |       33336.5   |  36374.9         |        64262.8  |            -0.00886742 |            -0.0536944  |                123.643  |                125.203  |             16763.1  |              17568.6 |               50370.8 |               52736.3 |                               6720.63 |                               7302.19 |                                6141    |                                7214.14 |          43.8107  |           43.1734  |                   49.579  |                   47.2321 |                       11.5289  |                       -3.68786  |                    -3.69615 |                     0.13055  |          -4.82842 |           -4.08204 |                         -0.821937 |             110.767   |              76.668   |                    505.525   |                       1.26154 |                    4.80514 |                     4.69618 |                                    8.65334  |                                     17.4749  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-035    |    402.283  |    814.663  |     541.043  |    1090.26   |            383.605  |            787.084  |             419.451 |            858.192  |                 0.562066 |                 0.540988 |                  0.789941 |                  0.52298  |              1.49624  |              1.39892  |               -1.53209 |               -1.48442 |   105.326   |     49.4557 |     50.484   |     20.773   |                     4.65969 |                     4.53554 |        23388    |      105385     |  53855.9         |        56837.3  |             0.195282   |             0.290502   |                135.064  |                102.528  |             17758.4  |              14802.2 |               48604.1 |               39971.7 |                               5550.03 |                               7765.87 |                                6507.4  |                                6813.76 |         102.51    |          101.511   |                  105.181  |                  104.599  |                       -3.75005 |                      -33.795    |                    -6.50453 |                    -3.11158  |         -53.0449  |          -58.8524  |                         -2.66437  |             350.593   |               5.53576 |                     48.76    |                     -24.0895  |                  -16.6466  |                   -17.7606  |                                   39.9248   |                                      4.70792 | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-036    |    777.938  |    150.661  |    1063.57   |     173.261  |            753.723  |            122.709  |             819.629 |            170.573  |                 0.552793 |                 0.407574 |                  0.541118 |                  0.538761 |              1.14812  |              1.43058  |               -1.50845 |               -1.56719 |   103.227   |     65.8343 |     40.4055  |     21.2541  |                     4.53761 |                     5.17717 |        78225.1  |        2040.66  | 105402           |         4496.8  |            -0.0195071  |            -0.074073   |                107.404  |                 94.3992 |             13833.3  |              11074.2 |               46967.8 |               44469.9 |                               7262.58 |                               6286.52 |                                8773.26 |                                6171.84 |         -80.6334  |          -83.7095  |                  -83.7196 |                  -79.189  |                      -26.2701  |                       -0.435564 |                    24.6017  |                     3.89375  |         -36.2239  |          -47.3979  |                         14.0945   |             -97.3913  |             -95.7337  |                    279.723   |                     -12.1084  |                  -19.9451  |                    -5.31832 |                                  -13.4396   |                                    -29.6516  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-037    |    590.349  |    155.35   |     826.814  |     205.511  |            588.956  |            145.504  |             597.145 |            163.606  |                 0.488391 |                 0.375287 |                  0.438259 |                  0.273059 |              1.49561  |              1.36297  |               -1.53571 |               -1.54589 |   106.914   |     24.1667 |     34.2842  |      6.1759  |                     5.2612  |                     3.14754 |        17354.6  |        5102.3   |  34658.1         |         6555.66 |             0.227752   |             0.264914   |                 89.8926 |                 64.6937 |             16931.8  |              11573.8 |               33149.9 |               26406.8 |                               6154.93 |                               6363.36 |                                5026.53 |                                6490.14 |         -73.6851  |          -75.1442  |                  -75.2945 |                  -72.602  |                      -23.1584  |                      -37.6946   |                    -8.86858 |                     0.662713 |         -77.3961  |          -81.9862  |                        -40.1746   |             -70.5997  |             -81.0848  |                     16.3167  |                     -28.0322  |                  -31.6444  |                   -20.3414  |                                    3.38643  |                                     29.1177  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-038    |   3882.36   |    106.717  |    5164.59   |     102.768  |           3621.79   |             72.7719 |            4652.96  |            129.659  |                 1.35036  |                 0.386588 |                  1.70287  |                  0.437897 |              1.20529  |              1.39501  |               -1.31684 |               -1.56853 |    84.2188  |     67.1697 |     48.7352  |     19.8514  |                     3.86189 |                     5.15537 |       219905    |        2692.89  | 440578           |         2230.48 |             0.358336   |             0.087855   |                321.101  |                 82.3574 |             37621.9  |              12188.9 |               83255.9 |               35609.1 |                              10266.7  |                               6476.07 |                               11368.7  |                                6785.82 |         -97.2512  |          -98.0101  |                  -97.9907 |                  -97.2134 |                      -71.3715  |                      -74.2847   |                    15.7414  |                    19.1132   |         -20.2438  |          -59.2668  |                         33.4934   |             -98.7754  |             -99.4937  |                    -75.4825  |                     -74.3515  |                  -67.6015  |                   -57.2293  |                                  -36.9215   |                                    -40.3116  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-039    |   2066.01   |   2038.02   |    3161.21   |    3213.41   |           2423.04   |           2076.03   |            2056.01  |           1724.34   |                 0.956985 |                 1.55557  |                  0.408239 |                  0.726992 |              1.22109  |              1.06356  |               -1.40514 |               -1.32548 |    45.3506  |     57.3889 |     24.3362  |     32.3041  |                     3.92724 |                     3.19946 |       124224    |      128551     | 264796           |       231933    |             0.0996579  |             0.319158   |                129.881  |                201.664  |             14038.8  |              20862   |               46025.9 |               64902.3 |                               9949.33 |                              11256.3  |                                9003.58 |                               11629.5  |          -1.35459 |            1.65152 |                  -14.3214 |                  -16.1316 |                       62.5487  |                       78.0798   |                   -12.9013  |                    -5.66937  |          26.5448  |           32.7409  |                        -18.5316   |               3.48383 |             -12.4106  |                    220.254   |                      55.2682  |                   48.6024  |                    41.0128  |                                   13.1363   |                                     29.1658  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-040    |    142.582  |     92.7449 |     201.058  |     122.338  |            142.372  |             86.6031 |             142.776 |             98.0288 |                 0.549361 |                 0.328306 |                  0.329492 |                  0.256978 |              1.12263  |              1.42428  |               -1.38483 |               -1.56158 |    22.2156  |     13.4371 |      6.18801 |      2.98023 |                     2.95859 |                     3.50499 |         1265.02 |        2263.54  |   2570.71        |         6511.94 |             0.307351   |             0.148735   |                 87.625  |                 58.4112 |              9525.47 |              10886.4 |               40274.9 |               26720   |                               8581.83 |                               6529.07 |                               10077.5  |                                6590.46 |         -34.9534  |          -39.1527  |                  -39.1713 |                  -31.3407 |                      -40.2385  |                      -22.008    |                    26.8702  |                    12.7635   |         -39.5148  |          -51.8386  |                         18.4681   |              78.9328  |             153.313   |                    -51.6075  |                     -33.3396  |                   14.2872  |                   -33.656   |                                  -23.9199   |                                    -34.6025  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-044    |   1326.29   |    846.644  |    1927.64   |    1167.52   |           1390.27   |            826.792  |            1307.44  |            866.425  |                 0.949191 |                 0.451006 |                  0.53249  |                  0.431185 |              0.76228  |              1.5567   |               -1.18788 |               -1.53488 |   105.468   |     64.3023 |     61.8896  |     19.431   |                     2.97858 |                     4.99396 |       329424    |       50686.5   | 628892           |        83059.6  |            -0.177638   |            -0.193941   |                147.173  |                 87.7317 |             16125    |               9983.3 |               60414.5 |               40998.5 |                               8359.52 |                               7525.68 |                                9672.11 |                                6367.89 |         -36.1645  |          -39.4328  |                  -40.5299 |                  -33.7314 |                      -52.4852  |                      -19.0248   |                   104.217   |                    29.2118   |         -39.0315  |          -68.6038  |                         67.6626   |             -84.6136  |             -86.7927  |                      9.17794 |                     -40.3886  |                  -38.0882  |                   -32.1379  |                                   -9.97476  |                                    -34.1624  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-045    |   3370.42   |    248.571  |    5001.01   |     342.141  |           3739.8    |            242.312  |            3238.07  |            253.894  |                 1.14125  |                 0.42289  |                  0.742135 |                  0.515247 |              1.14413  |              1.55579  |               -1.23196 |               -1.55692 |    68.6881  |     74.2566 |     41.9658  |     23.8409  |                     3.81757 |                     5.41538 |       213644    |        6611.25  |      1.94379e+06 |        12683.9  |             0.159857   |             0.103695   |                181.61   |                 93.8495 |             19172.3  |              15825.1 |               66161.2 |               35966   |                              11592.8  |                               6118.73 |                               10082.9  |                                5236.48 |         -92.6249  |          -93.1586  |                  -93.5207 |                  -92.1591 |                      -62.9449  |                      -30.5724   |                    35.9805  |                    26.3777   |           8.10695 |          -43.1898  |                         41.8541   |             -96.9055  |             -99.3475  |                    -35.1328  |                     -48.3235  |                  -17.4587  |                   -45.6388  |                                  -47.2195   |                                    -48.0656  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-047    |   2985.39   |   1018.95   |    4694.32   |    1415.82   |           3561.51   |           1003.52   |            2551.54  |           1038.16   |                 0.928519 |                 0.592517 |                  0.985893 |                  0.625582 |              1.45938  |              1.48273  |               -1.51152 |               -1.50646 |   112.841   |    111      |     46.1642  |     44.8601  |                     4.79853 |                     4.68872 |        64413.3  |       91406.8   |      1.60387e+06 |       301129    |             0.133252   |            -0.0242231  |                201.261  |                124.124  |             24960.7  |              16371.6 |               58736.2 |               53390.8 |                               8762.46 |                               7973.95 |                                8103.26 |                                7413.28 |         -65.8688  |          -69.8397  |                  -71.8231 |                  -59.3127 |                      -36.1869  |                      -36.5466   |                     1.59978 |                    -0.334558 |          -1.63161 |           -2.82494 |                         -2.28838  |              41.9068  |             -81.2249  |                   -118.178   |                     -38.3269  |                  -34.4106  |                    -9.10073 |                                   -8.99866  |                                     -8.51484 | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-049    |    647.083  |   1158.48   |     899.089  |    1554.64   |            637.576  |           1107.97   |             665.983 |           1219.13   |                 0.486273 |                 0.499019 |                  0.415797 |                  0.46955  |              1.37516  |              1.44902  |               -1.4293  |               -1.49467 |    89.8176  |     82.1121 |     30.6249  |     29.5351  |                     4.49276 |                     4.96811 |       126331    |       44658.1   |  95433.3         |       469293    |             0.0478916  |            -0.121129   |                 89.726  |                 96.4524 |             12344.1  |              14407.2 |               35902.7 |               41320.2 |                               8662.43 |                               8301.95 |                                6781.52 |                                7577.11 |          79.0308  |           72.9127  |                   73.7793 |                   83.0566 |                        2.62122 |                       12.9277   |                     5.3712  |                     4.57377  |          -8.57906 |           -3.55845 |                         10.5804   |             -64.65    |             391.75    |                   -352.924   |                       7.49662 |                   16.7135  |                    15.0896  |                                   -4.16136  |                                     11.7317  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-050    |    419.1    |    639.619  |     584.664  |     884.922  |            419.205  |            626.782  |             422.46  |            652.816  |                 0.479336 |                 0.469303 |                  0.520967 |                  0.325198 |              1.45749  |              1.32708  |               -1.54424 |               -1.50106 |    80.2817  |     58.0173 |     30.2326  |     17.3753  |                     4.89349 |                     4.42222 |        23902.9  |       39943.3   |  42093.1         |        64939.6  |             0.0651175  |             0.163049   |                100.396  |                 78.708  |             15128.1  |              11977.6 |               39863.9 |               31425   |                               6609.51 |                               8635.4  |                                5813.85 |                                6426.05 |          52.6172  |           51.3556  |                   49.5169 |                   54.5272 |                       -2.09309 |                      -37.578    |                    -8.94763 |                    -2.79597  |         -27.7328  |          -42.5279  |                         -9.6304   |              67.1064  |              54.276   |                    150.392   |                     -21.6022  |                  -20.8257  |                   -21.1693  |                                   30.6513   |                                     10.53    | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-051    |    703.07   |    965.728  |     976.057  |    1296.17   |            692.24   |            925.64   |             714.889 |           1016.93   |                 0.556159 |                 0.524398 |                  0.532982 |                  0.494397 |              1.30588  |              1.48339  |               -1.48273 |               -1.49551 |   109.784   |     73.8403 |     43.6878  |     27.2159  |                     4.51315 |                     5.10551 |        46186.1  |       94100.7   |  90622.4         |       712112    |             0.00446333 |             0.00905797 |                108.233  |                101.698  |             13837.3  |              14303.8 |               44790.4 |               41887.4 |                               8222.53 |                               8156.86 |                                7593.98 |                                7286.67 |          37.3586  |           32.7969  |                   33.7166 |                   42.25   |                       -5.71068 |                       -7.23943  |                    13.5934  |                     0.862106 |         -32.7406  |          -37.7035  |                         13.125    |             103.743   |             685.801   |                    102.942   |                      -6.03799 |                    3.37139 |                    -6.48113 |                                   -0.798679 |                                     -4.04682 | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-052    |    734.003  |    190.231  |    1045.52   |     294.404  |            745.146  |            208.43   |             723.288 |            168.704  |                 0.612276 |                 0.384326 |                  0.474821 |                  0.334058 |              1.35164  |              1.25306  |               -1.47806 |               -1.5509  |    84.9873  |    126.766  |     37.5549  |     30.3581  |                     4.2071  |                     3.18106 |        48967.2  |         765.02  |  78206.4         |         2037.59 |             0.0274028  |             0.224232   |                106.785  |                 71.7757 |             15013.3  |              12789.4 |               41925   |               26880.5 |                               8603.78 |                               6596.8  |                                7511.07 |                                6900.98 |         -74.0831  |          -71.8415  |                  -72.0283 |                  -76.6753 |                      -37.2299  |                      -29.6454   |                    -7.29379 |                     4.92862  |          49.1588  |          -19.1633  |                        -24.3883   |             -98.4377  |             -97.3946  |                    718.28    |                     -32.7851  |                  -14.813   |                   -35.8844  |                                  -23.3268   |                                     -8.12248 | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-053    |    526.571  |   1520.59   |     743.323  |    2213.55   |            526.285  |           1607.69   |             526.982 |           1479.71   |                 0.42582  |                 0.81518  |                  0.328984 |                  0.3829   |              1.55903  |              0.670304 |               -1.54282 |               -1.32729 |    66.6867  |     76.4118 |     17.2552  |     29.3583  |                     4.62859 |                     2.88719 |        19784.1  |      271576     |  38231.7         |       465100    |            -0.0695725  |             0.363341   |                 75.4231 |                118.592  |             11388.5  |              13305.2 |               31277.7 |               62535   |                               8243.45 |                               9556.03 |                                6655.49 |                               11385.4  |         188.771   |          197.791   |                  205.479  |                  180.789  |                       91.4376  |                       16.3888   |                   -57.0051  |                   -13.9695   |          14.5833  |           70.1416  |                        -37.6227   |            1272.7     |            1116.53    |                   -622.248   |                      57.2351  |                   16.8301  |                    99.9348  |                                   15.9228   |                                     71.0683  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-055    |    286.914  |    394.154  |     386.653  |     529.719  |            273.817  |            375.754  |             297.128 |            419.447  |                 0.425554 |                 0.403372 |                  0.420737 |                  0.283633 |              1.48359  |              1.45858  |               -1.55711 |               -1.50191 |    58.0422  |     40.0946 |     19.1602  |     11.739   |                     5.17845 |                     3.80753 |         7141.17 |       27885.1   |  13783.5         |        36493.9  |             0.294955   |             0.174989   |                 84.4567 |                 68.0705 |             14021    |              10319.5 |               32174.2 |               25048.3 |                               6767.37 |                               8344.85 |                                5108.49 |                                6060.13 |          37.3771  |           37.0012  |                   37.2283 |                   41.1672 |                       -5.21263 |                      -32.5867   |                    -1.68638 |                    -3.5451   |         -30.9216  |          -38.7322  |                        -26.4734   |             290.483   |             164.764   |                    -40.6726  |                     -19.4018  |                  -26.3995  |                   -22.1479  |                                   23.3101   |                                     18.6286  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-056    |     75.5478 |    601.629  |      90.8561 |     923.228  |             64.3291 |            653.738  |              83.861 |            546.052  |                 0.365634 |                 0.470279 |                  0.40416  |                  0.355771 |              1.50013  |              1.54742  |               -1.56883 |               -1.46233 |     5.30435 |    140.007  |      1.32823 |     39.0462  |                     4.78647 |                     5.04478 |         3844.8  |        7281.38  |   7957.96        |        16746.8  |             0.157549   |             0.0699429  |                 77.0262 |                 82.6565 |             13018    |              11151.5 |               28770.1 |               28478.9 |                               6329.47 |                               9874.34 |                                5411.11 |                                7957.77 |         696.355   |          916.143   |                  916.239  |                  551.14   |                       28.6199  |                      -11.9728   |                     3.15283 |                    -6.78838  |        2539.48    |         2839.72    |                          5.39654  |              89.3824  |             110.441   |                    -55.6057  |                       7.30963 |                  -14.3382  |                    -1.01221 |                                   56.0058   |                                     47.0635  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-064    |   5276.9    |    565.556  |    9237.55   |     807.913  |           4458.83   |            572.527  |            3891.1   |            554.665  |                 1.91383  |                 0.465935 |                  0.614782 |                  0.342793 |              0.902077 |              1.4181   |               -1.00712 |               -1.44002 |    36.375   |     93.3563 |     40.7847  |     28.5345  |                     3.18909 |                     3.99906 |        75681.8  |       17713.6   | 388589           |        25395.4  |             0.132285   |             0.0163907  |                393.251  |                 80.3053 |             15876.6  |              10651   |              117333   |               32562.3 |                              11662    |                               8380.9  |                               11880.7  |                                7842.41 |         -89.2824  |          -91.254   |                  -87.1597 |                  -85.7453 |                      -75.6544  |                      -44.2414   |                    57.2041  |                    42.9836   |         156.65    |          -30.0364  |                         25.3982   |             -76.5947  |             -93.4647  |                    -87.6095  |                     -79.5791  |                  -32.9138  |                   -72.2479  |                                  -28.1347   |                                    -33.9902  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-070    |    448.54   |     49.5592 |     626.78   |      62.4072 |            443.688  |             44.1869 |             453.965 |             53.6632 |                 0.374298 |                 0.40736  |                  0.266865 |                  0.381788 |              1.51164  |              1.31927  |               -1.54575 |               -1.56958 |    36.5926  |     24.56   |      8.08312 |      6.57362 |                     3.62749 |                     5.0367  |        15376.9  |         651.087 |  24749.6         |         1183.34 |             0.111287   |             0.0546201  |                 63.6264 |                 78.8951 |             11408    |              15335.7 |               26970.9 |               32001.7 |                               7946.05 |                               5755.12 |                                5640.99 |                                4776.11 |         -88.951   |          -90.0432  |                  -90.041  |                  -88.179  |                        8.83318 |                       43.0641   |                   -12.7261  |                     1.54185  |         -32.8826  |          -18.6747  |                         38.8481   |             -95.7658  |             -95.2188  |                    -50.9195  |                      23.9973  |                   34.4293  |                    18.6527  |                                  -27.5725   |                                    -15.3321  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| 24EI-003-071    |    356.451  |     91.9346 |     482.477  |     116.286  |            341.66   |             82.3227 |             368.209 |             99.3159 |                 0.408703 |                 0.368944 |                  0.385002 |                  0.333984 |              1.34509  |              1.48023  |               -1.41058 |               -1.5665  |    66.0815  |     21.734  |     18.6951  |      5.20601 |                     4.51521 |                     5.47809 |        10085.2  |         848.566 |  14569.9         |         1796.68 |             0.269577   |             0.164268   |                 78.9167 |                 70.217  |             10149.9  |              12989.5 |               28332.9 |               26373.7 |                               9127.32 |                               6759.42 |                                7634.65 |                                5087.81 |         -74.2083  |          -75.8981  |                  -75.9051 |                  -73.0273 |                       -9.72797 |                      -13.2513   |                    10.047   |                    11.0534   |         -67.1103  |          -72.1532  |                         21.3254   |             -91.586   |             -87.6685  |                    -39.0645  |                     -11.0239  |                   27.9761  |                    -6.91503 |                                  -25.943    |                                    -33.3589  | nan                       | nan                    | nan                        | nan                     | nan                               | nan                            | nan                               | nan                            | nan                                    | nan                                 | nan                                     | nan                                  | nan                                 | nan                              | nan                                  | nan                               |               nan |               nan |                     nan | nan                             | nan                          |                                 nan |                              nan | nan                       | nan                    | nan                        | nan                     | nan                                       | nan                                    | nan                           | nan                        | nan                           | nan                        | nan                                  | nan                               | nan                                   | nan                                | nan                                | nan                             | nan                                 | nan                              | nan                                                 | nan                                              | nan                                                  | nan                                               |
| Overall_Summary |    nan      |    nan      |     nan      |     nan      |            nan      |            nan      |             nan     |            nan      |               nan        |               nan        |                nan        |                nan        |            nan        |            nan        |              nan       |              nan       |   nan       |    nan      |    nan       |    nan       |                   nan       |                   nan       |          nan    |         nan     |    nan           |          nan    |           nan          |           nan          |                nan      |                nan      |               nan    |                nan   |                 nan   |                 nan   |                                nan    |                                nan    |                                 nan    |                                 nan    |         nan       |          nan       |                  nan      |                  nan      |                      nan       |                      nan        |                   nan       |                   nan        |         nan       |          nan       |                        nan        |             nan       |             nan       |                    nan       |                     nan       |                  nan       |                   nan       |                                  nan        |                                    nan       | 578.0 (234.0�979.0)       | 901.1 � 1082.7         | 817.4 (330.2�1308.6)       | 1322.7 � 1737.6         | 580.7 (233.8�932.5)               | 900.3 � 1063.0                 | 550.4 (233.1�1022.2)              | 878.1 � 994.9                  | 0.5 (0.4�0.6)                          | 0.6 � 0.3                           | 0.4 (0.3�0.5)                           | 0.5 � 0.2                            | 1.4 (1.3�1.5)                       | 1.3 � 0.2                        | -1.5 (-1.5�-1.4)                     | -1.5 � 0.1                        |               nan |               nan |                     nan | 77.9 (67.8�89.4)                | 78.7 � 14.1                  |                                 nan |                              nan | 67.9 (44.2�103.4)         | 73.1 � 37.2            | 27.8 (17.3�39.4)           | 27.8 � 16.7             | 4.5 (3.6�4.9)                             | 4.3 � 0.8                              | 23645.5 (6234.0�76317.6)      | 55917.7 � 75168.6          | 40162.4 (11502.4�236169.5)    | 199039.2 � 388310.1        | 0.1 (0.0�0.2)                        | 0.1 � 0.2                         | 89.8 (78.3�119.9)                     | 110.9 � 63.6                       | 13835.3 (11395.4�15838.0)          | 14418.1 � 4707.9                | 39488.1 (30650.8�47376.9)           | 42086.7 � 17429.8                | 8065.4 (6692.9�8642.2)                              | 8007.8 � 1501.9                                  | 6951.4 (6164.1�8143.2)                               | 7440.9 � 1840.0                                   |

## Clinical Correlations

| Feature                         | Clinical_Var   |   Day1_Spearman_R |   Day1_P_value |   Day5_Spearman_R |   Day5_P_value |   Change_Spearman_R |   Change_P_value |   Overall_Spearman_R |   Overall_P_value |
|:--------------------------------|:---------------|------------------:|---------------:|------------------:|---------------:|--------------------:|-----------------:|---------------------:|------------------:|
| sdnn                            | ANSD           |       -0.337832   |    0.124123    |      -0.498704    |     0.0181521  |         -0.144785   |       0.348398   |           -0.413925  |       0.00522038  |
| sdnn                            | OUTCOME        |       -0.166337   |    0.459406    |      -0.118812    |     0.598457   |          0.0475248  |       0.759344   |           -0.11872   |       0.442755    |
| sdnn                            | Adrenalin      |       -0.211745   |    0.344157    |      -0.394692    |     0.0690906  |         -0.175607   |       0.254204   |           -0.275055  |       0.0707601   |
| sdnn                            | Noradrenalin   |       -0.361942   |    0.0978766   |      -0.296443    |     0.180368   |          0.0604178  |       0.696843   |           -0.343607  |       0.0223929   |
| rmssd                           | ANSD           |       -0.353919   |    0.106109    |      -0.450443    |     0.0354022  |         -0.128698   |       0.405082   |           -0.405888  |       0.00626437  |
| rmssd                           | OUTCOME        |       -0.142575   |    0.52677     |      -0.0950497   |     0.673935   |          0.0475248  |       0.759344   |           -0.100912  |       0.514549    |
| rmssd                           | Adrenalin      |       -0.218521   |    0.328569    |      -0.38227     |     0.0791342  |         -0.191417   |       0.213237   |           -0.276747  |       0.0689742   |
| rmssd                           | Noradrenalin   |       -0.381141   |    0.0800988   |      -0.260305    |     0.242011   |          0.0728402  |       0.638439   |           -0.336836  |       0.0253662   |
| poincare_sd1                    | ANSD           |       -0.337832   |    0.124123    |      -0.450443    |     0.0354022  |         -0.128698   |       0.405082   |           -0.401869  |       0.0068511   |
| poincare_sd1                    | OUTCOME        |       -0.166337   |    0.459406    |      -0.0950497   |     0.673935   |          0.0475248  |       0.759344   |           -0.106848  |       0.489989    |
| poincare_sd1                    | Adrenalin      |       -0.204969   |    0.360171    |      -0.38227     |     0.0791342  |         -0.194805   |       0.205094   |           -0.273362  |       0.0725823   |
| poincare_sd1                    | Noradrenalin   |       -0.359684   |    0.100145    |      -0.260305    |     0.242011   |          0.068323   |       0.65945    |           -0.331476  |       0.0279474   |
| poincare_sd2                    | ANSD           |       -0.337832   |    0.124123    |      -0.530879    |     0.0110194  |         -0.209134   |       0.173064   |           -0.417944  |       0.00475773  |
| poincare_sd2                    | OUTCOME        |       -0.166337   |    0.459406    |      -0.142575    |     0.52677    |          0.0712873  |       0.645632   |           -0.124656  |       0.420115    |
| poincare_sd2                    | Adrenalin      |       -0.207228   |    0.354786    |      -0.343874    |     0.117117   |         -0.158667   |       0.303613   |           -0.25841   |       0.0903307   |
| poincare_sd2                    | Noradrenalin   |       -0.351779   |    0.108389    |      -0.335968    |     0.126344   |          0.0118577  |       0.939106   |           -0.349249  |       0.0201435   |
| systolic_duration               | ANSD           |       -0.353919   |    0.106109    |      -0.530879    |     0.0110194  |         -0.0643489  |       0.678153   |           -0.385794  |       0.00969895  |
| systolic_duration               | OUTCOME        |        0.213862   |    0.33924     |      -0.403961    |     0.0622492  |         -0.356436   |       0.017556   |           -0.053424  |       0.730531    |
| systolic_duration               | Adrenalin      |       -0.381141   |    0.0800988   |      -0.373235    |     0.0870993  |         -0.0852626  |       0.582121   |           -0.374639  |       0.012227    |
| systolic_duration               | Noradrenalin   |       -0.470356   |    0.0271683   |      -0.270469    |     0.223449   |          0.249012   |       0.103102   |           -0.347274  |       0.0209081   |
| diastolic_duration              | ANSD           |       -0.482617   |    0.0229102   |      -0.643489    |     0.00123357 |         -0.0160872  |       0.917451   |           -0.52243   |       0.0002751   |
| diastolic_duration              | OUTCOME        |        0.0475248  |    0.833654    |      -0.118812    |     0.598457   |         -0.166337   |       0.28053    |           -0.035616  |       0.818464    |
| diastolic_duration              | Adrenalin      |       -0.230943   |    0.301112    |      -0.383399    |     0.0781784  |         -0.0954263  |       0.537781   |           -0.298752  |       0.0488509   |
| diastolic_duration              | Noradrenalin   |       -0.677019   |    0.000538964 |      -0.570864    |     0.00552541 |          0.172219   |       0.263626   |           -0.620354  |       7.06723e-06 |
| systolic_slope                  | ANSD           |       -0.209134   |    0.350276    |      -0.0160872   |     0.943354   |          0.144785   |       0.348398   |           -0.132617  |       0.390807    |
| systolic_slope                  | OUTCOME        |        0.0237624  |    0.916404    |       0.118812    |     0.598457   |          0.0475248  |       0.759344   |            0.041552  |       0.788849    |
| systolic_slope                  | Adrenalin      |        0.0344438  |    0.879053    |       0.147374    |     0.512799   |          0.160926   |       0.296692   |            0.119049  |       0.441482    |
| systolic_slope                  | Noradrenalin   |        0.123659   |    0.583509    |      -0.418408    |     0.0526322  |         -0.244495   |       0.109713   |           -0.123281  |       0.4253      |
| diastolic_slope                 | ANSD           |        0.112611   |    0.617814    |      -0.337832    |     0.124123   |          0.241309   |       0.114566   |           -0.0964486 |       0.533413    |
| diastolic_slope                 | OUTCOME        |        0.0712873  |    0.752571    |      -0.118812    |     0.598457   |          0.0475248  |       0.759344   |           -0.035616  |       0.818464    |
| diastolic_slope                 | Adrenalin      |       -0.20271    |    0.365603    |      -0.167702    |     0.455677   |          0.101073   |       0.513875   |           -0.199732  |       0.193644    |
| diastolic_slope                 | Noradrenalin   |       -0.20271    |    0.365603    |      -0.000564653 |     0.99801    |         -0.166573   |       0.279839   |           -0.0981734 |       0.526084    |
| nn50                            | ANSD           |       -0.386094   |    0.0759328   |      -0.273483    |     0.218129   |         -0.0643489  |       0.678153   |           -0.301402  |       0.0467873   |
| nn50                            | OUTCOME        |       -0.142575   |    0.52677     |      -0.403961    |     0.0622492  |         -0.380199   |       0.0109044  |           -0.26712   |       0.0796241   |
| nn50                            | Adrenalin      |       -0.325805   |    0.138959    |      -0.299831    |     0.175203   |         -0.239977   |       0.116641   |           -0.309754  |       0.0407413   |
| nn50                            | Noradrenalin   |       -0.637493   |    0.00141607  |      -0.120271    |     0.593941   |          0.238848   |       0.118424   |           -0.355173  |       0.0179892   |
| pnn50                           | ANSD           |       -0.46653    |    0.0286186   |      -0.370006    |     0.0900861  |         -0.144785   |       0.348398   |           -0.438037  |       0.002941    |
| pnn50                           | OUTCOME        |       -0.0950497  |    0.673935    |      -0.308911    |     0.161862   |         -0.332674   |       0.0273525  |           -0.172144  |       0.263837    |
| pnn50                           | Adrenalin      |       -0.337098   |    0.124995    |      -0.36533     |     0.0945453  |         -0.120271   |       0.436775   |           -0.334579  |       0.0264277   |
| pnn50                           | Noradrenalin   |       -0.726708   |    0.000127893 |      -0.116883    |     0.604451   |          0.25127    |       0.0999135  |           -0.483532  |       0.000884062 |
| hrv_triangular_index            | ANSD           |       -0.209134   |    0.350276    |      -0.337832    |     0.124123   |         -0.241309   |       0.114566   |           -0.30542   |       0.0437932   |
| hrv_triangular_index            | OUTCOME        |       -0.0237624  |    0.916404    |       0.142575    |     0.52677    |          0.190099   |       0.216465   |            0.053424  |       0.730531    |
| hrv_triangular_index            | Adrenalin      |        0.0852626  |    0.70598     |       0.133823    |     0.552696   |          0.131564   |       0.394612   |            0.123845  |       0.423168    |
| hrv_triangular_index            | Noradrenalin   |       -0.0920384  |    0.683739    |      -0.526821    |     0.011766   |         -0.451158   |       0.00211436 |           -0.350377  |       0.0197172   |
| lf_power                        | ANSD           |       -0.482617   |    0.0229102   |      -0.546966    |     0.00843066 |         -0.17696    |       0.250506   |           -0.466168  |       0.00142617  |
| lf_power                        | OUTCOME        |       -0.0950497  |    0.673935    |       0.0237624   |     0.916404   |          0.166337   |       0.28053    |           -0.065296  |       0.673678    |
| lf_power                        | Adrenalin      |       -0.281762   |    0.203955    |      -0.359684    |     0.100145   |         -0.104461   |       0.499793   |           -0.297059  |       0.0502071   |
| lf_power                        | Noradrenalin   |       -0.525692   |    0.0119809   |      -0.36646     |     0.0934538  |         -0.0175042  |       0.910208   |           -0.392411  |       0.00842275  |
| hf_power                        | ANSD           |       -0.434355   |    0.0433913   |      -0.514792    |     0.0142255  |         -0.112611   |       0.466742   |           -0.442056  |       0.00266191  |
| hf_power                        | OUTCOME        |       -0.118812   |    0.598457    |       0.0475248   |     0.833654   |          0.190099   |       0.216465   |           -0.05936   |       0.701904    |
| hf_power                        | Adrenalin      |       -0.303219   |    0.17014     |      -0.261434    |     0.2399     |         -0.012987   |       0.933319   |           -0.262924  |       0.0846507   |
| hf_power                        | Noradrenalin   |       -0.551666   |    0.00777712  |      -0.418408    |     0.0526322  |          0.0626765  |       0.686082   |           -0.431906  |       0.00341637  |
| signal_skewness                 | ANSD           |        0.530879   |    0.0110194   |       0.353919    |     0.106109   |          0.0160872  |       0.917451   |            0.442056  |       0.00266191  |
| signal_skewness                 | OUTCOME        |       -0.0475248  |    0.833654    |      -0.118812    |     0.598457   |          0.0237624  |       0.878315   |           -0.083104  |       0.591745    |
| signal_skewness                 | Adrenalin      |        0.307736   |    0.163548    |      -0.28515     |     0.198337   |         -0.384529   |       0.00996111 |            0.0166443 |       0.914603    |
| signal_skewness                 | Noradrenalin   |        0.351779   |    0.108389    |       0.565217    |     0.0061226  |         -0.261434   |       0.0864939  |            0.468863  |       0.00132632  |
| peak_trend_slope                | ANSD           |       -0.498704   |    0.0181521   |      -0.595228    |     0.00347365 |          0.0160872  |       0.917451   |           -0.514392  |       0.000354212 |
| peak_trend_slope                | OUTCOME        |        0.142575   |    0.52677     |      -0.285149    |     0.198338   |         -0.332674   |       0.0273525  |           -0.035616  |       0.818464    |
| peak_trend_slope                | Adrenalin      |       -0.295313   |    0.182113    |      -0.44777     |     0.0366426  |         -0.00282326 |       0.985489   |           -0.375767  |       0.011948    |
| peak_trend_slope                | Noradrenalin   |       -0.617165   |    0.0022148   |      -0.435347    |     0.0428613  |          0.303219   |       0.0454138  |           -0.50864   |       0.000422842 |
| systolic_area                   | ANSD           |       -0.450443   |    0.0354022   |      -0.370006    |     0.0900861  |          0.160872   |       0.296856   |           -0.446075  |       0.0024064   |
| systolic_area                   | OUTCOME        |       -0.0237624  |    0.916404    |      -0.0712873   |     0.752571   |         -0.0237624  |       0.878315   |           -0.023744  |       0.878408    |
| systolic_area                   | Adrenalin      |       -0.281762   |    0.203955    |      -0.453416    |     0.0340615  |         -0.136081   |       0.378436   |           -0.322731  |       0.0326252   |
| systolic_area                   | Noradrenalin   |       -0.579898   |    0.004671    |      -0.369848    |     0.090235   |          0.303219   |       0.0454138  |           -0.486353  |       0.00081602  |
| diastolic_area                  | ANSD           |       -0.46653    |    0.0286186   |      -0.627402    |     0.00177492 |         -0.17696    |       0.250506   |           -0.526448  |       0.000241865 |
| diastolic_area                  | OUTCOME        |        0.237624   |    0.286946    |      -0.190099    |     0.396792   |         -0.380199   |       0.0109044  |            0.047488  |       0.759525    |
| diastolic_area                  | Adrenalin      |       -0.314512   |    0.153997    |      -0.427442    |     0.0472279  |         -0.00282326 |       0.985489   |           -0.373228  |       0.0125835   |
| diastolic_area                  | Noradrenalin   |       -0.630717   |    0.0016494   |      -0.436477    |     0.0422641  |          0.131564   |       0.394612   |           -0.513718  |       0.000361706 |
| systolic_amplitude_variability  | ANSD           |        0.112611   |    0.617814    |      -0.0804362   |     0.721965   |         -0.144785   |       0.348398   |            0.0160748 |       0.917515    |
| systolic_amplitude_variability  | OUTCOME        |        0.118812   |    0.598457    |      -0.0712873   |     0.752571   |         -0.118812   |       0.442399   |            0.02968   |       0.84833     |
| systolic_amplitude_variability  | Adrenalin      |       -0.0818746  |    0.717189    |      -0.0491248   |     0.828133   |         -0.103331   |       0.504465   |           -0.0778616 |       0.615407    |
| systolic_amplitude_variability  | Noradrenalin   |       -0.00282326 |    0.990051    |       0.181254    |     0.419523   |          0.0852626  |       0.582121   |            0.0953523 |       0.538097    |
| diastolic_amplitude_variability | ANSD           |        0.0160872  |    0.943354    |      -0.241309    |     0.279316   |         -0.112611   |       0.466742   |           -0.0602804 |       0.6975      |
| diastolic_amplitude_variability | OUTCOME        |        0.0950497  |    0.673935    |      -0.237624    |     0.286946   |         -0.285149   |       0.0606315  |           -0.08904   |       0.56545     |
| diastolic_amplitude_variability | Adrenalin      |       -0.207228   |    0.354786    |      -0.281762    |     0.203955   |         -0.0513834  |       0.740459   |           -0.261514  |       0.0863949   |
| diastolic_amplitude_variability | Noradrenalin   |       -0.176736   |    0.431398    |       0.157538    |     0.483816   |          0.302089   |       0.0462637  |            0.023697  |       0.878647    |
| heart_rate                      | ANSD           |        0.305657   |    0.166558    |       0.450443    |     0.0354022  |        nan          |     nan          |            0.373738  |       0.0124536   |
| heart_rate                      | OUTCOME        |       -0.261387   |    0.239989    |       0.332674    |     0.130339   |        nan          |     nan          |           -0.005936  |       0.969495    |
| heart_rate                      | Adrenalin      |        0.339356   |    0.122328    |       0.313382    |     0.155561   |        nan          |     nan          |            0.29847   |       0.0490749   |
| heart_rate                      | Noradrenalin   |        0.5607     |    0.00663806  |       0.621683    |     0.00201053 |        nan          |     nan          |            0.589322  |       2.5668e-05  |

### Clinical Correlations Heatmap

![Clinical Correlations Heatmap](plots\general\clinical_correlations_heatmap.png)

## Time Series Trends

### Trend for SDNN

![Trend](plots\general\sdnn_trend.png)

### Trend for RMSSD

![Trend](plots\general\rmssd_trend.png)

### Trend for POINCARE_SD1

![Trend](plots\general\poincare_sd1_trend.png)

### Trend for POINCARE_SD2

![Trend](plots\general\poincare_sd2_trend.png)

### Trend for SYSTOLIC_DURATION

![Trend](plots\general\systolic_duration_trend.png)

### Trend for DIASTOLIC_DURATION

![Trend](plots\general\diastolic_duration_trend.png)

### Trend for SYSTOLIC_SLOPE

![Trend](plots\general\systolic_slope_trend.png)

### Trend for DIASTOLIC_SLOPE

![Trend](plots\general\diastolic_slope_trend.png)

### Trend for NN50

![Trend](plots\general\nn50_trend.png)

### Trend for PNN50

![Trend](plots\general\pnn50_trend.png)

### Trend for HRV_TRIANGULAR_INDEX

![Trend](plots\general\hrv_triangular_index_trend.png)

### Trend for LF_POWER

![Trend](plots\general\lf_power_trend.png)

### Trend for HF_POWER

![Trend](plots\general\hf_power_trend.png)

### Trend for SIGNAL_SKEWNESS

![Trend](plots\general\signal_skewness_trend.png)

### Trend for PEAK_TREND_SLOPE

![Trend](plots\general\peak_trend_slope_trend.png)

### Trend for SYSTOLIC_AREA

![Trend](plots\general\systolic_area_trend.png)

### Trend for DIASTOLIC_AREA

![Trend](plots\general\diastolic_area_trend.png)

### Trend for SYSTOLIC_AMPLITUDE_VARIABILITY

![Trend](plots\general\systolic_amplitude_variability_trend.png)

### Trend for DIASTOLIC_AMPLITUDE_VARIABILITY

![Trend](plots\general\diastolic_amplitude_variability_trend.png)

