import pprint

theboard = {'topo-E': ' ', 'topo-M': ' ', 'topo-D': ' ', 'meio-E': ' ', 'meio-M': ' ', 'meio-D': ' ', 'base-E': ' ', 'base-M': ' ', 'base-D': ' '}

def printboard(board):
	print(board['topo-E'] + '|' + board['topo-M'] + '|' + board['topo-D'])
	print('-----')
	print(board['meio-E'] + '|' + board['meio-M'] + '|' + board['meio-D'])
	print('-----')
	print(board['base-E'] + '|' + board['base-M'] + '|' + board['base-D'])

printboard(theboard)