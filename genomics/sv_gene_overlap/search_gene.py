# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/27 17:22
@Auth ： zhenyaliu
@File ：search_gene.py
@IDE ：PyCharm
@Mail：zhenyaliu77@gmail.com

"""
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='The overlap relationship between svs and genes')
    parser.add_argument('--sv', type=str, default='./sv.txt', help='path to the sv file')
    parser.add_argument('--gff', type=str, default='./genome.gff', help='path to the gff file')
    parser.add_argument('--k', type=float, default=0.5, help='overlap ratio')
    return parser.parse_args()

def sv_dic(path):
    #将SV按照染色体存成字典
    sv = {}
    with open(path,"r") as f:
        for i in f.readlines():
            i = i.strip()
            if i.split("\t")[0].split("_")[-1] not in sv.keys():
                sv[i.split("\t")[0].split("_")[-1]] = []
                sv[i.split("\t")[0].split("_")[-1]].append(i.split("\t")[1]+"-"+i.split("\t")[2])
            else:
                sv[i.split("\t")[0].split("_")[-1]].append(i.split("\t")[1]+"-"+i.split("\t")[2])
    return sv

def gene_dic(path):
    #将gene按照染色体存成字典
    gene = {}
    with open(path, "r") as f:
        for i in f.readlines():
            i = i.strip()
            if i.split("\t")[0].split("_")[-1] not in gene.keys():
                gene[i.split("\t")[0].split("_")[-1]] = []
                gene[i.split("\t")[0].split("_")[-1]].append(i.split("\t")[1]+"-"+i.split("\t")[2]+"-"+i.split("\t")[3])
            else:
                gene[i.split("\t")[0].split("_")[-1]].append(i.split("\t")[1]+"-"+i.split("\t")[2]+"-"+i.split("\t")[3])
    return gene

def search(args):
    #sv和gene重合的四种情况,k代表重合百分比，比如k=0.5就表示重合大于等于50%
    sv = sv_dic(args.sv)
    gene = gene_dic(args.gff)

    for key in sv.keys():
        print(key)
        for s in sv[key]:
            for g in gene[key]:
                if int(s.split("-")[1]) > int(g.split("-")[0]) and int(s.split("-")[0]) < int(g.split("-")[0]):
                    if (int(s.split("-")[1]) - int(g.split("-")[0]))/(int(s.split("-")[1]) - int(s.split("-")[0])) >= args.k:
                        print(s+' '+g)
                    else:
                        continue
                    #break
                if int(s.split("-")[0]) < int(g.split("-")[1]) and int(s.split("-")[1]) > int(g.split("-")[1]):
                    if (int(g.split("-")[1]) - int(s.split("-")[0]))/(int(s.split("-")[1]) - int(s.split("-")[0])) >= args.k:
                        print(s+' '+g)
                    else:
                        continue
                    #break
                if int(g.split("-")[0]) <= int(s.split("-")[0]) and int(g.split("-")[1]) >= int(s.split("-")[1]):
                    print(s+' '+g)
                if int(g.split("-")[0]) > int(s.split("-")[0]) and int(g.split("-")[1]) < int(s.split("-")[1]):
                    print(s+' '+g)

if __name__ == "__main__":
    args = parse_args()
    search(args)
