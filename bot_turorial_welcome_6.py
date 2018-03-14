@client.event
async def on_member_join(member):
  canal = client.get_channel("423328604911304708")
  regras = client.get_channel("420612829838573588")
  msg = "Bem Vindo {}\n leia as {}".format(member.mention, regras.mention)
  await client.send_message(canal, msg)

@client.event
async def on_member_remove(member):
   canal = client.get_channel("423328604911304708")
   msg = "Adeus garotinho juvenil {}".format(member.mention)
   await client.send_message(canal, msg)
