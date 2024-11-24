# Generated by Django 4.2.2 on 2024-11-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country_code',
            field=models.CharField(blank=True, choices=[('1', '1, US'), ('7', '7, RU'), ('20', '20, EG'), ('27', '27, ZA'), ('30', '30, GR'), ('31', '31, NL'), ('32', '32, BE'), ('33', '33, FR'), ('34', '34, ES'), ('36', '36, HU'), ('39', '39, IT'), ('40', '40, RO'), ('41', '41, CH'), ('43', '43, AT'), ('44', '44, GB'), ('45', '45, DK'), ('46', '46, SE'), ('47', '47, NO'), ('48', '48, PL'), ('49', '49, DE'), ('51', '51, PE'), ('52', '52, MX'), ('53', '53, CU'), ('54', '54, AR'), ('55', '55, BR'), ('56', '56, CL'), ('57', '57, CO'), ('58', '58, VE'), ('60', '60, MY'), ('61', '61, AU'), ('62', '62, ID'), ('63', '63, PH'), ('64', '64, NZ'), ('65', '65, SG'), ('66', '66, TH'), ('81', '81, JP'), ('82', '82, KR'), ('84', '84, VN'), ('86', '86, CN'), ('90', '90, TR'), ('91', '91, IN'), ('92', '92, PK'), ('93', '93, AF'), ('94', '94, LK'), ('95', '95, MM'), ('98', '98, IR'), ('211', '211, SS'), ('212', '212, MA'), ('213', '213, DZ'), ('216', '216, TN'), ('218', '218, LY'), ('220', '220, GM'), ('221', '221, SN'), ('222', '222, MR'), ('223', '223, ML'), ('224', '224, GN'), ('225', '225, CI'), ('226', '226, BF'), ('227', '227, NE'), ('228', '228, TG'), ('229', '229, BJ'), ('230', '230, MU'), ('231', '231, LR'), ('232', '232, SL'), ('233', '233, GH'), ('234', '234, NG'), ('235', '235, TD'), ('236', '236, CF'), ('237', '237, CM'), ('238', '238, CV'), ('239', '239, ST'), ('240', '240, GQ'), ('241', '241, GA'), ('242', '242, CG'), ('243', '243, CD'), ('244', '244, AO'), ('245', '245, GW'), ('246', '246, IO'), ('247', '247, AC'), ('248', '248, SC'), ('249', '249, SD'), ('250', '250, RW'), ('251', '251, ET'), ('252', '252, SO'), ('253', '253, DJ'), ('254', '254, KE'), ('255', '255, TZ'), ('256', '256, UG'), ('257', '257, BI'), ('258', '258, MZ'), ('260', '260, ZM'), ('261', '261, MG'), ('262', '262, RE'), ('263', '263, ZW'), ('264', '264, NA'), ('265', '265, MW'), ('266', '266, LS'), ('267', '267, BW'), ('268', '268, SZ'), ('269', '269, KM'), ('290', '290, SH'), ('291', '291, ER'), ('297', '297, AW'), ('298', '298, FO'), ('299', '299, GL'), ('350', '350, GI'), ('351', '351, PT'), ('352', '352, LU'), ('353', '353, IE'), ('354', '354, IS'), ('355', '355, AL'), ('356', '356, MT'), ('357', '357, CY'), ('358', '358, FI'), ('359', '359, BG'), ('370', '370, LT'), ('371', '371, LV'), ('372', '372, EE'), ('373', '373, MD'), ('374', '374, AM'), ('375', '375, BY'), ('376', '376, AD'), ('377', '377, MC'), ('378', '378, SM'), ('380', '380, UA'), ('381', '381, RS'), ('382', '382, ME'), ('383', '383, XK'), ('385', '385, HR'), ('386', '386, SI'), ('387', '387, BA'), ('389', '389, MK'), ('420', '420, CZ'), ('421', '421, SK'), ('423', '423, LI'), ('500', '500, FK'), ('501', '501, BZ'), ('502', '502, GT'), ('503', '503, SV'), ('504', '504, HN'), ('505', '505, NI'), ('506', '506, CR'), ('507', '507, PA'), ('508', '508, PM'), ('509', '509, HT'), ('590', '590, GP'), ('591', '591, BO'), ('592', '592, GY'), ('593', '593, EC'), ('594', '594, GF'), ('595', '595, PY'), ('596', '596, MQ'), ('597', '597, SR'), ('598', '598, UY'), ('599', '599, CW'), ('670', '670, TL'), ('672', '672, NF'), ('673', '673, BN'), ('674', '674, NR'), ('675', '675, PG'), ('676', '676, TO'), ('677', '677, SB'), ('678', '678, VU'), ('679', '679, FJ'), ('680', '680, PW'), ('681', '681, WF'), ('682', '682, CK'), ('683', '683, NU'), ('685', '685, WS'), ('686', '686, KI'), ('687', '687, NC'), ('688', '688, TV'), ('689', '689, PF'), ('690', '690, TK'), ('691', '691, FM'), ('692', '692, MH'), ('800', '800, 001'), ('808', '808, 001'), ('850', '850, KP'), ('852', '852, HK'), ('853', '853, MO'), ('855', '855, KH'), ('856', '856, LA'), ('870', '870, 001'), ('878', '878, 001'), ('880', '880, BD'), ('881', '881, 001'), ('882', '882, 001'), ('883', '883, 001'), ('886', '886, TW'), ('888', '888, 001'), ('960', '960, MV'), ('961', '961, LB'), ('962', '962, JO'), ('963', '963, SY'), ('964', '964, IQ'), ('965', '965, KW'), ('966', '966, SA'), ('967', '967, YE'), ('968', '968, OM'), ('970', '970, PS'), ('971', '971, AE'), ('972', '972, IL'), ('973', '973, BH'), ('974', '974, QA'), ('975', '975, BT'), ('976', '976, MN'), ('977', '977, NP'), ('979', '979, 001'), ('992', '992, TJ'), ('993', '993, TM'), ('994', '994, AZ'), ('995', '995, GE'), ('996', '996, KG'), ('998', '998, UZ')], default='+98', max_length=3, null=True),
        ),
    ]
