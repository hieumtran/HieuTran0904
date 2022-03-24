from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

#Import and read the files
df = pd.read_csv(r'D:\ITAP\Summer Intern\Generate_Lat_Long\university_location_data_original.csv')

#Clean the unnecessary data in this file
z = []
m = df['College'].tolist()
for i in range(len(m)):
    if str(m[i]) == "nan":
        z.append(i)
df.drop(z, inplace=True)

lat = ['40.6849285', '38.8298118', '34.5278618', '38.91265', '37.2283843', '28.0587031', '32.8082159', '30.6187558', '39.5453407', '39.6820414', '38.7646231', '34.0544485', '34.0482035', '42.0266187', '38.9055726', '42.701848', '40.7761962', '40.2358911', '37.3530446', '29.5827351', '39.2556759', '40.7427996', '43.0406977', '36.53498', '31.1832649', '36.8049912', '43.6839617', '33.7756178', '44.1466439', '36.8858594', '44.3379097', '38.0335529', '38.5612918', '44.4731165', '41.9247559', '33.9627934', '33.9892914', '40.7277408', '40.007581', '39.6779504', '46.7288124', '39.0498687', '33.4711738', '34.1817955', '41.7073107', '41.6030995', '46.4116044', '37.789553', '38.4549178', 
'32.9857619', '32.8800604', '38.9869183', '35.3070929', '33.207488', '43.0949906', '33.4205807', '44.012598', '32.4205489', '39.3299013', '38.8341332', '40.7450708', '31.0527826', '35.0458509', '41.1194664', '31.8010955', '31.5667892', '37.5483122', '39.2877823', '38.9374948', '43.8144101', '39.8405491', '44.976168', '41.6929529', '35.106532', '35.0699148', '37.7255655', '40.573436', '39.1981614', '33.9955117', '38.8997145', '33.9799796', '33.5104954', '34.1057394', '35.9721829', '39.1754487', '21.2709554', '26.1859628', '30.0399053', '41.6050295', '42.5051879', '38.7914717', '40.1765166', '1.9783615', '35.9209678', '29.4716439', '34.1439951', '40.5008186', '32.7759894', 
'37.9953671', '37.3351874', '33.2140233', '38.9820658', '32.2318851', '37.8718992', '28.6024274', '41.6626963', '38.2122761', '34.6899339', '34.0223519', '40.1935599', '34.8057395', '43.0001253', '40.2049604', '26.0681177', '34.1620556', '33.7838235', '40.4427314', '36.122362', '43.5819086', '37.0627072', '33.7330326', '40.3040545', '39.7251537', '30.3292553', '40.4517646', '40.7678398', '36.0021884', '42.2506803', '33.791725', '33.753068', '38.9226843', '42.8627836', '37.6375208', '40.6787923', '41.9109667', '30.0279015', '38.8544225', '31.5889679', '33.8713557', '35.6464927', '36.0745588', '35.7846633', '40.8024835', '38.8870718', '41.5808528', '40.8059143', '37.1395334', '39.1660159', '32.8412178', '31.5470079', '36.970591', '39.3925121', '40.7692895', '33.377917', '34.068921', '37.3660652', '38.8962961', '33.9480053', '21.296939', '28.8166264', '35.1187498', '44.97399', '36.1085197', '41.2907061', '33.4323093', '30.6959406', '34.1462045', '40.2787626', '41.4639394', '35.6515968', '39.2165732', '40.9477325', '42.3265474', '31.483076', '40.7496973', '40.409654', '34.7827196', '41.3316093', '45.0812661', '35.1875036', '31.4382686', '39.6080683', '40.0920362', '33.3060092', '33.6075305', '35.8430861', '33.7120288', '32.5933574', '33.417748', '30.2773795', '41.150572', '40.0956316', '33.836824', '41.0081119', '42.3504997', '42.3656827', '33.6565009', '41.7218773', '40.326356', '41.8267718', '41.9214717', '42.3749673', '33.8624581', '37.6571459', '34.0667698', '34.2410366', '35.4083451', '44.4613633', '41.5043413', '42.8319541', '47.0073154', '33.7025855', '44.5638691', '32.7834441', '41.8411961', '37.5356691', '38.559479', '43.6140899', '37.270975', '33.2181719', '39.0808594', '38.8941309', '32.5026472', '41.9269546', '34.038649', '40.7403959', '40.7707237', '40.8713962', '40.695387', '33.8281347', '33.77509', '35.9733357', '34.0413848', '41.720017', '40.7375677', '41.522137', '37.7353214', '40.810769', '31.2983627', '37.3011274', '40.8980267', '39.4857867', '28.0219272', '37.3614051', '39.451256', '40.1326909', '38.9076089', '33.0804485', '34.1697568', '38.2322677', '33.8680064', '34.1511279', '37.789292', '42.9668968', '47.3130847', '32.4768502', '35.245152', '40.2943397', '21.320666', '40.8747332', '40.027988', '38.435092', '36.1905358', '43.1496558', '43.0120017', '40.5684406', '44.0088358', '40.8172349', '33.8316052', '34.3151336', '30.4132579', '38.4235252', '35.9340795', '39.5105334', '47.1167748', 
'40.4994115', '33.1595302', '36.5898671', '39.6799914', '34.0482035', '41.5498286', '46.8977528', '40.6730296', '42.3384764', '41.934233', '47.575258', '36.0507991', '44.5637806', '40.7110772', '33.1504224', '33.3779756', '39.191576', '36.6745007', '32.2320066', '35.5484627', '41.5353423', '41.5808528', '40.4237054', '40.2788009', '33.97677', '41.8763427', '40.0776546', '40.50382', '28.3362975', '41.4714594', '30.7129974', '29.4457849', '37.7241492', '37.3146947', '33.7579713', '37.3496418', '34.0165568', '44.1161419', '26.2169719', '37.3148783', '43.6469528', '34.945103', '29.4140246', '33.8742213', '35.59536', '39.9053418', '43.0391534', '33.4327519', '32.7474661', '36.1757592', '29.5731949', '29.4885633', '29.888411', '40.268439', '35.9544013', '36.343177', '31.7709368', '32.315745', '40.2203297', '41.63133', '42.4074843', '40.6660061', '33.5019893', '34.7251471', '35.3826091', '39.3061109', '38.5382322', '33.6404952', '36.9880503', '38.758081', '41.4318783', '39.6766174', '21.355188', '29.7199489', '29.7662579', '40.1019523', '34.1007589', '42.3867598', '41.62816', '42.2780436', '40.8201966', '36.0689296', '34.223874', '42.5121517', '34.0853753', '37.5751669', '32.7719191', '37.9582437', '36.7371496', '41.3148754', '28.5295554', '46.9184723', '40.0378952', '37.246308', '38.6487895', '42.2634903', '42.3310501', '42.327322', '42.2399046', '34.9816909', '39.1854572', '48.7952623', '34.2076585', '34.935098']
lon = ['-111.8722465', '-77.3095546', '-83.9866356', '-76.849793', '-80.4256107', '-82.4160479', '-83.7340792', '-96.3386712', '-119.8183597', '-75.5886239', '-104.7883984', '-117.8216832', '-117.847319', '-93.6486594', '-77.1301201', '-84.4843659', '-74.4343237', '-87.0115779', '-79.1791469', '-98.6210993', '-76.7131614', '-74.1792824', '-71.4555238', '-87.3570795', '-81.4889752', '-115.9973001', '-85.4874428', '-84.398479', '-72.6764968', '-76.3078991', '-69.7987062', '-78.5101712', '-121.4262459', '-73.2063292', '-87.6588405', '-84.0697649', '-84.6693164', '-74.0047943', '-105.2681357', '-75.7528054', '-117.0148024', '-76.5157574', '-82.0220152', '-117.3259159', '-71.6785546', '-93.6568421', '-117.0278594', '-122.167806', '-122.7239038', '-96.7522933', '-117.2362075', '-76.9447483', '-80.737358', '-97.1547802', '-75.2733688', '-111.936568', '-97.1130763', '-81.7887287', '-76.6227117', '-77.2388232', '-74.0270209', '-97.7760458', '-85.2975012', '-83.1902402', '-85.9594939', '-110.247951', '-77.4548745', '-77.8622759', '-77.0909969', '-111.785449', '-86.1730867', '-93.2707749', '-72.7704487', '-80.696106', '-78.9539764', '-122.4533298', '-105.0887413', '-75.5645153', '-85.9937642', '-77.0507932', '-84.0066349', '-112.1321242', '-117.7117481', '-79.997364', '-86.514821', '-157.8016128', '-80.165974', '-94.0777688', '-88.0827548', '-82.9751822', '-79.5172306', '-75.278955', '105.2371054', '-94.965902', '-98.705443', '-118.1181987', '-74.4473991', '-117.0712533', '-121.3195528', 
'-121.8810715', '-87.5391418', '-76.4839405', '-110.9501094', '-122.2585399', '-81.2000599', '-91.5548998', '-85.7585023', '-79.2005823', '-118.285117', '-92.5889708', '-86.9665343', '-85.2298079', '-85.4062846', '-80.3943067', '-119.043463', '-118.1140904', '-79.9429552', '-83.490358', '-84.7756364', '-76.4928349', '-116.3864666', '-108.163354', '-104.786609', '-87.6530263', '-79.8856212', '-73.9645291', '-78.9379535', '-83.624089', '-87.3671794', '-84.3852819', '-77.0194377', '-112.429762', '-77.4730666', '-74.232353', '-91.6521601', '-95.4776831', '-78.1222498', '-97.1726265', '-98.5215656', '-82.2975138', '-79.773152', '-78.6820946', '-77.859089', '-76.8269617', '-87.4735602', '-74.4987309', '-80.5511003', '-78.1583388', '-96.7845175', '-97.2709267', '-82.560716', '-76.6126392', '-45.227962', '-111.9760201', '-118.4451811', '-120.4224179', '-104.8061551', '-83.3773221', '-157.8171118', '-96.9784322', '-89.9374928', '-93.2277285', '-115.1431709', '-72.9615183', '-112.0391515', '-88.184236', '-118.1380151', '-111.7153739', '-87.0438893', '-78.7047179', '-81.5069939', '-74.1973109', '-122.8685265', '-83.5301943', '-73.9418612', '-104.7623827', '-86.568614', '-72.9226957', '-83.4446279', '-101.8482868', '-100.4602762', '-105.0188452', '-75.1659431', '-111.6785238', '-112.1594168', '-90.6748589', '-84.4042954', '-85.4951663', '-82.0510186', '-97.7485031', '-95.918158', '-74.222056', '-87.266029', '-76.4472749', '-71.1053991', '-71.2585395', '-117.7695803', '-71.1194292', '-74.131132', '-71.4025482', '-71.5376476', '-71.0695871', '-118.2544107', '-122.0574872', '-118.1684392', '-118.5276745', '-78.7394405', '-93.1559742', '-81.6083838', '-106.3249953', '-120.5362805', '-117.9505047', '-69.6626362', '-79.9370018', '-88.0729753', '-122.3350145', '-77.008945', '-116.5072495', '-76.7162468', '-96.6418315', '-108.5543371', '-104.8343351', '-84.9404306', '-91.4253502', '-117.100396', '-73.9832252', '-73.9892342', '-73.8963454', '-73.9878876', '-118.0249841', '-84.2973348', '-78.881712', '-118.1502645', '-72.215698', '-80.660375', '-90.574479', '-84.298672', '-74.144261', '-85.8364229', '-121.7650792', '-74.0306732', '-80.1630335', '-83.4650042', 
'-122.1277574', '-77.4179818', '-78.7801269', '-77.0722585', '-83.2319298', '-85.2074433', '-77.4935883', '-115.209373', '-118.2344419', '-122.398982', '-85.6667224', '-122.1798216', '-99.7340564', '-91.7235465', '-76.8844961', '-157.8697388', '-124.0789268', '-75.5706994', '-78.8697548', '-94.559179', '-93.2389794', '-83.7128817', '-80.0143294', '-123.0365018', '-73.5900738', '-118.1354535', '-118.4192444', '-91.1800023', '-82.4264145', '-82.0165918', '-84.7308768', '-88.5460218', '-74.4071571', '-117.3207192', '-121.8841746', '-77.3486971', '-117.845125', '-73.0729008', '-96.8024367', '-75.3227965', '-71.0893955', '-88.774069', '-122.6352126', '-95.9536715', '-123.2794443', '-74.004811', '-117.1826734', '-95.8283374', '-94.6755573', '-76.9375837', '-110.9219283', '-77.4064334', '-73.0815739', '-87.4735602', '-86.9211946', '-74.7379884', '-117.3798277', '-87.6251169', '-83.4578795', '-78.6376191', '-82.2572391', '-71.3006368', '-95.5472905', '-98.4959969', '-122.4799405', '-121.9271722', '-117.888884', '-121.9389875', '-118.4703948', '-93.29548', '-98.253595', '-89.5280438', '-70.2290826', '-106.9870161', '-98.4548113', '-84.2755766', '-79.7560519', '-75.3536225', '-76.1351158', '-86.1135613', '-97.3278753', '-85.5086374', '-97.9847891', '-97.412413', '-97.938351', '-74.777696', '-83.9294564', '-88.8644538', '-106.5046405', '-95.254231', '-74.7684128', '-85.0134723', '-71.1190232', '-74.3228022', '-86.8064433', '-86.639783', '-94.3736471', '-76.6164354', '-121.7617125', 
'-117.8442962', '-122.0582093', '-93.7383705', '-72.8035784', '-104.9618965', '-158.056065', '-95.3422334', '-95.3593594', '-88.2271615', '-117.7729742', '-72.5300515', '-71.0046292', '-83.7382241', '-96.7004763', '-79.8101975', '-77.8696036', '-92.4646469', '-118.0880287', '-77.5407146', '-117.188213', '-87.6746938', '-84.1638243', '-105.5665744', '-81.4252564', '-98.0039752', '-75.3433315', '-79.9737354', '-90.3107962', '-83.6655609', '-83.1861012', '-83.054443', '-97.0131156', '-101.9160329', '-119.7901185', '-122.4938545', '-118.3412543', '-80.995289']
longtitude = []
for i in lon:
    m = float(i) + 0.00219
    longtitude.append(m)
df['Latitude'] = lat
df['Longtitude'] = lon
df['Longtitude2'] = longtitude

df.to_csv(r'D:\ITAP\Summer Intern\Generate_Lat_Long\university_location_data_updated.csv', index=False)