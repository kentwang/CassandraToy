'''
Created on Nov 22, 2014

@author: ketongwang
'''

if __name__ == '__main__':
    f = open("./data/260mv_clean.txt", "r").read().splitlines()
    i = 0;
    for line in f:
        Distribution, Votes, Rank, Title = line.replace('\'',"").split(",");
        print "INSERT INTO movies (distribution, votes, rank, title) VALUES ('"+Distribution+"',"+Votes+","+Rank+", \'"+Title.lstrip()+"\');"
    