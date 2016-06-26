from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json
import time

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_doge = AuthServiceProxy("http://%s:%s@127.0.0.1:22555"%('dogecoinrpcuser', 'dogecoinrpcpassword'))

outset = set()
cache = set()
while True:
	mempool = rpc_doge.getrawmempool()
	for item in mempool:
		if item not in cache:
			cache.add(item)
			tx = rpc_doge.decoderawtransaction(rpc_doge.getrawtransaction(item))
			for i in range(0,len(tx['vout']),1):
				try:
					out = (tx['vout'][i]['value'])
					outset.add(out)
				except:
					continue
			if len(str(int(round(sum(outset),-1)))) == 1:
				print(''+str(int(round(sum(outset,-1)))))
			elif len(str(int(round(sum(outset),-1)))) == 2:
				print(' /\\')
				print(' '+str(int(round(sum(outset,-1)))))
				print(' \\/')
			elif len(str(int(round(sum(outset),-1)))) == 3:
				print('    _')
				print('   / \\')
				print('   '+str(int(round(sum(outset,-1)))))
				print('   \\_/')
			elif len(str(int(round(sum(outset),-1)))) == 4:
				print('       /\\')
				print('      /  \\')
				print('      '+str(int(round(sum(outset,-1)))))
				print('      \\  /')
				print('       \\/')
			elif len(str(int(round(sum(outset),-1)))) == 5:
				print('            _')
				print('           / \\')
				print('          /   \\')
				print('          '+str(int(round(sum(outset,-1)))))
				print('          \\   /')
				print('           \\_/')
			elif len(str(int(round(sum(outset),-1)))) == 6:
				print('                 /\\')
				print('                /  \\')
				print('               /    \\')
				print('               '+str(int(round(sum(outset,-1)))))
				print('               \\    /')
				print('                \\  /')
				print('                 \\/')
			elif len(str(int(round(sum(outset),-1)))) == 7:
				print('                        _')
				print('                       / \\')
				print('                      /   \\')
				print('                     /     \\')
				print('                     '+str(int(round(sum(outset,-1)))))
				print('                     \\     /')
				print('                      \\   /')
				print('                       \\_/')
			elif len(str(int(round(sum(outset),-1)))) == 8:
				print('                               /\\')
				print('                              /  \\')
				print('                             /    \\')
				print('                            /      \\')
				print('                            '+str(int(round(sum(outset,-1)))))
				print('                            \\      /')
				print('                             \\    /')
				print('                              \\  /')
				print('                               \\/')
			elif len(str(int(round(sum(outset),-1)))) == 9:
				print('                                        _')
				print('                                       / \\')
				print('                                      /   \\')
				print('                                     /     \\')
				print('                                    /       \\')
				print('                                    '+str(int(round(sum(outset,-1)))))
				print('                                    \\       /')
				print('                                     \\     /')
				print('                                      \\   /')
				print('                                       \\_/')
			elif len(str(int(round(sum(outset),-1)))) == 10:
				print('                                                 /\\')
				print('                                                /  \\')
				print('                                               /    \\')
				print('                                              /      \\')
				print('                                             /        \\')
				print('                                             '+str(int(round(sum(outset,-1)))))
				print('                                             \\        /')
				print('                                              \\      /')
				print('                                               \\    /')
				print('                                                \\  /')
				print('                                                 \\/')
			outset.clear()
	bestblockhash = rpc_doge.getbestblockhash()
	if bestblockhash not in cache:
		block = rpc_doge.getblock(bestblockhash)
		print('    _____________________ ')		
		print('   |                     |')		
		print('   |                     |')		
		print('   |                     |')		
		print('   |                     |')
		print('   |                     |')
		print('   |  wow such block     |')
		print('         '+str(len(block['tx'])))
		print('   |            many txs |')
		print('   |                     |')		
		print('   |                     |')		
		print('   |                     |')		
		print('   |                     |')
		print('   |_____________________|')
		cache.add(bestblockhash)
		