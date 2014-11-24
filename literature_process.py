'''
Created on Nov 12, 2014

@author: ketongwang
'''
if __name__ == '__main__':
    f = open("./data/liter_clear.txt", "r").read().splitlines()
    for line in f:
        result = {'MOVI': '\'NULL\'', 'NOVLAuthor': '\'NULL\'', 'NOVLTitle': '\'NULL\'', 'BOOKAuthor':'\'NULL\'', 'BOOKTitle':'\'NULL\'', 'ADPTAuthor':'\'NULL\'', 'ADPTTitle':'\'NULL\''}
        lineList = line.split(';')
        for term in lineList:
            identifier, content = term.lstrip().rstrip().split(':', 1)
            content = content.lstrip()
            if identifier == 'MOVI':
                result['MOVI'] = '\''+content+'\''
            else:
                author, title = content.split('.', 1)
                author = '\''+author+'\''
                title = title.lstrip().replace('\"','\'')
                if identifier == 'NOVL':
                    result['NOVLAuthor'] = author
                    result['NOVLTitle'] = title
                elif identifier == 'BOOK':
                    result['BOOKAuthor'] = author
                    result['BOOKTitle'] = title
                elif identifier == 'ADPT':
                    result['ADPTAuthor'] = author
                    result['ADPTTitle'] = title
        print 'INSERT INTO literature (MOVI, NOVLAuthor, NOVLTitle, BOOKAuthor, BOOKTitle, ADPTAuthor, ADPTTitle) VALUES ('+result['MOVI']+', '+result['BOOKAuthor']+', '+result['BOOKTitle']+', '+result['NOVLAuthor']+', '+result['NOVLTitle']+', '+result['ADPTAuthor']+', '+result['ADPTTitle']+');'
        
        