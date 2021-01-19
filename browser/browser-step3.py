# -*- coding: utf8 -*-
import argparse
import os
import requests

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow
and change shape, and that could be a boon to medicine
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
parser = argparse.ArgumentParser()
parser.add_argument('dir')

args = parser.parse_args()
if not os.path.exists(args.dir):
    os.makedirs(args.dir, exist_ok=True)

authorized_sites = {"bloomberg.com": [bloomberg_com, 'bloomberg'], "nytimes.com": [nytimes_com, 'nytimes']}
authorized_resume = [url for url in [resume[1] for resume in authorized_sites.values()]]

answer = ''
site_list = []
while answer != 'exit':
    answer = input()
    if answer != 'exit':
        if answer == 'back':
            if len(site_list) > 1:
                site_list.pop()
                with open(os.path.join(args.dir, site_list.pop()), 'r') as f:
                    print(''.join(f.readlines()))
        elif answer in authorized_resume:
            if not os.path.exists(os.path.join(args.dir, answer)):
                print('Error: Incorrect URL')
            else:
                with open(os.path.join(args.dir, answer), 'r') as f:
                    print(''.join(f.readlines()))
                site_list.append(answer)
        elif answer not in authorized_sites.keys():
            print(f'Error: authorized url are {", ".join(authorized_sites.keys())}')
        else:
            print(authorized_sites[answer][0])
            with open(os.path.join(args.dir, authorized_sites[answer][1]), 'w+') as f:
                f.write(authorized_sites[answer][0])
            site_list.append(authorized_sites[answer][1])
