# Design a firewall: Read firewall rules from a csv and create a function which allows incoming requests only based on the rules
# accept_packet(direction, protocol, port, ip_address)
# direction: inbound | outbound

import csv

class solution:
    rules = {}
    def __init__(self, path):
        # read csv file
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # create a combined rules dictionary
            self.rules["inbound-tcp"] = {}
            self.rules["outbound-tcp"] = {}
            self.rules["inbound-udp"] = {}
            self.rules["outbound-udp"] = {}
            for row in csv_reader:
                # pre-compute rules and combine into a condensed representation
                key = row[0] + "-" + row[1]
                # print(key)
                if "-" not in row[2]:
                    # create list of single valued IPs
                    val = self.rules[key].get("ports", [])
                    val.append(row[2])
                    self.rules[key]["ports"] = val
                else:
                    # print("ysbdsn")
                    if "port-range" not in self.rules[key]:
                        self.rules[key]["port-range"] = {}
                    self.rules[key]["port-range"].setdefault("starts", []).append(row[2].split("-")[0])
                    self.rules[key]["port-range"].setdefault("ends", []).append(row[2].split("-")[1])

                if "-" not in row[3]:
                    # create list of single valued IPs
                    val = self.rules[key].setdefault("ips", [])
                    val.append(row[3])
                    self.rules[key]["ips"] = val
                else:
                    if "ip-range" not in self.rules[key]:
                        self.rules[key]["ip-range"] = {}
                    self.rules[key]["ip-range"].setdefault("starts", []).append(row[2].split("-")[0])
                    self.rules[key]["ip-range"].setdefault("ends", []).append(row[2].split("-")[1])
        print(self.rules)

    # accept request based on rules
    def accept_packet(self, direction, protocol, port, ip_address):
            key = direction + "-" + protocol
            # port_flag = False
            # ip_flag = False

            if key not in self.rules:
                return False

            # check port
            if str(port) not in self.rules[key]["ports"]:
                print("FLOW")
                if not (self.checkPortRange(key, port)):
                    return False

            # check ip
            if str(ip_address) not in self.rules[key]["ips"]:
                if not (self.checkIpRange(key, ip_address)):
                    return False

            return True

    def checkPortRange(self, key, port):
        starts = self.rules[key]["port-range"].get("starts", [])
        ends = self.rules[key]["port-range"].get("ends", [])
        for index in range(len(starts)):
            if str(starts[index]) <= str(port) <= str(ends[index]):
                return True
        return False

    def checkIpRange(self, key, ip_address):
        starts = self.rules[key]["ip-range"].get("starts", [])
        ends = self.rules[key]["ip-range"].get("ends", [])
        for index in range(len(starts)):
            if str(starts[index]) <= str(ip_address) <= str(ends[index]):
                return True
        return False

# tests
obj = solution('input.csv')
print(obj.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
