#Fuel info - UBS Strategy
fuel={'consumption':2.6,'penalty':0.035,'laps':60,'lapdistance':5.148,'racedistance':309,'pitstoploss':17}

#Practice Data
fp1times=[['1', 'S. VETTEL', '1', '10:03:36', '2', '29:04.995', '3', '1:37.620', '4', '1:34.739', '5', '1:34.844', '6', '1:32.760', '7', '1:38.336', '8', '1:32.536', '9', '1:39.850', '10', '11:28.048', '11', '1:37.675', '12', '1:32.534', '13', '1:42.053', '14', '1:32.597', '15', '1:37.046', '16', '1:32.268', '17', '1:39.558', '18', '10:17.997', '19', '1:38.348', '20', '1:38.077', '21', '1:38.268', '22', '1:38.224', '23', '1:37.797', '24', '1:37.652', '25', '1:38.622', '26', '1:41.772', '27', '1:43.948'], ['2', 'M. WEBBER', '1', '10:08:39', '2', '24:15.521', '3', '1:35.663', '4', '1:34.022', '5', '1:40.107', '6', '1:33.741', '7', '1:33.008', '8', '1:42.879', '9', '14:00.030', '10', '1:38.060', '11', '1:38.791', '12', '1:32.599', '13', '1:32.217', '14', '1:35.364', '15', '1:42.702', '16', '12:55.325', '17', '1:38.542', '18', '1:37.806', '19', '1:37.799', '20', '1:37.490', '21', '1:40.886', '22', '1:37.566', '23', '1:38.045', '24', '1:52.591'], ['3', 'L. HAMILTON', '1', '10:06:52', '2', '18:19.578', '3', '1:34.982', '4', '1:33.576', '5', '1:37.906', '6', '1:32.996', '7', '1:41.359', '8', '23:18.631', '9', '1:33.462', '10', '1:40.059', '11', '1:33.009', '12', '1:41.394', '13', '19:41.434', '14', '1:38.567', '15', '1:33.799', '16', '1:39.984', '17', '1:34.332', '18', '1:59.447'], ['4', 'J. BUTTON', '1', '10:08:45', '2', '16:27.850', '3', '10:22.881', '4', '1:36.366', '5', '1:34.149', '6', '1:44.062', '7', '1:41.687', '8', '2:02.742', '9', '1:33.628', '10', '1:49.882', '11', '17:26.925', '12', '1:35.808', '13', '1:35.042', '14', '1:34.997', '15', '1:38.835', '16', '1:45.806', '17', '9:20.919', '18', '1:37.609', '19', '1:35.174', '20', '1:45.690', '21', '1:35.238', '22', '1:42.578'], ['5', 'F. ALONSO', '1', '10:04:45', '2', '1:59.975', '3', '13:09.710', '4', '1:57.488', '5', '11:49.872', '6', '1:37.524', '7', '1:35.560', '8', '1:38.705', '9', '1:34.099', '10', '1:37.271', '11', '1:33.586', '12', '2:03.620', '13', '8:26.648', '14', '1:41.405', '15', '1:32.574', '16', '1:43.287', '17', '1:32.037', '18', '1:38.681', '19', '1:31.981', '20', '1:50.469', '21', '2:34.616', '22', '10:09.172', '23', '1:35.595', '24', '1:36.279', '25', '1:37.793', '26', '1:42.778', '27', '1:45.636', '28', '1:49.210', '29', '1:31.894', '30', '2:03.352'], ['6', 'F. MASSA', '1', '10:03:47', '2', '2:04.749', '3', '5:04.863', '4', '1:59.540', '5', '23:32.061', '6', '1:36.947', '7', '1:36.089', '8', '1:42.106', '9', '1:35.309', '10', '1:34.782', '11', '1:37.496', '12', '1:34.742', '13', '2:00.829', '14', '6:59.980', '15', '1:33.262', '16', '1:42.154', '17', '1:32.798', '18', '1:32.681', '19', '1:44.694', '20', '1:54.745', '21', '2:45.287', '22', '21:42.199', '23', '2:02.016'], ['7', 'M. SCHUMACHER', '1', '10:05:04', '2', '10:30.276', '3', '10:14.359', '4', '1:36.457', '5', '1:36.203', '6', '1:45.562', '7', '1:35.054', '8', '1:44.600', '9', '2:44.258', '10', '1:35.657', '11', '1:35.407', '12', '1:47.794', '13', '1:35.028', '14', '1:48.932', '15', '10:09.920', '16', '1:34.336', '17', '1:41.485', '18', '1:34.097', '19', '1:55.219', '20', '2:34.374', '21', '1:33.937', '22', '1:33.863', '23', '1:44.540', '24', '1:57.195', '25', '1:40.319', '26', '10:14.499', '27', '1:36.914', '28', '1:36.501', '29', '1:36.428', '30', '1:39.462', '31', '1:45.032'], ['8', 'N. ROSBERG', '1', '10:04:03', '2', '3:08.723', '3', '13:51.715', '4', '1:38.170', '5', '1:35.751', '6', '1:35.112', '7', '1:35.046', '8', '1:53.762', '9', '2:31.850', '10', '1:35.670', '11', '1:34.724', '12', '1:42.397', '13', '1:34.005', '14', '1:51.232', '15', '15:02.727', '16', '1:38.218', '17', '1:33.831', '18', '1:42.795', '19', '1:34.530', '20', '1:55.339', '21', '2:21.918', '22', '1:41.135', '23', '1:33.934', '24', '1:41.014', '25', '1:33.787', '26', '1:50.959', '27', '8:40.579', '28', '1:40.678', '29', '1:35.829', '30', '1:37.018', '31', '1:36.810', '32', '1:38.082', '33', '1:41.005'], ['9', 'N. HEIDFELD', '1', '10:03:15', '2', '13:52.398', '3', '1:38.313', '4', '1:37.987', '5', '1:47.447', '6', '1:43.809', '7', '11:45.481', '8', '1:37.505', '9', '1:36.704', '10', '1:36.310', '11', '1:44.680', '12', '15:44.599', '13', '1:37.567', '14', '1:36.689', '15', '1:36.458', '16', '1:44.367', '17', '18:10.963', '18', '1:42.388', '19', '1:36.271', '20', '1:35.851', '21', '1:35.444', '22', '1:43.968'], ['10', 'V. PETROV', '1', '10:04:08', '2', '2:04.037', '3', '27:09.459', '4', '1:36.979', '5', '1:34.937', '6', '1:42.953', '7', '1:34.577', '8', '1:34.094', '9', '1:43.272', '10', '14:27.567', '11', '1:35.363', '12', '1:35.695', '13', '1:47.127', '14', '1:36.451', '15', '1:36.307', '16', '1:39.770', '17', '15:15.954', '18', '1:40.628', '19', '1:36.366', '20', '1:41.176', '21', '2:33.223', '22', '1:53.616'], ['11', 'R. BARRICHELLO', '1', '10:05:11', '2', '16:52.851', '3', '1:45.999', '4', '1:41.036', '5', '1:39.330', '6', '1:45.425', '7', '1:49.433', '8', '9:41.656', '9', '1:37.037', '10', '1:41.552', '11', '1:36.356', '12', '1:45.036', '13', '2:24.598', '14', '1:37.013', '15', '1:46.583', '16', '1:44.870', '17', '14:16.634', '18', '1:38.154', '19', '1:35.389', '20', '1:46.017', '21', '6:32.262', '22', '1:39.289', '23', '1:36.953', '24', '1:50.309'], ['12', 'P. MALDONADO', '1', '10:03:40', '2', '19:35.239', '3', '1:40.164', '4', '1:37.984', '5', '1:50.606', '6', '1:37.960', '7', '1:36.842', '8', '1:38.437', '9', '1:50.839', '10', '12:26.924', '11', '1:38.102', '12', '1:36.877', '13', '1:50.620', '14', '1:37.212', '15', '1:54.768', '16', '14:49.785', '17', '1:39.919', '18', '1:38.046', '19', '1:38.133', '20', '1:37.733', '21', '1:37.947', '22', '1:38.158', '23', '1:38.928', '24', '1:37.688', '25', '1:37.602', '26', '1:37.544', '27', '1:37.715', '28', '1:39.112', '29', '1:55.761'], ['14', 'A. SUTIL', '1', '10:05:15', '2', '26:14.319', '3', '1:40.774', '4', '1:37.496', '5', '1:36.818', '6', '1:35.840', '7', '1:35.350', '8', '1:49.110', '9', '11:59.668', '10', '1:36.531', '11', '1:35.554', '12', '1:39.366', '13', '1:35.849', '14', '1:39.259', '15', '1:46.269', '16', '12:13.533', '17', '1:34.096', '18', '1:33.832', '19', '1:42.221', '20', '1:34.579', '21', '1:34.591', '22', '1:35.133', '23', '1:37.879', '24', '1:35.486', '25', '1:34.907', '26', '1:36.389', '27', '1:52.734'], ['15', 'N. HULKENBERG', '1', '10:05:49', '2', '21:07.773', '3', '1:40.622', '4', '1:39.125', '5', '1:37.928', '6', '1:41.308', '7', '1:37.458', '8', '1:49.162', '9', '10:38.587', '10', '1:41.478', '11', '1:37.111', '12', '1:36.683', '13', '1:36.077', '14', '2:01.882', '15', '18:01.459', '16', '1:34.671', '17', '1:33.858', '18', '1:37.434', '19', '1:33.933', '20', '1:34.557', '21', '1:35.029', '22', '1:34.416', '23', '1:36.743', '24', '1:34.864', '25', '1:35.462', '26', '1:47.679'], ['16', 'K. KOBAYASHI', '1', '10:02:39', '2', '18:30.155', '3', '1:41.074', '4', '1:40.502', '5', '1:38.266', '6', '1:37.737', '7', '1:43.967', '8', '1:37.262', '9', '1:52.727', '10', '10:22.172', '11', '1:39.611', '12', '1:38.436', '13', '1:37.389', '14', '1:37.619', '15', '1:44.352', '16', '11:53.573', '17', '1:39.731', '18', '1:38.280', '19', '1:37.652', '20', '1:36.882', '21', '1:51.451', '22', '11:05.409', '23', '1:40.024', '24', '1:39.341', '25', '1:38.776', '26', '1:38.699', '27', '1:50.344'], ['17', 'S. PEREZ', '1', '10:02:23', '2', '16:17.694', '3', '1:40.730', '4', '1:40.415', '5', '1:38.448', '6', '1:46.222', '7', '1:37.786', '8', '1:58.310', '9', '10:25.389', '10', '1:40.506', '11', '1:38.828', '12', '1:38.094', '13', '1:49.424', '14', '13:15.902', '15', '1:37.311', '16', '1:36.842', '17', '1:40.785', '18', '1:41.377', '19', '1:36.371', '20', '1:45.494', '21', '15:08.523', '22', '2:03.999'], ['18', 'S. BUEMI', '1', '10:03:13', '2', '15:25.876', '3', '14:12.177', '4', '1:39.558', '5', '1:38.513', '6', '1:37.259', '7', '1:37.627', '8', '1:42.894', '9', '1:36.922', '10', '1:36.931', '11', '1:42.850', '12', '16:09.174', '13', '1:35.671', '14', '1:35.884', '15', '1:35.394', '16', '1:45.406', '17', '1:35.371', '18', '1:42.937', '19', '16:43.390'], ['19', 'J. ALGUERSUARI', '1', '10:02:20', '2', '18:17.657', '3', '1:40.333', '4', '1:38.945', '5', '1:37.391', '6', '1:41.263', '7', '1:36.926', '8', '1:36.791', '9', '1:43.036', '10', '14:12.049', '11', '1:36.504', '12', '1:36.588', '13', '1:35.830', '14', '1:35.534', '15', '1:35.260', '16', '1:35.229', '17', '1:50.782', '18', '16:15.985', '19', '10:53.235', '20', '1:35.394', '21', '1:38.878', '22', '1:35.115', '23', '1:49.572'], ['20', 'H. KOVALAINEN', '1', '10:01:58', '2', '12:54.907', '3', '17:50.509', '4', '1:39.746', '5', '1:37.456', '6', '1:36.490', '7', '1:43.987', '8', '1:38.028', '9', '1:36.392', '10', '1:45.385', '11', '8:45.081', '12', '1:38.550', '13', '1:38.651', '14', '1:38.824', '15', '1:44.673', '16', '1:39.622', '17', '1:37.527', '18', '1:45.293', '19', '11:43.304', '20', '1:39.146', '21', '1:38.790', '22', '1:38.145', '23', '1:46.313', '24', '1:38.170', '25', '1:39.642', '26', '1:42.590', '27', '1:38.548', '28', '1:49.370', '29', '1:48.838'], ['21', 'K. CHANDHOK', '1', '10:02:56', '2', '9:17.674', '3', '22:47.575', '4', '1:54.984', '5', '1:43.791', '6', '1:42.383', '7', '1:41.248', '8', '1:46.709', '9', '1:45.211', '10', '1:53.389', '11', '22:26.235', '12', '1:40.251', '13', '1:44.841', '14', '1:38.970', '15', '1:38.765', '16', '2:04.294', '17', '9:42.234', '18', '1:46.165', '19', '2:01.364'], ['22', 'D. RICCIARDO', '1', '10:03:11', '2', '17:49.200', '3', '1:47.768', '4', '1:44.593', '5', '1:42.153', '6', '1:41.444', '7', '1:41.635', '8', '1:40.817', '9', '1:41.247', '10', '1:45.633', '11', '15:58.946', '12', '1:41.860', '13', '1:40.790', '14', '1:40.316', '15', '1:40.299', '16', '1:48.259', '17', '1:40.595', '18', '1:41.984', '19', '1:40.575', '20', '1:48.191', '21', '21:00.266', '22', '1:41.133', '23', '1:39.279', '24', '2:00.412'], ['23', 'N. KARTHIKEYAN', '1', '10:03:10', '2', '21:09.431', '3', '10:01.211', '4', '14:31.626', '5', '1:45.211', '6', '1:42.350', '7', '1:41.389', '8', '1:40.760', '9', '1:40.407', '10', '1:42.173', '11', '1:41.226', '12', '1:40.118', '13', '1:47.898', '14', '14:09.269', '15', '1:39.689', '16', '1:38.518', '17', '1:38.981', '18', '1:52.217', '19', '1:38.504', '20', '1:44.803', '21', '1:39.004', '22', '1:54.645'], ['24', 'T. GLOCK', '1', '10:02:37', '2', '8:02.777', '3', '1:53.527', '4', '9:43.425', '5', '1:54.094', '6', '22:58.137', '7', '1:43.514', '8', '1:41.400', '9', '1:41.073', '10', '1:40.382', '11', '1:50.262', '12', '2:22.847', '13', '1:53.050', '14', '11:23.460', '15', '1:43.643', '16', '1:40.638', '17', '1:46.485', '18', '7:00.216', '19', '1:41.512', '20', '1:41.944', '21', '1:40.316', '22', '1:40.109', '23', '2:01.546'], ['25', "J. D'AMBROSIO", '1', '10:02:15', '2', '10:48.895', '3', '1:56.739', '4', '10:12.616', '5', '1:56.547', '6', '8:34.984', '7', '1:54.236', '8', '17:52.796', '9', '1:45.348', '10', '1:43.141', '11', '1:42.377', '12', '1:41.426', '13', '1:40.428', '14', '1:46.495', '15', '2:17.670', '16', '1:44.024', '17', '1:41.799', '18', '1:49.298', '19', '14:27.533', '20', '1:42.367', '21', '1:42.861', '22', '2:03.039']]

fp1classification=[['1', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari', '1:31.894', '201.675', '11:29:42', '30'], ['2', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:32.217', '0.323', '200.969', '11:02:56', '24'], ['3', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:32.268', '0.374', '0.051', '200.858', '11:04:54', '27'], ['4', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari', '1:32.681', '0.787', '0.413', '199.963', '11:03:08', '23'], ['5', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:32.996', '1.102', '0.315', '199.285', '10:31:31', '18'], ['6', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:33.628', '1.734', '0.632', '197.940', '10:45:48', '22'], ['7', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:33.787', '1.893', '0.159', '197.605', '11:12:30', '33'], ['8', '14', 'A. SUTIL', 'GER', 'Force India F1 Team', '1:33.832', '1.938', '0.045', '197.510', '11:18:39', '27'], ['9', '15', 'N. HULKENBERG', 'GER', 'Force India F1 Team', '1:33.858', '1.964', '0.026', '197.455', '11:17:24', '26'], ['10', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:33.863', '1.969', '0.005', '197.445', '11:07:51', '31'], ['11', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:34.094', '2.200', '0.231', '196.960', '10:41:25', '22'], ['12', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:35.115', '3.221', '1.021', '194.846', '11:29:49', '23'], ['13', '18', 'S. BUEMI', 'SUI', 'Scuderia Toro Rosso', '1:35.371', '3.477', '0.256', '194.323', '11:10:20', '20'], ['14', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:35.389', '3.495', '0.018', '194.286', '11:12:10', '24'], ['15', '9', 'N. HEIDFELD', 'GER', 'Lotus Renault GP', '1:35.444', '3.550', '0.055', '194.174', '11:29:17', '22'], ['16', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:36.371', '4.477', '0.927', '192.306', '11:07:43', '22'], ['17', '20', 'H. KOVALAINEN', 'FIN', 'Team Lotus', '1:36.392', '4.498', '0.021', '192.264', '10:42:35', '29'], ['18', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:36.842', '4.948', '0.450', '191.371', '10:31:39', '29'], ['19', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:36.882', '4.988', '0.040', '191.292', '11:10:07', '27'], ['20', '23', 'N. KARTHIKEYAN', 'IND', 'HRT F1 Team', '1:38.504', '6.610', '1.622', '188.142', '11:26:51', '22'], ['21', '21', 'K. CHANDHOK', 'IND', 'Team Lotus', '1:38.765', '6.871', '0.261', '187.645', '11:16:38', '19'], ['22', '22', 'D. RICCIARDO', 'AUS', 'HRT F1 Team', '1:39.279', '7.385', '0.514', '186.673', '11:30:28', '24'], ['23', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:40.109', '8.215', '0.830', '185.126', '11:30:20', '23'], ['24', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:40.428', '8.534', '0.319', '184.538', '11:04:04', '22']]



fp2times=[['1', 'S. VETTEL', '1', '14:06:47', '2', '1:34.977', '3', '1:37.912', '4', '1:41.005', '5', '1:33.951', '6', '1:33.823', '7', '1:44.431', '8', '15:48.042', '9', '1:38.459', '10', '1:34.097', '11', '1:34.606', '12', '1:33.981', '13', '1:39.783', '14', '18:14.320', '15', '1:37.799', '16', '1:32.084', '17', '1:55.245', '18', '1:39.402', '19', '12:18.693', '20', '1:37.482', '21', '1:48.001', '22', '1:36.888', '23', '1:36.899', '24', '1:37.126', '25', '1:36.657', '26', '1:42.582', '27', '1:37.022', '28', '1:46.070'], ['2', 'M. WEBBER', '1', '14:07:49', '2', '1:42.610', '3', '1:47.751', '4', '1:39.394', '5', '1:33.642', '6', '1:33.662', '7', '1:38.898', '8', '13:07.510', '9', '1:34.514', '10', '1:34.727', '11', '1:36.695', '12', '1:33.815', '13', '1:33.657', '14', '1:42.388', '15', '11:45.312', '16', '1:31.770', '17', '1:44.519', '18', '1:31.711', '19', '2:08.109', '20', '10:56.657', '21', '1:38.497', '22', '1:37.538', '23', '1:37.778', '24', '1:37.035', '25', '1:36.853', '26', '1:37.020', '27', '1:36.481', '28', '1:36.442', '29', '1:36.930', '30', '1:36.478', '31', '1:36.640', '32', '1:37.308', '33', '1:36.947', '34', '1:45.291'], ['3', 'L. HAMILTON', '1', '14:05:10', '2', '1:44.497', '3', '1:34.393', '4', '1:44.568', '5', '1:45.387', '6', '15:15.030', '7', '1:37.286', '8', '1:42.580', '9', '6:28.745', '10', '9:56.132', '11', '1:32.724', '12', '1:50.707', '13', '1:41.637', '14', '15:37.954', '15', '1:38.663', '16', '1:37.654', '17', '1:37.793', '18', '1:37.947', '19', '1:37.421', '20', '1:37.267', '21', '1:43.996', '22', '1:41.130', '23', '1:37.694', '24', '1:42.246', '25', '2:18.522', '26', '1:37.375', '27', '1:40.418', '28', '1:43.353'], ['4', 'J. BUTTON', '1', '14:05:01', '2', '1:41.377', '3', '1:45.846', '4', '12:26.305', '5', '1:41.652', '6', '2:08.066', '7', '1:41.641', '8', '2:09.777', '9', '1:35.559', '10', '1:49.013', '11', '17:57.007', '12', '1:36.895', '13', '1:35.549', '14', '1:45.681', '15', '6:55.356', '16', '1:33.225', '17', '1:53.523'], ['5', 'F. ALONSO', '1', '14:05:22', '2', '1:32.990', '3', '1:37.588', '4', '1:54.709', '5', '2:22.159', '6', '9:06.670', '7', '1:34.701', '8', '1:33.651', '9', '1:41.840', '10', '1:38.465', '11', '1:33.873', '12', '1:33.201', '13', '1:42.779', '14', '9:49.556', '15', '1:38.756', '16', '1:37.738', '17', '1:31.879', '18', '1:43.554', '19', '1:44.584', '20', '1:37.091', '21', '9:56.794', '22', '2:22.908', '23', '2:17.489', '24', '1:37.472', '25', '1:37.457', '26', '1:37.415', '27', '1:37.189', '28', '1:37.430', '29', '1:38.886', '30', '1:37.512', '31', '1:37.408', '32', '1:42.529', '33', '2:09.717', '34', '1:38.106', '35', '1:42.445', '36', '1:37.965', '37', '1:38.942', '38', '1:46.592'], ['6', 'F. MASSA', '1', '14:04:08', '2', '1:42.681', '3', '1:40.704', '4', '3:54.629', '5', '1:37.745', '6', '1:34.369', '7', '1:34.137', '8', '1:38.041', '9', '1:34.052', '10', '1:53.131', '11', '2:35.387', '12', '8:07.920', '13', '1:32.772', '14', '1:32.466', '15', '1:38.682', '16', '1:38.595', '17', '10:36.838', '18', '1:32.354', '19', '1:37.183', '20', '1:43.278', '21', '1:32.379', '22', '1:42.464', '23', '13:59.721', '24', '2:22.037', '25', '1:37.832', '26', '1:37.403', '27', '1:37.576', '28', '1:37.236', '29', '1:45.394', '30', '1:37.411', '31', '1:37.578', '32', '1:37.348', '33', '1:37.756', '34', '1:37.552', '35', '1:40.158', '36', '1:41.825'], ['7', 'M. SCHUMACHER', '1', '14:07:44', '2', '1:38.194', '3', '1:42.870', '4', '1:38.773', '5', '1:37.431', '6', '1:37.053', '7', '1:43.816', '8', '15:19.158', '9', '1:37.340', '10', '1:38.924', '11', '1:37.164', '12', '1:46.118', '13', '11:01.836', '14', '1:32.411', '15', '1:43.249', '16', '1:32.551', '17', '1:41.257', '18', '1:41.677', '19', '13:29.429', '20', '1:38.959', '21', '1:39.234', '22', '1:40.093', '23', '1:53.903', '24', '1:39.245', '25', '1:39.413', '26', '1:38.898', '27', '1:39.137', '28', '1:38.911', '29', '1:39.225', '30', '1:39.426', '31', '1:44.915'], ['8', 'N. ROSBERG', '1', '14:04:21', '2', '1:38.858', '3', '1:37.954', '4', '1:39.963', '5', '1:51.918', '6', '1:40.467', '7', '1:37.399', '8', '1:53.225', '9', '13:30.027', '10', '1:38.603', '11', '1:37.439', '12', '1:37.155', '13', '1:45.107', '14', '1:37.097', '15', '1:53.601', '16', '16:32.410', '17', '1:32.557', '18', '1:47.347', '19', '1:49.373', '20', '1:49.506', '21', '10:13.091', '22', '1:43.786', '23', '1:39.090', '24', '1:38.926', '25', '1:38.916', '26', '1:38.991', '27', '1:38.959', '28', '1:38.648', '29', '1:39.026', '30', '1:38.658', '31', '1:38.770', '32', '2:03.477'], ['9', 'N. HEIDFELD', '1', '14:05:16', '2', '1:45.704', '3', '1:35.267', '4', '1:49.601', '5', '1:47.033', '6', '46:31.158', '7', '1:33.905', '8', '1:33.682', '9', '1:42.304', '10', '1:36.614', '11', '1:38.836', '12', '15:03.406', '13', '1:33.098', '14', '1:43.948', '15', '1:33.628', '16', '1:35.119', '17', '1:40.280'], ['10', 'V. PETROV', '1', '14:09:18', '2', '1:45.754', '3', '12:54.969', '4', '1:34.265', '5', '1:33.956', '6', '1:38.020', '7', '11:18.611', '8', '1:38.086', '9', '1:33.760', '10', '1:34.749', '11', '1:38.999', '12', '23:34.272', '13', '1:33.138', '14', '1:41.055', '15', '1:33.315', '16', '1:39.978', '17', '7:54.494', '18', '1:40.464', '19', '1:39.973', '20', '1:39.783', '21', '1:40.313', '22', '1:50.505'], ['11', 'R. BARRICHELLO', '1', '14:04:18', '2', '4:44.478', '3', '1:42.963', '4', '1:42.835', '5', '1:45.357', '6', '1:37.728', '7', '1:45.807', '8', '11:19.839', '9', '1:39.120', '10', '1:37.386', '11', '1:44.943', '12', '8:58.236', '13', '1:41.109', '14', '1:49.540', '15', '6:25.474', '16', '1:34.989', '17', '1:42.074', '18', '1:34.344', '19', '1:45.218', '20', '8:37.240', '21', '2:14.480', '22', '1:40.107', '23', '1:39.263', '24', '1:42.204', '25', '1:39.477', '26', '1:39.112', '27', '1:45.671', '28', '2:11.945', '29', '1:39.631', '30', '1:45.469', '31', '1:39.751', '32', '1:40.111', '33', '1:39.352', '34', '1:45.912'], ['12', 'P. MALDONADO', '1', '14:03:10', '2', '1:45.249', '3', '1:38.227', '4', '2:02.540', '5', '1:52.556', '6', '1:43.142', '7', '1:49.853', '8', '8:50.468', '9', '1:38.367', '10', '1:37.653', '11', '1:52.073', '12', '1:37.618', '13', '1:37.984', '14', '1:37.485', '15', '1:44.111', '16', '1:45.781', '17', '9:45.289', '18', '1:35.002', '19', '1:45.613', '20', '1:34.996', '21', '1:48.897', '22', '17:50.651', '23', '1:41.300', '24', '1:41.588', '25', '1:40.152', '26', '1:39.895', '27', '1:39.439', '28', '1:39.333', '29', '1:43.405', '30', '1:41.164', '31', '1:39.819', '32', '1:40.858', '33', '1:46.382', '34', '1:40.950', '35', '1:47.242'], ['14', 'A. SUTIL', '1', '14:06:38', '2', '1:38.580', '3', '1:36.529', '4', '1:40.444', '5', '1:35.604', '6', '1:35.376', '7', '1:52.547', '8', '17:25.148', '9', '1:39.042', '10', '1:36.772', '11', '1:35.744', '12', '1:38.266', '13', '1:35.185', '14', '1:44.150', '15', '9:36.211', '16', '1:33.211', '17', '1:40.882', '18', '1:33.311', '19', '1:43.173', '20', '9:56.761', '21', '1:37.389', '22', '1:37.103', '23', '1:38.292', '24', '1:38.202', '25', '1:38.157', '26', '1:38.031', '27', '1:38.007', '28', '1:38.267', '29', '1:38.585', '30', '1:38.273', '31', '1:38.429', '32', '1:39.115', '33', '1:39.050', '34', '1:59.080'], ['15', 'P. DI RESTA', '1', '14:13:38', '2', '1:37.576', '3', '1:36.514', '4', '1:38.004', '5', '1:36.402', '6', '1:36.017', '7', '1:45.631', '8', '7:39.486', '9', '1:38.118', '10', '1:36.996', '11', '1:36.534', '12', '1:40.966', '13', '1:36.225', '14', '1:45.720', '15', '12:02.502', '16', '1:33.299', '17', '1:45.454', '18', '1:33.608', '19', '1:44.737', '20', '10:02.248', '21', '1:38.658', '22', '1:38.683', '23', '1:39.096', '24', '1:39.101', '25', '1:38.877', '26', '1:38.868', '27', '1:38.297', '28', '1:38.455', '29', '1:38.338', '30', '1:38.230', '31', '1:38.494', '32', '1:39.776', '33', '1:38.382', '34', '1:49.880'], ['16', 'K. KOBAYASHI', '1', '14:03:06', '2', '1:42.880', '3', '1:37.209', '4', '1:51.635', '5', '9:05.609', '6', '1:35.009', '7', '1:36.869', '8', '1:40.618', '9', '1:40.913', '10', '7:08.188', '11', '1:39.357', '12', '1:34.515', '13', '1:34.711', '14', '1:44.009', '15', '1:43.515', '16', '9:05.291', '17', '1:34.514', '18', '1:34.663', '19', '1:44.029', '20', '1:34.491', '21', '1:41.058', '22', '11:12.894', '23', '1:39.658', '24', '1:39.369', '25', '1:39.490', '26', '1:39.097', '27', '1:39.697', '28', '1:44.691', '29', '1:41.598', '30', '1:39.425', '31', '1:40.004', '32', '1:43.313', '33', '4:29.699', '34', '1:39.460', '35', '1:50.388'], ['17', 'S. PEREZ', '1', '14:02:01', '2', '1:42.634', '3', '1:42.129', '4', '1:37.763', '5', '2:00.477', '6', '10:04.160', '7', '1:35.370', '8', '1:36.610', '9', '1:42.355', '10', '1:34.836', '11', '1:42.677', '12', '10:04.962', '13', '1:36.409', '14', '1:37.597', '15', '1:35.852', '16', '1:46.512', '17', '1:50.105', '18', '10:45.406', '19', '1:34.210', '20', '1:49.775', '21', '1:36.101', '22', '1:37.436', '23', '1:34.113', '24', '1:45.371', '25', '8:46.717', '26', '1:38.806', '27', '1:38.865', '28', '1:38.335', '29', '1:38.549', '30', '1:38.409', '31', '1:38.984', '32', '1:38.888', '33', '1:38.773', '34', '1:38.258', '35', '2:02.718'], ['18', 'S. BUEMI', '1', '14:04:00', '2', '7:14.661', '3', '2:05.559'], ['19', 'J. ALGUERSUARI', '1', '14:02:16', '2', '1:36.498', '3', '1:41.085', '4', '1:35.725', '5', '1:41.243', '6', '1:43.450', '7', '9:11.245', '8', '1:36.150', '9', '1:38.208', '10', '1:36.802', '11', '1:36.467', '12', '1:36.363', '13', '1:41.458', '14', '11:39.638', '15', '1:34.487', '16', '1:34.601', '17', '1:34.723', '18', '1:43.561', '19', '13:53.566', '20', '2:19.421', '21', '1:40.547', '22', '1:40.211', '23', '1:39.952', '24', '1:39.663', '25', '1:39.601', '26', '1:39.573', '27', '1:39.591', '28', '1:39.724', '29', '1:39.485', '30', '1:39.360', '31', '1:39.172', '32', '1:39.146', '33', '1:39.219', '34', '1:40.052', '35', '1:39.682', '36', '1:39.797', '37', '1:50.910'], ['20', 'H. KOVALAINEN', '1', '14:02:10', '2', '1:38.971', '3', '1:46.075', '4', '1:38.313', '5', '1:42.952', '6', '1:43.964', '7', '1:43.680', '8', '1:44.422', '9', '9:11.814', '10', '1:40.357', '11', '1:39.446', '12', '1:39.659', '13', '1:39.056', '14', '1:40.002', '15', '1:38.870', '16', '1:38.459', '17', '1:38.714', '18', '1:38.665', '19', '1:39.975', '20', '1:52.011', '21', '9:13.835', '22', '1:38.399', '23', '1:35.753', '24', '1:43.899', '25', '1:47.596', '26', '7:41.227', '27', '1:40.162', '28', '1:40.043', '29', '1:47.254', '30', '1:40.232', '31', '1:39.912', '32', '1:39.808', '33', '1:39.520', '34', '1:39.239', '35', '1:39.140', '36', '1:39.149', '37', '1:39.537', '38', '1:39.245', '39', '1:56.245', '40', '1:40.012', '41', '1:39.638', '42', '1:48.608'], ['21', 'K. CHANDHOK', '1', '14:02:49', '2', '1:40.093', '3', '1:53.564', '4', '1:39.558', '5', '1:38.578', '6', '1:48.799', '7', '13:20.452', '8', '1:47.830', '9', '1:49.134', '10', '1:42.299', '11', '1:41.395', '12', '1:52.678', '13', '1:48.879', '14', '1:56.248', '15', '11:04.166', '16', '1:41.569', '17', '1:37.303', '18', '1:37.248', '19', '1:55.608', '20', '11:58.551', '21', '1:44.035', '22', '1:42.429', '23', '1:43.433', '24', '1:43.446', '25', '1:41.203', '26', '1:56.749', '27', '1:42.494', '28', '1:52.478', '29', '1:49.846', '30', '2:16.569', '31', '1:43.999', '32', '1:49.898', '33', '1:51.328'], ['22', 'D. RICCIARDO', '1', '14:02:54', '2', '1:41.864', '3', '1:40.737', '4', '1:41.770'], ['23', 'V. LIUZZI', '1', '14:02:03', '2', '1:43.762', '3', '1:41.552', '4', '1:40.569', '5', '1:49.907', '6', '1:48.799', '7', '1:48.060', '8', '15:11.186', '9', '1:39.361', '10', '1:46.914', '11', '1:38.944', '12', '1:49.137', '13', '1:39.629', '14', '1:43.846', '15', '14:52.575', '16', '1:38.775', '17', '1:38.145', '18', '1:42.639', '19', '1:38.453', '20', '1:51.587', '21', '13:23.581', '22', '1:41.813', '23', '1:41.021', '24', '1:41.927', '25', '1:41.831', '26', '1:40.959', '27', '1:41.475', '28', '1:43.390', '29', '1:41.368', '30', '1:41.212', '31', '1:46.230'], ['24', 'T. GLOCK', '1', '14:02:29', '2', '1:41.722', '3', '1:40.251', '4', '1:39.613', '5', '1:39.301', '6', '1:51.574', '7', '14:07.919', '8', '1:39.659', '9', '1:39.300', '10', '1:47.444', '11', '10:18.628', '12', '1:39.203', '13', '1:39.099', '14', '1:38.877', '15', '1:38.551', '16', '1:46.362', '17', '9:31.864', '18', '1:36.940', '19', '1:37.344', '20', '1:36.976', '21', '2:07.530', '22', '10:09.338', '23', '1:42.025', '24', '1:42.413', '25', '1:41.398', '26', '1:41.855', '27', '1:41.873', '28', '1:41.795', '29', '1:41.815', '30', '1:48.921', '31', '1:41.613', '32', '2:02.331'], ['25', "J. D'AMBROSIO", '1', '14:02:17', '2', '1:46.890', '3', '1:45.143', '4', '1:46.998', '5', '1:45.319', '6', '1:51.161', '7', '2:28.562', '8', '1:44.090', '9', '1:43.466', '10', '1:43.863', '11', '1:43.964', '12', '1:45.076', '13', '1:43.581', '14', '1:43.978', '15', '1:53.319', '16', '9:46.283', '17', '1:39.973', '18', '1:39.280', '19', '1:43.138', '20', '1:39.066', '21', '1:48.422', '22', '12:05.450', '23', '1:39.957', '24', '1:48.904', '25', '11:48.363', '26', '1:41.024', '27', '1:38.809', '28', '1:45.124', '29', '6:18.091', '30', '1:38.060', '31', '1:37.391', '32', '1:37.313', '33', '1:43.309']]

fp2classification=[['1', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:31.711', '202.078', '14:57:02', '34'], ['2', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari', '1:31.879', '0.168', '201.708', '14:47:53', '38'], ['3', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:32.084', '0.373', '0.205', '201.259', '15:01:46', '28'], ['4', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari', '1:32.354', '0.643', '0.270', '200.671', '14:50:32', '36'], ['5', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:32.411', '0.700', '0.057', '200.547', '14:52:15', '31'], ['6', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:32.557', '0.846', '0.146', '200.231', '14:58:05', '32'], ['7', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:32.724', '1.013', '0.167', '199.870', '14:48:31', '28'], ['8', '9', 'N. HEIDFELD', 'GER', 'Lotus Renault GP', '1:33.098', '1.387', '0.374', '199.067', '15:23:26', '17'], ['9', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:33.138', '1.427', '0.040', '198.982', '15:11:36', '22'], ['10', '14', 'A. SUTIL', 'GER', 'Force India F1 Team', '1:33.211', '1.500', '0.073', '198.826', '14:55:00', '34'], ['11', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:33.225', '1.514', '0.014', '198.796', '15:03:24', '17'], ['12', '15', 'P. DI RESTA', 'GBR', 'Force India F1 Team', '1:33.299', '1.588', '0.074', '198.638', '14:54:38', '34'], ['13', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:34.113', '2.402', '0.814', '196.920', '15:04:48', '34'], ['14', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:34.344', '2.633', '0.231', '196.438', '14:57:44', '34'], ['15', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:34.487', '2.776', '0.143', '196.141', '14:42:45', '37'], ['16', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:34.491', '2.780', '0.004', '196.132', '14:54:54', '35'], ['17', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:34.996', '3.285', '0.505', '195.090', '14:51:04', '35'], ['18', '20', 'H. KOVALAINEN', 'FIN', 'Team Lotus', '1:35.753', '4.042', '0.757', '193.547', '14:54:14', '42'], ['19', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:36.940', '5.229', '1.187', '191.178', '15:00:06', '32'], ['20', '21', 'K. CHANDHOK', 'IND', 'Team Lotus', '1:37.248', '5.537', '0.308', '190.572', '14:53:29', '33'], ['21', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:37.313', '5.602', '0.065', '190.445', '15:29:37', '33'], ['22', '23', 'V. LIUZZI', 'ITA', 'HRT F1 Team', '1:38.145', '6.434', '0.832', '188.830', '14:56:14', '31'], ['23', '22', 'D. RICCIARDO', 'AUS', 'HRT F1 Team', '1:40.737', '9.026', '2.592', '183.972', '14:06:16', '5'], ['24', '18', 'S. BUEMI', 'SUI', 'Scuderia Toro Rosso', '3']]



fp3times=[]

fp3classification=[]


#Qualifying
qualitimes=[]

qualiclassification=[]

qualisectors=[]
qualitrap=[]
qualispeeds=[]

#Race
stops=[]
analysis=[]
chart=[]
history=[]
speeds=[]
sectors=[]
trap=[]
classification=[]

#Drivers
#from GBR, 22: KAR-> RIC
driverShort={'1':"VET",'2':"WEB",'3':"HAM",'4':"BUT",'5':"ALO",'6':"MAS",'7':"SCH",'8':"ROS",'9':"HEI",'10':"PET",'11':"BAR",'12':"MAL",'14':"SUT",'15':"RES",'16':"KOB",'17':"PER",'18':"BUE",'19':"ALG",'20':"KOV",'21':"CHA",'22':"RIC",'23':"LIU",'24':"GLO",'25':"AMB"}


#Tyre data from Pirelli
tyres=[]