tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    size = []
    colWidth = 0
    for row in data:
        size.append(len(max(row)))
    for i in size:
        colWidth += i

    for items in data:
        print((*items[:len(items)], sep = ", ").rjust(
        
            
        

data = tableData
#tablewidth(tableData)
printTable(tableData)
        
    
