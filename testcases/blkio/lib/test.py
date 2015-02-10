#!/usr/bin/env python

from cgroup import *

if __name__ == '__main__':
    cg1 = Cgroup('cpu_cpuset', '', ['cpu', 'cpuset'])
    cg1.create()
    cg2 = Cgroup('cpu_qwe', cg1)
    cg2.create()
    #cg2.delete()
    #print cg1.is_hname_used('cpu___cpuset')
    #print cg1.is_hsystem_mounted('ns')
    #print cg1.is_hpath_used('/cgroup/cpu')
