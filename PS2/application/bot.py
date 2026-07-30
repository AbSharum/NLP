# Abraham Sharum
# CS4343
# PS2
# Due Date: September 30, 2024 11:00PM
import math
import os
import string
import discord
import time
start = time.time()
import main

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = os.environ["NLP_BOT_TOKEN"]

@client.event
async def on_ready():
    print("Constructing Model...")
    print(f'We have logged in as {client.user}')
    print("Model constructed! Ready to generate, please navigate to discord.")

@client.event
async def on_message(message):
    content = message.content
    content = content.lower()

    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    
    if client.user in message.mentions:
        content = content.split()
        prompt = ""
        print(content)

        for i in range(1,len(content)):
            prompt += " " + content[i]
        
      
        program = main

        prompt = prompt.translate(str.maketrans('', '',string.punctuation))

        biresponse = program.main(prompt,"bi")
        biprobs = biresponse[1]
        
        total = 0
        if biprobs == 0:
            temp = biresponse[0].split()
            temp2 = prompt.split()
            prompt_len = len(temp2)
            if prompt_len > 1:
                await message.channel.send(f"Sorry, I have never seen the word {temp[0]} before nor the bigram [{temp2[prompt_len - 2]} {temp2[prompt_len - 1]}], I can't predict the next words!")
            elif len(temp) > 0:
                await message.channel.send(f"Sorry, I have never seen the word {temp[0]} before, I can't predict the next words!")

        else:
            
            for key in biprobs.keys():
                count = 0
                for word in biresponse[0].split():
                    if word == key:
                        count += 1
                if biprobs[key] == 0:
                    total = 0
                    break
                total += (biprobs[key] * count)
            await message.channel.send("Bigram generation: " + biresponse[0])
            
            await message.channel.send(f"Bigram Probability: P({biresponse[0]}) = {str(round(total,15)):4}")

            biprob = []
            biprob.append("Output:" + biresponse[0])
            biprob.append(f" Bigram Probability: P({biresponse[0]}) = {str(round(total,15)):4}")
            for key in biprobs.keys():
                biprob.append(f" P({key}) = {str(round(math.pow(10,biprobs[key]),10)):4}")
            main.grams.save_to_file(biprob,"bigramOutput",True)

        total = 0
        triresponse = program.main(prompt,"tri")
        triprobs = triresponse[1]
        if triprobs == 0:
            temp = biresponse[0].split()
            if len(temp) > 1:
                await message.channel.send(f"Sorry, I have never seen the bigram [{temp[0]} {temp[1]}] before, I can't predict the next words!")
                
        else:
            await message.channel.send("Trigram generation: "+ triresponse[0])
            for key in triprobs.keys():
                count = 0
                for word in triresponse[0].split():
                    if word == key:
                        count += 1
                if triprobs[key] == 0:
                    total = 0
                    break
                
                total += (triprobs[key] * count)
            await message.channel.send(f"Trigram Probability: P({triresponse[0]}) = {str(round(total,15)):4}")
            if total == 0:
                await message.channel.send(f"The sentence proability being zero means there exists a word that is not in the lexicon and was not used for sentence generation.")
            triprob = []
            triprob.append("Output:" + triresponse[0])
            triprob.append(f" Trigram Probability: P({triresponse[0]}) = {str(round(total,15)):4}")
            for key in triprobs.keys():
                triprob.append(f" P({key}) = {str(round(math.pow(10,triprobs[key]),15)):4}")
            main.grams.save_to_file(triprob,"trigramOutput",True)

client.run(token)