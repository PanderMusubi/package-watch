#!/usr/bin/env python3

# name: retrive.py
# description: TODO
# license: MIT
# date: 2016-03-24


watching_spec = []
watching_wild = []
for line in open('packages-watching.txt'):
    if line[0] == '#':
        continue
    line = line[:-1]
    if line == '' or line[-1] == '*':
        if line[:-1] not in watching_wild:
            watching_wild.append(line[:-1])
    else:
        if line not in watching_spec:
            watching_spec.append(line)
#print(sorted(watching_spec))
#print(sorted(watching_wild))

report = {}
src_packages = {}
bin_packages = {}
from os import listdir
for filename in listdir('.'):
    if filename.startswith('Sources-'):
        source = filename.replace('Sources-', '')
        dis, begin, end, cat = source.split('_')
        rep = None
        if end == 'base':
            rep = begin
        else:
            rep = '{}-{}'.format(begin, end)
#        print(dis, rep, cat)
        package = None
        binaries = []
        version = None
        for line in open(filename, 'r'):
            line = line[:-1]
            if line.startswith('Package: '):
                package = line.replace('Package: ', '')
            elif line.startswith('Binary: '):
                binaries = line.replace('Binary: ', '').split(', ')
            elif line.startswith('Version: '):
                version = line.replace('Version: ', '')
            if package and binaries and version:
#                print(dis, rep, cat, package)
#                print(dis, rep, cat, package, version)
                if package in watching_spec:
                    if package not in src_packages:
                        src_packages[package] = {}
                    if dis not in src_packages[package]:
                        src_packages[package][dis] = {}
                        if dis not in report:
                            report[dis] = {}
                    if rep not in src_packages[package][dis]:
                        src_packages[package][dis][rep] = {}
                        if rep not in report[dis]:
                            report[dis][rep] = {}
                    if cat not in src_packages[package][dis][rep]:
                        src_packages[package][dis][rep][cat] = []
                        if cat not in report[dis][rep]:
                            report[dis][rep][cat] = {}
                    src_packages[package][dis][rep][cat].append(version)
                for binary in binaries:
                    if binary in watching_spec:
                        if binary not in bin_packages:
                            bin_packages[binary] = {}
                        if dis not in bin_packages[binary]:
                            bin_packages[binary][dis] = {}
                            if dis not in report:
                                report[dis] = {}
                        if rep not in bin_packages[binary][dis]:
                            bin_packages[binary][dis][rep] = {}
                            if rep not in report[dis]:
                                report[dis][rep] = {}
                        if cat not in bin_packages[binary][dis][rep]:
                            bin_packages[binary][dis][rep][cat] = []
                            if cat not in report[dis][rep]:
                                report[dis][rep][cat] = {}
                        bin_packages[binary][dis][rep][cat].append(version)
                package = None
                binaries = []
                version = None

#for dis, value in src_packages.items():
#    print(dis)
#    for rep, value in value.items():
#        print('  ',rep)
#        for cat, value in value.items():
#            print('    ',cat)
#            for binary, value in value.items():
#                print('      ',binary)
#                for version in sorted(value):
#                    print('        ',version)
for binary, value in sorted(bin_packages.items()):
    print(binary)
    for dis, value in sorted(value.items()):
        print('  ',dis)
        for rep, value in sorted(value.items()):
#            print('    ',rep)
            for cat, value in sorted(value.items()):
                print('      ',rep,cat, ', '.join(sorted(value)))
#                for version in sorted(value):
#                    print('        ',version)





#from datetime import datetime, timedelta
#utcnow = datetime.utcnow()
#year = utcnow.strftime('%Y')
#dtstamp = utcnow.strftime('%Y%m%dT%H%M%SZ')
#now = time()
#                date = datetime.strptime(
#                    '{}{}{}'.format(year, month, day), '%Y%m%d')
#                calendar.write('DTSTART;VALUE=DATE-TIME:{}T080000\n'.format(
#                    date.strftime('%Y%m%d')))
#                calendar.write('DTEND;VALUE=DATE-TIME:{}T080000\n'.format(
#                    date.strftime('%Y%m%d')))
