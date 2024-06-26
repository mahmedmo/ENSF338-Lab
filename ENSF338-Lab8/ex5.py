class GraphNode:
    def __init__(self, data):
        self.data = data
        self.edges = {}

class Graph:
    def __init__(self):
        self.nodes = {}
        
    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def removeNode(self, node):
        if node.data in self.nodes:
            del self.nodes[node.data]

    def addEdge(self, n1, n2, weight):
        if n1 in self.nodes and n2 in self.nodes:
            if n1 not in self.nodes[n2].edges:
                self.nodes[n1].edges[n2] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            if n1 in self.nodes[n2].edges:
                del self.nodes[n1].edges[n2]

    def isdag(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)

            for neighbor in self.nodes[node].edges:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in stack:
                    return True

            stack.remove(node)
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return False

        return True

    def toposort(self):
        if not self.isdag():
            return None

        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)

            for neighbor in self.nodes[node].edges:
                if neighbor not in visited:
                    dfs(neighbor)

            stack.append(node)

        for node in self.nodes:
            if node not in visited:
                dfs(node)

        return stack[::-1]

    def importFromFile(self, file):
        # clears nodes
        self.nodes = {}

        try:
            with open(file, 'r') as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()

                if not '--' in line:
                    continue

                parts = line.split('--')
                n1 = parts[0].strip()
                n2 = parts[1].split('[')[0].strip()

                if n1 not in self.nodes:
                    self.addNode(n1)
                if n2 not in self.nodes:
                    self.addNode(n2)

                weight = 1
                if '[' in parts[1] and 'weight' in parts[1]:
                    weight = int(parts[1].split('weight=')[1].split(']')[0])

                self.addEdge(n1, n2, weight)

        except Exception as e:
            # return null if there are errors
            return None

    def printGraph(self):
        for node, graphnode in self.nodes.items():
            print(f"Node {node} has edges: {graphnode.edges}")

# Test case 1: Acyclic graph

graph1 = Graph()
graph1.addNode('A')
graph1.addNode('B')
graph1.addNode('C')
graph1.addEdge('A', 'B', 1)
graph1.addEdge('B', 'C', 1)

print("Test case 1:")
print("Graph is a DAG:", graph1.isdag())  # True
print("Topological order:", graph1.toposort())  # ['A', 'B', 'C']

# Test case 2: A cyclic graph
graph2 = Graph()
graph2.addNode('A')
graph2.addNode('B')
graph2.addNode('C')
graph2.addEdge('A', 'B', 1)
graph2.addEdge('B', 'C', 1)
graph2.addEdge('C', 'A', 1)

print("\nTest case 2:")
print("Graph is a DAG:", graph2.isdag())  # False
print("Topological order:", graph2.toposort())  # None

# Test case 3: A disconnected graph
graph3 = Graph()
graph3.addNode('A')
graph3.addNode('B')
graph3.addNode('C')

print("\nTest case 3:")
print("Graph is a DAG:", graph3.isdag())  # True
print("Topological order:", graph3.toposort())  # Nodes in any order because they are all disconnected

graphrand = Graph()
graphrand.importFromFile("random.dot")
print("\nTest case 4:")
print("Graph is a DAG:", graphrand.isdag())
print("Topological order:", graphrand.toposort())

# #Test case 4:
# Graph is a DAG: True
# Topological order: ['808', '732', '696', '695', '685', '684', '679', '632', '597', '579', '573', '836', '568', '529', '526', '504', '499', '498', '483', '479', '471', '467', '466', '465', '460', '447', '438', '436', '390', '446', '380', '372', '477', '369', '449', '367', '352', '349', '348', '347', '345', '338', '336', '614', '331', '330', '328', '327', '318', '316', '315', '313', '744', '835', '404', '421', 
# '312', '309', '303', '298', '297', '356', '294', '576', '293', '289', '424', '288', '282', '333', '652', '849', '281', '279', '276', '548', '275', '417', '273', '264', '831', '670', '729', '340', '260', '256', '255', '252', '472', '251', '985', '611', '425', '250', '244', '342', '618', '242', '418', '280', '238', '247', '285', '234', '231', '229', '227', '226', '594', '225', '222', '221', '219', '217', '215', '693', '212', '205', '332', '359', '213', '204', '198', '228', '488', '196', '272', '195', '701', '194', '389', '191', '308', '416', '982', '270', '187', '185', '758', '481', '220', '184', '470', '301', '179', '178', '175', '174', '171', '323', '170', '588', '241', '165', '159', '158', '166', '157', '156', '168', '904', '398', '152', '151', '148', '197', '147', '484', '428', '581', '144', '997', '456', '263', '160', '143', '354', '141', '950', '343', '140', '422', '403', '138', '237', '137', '135', '823', '134', '448', '833', '337', '132', '173', '406', '641', '129', '127', '126', '511', '642', '373', '397', '300', '525', '681', '501', '125', '136', '580', '230', '124', '537', '154', '903', '673', '122', '186', '146', '341', '121', '120', '118', '480', '261', '364', '455', '797', '559', '117', '116', '115', '877', '591', '462', '570', '176', '486', '799', '536', '114', '545', '181', '232', '540', '110', '296', '109', '108', '524', '180', '214', '408', '107', '884', '287', '104', '872', '711', '103', '314', '101', 
# '776', '454', '100', '562', '99', '233', '617', '98', '961', '97', '795', '876', '546', '96', '508', '929', '407', '507', '106', '714', '92', '90', '254', '89', '88', '703', '86', '769', '431', '608', '199', '520', '85', '163', '589', '84', '344', '83', '305', '517', '610', '81', '78', '569', '87', '639', '768', '149', '77', '689', '475', '76', '637', '75', '662', '896', '271', '845', '692', '74', '415', '954', '459', '946', '182', '706', '320', '351', '73', '72', '210', '535', '71', '834', '70', '131', '607', '427', '262', '68', '730', '67', '855', '464', '66', '402', '65', '162', '813', '519', '489', '209', '346', '755', '671', '257', '164', '200', '603', '512', '169', '63', '383', '468', '443', '370', '624', '792', '487', '62', '430', '339', '61', '516', '290', '704', '561', '728', '702', '60', '716', '522', '59', '384', '506', '781', '58', '426', '794', '57', '439', '429', '625', '441', '432', '543', '719', '547', '91', '378', '223', '528', '527', '153', '55', '636', '376', '784', '54', '394', '48', '782', '832', '277', '601', '47', '56', '105', '119', '473', '46', '45', '888', '133', '155', '49', '44', '42', '391', '718', '189', '666', '246', '41', '324', '374', '926', '433', '258', '40', '319', '39', '38', '605', '697', '64', '43', '37', '371', '266', '934', '113', '36', '268', '240', '510', '860', '409', '363', '361', '565', '190', '93', '283', '112', '806', '35', '712', '34', '111', '556', '311', '595', '682', 
# '469', '33', '32', '248', '350', '897', '52', '239', '968', '392', '843', '291', '167', '965', '785', '531', '858', '192', '586', '771', '31', '740', '188', '672', '453', '587', '30', '235', '870', '912', '970', '668', '401', '847', '869', '754', '721', '29', '396', '800', '826', '80', '28', '756', '635', '893', '542', '717', '814', '27', '578', '941', '284', '382', '638', '986', '334', '984', '743', '492', '957', '444', '553', '458', '395', '705', '747', '658', '482', '653', '490', '575', '584', '218', '532', '582', '420', '211', '883', '26', '25', '572', '79', '329', '474', '688', '335', '24', '150', '720', '790', '737', '731', '23', '22', '967', '544', '325', '419', '193', '304', '21', '911', '413', '286', '362', '772', '972', '602', '411', '267', '842', '259', '654', '497', '767', '633', '321', '130', '399', 
# '620', '801', '538', '690', '20', '574', '461', '491', '478', '534', '51', '379', '253', '243', '19', '365', '651', '387', '811', '269', '541', '804', '664', '434', '973', '656', '686', '687', '783', '388', '245', '567', '810', '713', '723', '393', '533', '457', '683', '850', '161', '514', '18', '628', '708', '451', '978', '17', '609', '956', '102', '645', '742', '676', '423', '564', '16', '778', '224', '94', '936', '841', '818', '657', '935', '613', '405', '923', '762', '722', '922', '558', '674', '53', '634', '885', '825', '930', '445', '550', '917', '123', '592', '509', '494', '918', '631', '902', '938', '763', '959', '50', '861', '15', '796', '749', '208', '355', '265', '809', '906', '992', '820', '665', '894', '292', '939', '502', '726', '295', '991', '14', '554', '803', '69', '623', '505', '815', '599', '798', '13', '874', '206', '530', '216', '322', '353', '875', '201', '753', '807', '700', '667', '736', '848', '368', '793', '172', '12', '999', '450', '11', '751', '990', '852', '551', '10', '775', '827', '493', '604', '866', '615', '9', '440', '908', '865', '822', '95', '979', '381', '677', '844', '837', '274', '82', '914', '128', '882', '606', '500', '655', '901', '905', '987', '757', '616', '600', '278', '437', '779', '746', '521', '612', '880', '496', '921', '183', '177', '898', '326', '864', '299', '975', '710', '566', '660', '7', '910', '840', '523', '955', '725', '627', '927', '963', '816', '307', '650', '960', '879', '590', '773', '6', '583', '966', '994', '952', '867', '8', '236', '805', '983', '709', '915', '385', '989', '360', '630', '539', '694', '780', '644', '899', '619', '791', '748', '659', '777', '741', '971', '675', '998', '846', '414', '873', '386', '621', '871', '734', '942', '724', '442', '560', '953', '463', '824', '555', '577', '733', '937', '643', '907', '890', '993', '895', '891', '881', '830', '139', '629', '515', '750', '887', '981', '819', '752', '680', '958', '995', '931', '649', '838', '774', '485', '647', '249', '851', '661', '920', '856', '552', '928', '889', '770', '854', '715', '944', 
# '5', '913', '622', '317', '933', '357', '878', '857', '310', '698', '924', '4', '839', '886', '962', '766', '916', '996', '949', '663', '735', '925', '640', '495', '707', '3', '739', '940', '518', '513', '377', '598', '207', '646', '648', '435', '765', '900', '678', '412', '853', '302', '563', '964', '828', '2', '786', '1', '788', '945', '862', '988', '789', '306', '410', '691', '787', '400', '829', '932', '585', '761', '760', '571', '868', '626', '764', '980', '476', '366', '745', '974', '503', '976', '727', '452', '892', '859', '821', '947', '812', '969', '0', '817', '802', '596', '919', '759', '948', '557', 
# '977']