from PublicReference.base import *

真·死灵术士等级 = 100 + 5

class 真·死灵术士主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '手杖':
            if self.所在等级==50 or self.所在等级==85 or self.所在等级==100:
                return round(self.CD / self.恢复 * 1.1, 1)
            else:
                return round(self.CD / self.恢复 * 1.0, 1)        
        elif 武器类型 == '匕首':
            return round(self.CD / self.恢复 * 0.95, 1)

                
class 真·死灵术士技能0(真·死灵术士主动技能):
    名称 = '暗魂波'
    所在等级 = 5
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔), 等级精通) 
    数据1 = [0, 136, 149, 164, 176, 192, 206, 220, 233, 248, 261, 276, 285, 301, 316, 328, 345, 354, 371, 387, 397, 412,429, 437, 453, 468, 480, 496, 509, 520, 537, 550, 565, 580, 592, 605, 620, 636, 646, 663, 676, 687, 703, 718,730, 746, 755, 770, 788, 800, 812, 828, 840, 854, 869, 881, 896, 911, 923, 937, 951, 964, 979, 994, 1008,1020, 1035, 1047, 1062, 1078, 1089]
    攻击次数1 = 3
    攻击倍率1 = 1.35
    数据2 = [0, 566, 626, 679, 742, 797, 857, 910, 970, 1029, 1087, 1140, 1206, 1254, 1315, 1375, 1428, 1494, 1547, 1598,1664, 1718, 1773, 1837, 1893, 1947, 2006, 2062, 2124, 2182, 2236, 2292, 2351, 2407, 2467, 2526, 2581, 2637,2700, 2751, 2812, 2874, 2926, 2980, 3046, 3096, 3160, 3217, 3270, 3334, 3389, 3439, 3504, 3565, 3618, 3676,3731, 3791, 3848, 3904, 3962, 4020, 4077, 4132, 4191, 4250, 4309, 4368, 4421, 4477, 4544]
    攻击次数2 = 1
    攻击倍率2 = 1.35
    CD = 3.5
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.攻击倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真·死灵术士技能1(真·死灵术士主动技能):
    名称 = '诅咒之剑'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 380, 418, 456, 495, 534, 572, 611, 649, 687, 727, 766, 804, 843, 881, 919, 958, 997, 1035, 1074, 1112,1151, 1189, 1229, 1267, 1306, 1344, 1383, 1421, 1459, 1498, 1537, 1575, 1614, 1652, 1690, 1730, 1769, 1807,1846, 1884, 1922, 1961, 2000, 2038, 2077, 2115, 2154, 2192, 2231, 2270, 2309, 2347, 2386, 2424, 2462, 2501,2540, 2578, 2617, 2655, 2693, 2733, 2772, 2810, 2849, 2887, 2925, 2964, 3003, 3041]
    攻击次数 = 5
    CD = 10
    TP成长 = 0.24
    TP上限 = 5
    攻击倍率 = 1.116

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率


class 真·死灵术士技能2(真·死灵术士主动技能):
    名称 = '降临：尼古拉斯（蜘蛛团）'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 105, 114, 126, 135, 147, 158, 169, 179, 191, 200, 213, 222, 234, 243, 255, 263, 274, 285, 297, 306, 318,327, 340, 349, 361, 371, 382, 393, 405, 414, 425, 435, 447, 457, 468, 479, 489, 501, 511, 522, 533, 543, 555,565, 575, 586, 596, 607, 618, 629, 640, 650, 661, 672, 683, 694, 704, 715, 726, 736, 748, 757, 769, 779, 791, 800, 812, 822, 834, 844]
    攻击次数1 = 3
    攻击倍率 = [0,2.196825,2.38730,2.59047,2.793650,2.996587]
    CD = 1
    TP成长 = 0
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        if self.TP等级 == 0:
            return self.数据1[self.等级] * self.攻击次数1 * self.倍率
        else:
            if self.TP等级 <= 5:
                return self.数据1[self.等级] * self.攻击次数1 * self.倍率 * self.攻击倍率[self.TP等级]


class 真·死灵术士技能3(真·死灵术士主动技能):
    名称 = '降临：尼古拉斯（艾克洛索）'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    数据1 = [0, 208, 229, 251, 272, 294, 316, 337, 359, 379, 400, 423, 444, 466, 487, 508, 528, 549, 572, 593, 614, 636,657, 678, 700, 721, 743, 764, 786, 808, 829, 851, 872, 894, 916, 937, 959, 980, 1001, 1023, 1044, 1065, 1087,1109, 1131, 1151, 1172, 1194, 1215, 1238, 1259, 1280, 1299, 1321, 1343, 1365, 1386, 1407, 1429, 1451, 1473,1494, 1515, 1537, 1559, 1581, 1602, 1622, 1644, 1666, 1687]
    攻击次数1 = 1
    数据2 = [0, 623, 687, 753, 814, 880, 943, 1008, 1073, 1136, 1201, 1266, 1331, 1396, 1459, 1524, 1586, 1652, 1715,1780, 1844, 1909, 1974, 2037, 2103, 2167, 2231, 2295, 2358, 2423, 2487, 2553, 2617, 2681, 2746, 2809, 2874,2939, 3003, 3067, 3132, 3197, 3261, 3325, 3390, 3454, 3518, 3582, 3647, 3711, 3777, 3841, 3904, 3969, 4033,4097, 4161, 4225, 4290, 4355, 4420, 4484, 4548, 4612, 4676, 4740, 4805, 4868, 4933, 4998, 5063]
    攻击次数2 = 1
    攻击倍率 = [0,1.101083,1.1985559,1.2996389,1.400722,1.501805]
    CD = 1
    TP成长 = 0
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        if self.TP等级 == 0:
            return self.数据1[self.等级] * self.攻击次数1* self.倍率
        else:
            if self.TP等级 <= 5:
                return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率 * self.攻击倍率[self.TP等级]

class 真·死灵术士技能4(真·死灵术士主动技能):
    名称 = '驱使僵尸（自爆）'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 403, 443, 483, 524, 565, 606, 646, 688, 728, 770, 809, 850, 891, 933, 974, 1014, 1054, 1095, 1137, 1177,1218, 1259, 1300, 1340, 1381, 1422, 1461, 1503, 1542, 1585, 1625, 1666, 1707, 1747, 1789, 1829, 1871, 1912,1953, 1992, 2033, 2075, 2116, 2156, 2198, 2236, 2278, 2319, 2359, 2400, 2440, 2480, 2523, 2564, 2606, 2645,2686, 2728, 2769, 2808, 2848, 2890, 2931, 2972, 3013, 3052, 3092, 3133, 3174, 3215]
    攻击次数 = 5
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    攻击倍率 = 1.322

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率
    
class 真·死灵术士技能5(真·死灵术士主动技能):
    名称 = '服从（远程）'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['降临：尼古拉斯（蜘蛛团）', '降临：尼古拉斯（艾克洛索）']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.04 * self.等级, 5)

class 真·死灵术士技能6(被动技能):
    名称 = '黑暗之环'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['无']

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '暗属性强化+' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (48 + self.等级 * 3)

class 真·死灵术士技能7(真·死灵术士主动技能):
    名称 = '暗影蜘蛛阵'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 285, 314, 342, 370, 400, 429, 457, 486, 514, 544, 573, 601, 630, 659, 688, 717, 745, 775, 803, 832, 861,890, 918, 948, 977, 1004, 1033, 1062, 1091, 1119, 1148, 1178, 1207, 1235, 1265, 1292, 1322, 1351, 1379, 1408,1436, 1466, 1495, 1524, 1553, 1582, 1609, 1639, 1668, 1696, 1726, 1753, 1784, 1812, 1840, 1869, 1898, 1927,1956, 1985, 2014, 2042, 2071, 2100, 2130, 2158, 2186, 2216, 2244, 2273]
    攻击次数 = 19
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    攻击倍率 = 1.187

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 真·死灵术士技能8(真·死灵术士主动技能):
    名称 = '死亡之爪'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 2565, 2825, 3086, 3346, 3606, 3866, 4127, 4387, 4647, 4907, 5168, 5428, 5688, 5949, 6209, 6469, 6729,6990, 7250, 7510, 7770, 8031, 8291, 8551, 8811, 9072, 9332, 9592, 9853, 10113, 10373, 10633, 10894, 11154,11414, 11674, 11935, 12195, 12455, 12716, 12976, 13236, 13496, 13757, 14017, 14277, 14537, 14798, 15058,15318, 15578, 15839, 16099, 16359, 16620, 16880, 17140, 17400, 17661, 17921, 18181, 18441, 18702, 18962,19222, 19483, 19743, 20003, 20263, 20524]
    攻击次数 = 1
    CD = 7
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 

class 真·死灵术士技能9(真·死灵术士主动技能):
    名称 = '死灵之怨'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 267, 294, 320, 348, 375, 402, 429, 456, 483, 510, 538, 565, 591, 618, 646, 673, 700, 727, 754, 781, 809,836, 862, 889, 917, 944, 971, 998, 1025, 1052, 1079, 1107, 1133, 1160, 1188, 1215, 1242, 1269, 1296, 1323,1350, 1378, 1405, 1431, 1458, 1486, 1513, 1540, 1567, 1594, 1621, 1649, 1676, 1702, 1729, 1757, 1784, 1811,1838, 1865, 1892, 1919, 1947, 1973, 2000, 2028, 2055, 2082, 2108, 2136]
    攻击次数 = 13
    CD = 10
    TP成长 = 0.10
    TP上限 = 5
    攻击倍率 = 1.185

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 真·死灵术士技能10(真·死灵术士主动技能):
    名称 = '百鬼夜行'
    备注 = '(自爆)'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 262, 288, 314, 342, 368, 394, 422, 448, 474, 502, 526, 552, 578, 606, 632, 658, 686, 712, 738, 766, 792,818, 846, 872, 898, 926, 952, 978, 1006, 1030, 1056, 1082, 1110, 1136, 1162, 1190, 1216, 1242, 1270, 1296,1322, 1350, 1376, 1402, 1430, 1456, 1482, 1506, 1534, 1560, 1588, 1614, 1640, 1668, 1694, 1720, 1748, 1774,1800, 1828, 1854, 1880, 1908, 1934, 1960, 1984, 2012, 2038, 2064, 2092]
    攻击次数 = 14
    攻击倍率 = 1.26 #1.2 * 1.05
    CD = 10
    TP成长 = 0
    TP上限 = 5
 
    def 等效百分比(self, 武器类型):
        if self.TP等级 == 0:
            return self.数据[self.等级] * self.攻击次数 * self.攻击倍率 * self.倍率
        else:
            if self.TP等级 <= 3:
                return self.数据[self.等级] * (self.攻击次数 + (self.TP等级 + 1)) * self.攻击倍率 * self.倍率
            else:
                if self.TP等级 <= 5:
                    return self.数据[self.等级] * (self.攻击次数 + (self.TP等级 + 2)) * self.攻击倍率 * self.倍率

class 真·死灵术士技能11(被动技能):
    名称 = '黑魔法书：亡者之魂'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 1
    关联技能 = ['暗魂波','诅咒之剑','驱使僵尸（自爆）','暗影蜘蛛阵','死亡之爪','死灵之怨', '百鬼夜行', '降临：暴君巴拉克（3下平x+黑手）', '降临：暴君巴拉克（暗击拳爆炸）', '降临：暴君巴拉克（强击）', '降临：暴君巴拉克（杀戮乱舞）', '吸魂暗劲波', '巴拉克的野心', '降临：僵尸莱迪娅','巴拉克的愤怒', '千魂祭', '死灵之缚', '释魂暗劲波', '暗黑蜘蛛引', '暴君极刑斩', '亡者君临：巴拉克之戮', '亡者之茧', '原初恐惧·摩罗斯']
 
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.185 + 0.015 * self.等级, 5)

class 真·死灵术士技能12(真·死灵术士主动技能):
    名称 = '降临：暴君巴拉克（3下平x+黑手）'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 686, 706, 729, 751, 774, 799, 824, 849, 875, 903, 929, 959, 988, 1019, 1051, 1083, 1116, 1150, 1186, 1221,1260, 1299, 1339, 1381, 1424, 1468, 1508, 1553, 1593, 1636, 1679, 1716, 1764, 1805, 1848, 1890, 1933, 1975,2019, 2059, 2101, 2144, 2185, 2230, 2270, 2311, 2354, 2399, 2441, 2480, 2525, 2568, 2608, 2650, 2694, 2736,2776, 2821, 2864, 2905, 2948, 2990, 3033, 3074, 3116, 3159, 3200, 3245, 3288, 3330]#1
    攻击次数1 = 1
    数据2 = [0, 760, 783, 808, 833, 860, 886, 914, 940, 970, 1001, 1030, 1064, 1096, 1130, 1165, 1201, 1238, 1276, 1316,1356, 1400, 1443, 1488, 1533, 1580, 1629, 1676, 1726, 1771, 1816, 1865, 1910, 1960, 2008, 2053, 2099, 2146,2196, 2241, 2286, 2335, 2380, 2430, 2478, 2525, 2570, 2616, 2664, 2711, 2761, 2804, 2851, 2898, 2945, 2993,3040, 3088, 3134, 3181, 3226, 3274, 3321, 3369, 3415, 3463, 3510, 3558, 3605, 3651, 3696]#2
    攻击次数2 = 1
    数据3 = [0, 400, 411, 425, 439, 453, 466, 479, 495, 511, 526, 543, 558, 576, 594, 613, 633, 650, 670, 693, 714, 736,759, 781, 805, 830, 858, 880, 905, 931, 956, 979, 1006, 1030, 1055, 1078, 1103, 1130, 1153, 1176, 1204,1226, 1251, 1276, 1300, 1328, 1350, 1375, 1401, 1424, 1445, 1474, 1499, 1524, 1548, 1573, 1598, 1623, 1648,1671, 1696, 1721, 1746, 1771, 1795, 1820, 1845, 1870, 1890, 1915, 1940]
    攻击次数3 = 5
    数据4 = [0, 1752, 1807, 1864, 1919, 1981, 2040, 2104, 2169, 2234, 2304, 2376, 2451, 2528, 2603, 2683, 2768, 2852,2941, 3030, 3125, 3222, 3322, 3424, 3531, 3640, 3753, 3856, 3966, 4072, 4180, 4289, 4402, 4503, 4610, 4723,4829, 4936, 5047, 5155, 5263, 5371, 5479, 5589, 5698, 5800, 5909, 6019, 6132, 6230, 6345, 6454, 6559, 6670,6775, 6882, 6992, 7101, 7208, 7315, 7428, 7536, 7642, 7747, 7858, 7965, 8074, 8183, 8290, 8397, 8506]  # 3&4
    攻击次数4 = 1
    攻击倍率 = 0.625
    CD = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 真·死灵术士技能13(真·死灵术士主动技能):
    名称 = '降临：暴君巴拉克（暗击拳爆炸）'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 1593, 1643, 1693, 1745, 1798, 1855, 1913, 1970, 2033, 2095, 2160, 2225, 2295, 2365, 2440, 2515, 2593,2673, 2755, 2840, 2928, 3020, 3113, 3208, 3308, 3410, 3508, 3605, 3705, 3800, 3900, 3998, 4095, 4195, 4295,4393, 4490, 4590, 4685, 4785, 4885, 4980, 5080, 5175, 5278, 5378, 5473, 5573, 5670, 5768, 5865, 5965, 6065,6160, 6260, 6358, 6458, 6555, 6653, 6753, 6850, 6950, 7045, 7145, 7243, 7343, 7440, 7538, 7638, 7735]
    攻击次数 = 1
    #数据 = [0, 1271, 1309, 1350, 1391, 1433, 1478, 1523, 1571, 1620, 1669, 1721, 1774, 1830, 1886, 1946, 2006, 2066,2130, 2198, 2265, 2333, 2408, 2483, 2558, 2636, 2719, 2794, 2876, 2951, 3026, 3109, 3184, 3266, 3341, 3420,3503, 3578, 3660, 3735, 3810, 3889, 3968, 4050, 4125, 4208, 4283, 4361, 4444, 4519, 4601, 4673, 4751, 4830,4909, 4988, 5066, 5145, 5224, 5303, 5378, 5456, 5535, 5614, 5693, 5771, 5850, 5929, 6008, 6086, 6161]
    CD = 3.0
    TP成长 = 0.1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 

class 真·死灵术士技能14(真·死灵术士主动技能):
    名称 = '降临：暴君巴拉克（强击）'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 2936, 3026, 3119, 3216, 3314, 3419, 3526, 3633, 3748, 3861, 3980, 4101, 4230, 4361, 4496, 4636, 4780,4928, 5079, 5236, 5398, 5568, 5739, 5914, 6098, 6285, 6469, 6648, 6830, 7009, 7190, 7370, 7551, 7734, 7915,8099, 8276, 8460, 8639, 8821, 9003, 9183, 9364, 9545, 9730, 9914, 10091, 10275, 10454, 10636, 10815, 10996,11181, 11358, 11541, 11724, 11905, 12088, 12266, 12450, 12630, 12814, 12990, 13175, 13354, 13536, 13718,13899, 14079, 14263]
    攻击次数 = 1
    CD = 2.0
    TP成长 = 0.1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真·死灵术士技能15(真·死灵术士主动技能):
    名称 = '降临：暴君巴拉克（杀戮乱舞）'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 1344, 1384, 1426, 1471, 1516, 1564, 1614, 1663, 1715, 1766, 1820, 1876, 1935, 1996, 2056, 2121, 2188,2255, 2324, 2396, 2470, 2548, 2626, 2706, 2790, 2875, 2961, 3043, 3125, 3209, 3290, 3373, 3456, 3539, 3620,3706, 3786, 3870, 3954, 4036, 4118, 4203, 4284, 4370, 4453, 4536, 4619, 4703, 4784, 4869, 4950, 5031, 5116,5198, 5281, 5366, 5448, 5533, 5614, 5698, 5780, 5864, 5945, 6030, 6111, 6194, 6278, 6361, 6441, 6528]
    攻击次数1 = 3
    CD = 7.0
    TP成长 = 0.1
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率 

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 2
        elif x == 1:
            self.倍率 *= 2 + 0.08

class 真·死灵术士技能16(真·死灵术士主动技能):
    名称 = '吸魂暗劲波'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 1327, 1461, 1596, 1731, 1865, 2000, 2134, 2269, 2404, 2538, 2673, 2808, 2942, 3077, 3212, 3346, 3481,3615, 3750, 3885, 4019, 4154, 4289, 4423, 4558, 4693, 4827, 4962, 5096, 5231, 5366, 5500, 5635, 5770, 5904,6039, 6174, 6308, 6443, 6577, 6712, 6847, 6981, 7116, 7251, 7385, 7520, 7655, 7789, 7924, 8058, 8193, 8328,8462, 8597, 8732, 8866, 9001, 9136, 9270, 9405, 9539, 9674, 9809, 9943, 10078, 10213, 10347, 10482, 10617]
    攻击次数1 = 2
    数据2 = [0, 5977, 6583, 7190, 7796, 8403, 9009, 9615, 10222, 10828, 11435, 12041, 12647, 13254, 13860, 14467, 15073, 15679, 16286, 16892, 17499, 18105, 18712, 19318, 19924, 20531, 21137, 21744, 22350, 22956, 23563, 24169, 24776, 25382, 25988, 26595, 27201, 27808, 28414, 29020, 29627, 30233, 30840, 31446, 32053, 32659, 33265, 33872, 34478, 35085, 35691, 36297, 36904, 37510, 38117, 38723, 39329, 39936, 40542, 41149, 41755, 42361, 42968, 43574, 44181, 44787, 45394, 46000, 46606, 47213, 47819]
    攻击次数2 = 1
    CD = 35
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真·死灵术士技能17(真·死灵术士主动技能):
    名称 = '巴拉克的野心'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 2090, 2302, 2514, 2726, 2938, 3150, 3362, 3574, 3786, 3998, 4210, 4422, 4634, 4846, 5058, 5270, 5482, 5694,5906, 6118, 6330, 6542, 6754, 6966, 7178, 7390, 7602, 7814, 8026, 8238, 8450, 8662, 8874, 9087, 9299, 9511,9723, 9935, 10147, 10359, 10571, 10783, 10995, 11207, 11419, 11631, 11843, 12055, 12267, 12479, 12691, 12903,13115, 13327, 13539, 13751, 13963, 14175, 14387, 14599, 14811, 15023, 15235, 15447, 15659, 15871, 16084,16296, 16508, 16720]
    攻击次数1 = 1
    数据2 = [0, 7389, 8139, 8888, 9638, 10388, 11137, 11887, 12637, 13386, 14136, 14886, 15635, 16385, 17135, 17884, 18634, 19384, 20133, 20883, 21633, 22382, 23132, 23881, 24631, 25381, 26130, 26880, 27630, 28379, 29129, 29879, 30628, 31378, 32128, 32877, 33627, 34377, 35126, 35876, 36626, 37375, 38125, 38875, 39624, 40374, 41124, 41873, 42623, 43373, 44122, 44872, 45622, 46371, 47121, 47871, 48620, 49370, 50120, 50869, 51619,52369, 53118, 53868, 54617, 55367, 56117, 56866, 57616, 58366, 59115]
    攻击次数2 = 1
    CD = 25
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 1 * 1.18
            self.攻击次数2 = 1 * 1.18
            self.倍率 *= 1.09
            self.CD *= 0.94
        elif x == 1:
            self.攻击次数1 = 1 * 1.18
            self.攻击次数2 = 1 * 1.18
            self.倍率 *= 1.09 + 0.09
            self.CD *= 0.94

class 真·死灵术士技能18(被动技能):
    名称 = '巴拉克的盟约'
    所在等级 = 40
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.38 + 0.02 * self.等级, 5)


class 真·死灵术士技能19(真·死灵术士主动技能):
    名称 = '降临：僵尸莱迪娅'
    备注 = '(蓄力)'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 428, 471, 515, 557, 600, 644, 688, 732, 773, 818, 861, 904, 947, 992, 1034, 1077, 1121, 1164, 1208, 1250, 1294, 1337, 1381, 1424, 1468, 1511, 1554, 1598, 1641, 1684, 1728, 1771, 1814, 1857, 1901, 1945, 1989, 2030, 2076, 2118, 2162, 2204, 2249, 2290, 2334, 2379, 2423, 2466, 2507, 2552, 2594, 2639, 2682, 2724, 2768, 2812, 2856, 2898, 2942, 2985, 3029, 3071, 3115, 3159, 3202, 3245, 3288, 3333, 3375, 3419]
    攻击次数 = 30
    攻击倍率 = 1.3767 #=1.3 * 1.059
    CD = 45
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * self.攻击倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真·死灵术士技能20(真·死灵术士主动技能):
    名称 = '巴拉克的愤怒'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1=[0, 1786, 1966, 2148, 2329, 2511, 2692, 2873, 3054, 3235, 3417, 3598, 3780, 3960, 4142, 4323, 4504, 4686, 4866, 5048, 5229, 5411, 5592, 5772, 5954, 6135, 6317, 6498, 6679, 6860, 7042, 7223, 7404, 7586, 7766, 7948, 8129, 8311, 8492, 8672, 8854, 9035, 9217, 9398, 9579, 9760, 9941, 10123, 10304, 10485, 10666, 10848, 11029, 11211, 11392, 11572, 11754, 11935, 12117, 12298, 12479, 12660, 12841, 13023, 13204, 13385, 13566, 13748, 13929, 14110, 14291]#第一击
    攻击次数1 = 1
    数据2 = [0, 757, 834, 910, 987, 1064, 1141, 1218, 1294, 1371, 1448, 1525, 1602, 1679, 1755, 1832, 1909, 1986, 2063, 2139, 2216, 2293, 2370, 2447, 2524, 2600, 2677, 2754, 2831, 2908, 2984, 3061, 3138, 3215, 3292, 3369, 3445, 3522, 3599, 3676, 3753, 3830, 3906, 3983, 4060, 4137, 4214, 4290, 4367, 4444, 4521, 4598, 4675, 4751, 4828, 4905, 4982, 5059, 5135, 5212, 5289, 5366, 5443, 5520, 5596, 5673, 5750, 5827, 5904, 5980, 6057]#多段
    攻击次数2 = 4
    数据3 =[0, 11277, 12422, 13566, 14710, 15854, 16999, 18142, 19287, 20431, 21575, 22719, 23864, 25007, 26152, 27296, 28440, 29584, 30729, 31872, 33017, 34161, 35305, 36449, 37594, 38737, 39882, 41026, 42170, 43314, 44459, 45602, 46747, 47891, 49035, 50180, 51323, 52468, 53612, 54756, 55900, 57045, 58188, 59333, 60477, 61621, 62765, 63910, 65053, 66198, 67342, 68486, 69630, 70775, 71918, 73063, 74207, 75351, 76495, 77640, 78783, 79928, 81072, 82216, 83360, 84505, 85649, 86793, 87938, 89081, 90226]#第二击
    攻击次数3 = 1
    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 1 * 1.12
            self.攻击次数2 = 4 * 1.12
            self.攻击次数3 = 1 * 1.12
            self.倍率 *= 1.05
            self.CD *= 0.89
        elif x == 1:
            self.攻击次数1 = 1 * 1.12
            self.攻击次数2 = 4 * 1.12
            self.攻击次数3 = 1 * 1.12
            self.倍率 *= 1.05 + 0.08
            self.CD *= 0.89

class 真·死灵术士技能21(被动技能):
    名称 = '屠戮之惧'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

class 真·死灵术士技能22(真·死灵术士主动技能):
    名称 = '千魂祭'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 625, 770, 916, 1061, 1206, 1351, 1496, 1641, 1786, 1931, 2077, 2222, 2367, 2512, 2657, 2802, 2947, 3092,3238, 3383, 3528, 3673, 3818, 3963, 4108, 4253, 4399, 4544, 4689, 4834, 4979, 5124, 5269, 5414, 5560, 5705,5850, 5995, 6140, 6285]
    攻击次数1 = 9
    数据2 = [0, 1933, 2381, 2829, 3277, 3726, 4174, 4622, 5070, 5519, 5967, 6415, 6863, 7312, 7760, 8208, 8656, 9105,9553, 10001, 10449, 10898, 11346, 11794, 12242, 12691, 13139, 13587, 14035, 14484, 14932, 15380, 15828,16277, 16725, 17173, 17621, 18070, 18518, 18966, 19414]
    攻击次数2 = 13
    数据3 = [0, 12565, 15478, 18392, 21305, 24219, 27133, 30046, 32960, 35874, 38787, 41701, 44614, 47528, 50442, 53355,56269, 59183, 62096, 65010, 67923, 70837, 73751, 76664, 79578, 82492, 85405, 88319, 91232, 94146, 97060,99973, 102887, 105801, 108714, 111628, 114542, 117455, 120369, 123282, 126196]
    攻击次数3 = 1
    CD = 145
    攻击倍率 = 1.066

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 真·死灵术士技能23(真·死灵术士主动技能):
    名称 = '死灵之缚'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 658, 725, 792, 859, 926, 992, 1059, 1126, 1193, 1260, 1327, 1393, 1460, 1527, 1594, 1661, 1728, 1794, 1861,1928, 1995, 2062, 2128, 2195, 2262, 2329, 2396, 2463, 2529, 2596, 2663, 2730, 2797, 2864, 2930, 2997, 3064,3131, 3198, 3265, 3331, 3398, 3465, 3532, 3599, 3666, 3732, 3799, 3866, 3933, 4000, 4067, 4133, 4200, 4267,4334, 4401, 4468, 4534, 4601, 4668, 4735, 4802, 4869, 4935, 5002, 5069, 5136, 5203, 5269]
    攻击次数 = 20
    CD = 30
    攻击倍率 = 1.218
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率  * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 20 * (0.3 + 0.99)
        elif x == 1:
            self.攻击次数 = 20 * (0.3 + 0.99 + 0.1)

class 真·死灵术士技能24(真·死灵术士主动技能):
    名称 = '释魂暗劲波'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 1264, 1392, 1520, 1650, 1777, 1904, 2033, 2162, 2291, 2417, 2547, 2675, 2804, 2932, 3059, 3186, 3314,3444, 3572, 3700, 3829, 3958, 4084, 4213, 4343, 4471, 4598, 4727, 4853, 4982, 5112, 5239, 5367, 5496, 5625,5752, 5882, 6010, 6137, 6266, 6394, 6523, 6649, 6779, 6905, 7034, 7163, 7293, 7419, 7548, 7677, 7804, 7932,8062, 8190, 8319, 8446, 8572, 8702, 8831, 8959, 9086, 9215, 9343, 9472, 9600, 9729, 9856, 9986, 10113]
    攻击次数1 = 6
    数据2 = [0, 10969, 12081, 13194, 14306, 15419, 16530, 17645, 18757, 19871, 20982, 22097, 23208, 24322, 25435, 26547,27658, 28770, 29884, 30997, 32110, 33223, 34337, 35449, 36561, 37674, 38787, 39898, 41013, 42123, 43236,44350, 45462, 46576, 47689, 48802, 49915, 51027, 52139, 53252, 54366, 55478, 56591, 57701, 58816, 59928,61042, 62154, 63266, 64378, 65491, 66605, 67717, 68830, 69944, 71056, 72169, 73282, 74393, 75508, 76619,77732, 78844, 79958, 81069, 82184, 83296, 84410, 85522, 86637, 87746]
    攻击次数2= 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 6 * 1.27
            self.攻击次数2 = 1 * 1.27
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数1 = 6 * 1.27
            self.攻击次数2 = 1 * (1.27 + 0.06)
            self.CD *= 0.9

class 真·死灵术士技能25(真·死灵术士主动技能):
    名称 = '暗黑蜘蛛引'#一部分伤害分给尼古拉斯了，约2.32765倍
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 5435, 5986, 6537, 7089, 7640, 8192, 8743, 9294, 9846, 10397, 10949, 11500, 12051, 12603, 13154, 13706,14257, 14808, 15360, 15911, 16463, 17014, 17565, 18117, 18668, 19219, 19771, 20322, 20874, 21425, 21976,22528, 23079, 23631, 24182, 24733, 25285, 25836, 26388, 26939]
    攻击次数1 = 1
    数据2 = [0, 7246, 7982, 8717, 9452, 10187, 10922, 11658, 12393, 13128, 13863, 14598, 15333, 16069, 16804, 17539,18274, 19009, 19745, 20480, 21215, 21950, 22685, 23421, 24156, 24891, 25626, 26361, 27097, 27832, 28567,29302, 30037, 30772, 31508, 32243, 32978, 33713, 34448, 35184, 35919]
    攻击次数2 = 1
    数据3 = [0, 905, 997, 1089, 1181, 1273, 1365, 1457, 1549, 1641, 1732, 1824, 1916, 2008, 2100, 2192, 2284, 2376, 2468,2560, 2651, 2743, 2835, 2927, 3019, 3111, 3203, 3295, 3387, 3479, 3570, 3662, 3754, 3846, 3938, 4030, 4122,4214, 4306, 4398, 4489]
    攻击次数3 = 6
    CD = 20
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 = 0
            self.攻击次数3 = 6 * (1 + 3.53)
            self.CD *= 0.9

class 真·死灵术士技能26(被动技能):
    名称 = '亡魂之息'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['降临：尼古拉斯（蜘蛛团）', '降临：尼古拉斯（艾克洛索）', '驱使僵尸（自爆）', '暗影蜘蛛阵', '死亡之爪', '死灵之怨', '百鬼夜行', 
            '降临：暴君巴拉克（3下平x+黑手）', '降临：暴君巴拉克（暗击拳爆炸）', '降临：暴君巴拉克（强击）', '降临：暴君巴拉克（杀戮乱舞）', '吸魂暗劲波', '巴拉克的野心', '降临：僵尸莱迪娅',
            '巴拉克的愤怒', '千魂祭', '死灵之缚', '释魂暗劲波', '暗黑蜘蛛引', '暴君极刑斩', '亡者君临：巴拉克之戮', '亡者之茧', '原初恐惧·摩罗斯']
    关联技能2 = ['暗魂波', '诅咒之剑']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.31 + 0.02 * self.等级, 5)

class 真·死灵术士技能27(真·死灵术士主动技能):
    名称 = '暴君极刑斩'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 43448, 47856, 52264, 56671, 61079, 65487, 69895, 74303, 78710, 83118, 87526, 91934, 96342, 100750, 105157,109565, 113973, 118381, 122789, 127196, 131604, 136012, 140420, 144828, 149236, 153643, 158051, 162459,166867, 171275, 175682, 180090, 184498, 188906, 193314, 197722, 202129, 206537, 210945, 215353]
    攻击次数 = 1
    CD = 45
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.31

class 真·死灵术士技能28(真·死灵术士主动技能):
    名称 = '亡者君临：巴拉克之戮'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 18411, 22681, 26949, 31219, 35489, 39758, 44028, 48297, 52566, 56835, 61105, 65376, 69644, 73914, 78182,82452, 86722, 90990, 95261, 99530, 103799, 108069, 112338, 116607, 120876, 125147, 129416, 133685, 137955,142223, 146493, 150763, 155032, 159302, 163571, 167840, 172110, 176379, 180648, 184917]
    攻击次数1 = 1
    数据2 = [0, 2509, 3091, 3673, 4255, 4837, 5419, 6002, 6584, 7166, 7748, 8329, 8911, 9493, 10075, 10657, 11239, 11821,12403, 12985, 13567, 14149, 14731, 15313, 15895, 16477, 17060, 17642, 18224, 18805, 19387, 19969, 20550,21132, 21714, 22296, 22878, 23460, 24042, 24624, 25206]
    攻击次数2 = 11
    数据3 = [0, 46029, 56704, 67377, 78051, 88725, 99397, 110071, 120745, 131419, 142093, 152766, 163440, 174113, 184787,195461, 206134, 216808, 227482, 238156, 248829, 259503, 270176, 280850, 291524, 302198, 312872, 323544,334218, 344892, 355565, 366240, 376914, 387587, 398261, 408933, 419607, 430282, 440955, 451629, 462303]
    攻击次数3 = 1
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真·死灵术士技能29(被动技能):
    名称 = '阿刻戎之钥'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 真·死灵术士技能30(真·死灵术士主动技能):
    名称 = '亡者之茧'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    基础 = 4315.8
    成长 = 487.2
    攻击次数 = 5
    基础2 = 50347.6
    成长2 = 5684.4
    攻击次数2 = 1
    CD = 60.0

    #def 等效百分比(self, 武器类型):
        #return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真·死灵术士技能31(真·死灵术士主动技能):
    名称 = '原初恐惧·摩罗斯'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((真·死灵术士等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    基础 = 218068.35311
    成长 = 65832.64688
    攻击次数 = 1
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

真·死灵术士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('真·死灵术士技能列表.append(真·死灵术士技能' + str(i) + '())')
        i += 1
    except:
        i = -1

真·死灵术士技能序号 = dict()
for i in range(len(真·死灵术士技能列表)):
    真·死灵术士技能序号[真·死灵术士技能列表[i].名称] = i

真·死灵术士一觉序号 = 0
真·死灵术士二觉序号 = 0
真·死灵术士三觉序号 = 0
for i in 真·死灵术士技能列表:
    if i.所在等级 == 50:
        真·死灵术士一觉序号 = 真·死灵术士技能序号[i.名称]
    if i.所在等级 == 85:
        真·死灵术士二觉序号 = 真·死灵术士技能序号[i.名称]
    if i.所在等级 == 100:
        真·死灵术士三觉序号 = 真·死灵术士技能序号[i.名称]

真·死灵术士护石选项 = ['无']
for i in 真·死灵术士技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        真·死灵术士护石选项.append(i.名称)

真·死灵术士符文选项 = ['无']
for i in 真·死灵术士技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        真·死灵术士符文选项.append(i.名称)


class 真·死灵术士角色属性(角色属性):
    实际名称 = '真·死灵术士'
    角色 = '暗夜使者'
    职业 = '死灵术士'

    武器选项 = ['匕首', '手杖']

    伤害类型选择 = ['魔法百分比']

    伤害类型 = '魔法百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['智力']

    主BUFF = 2.14

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(真·死灵术士技能列表)
        self.技能序号 = deepcopy(真·死灵术士技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.暗属性强化 += self.技能栏[self.技能序号['黑暗之环']].属强加成()

        self.技能栏[3].等级 = self.技能栏[2].等级
        self.技能栏[3].TP等级 = self.技能栏[2].TP等级

class 真·死灵术士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 真·死灵术士角色属性()
        self.角色属性A = 真·死灵术士角色属性()
        self.角色属性B = 真·死灵术士角色属性()
        self.一觉序号 = 真·死灵术士一觉序号
        self.二觉序号 = 真·死灵术士二觉序号
        self.三觉序号 = 真·死灵术士三觉序号
        self.护石选项 = deepcopy(真·死灵术士护石选项)
        self.符文选项 = deepcopy(真·死灵术士符文选项)