@client.event
async def on_member_join(member):
  canal = client.get_channel("462791105771995158")
  regras = client.get_channel("463111133096574987")
  msg = "Bem Vindo {}\n reuniões:{}".format(member.mention, regras.mention)
  await client.send_message(canal, msg) #substitua canal por member para enviar a msg no DM do membro

@client.event
async def on_member_remove(member):
   canal = client.get_channel("423328604911304708")
   msg = "Adeus{}".format(member.mention)
   await client.send_message(canal, msg) #substitua canal por member para enviar a msg no DM do membro
